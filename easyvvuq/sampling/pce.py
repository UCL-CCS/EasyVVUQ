import logging
import chaospy as cp
import numpy as np
import random
from .base import BaseSamplingElement, Vary
from .transformations import Transformations

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
                 growth=False,
                 relative_analysis=False,
                 nominal_value=None):
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

        relative_analysis (bool, None), optional
            If True, we add one additional sample with all parameters having zero (nominal) value.
            This is used in the relative analysis, where the model output is represented
            relative to the nominal output, and similarly, the parameters represent the delta of
            the parameter nominal value (i.e. zero represents parameter's nominal value, nominal + delta*nominal)

        nominal_value : dict, optional
            Evaluate derivative of the model at the nominal value of the parameters.
            It should be a dict with the keys which are present in vary.
            In case the base_value is None, the mean of the distribution is used (assuming cp.Normal).    
        """

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

        # Remember whether to add the extra run using the base value of the parameters (0 corresponding to the mean)
        logging.info(f"Performing relative analysis: {relative_analysis}")
        self.relative_analysis = relative_analysis

        self.vary = Vary(vary)
        self.polynomial_order = polynomial_order

        # List of the probability distributions of uncertain parameters
        self.params_distribution = list(vary.values())
        params_num = len(self.params_distribution)

        # Nominal value of the parameters
        if nominal_value is None:
            # Assumes that v is cp.Normal()
            if (all([type(v) == type(cp.Normal()) for v in vary.values()])):
                nominal_value = {k: v.get_mom_parameters()['shift'][0] for k,v in vary.items()} #Set nominal_value to the mean_of_the_parameters
                logging.info(f"Using parameter mean for the relative analysis {nominal_value}")
        else:
            if (len(nominal_value) != params_num):
                msg = ("'nominal_value' must be a 1D array of the same size as the number of parameters.")
                logging.error(msg)
                raise ValueError(msg)
            logging.info(f"Using user-provided nominal value for relative analysis {nominal_value}")
        self.nominal_value = nominal_value

        # Multivariate distribution, the behaviour changes based on the
        # 'distribution' argument, which can be:
        #   None            - use default joint
        #   cp.Distribution - use Rosenblatt if the distribution is dependent
        #   matrix-lie      - use Cholesky
        self._is_dependent = False
        self._transformation = None
        self.distribution_dep = None
        if distribution is None:
            logging.info("Using default joint distribution")
            self.distribution = cp.J(*self.params_distribution)
        elif 'distributions' in str(type(distribution)):
            if distribution.stochastic_dependent:
                if not isinstance(distribution, cp.MvNormal):
                    raise ValueError("User provided joint distribution needs to be a cp.MvNormal")
                if not len(distribution._parameters['mean']) == params_num:
                    raise ValueError("User provided joint distribution does not contain all the parameters listed in vary")
                logging.info("Using user provided joint distribution with Rosenblatt transformation")
                
                self._is_dependent = True
                self._transformation = "Rosenblatt"
                self.distribution_dep = distribution
            else:
                logging.info("Using user provided joint distribution without any transformation")
                self.distribution = distribution
                assert(self._is_dependent == False)
        elif 'list' in str(type(distribution)) or 'ndarray' in str(type(distribution)):
            if not len(distribution) == params_num:
                raise ValueError("User provided correlation matrix does not contain all the parameters listed in vary")
            for i in range(params_num):
                if not distribution[i][i] == 1.0:
                     raise ValueError("User provided correlation matrix is not a correlation matrix (diagonal elements are not 1.0)")            
            logging.info("Using user provided correlation matrix for Cholesky transformation")
            
            self._is_dependent = True
            self._transformation = "Cholesky"
            self.distribution_dep = np.array(distribution)
        else:
            logging.error("Unsupported type of the distribution argument. It should be either cp.Distribution or a matrix-like array")
            exit()

        # Build independent joint multivariate distribution considering each uncertain paramter
        if not self.distribution_dep is None:
            
            params_distribution = [vary_dist for vary_dist in vary.values()]
            self.distribution = cp.J(*params_distribution)
            
            # This assumes that the order of the parameters in distribution and distribution_dep is the same
            # and the distribution type is cp.Normal
            for id_v, v in enumerate(vary):
                assert(type(vary[v]) == type(cp.Normal()))
                if self._transformation == "Rosenblatt":
                    assert(vary[v].get_mom_parameters()['shift'][0] == self.distribution_dep._parameters['mean'][id_v])
                    assert(vary[v].get_mom_parameters()['shift'][0] == self.distribution[id_v].get_mom_parameters()['shift'][0])
            logging.debug(f"The independent distribution consists of: {self.distribution}")
            logging.debug(f"Using parameter permutation: {list(vary.keys())}")

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

        # To determinate the PCE vraint to use
        self.regression = regression

        # indices of cp.DiscreteUniform parameters
        idx_discrete = np.where([isinstance(p, cp.DiscreteUniform) for p in self.params_distribution])[0]

        # Regression variante (Point collocation method)
        if regression:
            logging.info(f"Using point collocation method to create PCE")
            # Change the default rule
            if rule == "G":
                self.rule = "M"

            # Generates samples
            self._n_samples = 2 * len(self.P)
            logging.info(f"Generating {self._n_samples} samples using {self.rule} rule")
            self._nodes = cp.generate_samples(order=self._n_samples,
                                              domain=self.distribution,
                                              rule=self.rule)
            
            # Transform relative nodes to absolute nodes
            if self.relative_analysis:
                for pi,p in enumerate(vary.keys()):
                    self._nodes[pi] = (1.0 + self._nodes[pi]) * nominal_value[p] 

            self._weights = None

            # Nodes transformation
            if self._is_dependent:
                if self._transformation == "Rosenblatt":
                    logging.info("Performing Rosenblatt transformation")
                    self._nodes_dep = Transformations.rosenblatt(self._nodes, self.distribution, self.distribution_dep, regression)
                elif self._transformation == "Cholesky":
                    logging.info("Performing Cholesky transformation")
                    self._nodes_dep = Transformations.cholesky(self._nodes, self.vary, self.distribution_dep, regression)
                else:
                    logging.critical("Error: How did this happen? We are transforming the nodes but not with Rosenblatt nor Cholesky")
                    exit()

        # Projection variante (Pseudo-spectral method)
        else:
            if type(self.rule) is str and idx_discrete.size > 0:
                tmp = []
                for i in range(params_num):
                    if i in idx_discrete:
                        tmp.append("discrete")
                    else:
                        tmp.append(rule)
                self.rule = tmp

            logging.info(f"Using pseudo-spectral method to create PCE")
            # Nodes and weights for the integration
            self._nodes, self._weights = cp.generate_quadrature(order=polynomial_order,
                                                                dist=self.distribution,
                                                                rule=self.rule,
                                                                sparse=sparse,
                                                                growth=self.quad_growth)
            # Number of samples
            self._n_samples = len(self._nodes[0])
            logging.info(f"Generated {self._n_samples} nodes/weights pairs using {self.rule} rule")

            # Nodes transformation
            if self._is_dependent:
                # Scale the independent nodes
                raise NotImplementedError(f'Transformation of the independent nodes not supported with {regression = }')

            if self.relative_analysis:
                raise NotImplementedError(f'Transformation of the relative nodes not supported with {regression = }')
            
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
        if self.count < self._n_samples: #base Train samples used to evaluate the PCE
            run_dict = {}
            for i, param_name in enumerate(self.vary.vary_dict):
                # These are nodes that need to be returned as samples o be used for the model execution,
                # for the SA in EasyVVUQ we will use only the raw independent nodes
                if self._is_dependent:
                    # Return transformed nodes reflecting the dependencies
                    run_dict[param_name] = self._nodes_dep[i][self.count]
                else:
                    current_param = self._nodes[i][self.count]
                    # all parameters self.xi_d will store floats. If current param is
                    # DiscreteUniform, convert e.g. 2.0 to 2 before running
                    # the simulation.
                    if isinstance(self.params_distribution[i], cp.DiscreteUniform):
                        current_param = int(current_param)
                    run_dict[param_name] = current_param
            self.count += 1
            return run_dict
        elif self.relative_analysis and self.count == self._n_samples: #extra sample for the nominal case
            run_dict = self.nominal_value
            self.count += 1
            return run_dict
        else:
            raise StopIteration