import logging
import chaospy as cp
from .base import BaseSamplingElement, Vary

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
                 count=0,
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

        self.vary = Vary(vary)
        self.count = count
        self.polynomial_order = polynomial_order
        self.quadrature_rule = quadrature_rule
        self.sparse = sparse

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

    def element_version(self):
        return "0.3"

    def is_finite(self):
        return True

    def is_restartable(self):
        return True

    def __next__(self):
        if self.count < self._number_of_samples:
            run_dict = {}
            i_par = 0
            for param_name in self.vary.get_keys():
                run_dict[param_name] = self._nodes.T[self.count][i_par]
                i_par += 1
            self.count += 1
            return run_dict
        else:
            raise StopIteration

    def get_restart_dict(self):
        return {"vary": self.vary.serialize(),
                "count": self.count,
                "polynomial_order": self.polynomial_order,
                "quadrature_rule": self.quadrature_rule,
                "sparse": self.sparse}
