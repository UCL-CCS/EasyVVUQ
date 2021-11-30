import logging
import chaospy as cp
import numpy as np
from .base import BaseSamplingElement, Vary

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


class PCESampler(BaseSamplingElement, sampler_name="PCE_sampler"):
    def __init__(self,
                 vary=None,
                 distribution=None,
                 count=0,
                 polynomial_order=4,
                 regression=False,
                 rule="G",
                 sparse=False,
                 growth=False):
        """
        Create the sampler for the Polynomial Chaos Expansion using
        pseudo-spectral projection or regression (Point Collocation).

        Parameters
        ----------
        vary: dict or None
            keys = parameters to be sampled, values = distributions.

        distribution: cp.Distribution or matrix-like
            Joint distribution specifying dependency between the parameters in vary or
            correlation matrix of the variables. Depending on the type of the parameter
            either Rosenblatt or Cholesky transformation will be used to handle the
            dependent parameters.

        count : int, optional
            Specified counter for Fast forward, default is 0.

        polynomial_order : int, optional
            The polynomial order, default is 4.

        regression : bool, optional
            If True, regression variante (point collecation) will be used,
            otherwise projection variante (pseud-spectral) will be used.
            Default value is False.

        rule : char, optional
            The quadrature method, in case of projection (default is Gaussian "G").
            The sequence sampler in case of regression (default is Hammersley "M")

        sparse : bool, optional
            If True, use Smolyak sparse grid instead of normal tensor product
            grid. Default value is False.

        growth (bool, None), optional
            If True, quadrature point became nested.
        """

        #%%%%%%%%%%%%%%%%%  USI DEBUG INFO   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        samplerFile_src = "/Users/Juraj/Documents/DXT/EasyVVUQ-fork/easyvvuq/sampling/pce.py"
        fileStatsObj = stat(samplerFile_src)
        modificationTime1 = ctime(fileStatsObj.st_mtime)
        print("Using USI version of the PCE Sampler %s" % (samplerFile_src))
        print("Last Modified Time of the source file : ", modificationTime1 )

        samplerFile_lib = path.dirname(path.abspath(__file__))
        fileStatsObj = stat(samplerFile_lib)
        modificationTime2 = ctime(fileStatsObj.st_mtime)
        print("Last Time of the EasyVVUQ library build : ", modificationTime2)

        if (modificationTime1 > modificationTime2):
            print("Warning: The EasyVVUQ library does not contain the latest changes in the src")
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        if vary is None:
            msg = ("'vary' cannot be None. RandomSampler must be passed a "
                   "dict of the names of the parameters you want to vary, "
                   "and their corresponding distributions.")
            logging.error(msg)
            raise Exception(msg)
        if not isinstance(vary, dict):
            msg = ("'vary' must be a dictionary of the names of the "
                   "parameters you want to vary, and their corresponding "
                   "distributions.")
            logging.error(msg)
            raise Exception(msg)
        if len(vary) == 0:
            msg = "'vary' cannot be empty."
            logging.error(msg)
            raise Exception(msg)

        self.vary = Vary(vary)
        self.polynomial_order = polynomial_order

        # List of the probability distributions of uncertain parameters
        params_distribution = list(vary.values())
        params_num = len(params_distribution)

        # Multivariate distribution
        self._is_dependent = False
        self._transformation = None
        self.distribution_dep = None
        if distribution is None:
            print("Using default joint distribution")
            self.distribution = cp.J(*params_distribution)
        elif 'distributions' in str(type(distribution)):
            if distribution.stochastic_dependent:
                assert(isinstance(distribution, cp.MvNormal))
                assert(len(distribution._parameters['mean']) == params_num) # all parameters listed in vary must be in the cp.MvNormal
                print("Using user provided joint distribution with Rosenblatt transformation")
                self._is_dependent = True
                self._transformation = "Rosenblatt"
                self.distribution_dep = distribution
                # Build joint multivariate distribution considering each uncertain paramter as a unit Normal
                params_distribution = [cp.Normal() for i in range(params_num)]
                self.distribution = cp.J(*params_distribution)
            else:
                print("Using user provided joint distribution without any transformation")
                self.distribution = distribution
        elif 'list' in str(type(distribution)) or 'ndarray' in str(type(distribution)):
            assert(len(distribution) == params_num) # check the correct size of the corr
            for i in range(params_num):
                assert(distribution[i][i] == 1.0) # must be correlation matrix
            print("Using user provided correlation matrix for Cholesky transformation")
            self._is_dependent = True
            self._transformation = "Cholesky"
            self.distribution_dep = np.array(distribution)
            # Build joint multivariate distribution considering each uncertain paramter as a unit Normal
            params_distribution = [cp.Normal() for i in range(params_num)]
            self.distribution = cp.J(*params_distribution)
        else:
            print("Unsupported type of the distribution argument. It should be either cp.distribution or a matrix-like array")
            exit()

        # The orthogonal polynomials corresponding to the joint distribution
        self.P = cp.expansion.stieltjes(polynomial_order, self.distribution, normed=True)

        # The quadrature information
        self.quad_sparse = sparse
        self.rule = rule

        # Clenshaw-Curtis should be nested if sparse (#139 chaospy issue)
        self.quad_growth = growth
        cc = ['c', 'C', 'clenshaw_curtis', 'Clenshaw_Curtis']
        if sparse and rule in cc:
            self.quad_growth = True

        # To determinate the PCE vrainte to use
        self.regression = regression

        # Regression variante (Point collocation method)
        if regression:
            # Change the default rule
            if rule == "G":
                self.rule = "M"

            # Generates samples
            self._n_samples = 2 * len(self.P)
            print("Generating %d samples using %s rule" % (self._n_samples, self.rule))
            self._nodes = cp.generate_samples(order=self._n_samples,
                                              domain=self.distribution,
                                              rule=self.rule)

            self._weights = None

            # Nodes transformation
            if self._is_dependent:
                if self._transformation == "Rosenblatt":
                    print("Performing Rosenblatt transformation")
                    self._nodes_dep = self.distribution_dep.inv(self.distribution.fwd(self._nodes))
                elif self._transformation == "Cholesky":
                    print("Performing Cholesky transformation")
                    L = np.linalg.cholesky(self.distribution_dep)
                    self._nodes_dep = np.matmul(L, self._nodes)
                    for i, key in enumerate(vary.keys()):
                        a = vary[key]._parameters['shift'] #mu
                        b = vary[key]._parameters['scale'] #sigma
                        self._nodes_dep[i] = a + b*self._nodes_dep[i]
                else:
                    print("Error: How did this happen?")
                    exit()


            #%%%%%%%%%%%%%%%%%  USI DEBUG INFO   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            print("Dumping nodes to /Users/Juraj/Documents/DXT/EasyVVUQ-fork/nodes_EasyVVUQ.txt")
            f = open("/Users/Juraj/Documents/DXT/EasyVVUQ-fork/nodes_EasyVVUQ.txt", "w")
            f.write(json.dumps(list(list(r) for r in self._nodes)))
            f.close()
            #diff /Users/Juraj/Documents/DXT/MPSProject_USI/github/MPSProject_Standalone/chaospy/nodes_chaospy.txt /Users/Juraj/Documents/DXT/EasyVVUQ-fork/nodes_EasyVVUQ.txt
            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # Projection variante (Pseudo-spectral method)
        else:
            # Nodes and weights for the integration
            self._nodes, self._weights = cp.generate_quadrature(order=polynomial_order,
                                                                dist=self.distribution,
                                                                rule=self.rule,
                                                                sparse=sparse,
                                                                growth=self.quad_growth)
            # Number of samples
            self._n_samples = len(self._nodes[0])
            print("Generated %d nodes/weights pairs using %s rule" % (self._n_samples, self.rule))

            # Nodes transformation
            if self._is_dependent:
                if self._transformation == "Rosenblatt":
                    print("Performing Rosenblatt transformation")
                    self._nodes_dep = self.distribution_dep.inv(self.distribution.fwd(self._nodes))
                    self._weights_dep = self._weights * self.distribution_dep.pdf(self._nodes_dep)/self.distribution.pdf(self._nodes)
                elif self._transformation == "Cholesky":
                    print("Performing Cholesky transformation")
                    print("Error: not implemented with pseudo-spectral method")
                    exit()
                else:
                    print("Error: How did this happen?")
                    exit()
                

        # Fast forward to specified count, if possible
        self.count = 0
        if self.count >= self._n_samples:
            msg = (f"Attempt to start sampler fastforwarded to count {self.count}, "
                   f"but sampler only has {self.n_samples} samples, therefore"
                   f"this sampler will not provide any more samples.")
            logging.warning(msg)
        else:
            for i in range(count):
                self.__next__()

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
        from easyvvuq.analysis import PCEAnalysis
        return PCEAnalysis

    def __next__(self):
        if self.count < self._n_samples:
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
