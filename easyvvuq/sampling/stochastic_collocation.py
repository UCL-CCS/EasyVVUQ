import logging
from .base import BaseSamplingElement
#import numpy as np
import chaospy as cp
#from itertools import product


# Author: Wouter Edeling

__license__ = "LGPL"


class SCSampler(BaseSamplingElement, sampler_name="sc_sampler"):

    def __init__(self,
                 vary=None,
                 polynomial_order=4,
                 quadrature_rule="G"):
        """
        Create the sampler for the Polynomial Chaos Expansion method.

        Parameters
        ----------
        vary: dict or None
            keys = parameters to be sampled, values = distributions.
        polynomial_order : int, optional
            The polynomial order, default is 4.

        quadrature_rule : char, optional
            The quadrature method, default is Gaussian "G".

        sparse : bool, optional
            If True use sparse grid instead of normal tensor product grid,
            default is False.
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

        self.vary = vary

        # List of the probability distributions of uncertain parameters
        params_distribution = list(vary.values())

        # Multivariate distribution
        self.joint_dist = cp.J(*params_distribution)

        # The quadrature information: order, rule and sparsity
        self.quad_order = polynomial_order + 1
        self.quad_rule = quadrature_rule
        #self.quad_sparse = sparse

        # the nodes of the collocation grid
        xi_d, _ = cp.generate_quadrature(self.quad_order, self.joint_dist, rule=quadrature_rule)

        self.xi_d = xi_d.T

        self._number_of_samples = self.xi_d.shape[0]

        # required counter in generate_runs()
        self.count = 0

    def element_version(self):
        return "0.3"

    def is_finite(self):
        return True

    # SC collocations points are not random, generate_runs simply returns
    # one collocation point from the tensor product after the other
    def generate_runs(self):

        for i_val in range(self._number_of_samples):
            run_dict = {}
            i_par = 0
            for param_name in self.vary.keys():
                run_dict[param_name] = self.xi_d[i_val][i_par]
                i_par += 1

            self.count += 1
            yield run_dict
