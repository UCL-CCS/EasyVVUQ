from .base import BaseSamplingElement, Vary
import chaospy as cp

__author__ = "Wouter Edeling"
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
        self.quad_order = polynomial_order
        self.quad_rule = quadrature_rule
        # self.quad_sparse = sparse

        # the nodes of the collocation grid
        xi_d, _ = cp.generate_quadrature(self.quad_order,
                                         self.joint_dist,
                                         rule=quadrature_rule)

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
