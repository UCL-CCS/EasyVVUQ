#from hashlib import shake_128
import logging
import chaospy as cp
import numpy as np
import random
from .base import BaseSamplingElement, Vary
from .transformations import Transformations


# DEBUG USI
from os import stat, path
from time import ctime
import json

__author__ = "Jalal Lakhlili"
__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


class FDSampler(BaseSamplingElement, sampler_name="FD_sampler"):
    def __init__(self,
                 vary=None,
                 distribution=None,
                 perturbation=0.05,
                 count=0,
                 relative_analysis=False):
        """
        Create the sampler for the Polynomial Chaos Expansion using
        pseudo-spectral projection or regression (Point Collocation).

        Parameters
        ----------
        vary: dict or None
            keys = parameters to be sampled, values = distributions.

        distribution: cp.Distribution or matrix-like
            Joint distribution specifying dependency between the parameters or
            correlation matrix of the parameters. Depending on the type of the argument
            either Rosenblatt or Cholesky transformation will be used to handle the
            dependent parameters.

        perturbation: float
            Perturbation of the parameters used in the finite difference scheme

        count : int, optional
            Specified counter for Fast forward, default is 0.

        relative_analysis (bool, None), optional
            If True, we add one additional sample with all parameters having zero (nominal) value.
            This is used in the relative analysis, where the model output is represented
            relative to the nominal output, and similarly, the parameters represent the delta of
            the parameter nominal value (i.e. zero represents parameter's nominal value)
        """
        # Create and initialize the logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Logger is already configured, remove all handlers
        if self.logger.hasHandlers():
            self.logger.handlers = []
        
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

        file_handler = logging.FileHandler('FD.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

        #%%%%%%%%%%%%%%%%%  USI DEBUG INFO   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        samplerFile_src = "/Users/Juraj/Documents/DXT/EasyVVUQ-fork/easyvvuq/sampling/FD.py"
        fileStatsObj1 = stat(samplerFile_src)
        modificationTime1 = ctime(fileStatsObj1.st_mtime)
        self.logger.info(f"Using USI version of the FD Sampler {samplerFile_src}")

        samplerFile_lib = path.dirname(path.abspath(__file__))
        fileStatsObj2 = stat(samplerFile_lib)
        modificationTime2 = ctime(fileStatsObj2.st_mtime)

        if (fileStatsObj1.st_mtime > fileStatsObj2.st_mtime):
            self.logger.warning("The EasyVVUQ library does not contain the latest changes in the src")
            self.logger.info(f"Last Modified Time of the source file : {modificationTime1}")
            self.logger.info(f"Last Time of the EasyVVUQ library build : {modificationTime2}")
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        if vary is None:
            msg = ("'vary' cannot be None. RandomSampler must be passed a "
                   "dict of the names of the parameters you want to vary, "
                   "and their corresponding distributions.")
            self.logger.error(msg)
            raise Exception(msg)
        if not isinstance(vary, dict):
            msg = ("'vary' must be a dictionary of the names of the "
                   "parameters you want to vary, and their corresponding "
                   "distributions.")
            self.logger.error(msg)
            raise Exception(msg)
        if len(vary) == 0:
            msg = "'vary' cannot be empty."
            self.logger.error(msg)
            raise Exception(msg)

        self.vary = Vary(vary)

        # List of the probability distributions of uncertain parameters
        params_distribution = list(vary.values())
        params_num = len(params_distribution)

        # Multivariate distribution, the behaviour changes based on the
        # 'distribution' argument, which can be:
        #   None            - use default joint
        #   cp.Distribution - use Rosenblatt if the distribution is dependent
        #   matrix-lie      - use Cholesky
        self._is_dependent = False
        self._transformation = None
        self.distribution_dep = None
        if distribution is None:
            self.logger.info("Using default joint distribution")
            self.distribution = cp.J(*params_distribution)
        elif 'distributions' in str(type(distribution)):
            if distribution.stochastic_dependent:
                assert(isinstance(distribution, cp.MvNormal))
                assert(len(distribution._parameters['mean']) == params_num) # all parameters listed in vary must be in the cp.MvNormal
                self.logger.info("Using user provided joint distribution with Rosenblatt transformation")
                self._is_dependent = True
                self._transformation = "Rosenblatt"
                self.distribution_dep = distribution
            else:
                self.logger.info("Using user provided joint distribution without any transformation")
                self.distribution = distribution
                assert(self._is_dependent == False)
        elif 'list' in str(type(distribution)) or 'ndarray' in str(type(distribution)):
            assert(len(distribution) == params_num) # check the correct size of the corr
            for i in range(params_num):
                assert(distribution[i][i] == 1.0) # must be correlation matrix
            self.logger.info("Using user provided correlation matrix for Cholesky transformation")
            self._is_dependent = True
            self._transformation = "Cholesky"
            self.distribution_dep = np.array(distribution)
            raise NotImplementedError(f'Not tested the Cholesky with respect to scaling of the samples!')
        else:
            self.logger.error("Unsupported type of the distribution argument. It should be either cp.Distribution or a matrix-like array")
            exit()

        # Build independent joint for the dependent distribution
        # Build independent joint multivariate distribution considering each uncertain paramter
        # Use Uniform or Normal distribution depending on the distr. of each parameter
        if not self.distribution_dep is None:
            #params_distribution = [cp.Normal() for i in range(params_num)]
            #params_distribution = [cp.Uniform() for i in range(params_num)]
            #params_distribution = [cp.Uniform() if type(vary_dist).__name__ == "Uniform"
            #                       else cp.Normal()
            #                       for vary_dist in vary.values()]
            params_distribution = [vary_dist for vary_dist in vary.values()]
            self.distribution = cp.J(*params_distribution)
            self.logger.debug(f"The independent distribution consists of: {self.distribution}")

        # Generate the perturbed values of the parameters for the FD
        #FD = 0.5*(y_pos/y_base-1)/(delta) + 0.5*(y_neg/y_base - 1)/(-delta)
        self._n_samples = 2*params_num + 1
        self._perturbation = perturbation

        # Perturbation of the parameters
        if relative_analysis:
            self.logger.info(f"Performing relative perturbation of the nodes, base value = 0, with delta = {perturbation}")
            base_value = np.zeros(params_num)
        else:
            self.logger.info(f"Performing relative perturbation of the nodes, base value = mean, with delta = {perturbation}")
            #base_value = mean_of_the_parameters
            raise NotImplementedError("Set base_value to the mean_of_the_parameters")

        # Create base values of the parameters
        self._nodes = np.array([ base_value[i] * np.ones(self._n_samples) for i in range(params_num)])

        offset = 1 #the first sample is the nominal value at x0
        for p in range(params_num):

            if relative_analysis:
                self._nodes[p][offset]   = perturbation
                self._nodes[p][offset+1] = -perturbation
            else:
                self._nodes[p][offset]   = self._nodes[p][offset] + perturbation*self._nodes[p][offset]
                self._nodes[p][offset+1] = self._nodes[p][offset+1] - perturbation*self._nodes[p][offset+1]
            
            offset = offset + 2
        
        self.logger.info(f"Generated {offset}/{self._n_samples} samples for the FD scheme")

        # Nodes transformation
        regression = True
        if self._is_dependent:
            if self._transformation == "Rosenblatt":
                self.logger.info("Performing Rosenblatt transformation")
                self._nodes_dep = Transformations.rosenblatt(self._nodes, self.distribution, self.distribution_dep, regression)
            elif self._transformation == "Cholesky":
                self.logger.info("Performing Cholesky transformation")
                self._nodes_dep = Transformations.cholesky(self._nodes, self.vary, self.distribution_dep, regression)
            else:
                self.logger.critical("Error: How did this happen? We are transforming the nodes but not with Rosenblatt nor Cholesky")
                exit()

            # # Scale the independent nodes
            # for i, param_dist in enumerate(vary.values()):
            #     if type(param_dist).__name__ == "Normal":
            #         mu = param_dist._parameters['shift'][0]
            #         sigma = param_dist._parameters['scale'][0]
            #         self._nodes[i] = sigma*self._nodes[i] + mu
            #     elif type(param_dist).__name__ == "Uniform":
            #         low = param_dist._parameters['lower'][0]
            #         up = param_dist._parameters['upper'][0]
            #         self._nodes[i] = (up - low)*self._nodes[i] + low
            #     else:
            #         raise NotImplementedError(f'Not supported distribution: {type(param_dist)}!')
                

        #%%%%%%%%%%%%%%%%%  USI DEBUG INFO   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # self.logger.debug(f"Sparse grid:\n{self._nodes}")
        # self.logger.debug(f"Transformed parse grid:\n{self._nodes_dep}")
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # Fast forward to specified count, if possible
        self.count = 0
        if self.count >= self._n_samples:
            msg = (f"Attempt to start sampler fastforwarded to count {self.count}, "
                   f"but sampler only has {self.n_samples} samples, therefore"
                   f"this sampler will not provide any more samples.")
            self.logger.warning(msg)
        else:
            for i in range(count):
                self.__next__()

        # Remember whether to add the extra run
        self.logger.info(f"Performing relative analysis: {relative_analysis}")
        self.relative_analysis = relative_analysis

    def is_finite(self):
        return True

    @property
    def n_samples(self):
        """
        Number of samples (Ns) of PCE method.
        - When using pseudo-spectral projection method with tensored
          quadrature: Ns = (p + 1)**d
        - When using pseudo-spectral projection method with sparce grid
          quadratue: Ns = bigO((p + 1)*log(p + 1)**(d-1))
        - When using regression method: Ns = 2*(p + d)!/p!*d!
        Where: p is the polynomial degree and d is the number of
        uncertain parameters.

        Ref: Eck et al. 'A guide to uncertainty quantification and
        sensitivity analysis for cardiovascular applications' [2016].
        """
        return self._n_samples

    @property
    def analysis_class(self):
        """Return a corresponding analysis class.
        """
        from easyvvuq.analysis import FDAnalysis
        return FDAnalysis

    def __next__(self):
        if self.count < self._n_samples: #base Train samples used to evaluate the PCE
            run_dict = {}
            for i, param_name in enumerate(self.vary.vary_dict):
                # These are nodes that need to be returned as samples o be used for the model execution,
                # for the SA in EasyVVUQ we will use only the raw independent nodes
                if self._is_dependent:
                    # Return transformed nodes reflecting the dependencies
                    run_dict[param_name] = self._nodes_dep[i][self.count]
                else:
                    run_dict[param_name] = self._nodes[i][self.count]
            self.count += 1
            return run_dict
        else:
            raise StopIteration