import logging
import numpy as np
import chaospy as cp
from .base import BaseSamplingElement
import json

# author: Jalal Lakhlili
__license__ = "LGPL"


class PCESampler(BaseSamplingElement, sampler_name="PCE_sampler"):
    def __init__(self,
                 vary=None,
                 polynomial_order=4,
                 quadrature_rule="G",
                 sparse=False):
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
        self.distribution = cp.J(*params_distribution)

        # The orthogonal polynomials corresponding to the joint distribution
        self.P = cp.orth_ttr(polynomial_order, self.distribution)

        # The quadrature information: order, rule and sparsity
        self.quad_order = polynomial_order + 1
        self.quad_rule = quadrature_rule
        self.quad_sparse = sparse

        # Nodes and weights for the integration
        self._nodes, _ = cp.generate_quadrature(order=self.quad_order,
                                                domain=self.distribution,
                                                rule=quadrature_rule,
                                                sparse=sparse)

        # Number of samples
        self._number_of_samples = len(self._nodes[0])

        # Keep track of how many samples we have drawn
        self.count = 0

    def element_version(self):
        return "0.3"

    def is_finite(self):
        return True

    def generate_runs(self):

        for i_val in range(self._number_of_samples):
            run_dict = {}
            i_par = 0
            for param_name in self.vary.keys():
                run_dict[param_name] = self._nodes.T[i_val][i_par]
                i_par += 1

            self.count += 1
            yield run_dict

    def get_restart_dict(self):
        return json.dumps({"count": self.count})
