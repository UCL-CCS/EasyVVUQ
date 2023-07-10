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
                 nominal_value=None,
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

        nominal_value : dict, optional
            FD sampler perturbs the base value (NV) of the parameters by the value specified.
            It should be a dict with the keys which are present in vary.
            In case the nominal_value is None, the mean of the distribution is used (assuming cp.Normal).    

        count : int, optional
            Specified counter for Fast forward, default is 0.

        relative_analysis : bool, optional
            Default False, the nodes are perturbed by the value specified in perturbation
            such that n = NV + perturbation. If True, the nodes are perturbed by the relative
            value specified in perturbation such that n = NB * (1 + perturbation).

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

        # Remember whether to add the extra run
        self.logger.info(f"Performing relative analysis: {relative_analysis}")
        self.relative_analysis = relative_analysis
        self._perturbation = perturbation

        # Perturbation of the parameters
        if nominal_value is None:
            self.logger.info(f"Performing perturbation of the nodes, base value = mean, with delta = {perturbation}")
            # Assumes that v is cp.Normal()
            assert(all([type(v) == type(cp.Normal()) for v in vary.values()]))
            nominal_value = {k: v.get_mom_parameters()['shift'][0] for k,v in vary.items()} #Set nominal_value to the mean_of_the_parameters
        else:
            if (len(nominal_value) != params_num):
                msg = ("'nominal_value' must be a 1D array of the same size as the number of parameters.")
                self.logger.error(msg)
                raise ValueError(msg)
            self.logger.info(f"Performing perturbation of the nodes, base value = {nominal_value}, with delta = {perturbation}")            

        # Generate the perturbed values of the parameters for the FD
        #FD = 0.5*(y_pos/y_base-1)/(delta) + 0.5*(y_neg/y_base - 1)/(-delta)
        self.generate_nodes(nominal_value, vary, distribution)

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

        
    def permute_problem(self, perm, mean, sigma, cov):
        # Apply selected permutation to the problem
        nParams = len(mean)
        # cyclic permutation i = perm_step, N = nParams
        # perm = [i i+1 ... N-1 0 1 ... i-1]
        assert(len(perm) == nParams)
        # create permutation matrix
        P = np.eye(nParams)[perm]

        # Model properties that need to be permuted
        mean_ = P@mean
        sigma_ = P@sigma
        cov_ = np.matmul(P, np.matmul(cov, P.transpose()))

        return mean_, sigma_, cov_

    def generate_nodes(self, nominal_value, vary, distribution):
        params_num = len(nominal_value)
        self._n_samples = 2*params_num + 1

        # Multivariate distribution, the behaviour changes based on the
        # 'distribution' argument, which can be:
        #   None            - use default joint
        #   cp.Distribution - use Rosenblatt if the distribution is dependent
        #   matrix-like      - use Cholesky
        self._is_dependent = False
        self._transformation = None
        self.distribution_dep = None
        if 'distributions' in str(type(distribution)):
            if not distribution.stochastic_dependent:
                raise ValueError("User provided joint distribution needs to contain dependency between the parameters")
            if not isinstance(distribution, cp.MvNormal):
                raise ValueError("User provided joint distribution needs to be a cp.MvNormal")
            if not len(distribution._parameters['mean']) == params_num:
                raise ValueError("User provided joint distribution does not contain all the parameters listed in vary")
            self.logger.info("Using user provided joint distribution with Rosenblatt transformation")
            
            self._is_dependent = True
            self._transformation = "Rosenblatt"
            self.distribution_dep = distribution
            
            mu = distribution._parameters['mean']
            cov = distribution._covariance
                
        elif 'list' in str(type(distribution)) or 'ndarray' in str(type(distribution)):
            if not len(distribution) == params_num:
                raise ValueError("User provided correlation matrix does not contain all the parameters listed in vary")
            for i in range(params_num):
                if not distribution[i][i] == 1.0:
                     raise ValueError("User provided correlation matrix is not a correlation matrix (diagonal elements are not 1.0)")            
            self.logger.info("Using user provided correlation matrix for Cholesky transformation")
            
            self._is_dependent = True
            self._transformation = "Cholesky"
            self.distribution_dep = np.array(distribution)
        elif distribution is None:
            pass
        else:
            raise ValueError("Unsupported type of the distribution argument. It should be either cp.Distribution or a matrix-like array")

        # Set up independent perturbations
        #G: [0, d, -d, 0, 0, 0, 0]
        #C: [0, 0, 0, d, -d, 0, 0]
        #E: [0, 0, 0, 0, 0, d, -d]
        self._perturbations = np.zeros((params_num, self._n_samples))
        offset = 1 #the first sample is the nominal value at x0
        for p in range(params_num):
            self._perturbations[p][offset]   = + self._perturbation
            self._perturbations[p][offset+1] = - self._perturbation
            offset = offset + 2

        # Convert perturbation to absolute values
        self._nodes = np.array([ nominal_value[p] * np.ones(self._n_samples) for p in vary.keys() ])
        offset = 1 #the first sample is the nominal value at x0
        for p in range(params_num):

            if self.relative_analysis:
                self._nodes[p][offset]   = (1 + self._perturbations[p][offset]) * self._nodes[p][offset]
                self._nodes[p][offset+1] = (1 + self._perturbations[p][offset+1]) * self._nodes[p][offset+1]
            else:
                self._nodes[p][offset]   = self._nodes[p][offset] + self._perturbations[p][offset]
                self._nodes[p][offset+1] = self._nodes[p][offset+1] + self._perturbations[p][offset+1]
            
            offset = offset + 2

        self.logger.info(f"Generated {offset}/{self._n_samples} samples for the FD scheme")

        # Create perturbed values with correlations
        # dependent Nodes, where di is the induced movement of the parameter i caused by movement in d
        #G: [0, -d,   d,   0, 0,  0, 0]
        #C: [0, -di, di,  -d, d,  0, 0]
        #E: [0, -di, di, -di, di, -d, d]
        if self._is_dependent:

            # Assume permutation [0,1,2]
            perm = [(i) % params_num for i in range(params_num)]
            vary_ = {x: vary[x] for i, x in enumerate([list(vary.keys())[i] for i in perm])}

            if self._transformation == "Rosenblatt":
                self.logger.info("Performing Rosenblatt transformation")

                # Create the dependent distribution
                mean_, _, cov_ = self.permute_problem(perm, mu, np.zeros(params_num), cov)
                distribution_dep_ = cp.MvNormal(mean_, cov_)

                # Create the independent distribution
                params_distribution = [vary_dist for vary_dist in vary_.values()]
                distribution_ = cp.J(*params_distribution)
                
                # This assumes that the order of the parameters in distribution and distribution_dep is the same
                # and the distribution type is cp.Normal
                for id_v, v in enumerate(vary_):
                    assert(type(vary_[v]) == type(cp.Normal()))
                    assert(vary_[v].get_mom_parameters()['shift'][0] == distribution_dep_._parameters['mean'][id_v])
                    assert(vary_[v].get_mom_parameters()['shift'][0] == distribution_[id_v].get_mom_parameters()['shift'][0])
                self.logger.debug(f"The independent distribution consists of: {distribution_}")
                self.logger.debug(f"Using parameter permutation: {list(vary_.keys())}")

                self._nodes_dep = Transformations.rosenblatt(self._nodes, distribution_, distribution_dep_)
                #self._perturbations_dep = Transformations.rosenblatt(self._perturbations, distribution_, distribution_dep_)
            elif self._transformation == "Cholesky":
                self.logger.info("Performing Cholesky transformation")

                _, _, distribution_ = self.permute_problem(perm, np.zeros(params_num), np.zeros(params_num), distribution)
                self._nodes_dep = Transformations.cholesky(self._nodes, vary_, distribution_)
                #self._perturbations_dep = Transformations.cholesky(self._perturbations, vary_, distribution_)
            else:
                self.logger.critical("Error: How did this happen? We are transforming the nodes but not with Rosenblatt nor Cholesky")
                exit()
        
        return


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