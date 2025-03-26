from .base import BaseSamplingElement, Vary
import chaospy as cp
import numpy as np
import pickle
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
    """
    Stochastic Collocation sampler
    """

    def __init__(self,
                 vary=None,
                 polynomial_order=4,
                 quadrature_rule="G",
                 count=0,
                 growth=False,
                 sparse=False,
                 midpoint_level1=True,
                 dimension_adaptive=False):
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

        midpoint_level1 : bool, optional
            Used only for sparse=True (or for cp.DiscreteUniform distribution).
            Determines how many points the 1st level of a sparse grid will have.
            If True, order 0 quadrature will be generated,
            default is True.

        dimension_adaptive : bool, optional
            Determines wether to use an insotropic sparse grid, or to
            adapt the levels in the sparse grid based on a hierachical
            error measure, default is False.
        """

        self.vary = Vary(vary)

        # List of the probability distributions of uncertain parameters
        self.params_distribution = list(self.vary.get_values())
        # N = number of uncertain parameters
        self.N = len(self.params_distribution)

        logging.debug("param dist {}".format(self.params_distribution))


        self.joint_dist = cp.J(*self.params_distribution)

        # The quadrature information: order, rule and sparsity
        if isinstance(polynomial_order, int):
            logging.debug('Received integer polynomial order, assuming isotropic grid')
            self.polynomial_order = [polynomial_order for i in range(self.N)]
        else:
            self.polynomial_order = polynomial_order

        self.quad_rule = quadrature_rule
        self.sparse = sparse
        self.midpoint_level1 = midpoint_level1
        self.dimension_adaptive = dimension_adaptive
        self.nadaptations = 0
        self.growth = growth
        self.check_max_quad_level()

        # determine if a nested sparse grid is used
        if self.sparse is True and self.growth is True and \
           (self.quad_rule == "C" or self.quad_rule == "clenshaw_curtis"):
            self.nested = True
        elif self.sparse is True and self.growth is False and self.quad_rule == "gauss_patterson":
            self.nested = True
        elif self.sparse is True and self.growth is True and self.quad_rule == "newton_cotes":
            self.nested = True
        else:
            self.nested = False

        # L = level of (sparse) grid
        self.L = np.max(self.polynomial_order)

        # compute the 1D collocation points (and quad weights)
        self.compute_1D_points_weights(self.L, self.N)

        # compute N-dimensional collocation points
        if not self.sparse:

            # generate collocation as a standard tensor product
            l_norm = np.array([self.polynomial_order])
            self.xi_d = self.generate_grid(l_norm)

        else:
            self.l_norm = self.compute_sparse_multi_idx(self.L, self.N)
            # create sparse grid of dimension N and level q using the 1d
            # rules in self.xi_1d
            self.xi_d = self.generate_grid(self.l_norm)

        self._n_samples = self.xi_d.shape[0]

        self.count = 0

    @property
    def analysis_class(self):
        """Return a corresponding analysis class.
        """
        from easyvvuq.analysis import SCAnalysis
        return SCAnalysis

    def compute_1D_points_weights(self, L, N):
        """
        Computes 1D collocation points and quad weights,
        and stores this in self.xi_1d, self.wi_1d.

        Parameters
        ----------
        L : (int) the max polynomial order of the (sparse) grid
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

            # if level one of the sparse grid is a midpoint rule, generate
            # the quadrature with order 0 (1 quad point). Else set order at
            # level 1 to 1
            if self.midpoint_level1:
                j = 0
            else:
                j = 1

            for n in range(N):
                # check if input is discrete uniform, in which case the
                # rule and growth flag must be modified
                if isinstance(self.params_distribution[n], cp.DiscreteUniform):
                    rule = "discrete"
                else:
                    rule = self.quad_rule

                for i in range(L):
                    xi_i, wi_i = cp.generate_quadrature(i + j,
                                                        self.params_distribution[n],
                                                        rule=rule,
                                                        growth=self.growth)
                    self.xi_1d[n][i + 1] = xi_i[0]
                    self.wi_1d[n][i + 1] = wi_i
        else:
            for n in range(N):
                # check if input is discrete uniform, in which case the
                # rule flag must be modified
                if isinstance(self.params_distribution[n], cp.DiscreteUniform):
                    rule = "discrete"
                else:
                    rule = self.quad_rule

                xi_i, wi_i = cp.generate_quadrature(self.polynomial_order[n],
                                                    self.params_distribution[n],
                                                    rule=rule,
                                                    growth=self.growth) 

                self.xi_1d[n][self.polynomial_order[n]] = xi_i[0]
                self.wi_1d[n][self.polynomial_order[n]] = wi_i

    def check_max_quad_level(self):
        """

        If a discrete variable is specified, there is the possibility of
        non unique collocation points if the quadrature order is high enough.
        This subroutine prevents that.

        NOTE: Only detects cp.DiscreteUniform thus far

        The max quad orders are stores in self.max_quad_order

        Returns
        -------
        None

        """
        # assume no maximum by default
        self.max_level = np.ones(self.N) * 1000
        for n in range(self.N):

            # if a discrete uniform is specified check max order
            if isinstance(self.params_distribution[n], cp.DiscreteUniform):

                #TODO: it is assumed that self.sparse=True, but this assumption
                #does not have to hold here!!!

                # if level one of the sparse grid is a midpoint rule, generate
                # the quadrature with order 0 (1 quad point). Else set order at
                # level 1 to 1
                if self.midpoint_level1:
                    j = 0
                else:
                    j = 1

                number_of_points = 0
                for order in range(1000):
                    xi_i, wi_i = cp.generate_quadrature(order + j,
                                                        self.params_distribution[n],
                                                        growth=self.growth)
                    # if the quadrature points no longer grow with the quad order,
                    # then the max order has been reached
                    if xi_i.size == number_of_points:
                        break
                    number_of_points = xi_i.size

                logging.debug("Input %d is discrete, setting max quadrature order to %d"
                              % (n, order - 1))
                # level 1 = order 0 etc
                self.max_level[n] = order

    def next_level_sparse_grid(self):
        """
        Adds the points of the next level for isotropic hierarchical sparse grids.

        Returns
        -------
        None.

        """

        if self.nested is False:
            print('Only works for nested sparse grids')
            return

        self.look_ahead(self.l_norm)
        self.l_norm = np.append(self.l_norm, self.admissible_idx, axis=0)

    def look_ahead(self, current_multi_idx):
        """
        The look-ahead step in (dimension-adaptive) sparse grid sampling. Allows
        for anisotropic sampling plans.

        Computes the admissible forward neighbors with respect to the current level
        multi-indices. The admissible level indices l are added to self.admissible_idx.
        The code will be evaluated next iteration at the new collocation points
        corresponding to the levels in admissble_idx.

        Source: Gerstner, Griebel, "Numerical integration using sparse grids"

        Parameters
        ----------
        current_multi_idx : array of the levels in the current iteration
        of the sparse grid.

        Returns
        -------
        None.

        """

        # compute all forward neighbors for every l in current_multi_idx
        forward_neighbor = []
        e_n = np.eye(self.N, dtype=int)
        for l in current_multi_idx:
            for n in range(self.N):
                # the forward neighbor is l plus a unit vector
                forward_neighbor.append(l + e_n[n])

        # remove duplicates
        forward_neighbor = np.unique(np.array(forward_neighbor), axis=0)
        # remove those which are already in the grid
        forward_neighbor = setdiff2d(forward_neighbor, current_multi_idx)
        # make sure the final candidates are admissible (all backward neighbors
        # must be in the current multi indices)
        logging.debug('Computing admissible levels...')
        admissible_idx = []
        for l in forward_neighbor:
            admissible = True
            for n in range(self.N):
                backward_neighbor = l - e_n[n]
                # find backward_neighbor in current_multi_idx
                idx = np.where((backward_neighbor == current_multi_idx).all(axis=1))[0]
                # if backward neighbor is not in the current index set
                # and it is 'on the interior' (contains no 0): not admissible
                if idx.size == 0 and backward_neighbor[n] != 0:
                    admissible = False
                    break
            # if all backward neighbors are in the current index set: l is admissible
            if admissible:
                admissible_idx.append(l)
        logging.debug('done')

        self.admissible_idx = np.array(admissible_idx)
        # make sure that all entries of each index are <= the max quadrature order
        # The max quad order can be low for discrete input variables
        idx = np.where((self.admissible_idx <= self.max_level).all(axis=1))[0]
        self.admissible_idx = self.admissible_idx[idx]
        logging.debug('Admissible multi-indices:\n%s', self.admissible_idx)

        # determine the maximum level L of the new index set L = |l| - N + 1
        # self.L = np.max(np.sum(self.admissible_idx, axis=1) - self.N + 1)
        self.L = np.max(self.admissible_idx)
        # recompute the 1D weights and collocation points
        self.compute_1D_points_weights(self.L, self.N)
        # compute collocation grid based on the admissible level indices
        admissible_grid = self.generate_grid(self.admissible_idx)
        # remove collocation points which have already been computed
        if not hasattr(self, 'xi_d'):
            self.xi_d = self.generate_grid(self.admissible_idx)
            self._n_samples = self.xi_d.shape[0]
        new_points = setdiff2d(admissible_grid, self.xi_d)

        logging.debug('%d new points added' % new_points.shape[0])

        # keep track of the number of points added per iteration
        if not hasattr(self, 'n_new_points'):
            self.n_new_points = []
        self.n_new_points.append(new_points.shape[0])

        # update the number of samples
        self._n_samples += new_points.shape[0]

        # update the N-dimensional sparse grid if unsampled points are added
        if new_points.shape[0] > 0:
            self.xi_d = np.concatenate((self.xi_d, new_points))

        # count the number of times the dimensions were adapted
        self.nadaptations += 1

    def is_finite(self):
        return True

    @property
    def n_samples(self):
        """
        Number of samples (Ns) of SC method.
        - When using tensor quadrature: Ns = (p + 1)**d
        - When using sparid: Ns = bigO((p + 1)*log(p + 1)**(d-1))
        Where: p is the polynomial degree and d is the number of
        uncertain parameters.

        Ref: Eck et al. 'A guide to uncertainty quantification and
        sensitivity analysis for cardiovascular applications' [2016].
        """
        return self._n_samples

    # SC collocations points are not random, generate_runs simply returns
    # one collocation point from the tensor product after the other
    def __next__(self):
        if self.count < self._n_samples:
            run_dict = {}
            i_par = 0
            for param_name in self.vary.get_keys():
                # the current input parameter
                current_param = self.xi_d[self.count][i_par]
                # all parameters self.xi_d will store floats. If current param is
                # DiscreteUniform, convert e.g. 2.0 to 2 before running
                # the simulation.
                if isinstance(self.params_distribution[i_par], cp.DiscreteUniform):
                    current_param = int(current_param)
                run_dict[param_name] = current_param
                i_par += 1
            self.count += 1
            return run_dict
        else:
            raise StopIteration

    def save_state(self, filename):
        logging.debug("Saving sampler state to %s" % filename)
        file = open(filename, 'wb')
        pickle.dump(self.__dict__, file)
        file.close()

    def load_state(self, filename):
        logging.debug("Loading sampler state from %s" % filename)
        file = open(filename, 'rb')
        self.__dict__ = pickle.load(file)
        file.close()

    """
    =========================
    (SPARSE) GRID SUBROUTINES
    =========================
    """

    def generate_grid(self, l_norm):

        dimensions = range(self.N)
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

    # L : (int) max polynomial order
    # N : (int) the number of uncertain parameters
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
        # old implementation: does not scale well
        # P = np.array(list(product(range(1, L + 1), repeat=N)))
        # multi_idx = P[np.where(np.sum(P, axis=1) <= L + N - 1)[0]]

        # use the look_ahead subroutine to build an isotropic sparse grid (faster)
        multi_idx = np.array([np.ones(self.N, dtype='int')])
        for l in range(self.L - 1):
            self.look_ahead(multi_idx)
            # accept all admissible indices to build an isotropic grid
            multi_idx = np.append(multi_idx, self.admissible_idx, axis=0)

        return multi_idx


def setdiff2d(X, Y):
    """
    Computes the difference of two 2D arrays X and Y

    Parameters
    ----------
    X : 2D numpy array
    Y : 2D numpy array

    Returns
    -------
    The difference X \\ Y as a 2D array

    """
    diff = set(map(tuple, X)) - set(map(tuple, Y))
    return np.array(list(diff))
