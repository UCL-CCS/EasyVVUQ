from .base import BaseSamplingElement, Vary
import chaospy as cp
import numpy as np
from itertools import product, chain
import logging

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
                 count=0,
                 growth=False,
                 sparse=False):
        """
        Create the sampler for the Stochastic Collocation method.

        Parameters
        ----------
        vary: dict or None
            keys = parameters to be sampled, values = distributions.
        polynomial_order : int, optional
            The polynomial order, default is 4.

        quadrature_rule : char, optional
            The quadrature method, default is Gaussian "G".

        growth: bool, optional
             Sets the growth rule to exponential for Clenshaw Curtis quadrature,
             which makes it nested, and therefore more efficient for sparse grids.
             Default is False.

        sparse : bool, optional
            If True use sparse grid instead of normal tensor product grid,
            default is False.
        """

        self.vary = Vary(vary)
        self.quadrature_rule = quadrature_rule

        # List of the probability distributions of uncertain parameters
        params_distribution = list(self.vary.get_values())
        # N = number of uncertain parameters
        N = len(params_distribution)

        logging.debug("param dist {}".format(params_distribution))

        # Multivariate distribution
        self.joint_dist = cp.J(*params_distribution)

        # The quadrature information: order, rule and sparsity
        if type(polynomial_order) == int:
            print('Received integer polynomial order, assuming isotropic grid')
            self.polynomial_order = [polynomial_order for i in range(N)]
        else:
            self.polynomial_order = polynomial_order

        self.quad_rule = quadrature_rule
        self.sparse = sparse
        self.quad_sparse = sparse
        self.growth = growth
        self.params_distribution = params_distribution

        # L = level of (sparse) grid
        L = np.max(self.polynomial_order)

        # for every dimension (parameter), create a hierachy of 1D
        # quadrature rules of increasing order
        self.xi_1d = {}
        self.wi_1d = {}

        for n in range(N):
            self.xi_1d[n] = {}
            self.wi_1d[n] = {}

        if sparse:
            for n in range(N):
                for i in range(1, L + 1):
                    xi_i, wi_i = cp.generate_quadrature(i + 1,
                                                        params_distribution[n],
                                                        rule=self.quad_rule,
                                                        growth=self.growth)

                    self.xi_1d[n][i] = xi_i[0]
                    self.wi_1d[n][i] = wi_i
        else:
            for n in range(N):
                xi_i, wi_i = cp.generate_quadrature(self.polynomial_order[n],
                                                    params_distribution[n],
                                                    rule=self.quad_rule,
                                                    growth=self.growth)

                self.xi_1d[n][self.polynomial_order[n]] = xi_i[0]
                self.wi_1d[n][self.polynomial_order[n]] = wi_i

        if not sparse:
            # Generate collocation grid via chaospy
            #NOTE: different poly orders per dimension does not work for all
            #      guadarture rules - use self.generate_grid subroutine instead
            # # the nodes of the collocation grid
            # xi_d, _ = cp.generate_quadrature(self.polynomial_order,
            #                                  self.joint_dist,
            #                                  rule=quadrature_rule)
            # self.xi_d = xi_d.T

            #generate collocation grid locally
            l_norm = np.array([self.polynomial_order])
            self.xi_d = self.generate_grid(L, N, l_norm)

        # sparse grid = a linear combination of tensor products of 1D rules
        # of different order. Use chaospy to compute these 1D quadrature rules
        else:

            # L >= N must hold
            if L < N:
                raise RuntimeError(("Sparse grid level is lower than the number of params. "
                                    "Increase level (via polynomial_order) p such that p-1 >= N"))

            # multi-index l, such that |l| <= L
            l_norm_le_L = self.compute_sparse_multi_idx(L, N)

            # create sparse grid of dimension N and level q using the 1d
            #rules in self.xi_1d
            self.xi_d = self.generate_grid(L, N, l_norm_le_L)

        self.L = L
        self.N = N
        self._number_of_samples = self.xi_d.shape[0]

        # Fast forward to specified count, if possible
        self.count = 0
        if self.count >= self._number_of_samples:
            msg = (f"Attempt to start sampler fastforwarded to count {self.count}, "
                   f"but sampler only has {self._number_of_samples} samples, therefore"
                   f"this sampler will not provide any more samples.")
            logging.warning(msg)
        else:
            for i in range(count):
                self.__next__()

    def element_version(self):
        return "0.4"

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
            "count": self.count,
            "growth": self.growth,
            "sparse": self.sparse}

    """
    =========================
    (SPARSE) GRID SUBROUTINES
    =========================
    """

    def generate_grid(self, L, N, l_norm, **kwargs):

        if 'dimensions' in kwargs:
            dimensions = kwargs['dimensions']
        else:
            dimensions = range(N)

        H_L_N = []
        # loop over all multi indices i
        for l in l_norm:

            # compute the tensor product of nodes indexed by i
            X_l = [self.xi_1d[n][l[n]] for n in dimensions]
            H_L_N.append(list(product(*X_l)))

        # flatten the list of lists
        H_L_N = np.array(list(chain(*H_L_N)))

        # return unique nodes
        return np.unique(H_L_N, axis=0)

    def compute_sparse_multi_idx(self, L, N):
        """
        computes all N dimensional multi-indices l = (l1,...,lN) such that
        |l| <= Q. Here |l| is the internal sum of i (l1+...+lN)
        """
        P = np.array(list(product(range(1, L + 1), repeat=N)))
        l_norm_le_q = P[np.where(np.sum(P, axis=1) <= L)[0]]
        return l_norm_le_q
