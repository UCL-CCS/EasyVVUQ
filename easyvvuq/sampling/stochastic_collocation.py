import logging
from .base import BaseSamplingElement, Vary
#import numpy as np
import chaospy as cp
#from itertools import product


# Author: Wouter Edeling

__license__ = "LGPL"


class SCSampler(BaseSamplingElement, sampler_name="sc_sampler"):

    def __init__(self,
                 vary=None,
                 polynomial_order=4,
                 quadrature_rule="G",
                 count=0):
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

        self.vary = Vary(vary)
        self.polynomial_order = polynomial_order
        self.quadrature_rule = quadrature_rule
        self.count = count

        # List of the probability distributions of uncertain parameters
        params_distribution = list(self.vary.get_values())

        print("param dist", params_distribution)

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

    def element_version(self):
        return "0.3"

    def is_finite(self):
        return True

    # SC collocations points are not random, generate_runs simply returns
    # one collocation point from the tensor product after the other
    def __next__(self):
        if self.count < self._number_of_samples:
            run_dict = {}
            i_par = 0
            for param_name in self.vary.get_keys():
                run_dict[param_name] = self.xi_d[self.count][i_par]
                i_par += 1
            self.count += 1
            return run_dict
        else:
            raise StopIteration

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {
            "vary": self.vary.serialize(),
            "polynomial_order": self.polynomial_order,
            "quadrature_rule": self.quadrature_rule,
            "count": self.count}
