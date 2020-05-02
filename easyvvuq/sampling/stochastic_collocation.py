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
                 sparse=False,
                 midpoint_level1 = False):
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
        if isinstance(polynomial_order, int):
            print('Received integer polynomial order, assuming isotropic grid')
            self.polynomial_order = [polynomial_order for i in range(N)]
        else:
            self.polynomial_order = polynomial_order

        self.quad_rule = quadrature_rule
        self.sparse = sparse
        #determines how many points the 1st level of a sparse grid will have.
        #If midpoint_level1 = True, order 0 quadrature will be generated
        self.midpoint_level1 = midpoint_level1
        self.quad_sparse = sparse
        self.growth = growth
        self.params_distribution = params_distribution

        #determine if a nested sparse grid is used
        if self.sparse is True and self.growth is True and (self.quad_rule == "C" or self.quad_rule == "clenshaw_curtis"):
            self.nested = True
        elif self.sparse is True and self.growth is False and self.quad_rule == "gauss_patterson":
            self.nested = True
        elif self.sparse is True and self.growth is True and self.quad_rule == "newton_cotes":
            self.nested = True
        else:
            self.nested = False

        # L = level of (sparse) grid
        L = np.max(self.polynomial_order)

        #compute the 1D collocation points (and quad weights)
        self.compute_1D_points_weights(L, N)

        #compute N-dimensional collocation points
        if not self.sparse:

            # generate collocation grid locally
            l_norm = np.array([self.polynomial_order])
            self.xi_d = self.generate_grid(L, N, l_norm)

        # sparse grid = a linear combination of tensor products of 1D rules
        # of different order. Use chaospy to compute these 1D quadrature rules
        else:

            # simplex set of multi indices
            multi_idx = self.compute_sparse_multi_idx(L, N)

            # create sparse grid of dimension N and level q using the 1d
            #rules in self.xi_1d
            self.xi_d = self.generate_grid(L, N, multi_idx)

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

    def compute_1D_points_weights(self, L, N):
        """
        Computes 1D collocation points and quad weights,
        and stores this in self.xi_1d, self.wi_1d.

        Parameters
        ----------
        L : (int) the max level of the (sparse) grid
        N : (int) the number of uncertain parameters

        Returns
        -------
        None.

        """
        # for every dimension (parameter), create a hierachy of 1D
        # quadrature rules of increasing order
        self.xi_1d = [{} for n in range(N)]
        self.wi_1d = [{} for n in range(N)]

        if self.sparse:

            #if level one of the sparse grid is a midpoint rule, generate
            #the quadrature with order 0 (1 quad point). Else set order at
            #level 1 to 1
            if self.midpoint_level1:
                j = 0
            else:
                j = 1

            for n in range(N):
                for i in range(L):
                    xi_i, wi_i = cp.generate_quadrature(i + j,
                                                        self.params_distribution[n],
                                                        rule=self.quad_rule,
                                                        growth=self.growth)

                    self.xi_1d[n][i + 1] = xi_i[0]
                    self.wi_1d[n][i + 1] = wi_i
        else:
            for n in range(N):
                xi_i, wi_i = cp.generate_quadrature(self.polynomial_order[n],
                                                    self.params_distribution[n],
                                                    rule=self.quad_rule,
                                                    growth=self.growth)

                self.xi_1d[n][self.polynomial_order[n]] = xi_i[0]
                self.wi_1d[n][self.polynomial_order[n]] = wi_i

    def next_level_sparse_grid(self):
        """
        Adds the points of the next level for hierarchical sparse grids.

        Returns
        -------
        None.

        """

        if self.nested is False:
            logging.debug('Only works for nested sparse grids')
            return

        #update level of sparse grid
        L = np.max(self.polynomial_order) + 1
        self.polynomial_order = [p + 1 for p in self.polynomial_order]

        print('Moving grid from level %d to level %d' % (L - 1, L))

        #compute all multi indices
        multi_idx = self.compute_sparse_multi_idx(L, self.N)

        #find only the indices of the new level (|l| = L + N - 1)
        new = np.where(np.sum(multi_idx, axis=1) == L + self.N - 1)[0]

        #update the 1D points and weights
        self.compute_1D_points_weights(L, self.N)

        #generate the new N-dimensional collocation points
        new_points = self.generate_grid(L, self.N, multi_idx[new])

        print('%d new points added' % new_points.shape[0])

        #update the number of samples
        self._number_of_samples += new_points.shape[0]

        #update the N-dimensional sparse grid
        self.xi_d = np.concatenate((self.xi_d, new_points))

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

    def generate_grid(self, L, N, l_norm):

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
        |l| <= L + N - 1, i.e. a simplex set:
        3    *
        2    *    *          (L=3 and N=2)
        1    *    *    *
             1    2    3
        Here |l| is the internal sum of i (l1+...+lN)
        """
        P = np.array(list(product(range(1, L + 1), repeat=N)))
        multi_idx = P[np.where(np.sum(P, axis=1) <= L + N - 1)[0]]
        return multi_idx
