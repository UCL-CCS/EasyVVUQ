"""
-------------------------------------------------------------------------
THE SIMPLEX STOCASTIC COLLOCATION SAMPLER OF JEROEN WITTEVEEN (1980-2015)
-------------------------------------------------------------------------

Source:

Witteveen, J. A. S., & Iaccarino, G. (2013).
Simplex stochastic collocation with ENO-type stencil selection for robust
uncertainty quantification. Journal of Computational Physics, 239, 1-21.

Edeling, W. N., Dwight, R. P., & Cinnella, P. (2016).
Simplex-stochastic collocation method with improved scalability.
Journal of Computational Physics, 310, 301-328.

"""

from .base import BaseSamplingElement, Vary
# import chaospy as cp
import numpy as np
import pickle
from itertools import product, combinations
# import logging
from scipy.spatial import Delaunay
from scipy.special import factorial
import multiprocessing as mp


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


class SSCSampler(BaseSamplingElement, sampler_name="ssc_sampler"):
    """
    Simplex Stochastic Collocation sampler
    """

    def __init__(self, vary=None, max_polynomial_order=4):
        """
        Create an SSC sampler object.

        Parameters
        ----------
        vary: dict or None
            keys = parameters to be sampled, values = distributions.
        max_polynomial_order : int, optional
            The maximum polynomial order, default is 4.
        Returns
        -------
        None.

        """
        # number of random inputs
        self.n_xi = len(vary)
        # vary dictionary of Chaospy input distribution
        self.vary = Vary(vary)
        # initial Delaunay triangulation
        self.tri = self.init_grid()
        # code sample counter
        self.count = 0
        self._n_samples = self.tri.points.shape[0]
        self.set_pmax_cutoff(max_polynomial_order)

    def init_grid(self):
        """
        Create the initial n_xi-dimensional Delaunay discretization


        Returns
        -------
        tri : scipy.spatial.qhull.Delaunay
            Initial triagulation of 2 ** n_xi + 1 points.

        """

        # create inital hypercube points through n_xi dimensional
        # carthesian product of the lower and upper limits of the
        # chasopy input distributions
        corners = [[param.lower[0], param.upper[0]] for param in self.vary.get_values()]
        self.corners = corners
        xi_k_jl = np.array(list(product(*corners)))

        # add a point in the middle of the hypercube
        xi_k_jl = np.append(xi_k_jl, np.mean(xi_k_jl, axis=0).reshape([1, -1]), 0)

        if self.n_xi > 1:
            # Create initial Delaunay discretization
            """
            NOTE: FOUND AN ERROR IN THE 'incremental' OPTION. IN A 3D CASE IT USES
            4 VERTICES TO MAKE A SQUARE IN A PLANE, NOT A 3D SIMPLEX. TURNED IT OFF.
            CONSEQUENCE: I NEED TO RE-MAKE A NEW 'Delaunay' OBJECT EVERYTIME THE GRID
            IS REFINED.
            """
            # tri = Delaunay(xi_k_jl, incremental=True)
            tri = Delaunay(xi_k_jl)

        else:
            tri = Tri1D(xi_k_jl)

        return tri

    def find_pmax(self, n_s):
        """
        Finds the maximum polynomial stencil order that can be sustained
        given the current number of code evaluations. The stencil size
        required for polynonial order p is given by;

        stencil size = (n_xi + p)! / (n_xi!p!)

        where n_xi is the number of random inputs. This formula is used
        to find p.

        Parameters
        ----------
        n_xi : int
            Number of random parameters.
        n_s : int
            Number of code samples.

        Returns
        -------
        int
            The highest polynomial order that can be sustained given
            the number of code evaluations.

        """
        p = 1
        stencil_size = factorial(self.n_xi + p) / (factorial(self.n_xi) * factorial(p))
        while stencil_size <= n_s:
            p += 1
            stencil_size = factorial(self.n_xi + p) / (factorial(self.n_xi) * factorial(p))

        return p - 1

    def set_pmax_cutoff(self, pmax_cutoff):
        """
        Set the maximum allowed polynomial value of the surrogate.

        Parameters
        ----------
        p_max_cutoff : int
            The max polynomial order.

        Returns
        -------
        None.

        """

        self.pmax_cutoff = pmax_cutoff
        self.i_norm_le_pj = self.compute_i_norm_le_pj(pmax_cutoff)

    def compute_vol(self):
        """
        Use analytic formula to compute the volume of all simplices.

        https://en.wikipedia.org/wiki/Simplex#Volume

        Returns
        -------
        vols : array, size (n_e,)
            The volumes of the n_e simplices.

        """
        n_e = self.tri.nsimplex
        vols = np.zeros(n_e)
        for j in range(n_e):
            xi_k_jl = self.tri.points[self.tri.simplices[j]]
            D = np.zeros([self.n_xi, self.n_xi])

            for i in range(self.n_xi):
                D[:, i] = xi_k_jl[i, :] - xi_k_jl[-1, :]

            det_D = np.linalg.det(D)
            if det_D == 0:
                print('Warning: zero determinant in volume calculation.')
            vols[j] = 1. / factorial(self.n_xi) * np.abs(det_D)

        return vols

    def compute_xi_center_j(self):
        """
        Compute the center of all simplex elements.

        Returns
        -------
        xi_center_j : array, size (n_e,)
            The cell centers of the n_e simplices.

        """
        # number of simplex elements
        n_e = self.tri.nsimplex
        xi_center_j = np.zeros([n_e, self.n_xi])
        for j in range(n_e):
            xi_center_j[j, :] = 1 / (self.n_xi + 1) * \
                np.sum(self.tri.points[self.tri.simplices[j]], 0)

        return xi_center_j

    def compute_sub_simplex_vertices(self, simplex_idx):
        """
        Compute the vertices of the sub-simplex. The  sub simplex is contained
        in the larger simplex. The larger simplex is refined by randomly
        placing a sample within the sub simplex.

        Parameters
        ----------
        simplex_idx : int
            The index of the simplex

        Returns
        -------
        xi_sub_jl : array, size (n_xi + 1, n_xi)
            The vertices of the sub simplex.

        """
        xi_k_jl = self.tri.points[self.tri.simplices[simplex_idx]]
        xi_sub_jl = np.zeros([self.n_xi + 1, self.n_xi])
        for l in range(self.n_xi + 1):
            idx = np.delete(range(self.n_xi + 1), l)
            xi_sub_jl[l, :] = np.sum(xi_k_jl[idx], 0)
        xi_sub_jl = xi_sub_jl / self.n_xi

        return xi_sub_jl

    def sample_inputs(self, n_mc):
        """
        Draw n_mc random values from the input distribution.

        Parameters
        ----------
        n_mc : int
            The number of Monte Carlo samples.

        Returns
        -------
        xi : array, shape(n_mc, n_xi)
            n_mc random samples from the n_xi input distributions.

        """
        xi = np.zeros([n_mc, self.n_xi])
        for i, param in enumerate(self.vary.get_values()):
            xi[:, i] = param.sample(n_mc)
        return xi

    def compute_probability(self):
        """
        Compute the probability Omega_j for all simplex elements;

        Omega_j = int p(xi) dxi,

        with integration separately over each simplex using Monte Carlo
        sampling.

        Returns
        -------
        prob_j : array, size (n_e,)
            The probabilities of each simplex.

        """
        n_e = self.tri.nsimplex

        print('Computing simplex probabilities...')
        prob_j = np.zeros(n_e)

        # number of MC samples
        n_mc = np.min([10 ** (self.n_xi + 3), 10 ** 7])

        xi = self.sample_inputs(n_mc)

        # find the simplix indices of xi
        idx = self.tri.find_simplex(xi)

        # compute simplex probabolities
        for i in range(n_mc):
            prob_j[idx[i]] += 1

        prob_j = prob_j / np.double(n_mc)
        print('done, used ' + str(n_mc) + ' samples.')
        zero_idx = (prob_j == 0).nonzero()[0].size
        print('% of simplices with no samples = ' + str((100.0 * zero_idx) / n_e))

        return prob_j

    def compute_i_norm_le_pj(self, p_max):
        """
        Compute the multi-index set {i | |i| = i_1 + ... + i_{n_xi} <= p},
        for p = 1,...,p_max

        Parameters
        ----------
        p_max : int
            The max polynomial order of the index set.

        Returns
        -------
        i_norm_le_pj : dict
            The Np + 1 multi indices per polynomial order.

        """
        i_norm_le_pj = {}

        for p in range(1, p_max + 1):
            # max(i_1, i_2, ...i _{n_xi}) <= p
            multi_idx = np.array(list(product(range(p + 1), repeat=self.n_xi)))

            # i_1 + i_2 <= N
            idx = np.where(np.sum(multi_idx, axis=1) <= p)[0]
            multi_idx = multi_idx[idx]

            i_norm_le_pj[p] = multi_idx

        return i_norm_le_pj

    def compute_Psi(self, xi_Sj, pmax):
        """
        Compute the Vandermonde matrix Psi, given N + 1 points xi from the
        j-th interpolation stencil, and a multi-index set of polynomial
        orders |i| = i_1 + ... + i_n_xi <= polynomial order.

        Parameters
        ----------
        xi_Sj : array, shape (N + 1, n_xi)
            The simplex n_xi-dimensional points of the j-th interpolation
            stencil S_j.
        pmax : int
            The max polynomial order of the local stencil.

        Returns
        -------
        Psi : array, shape (N + 1, N + 1)
            The Vandermonde interpolation matrix consisting of monomials
            xi_1 ** i_1 + ... + xi_{n_xi} ** i_{n_xi}.

        """
        Np1 = xi_Sj.shape[0]

        Psi = np.ones([Np1, Np1])

        for row in range(Np1):
            for col in range(Np1):
                for j in range(self.n_xi):
                    # compute monomial xi_1 ** i_1 + ... + xi_{n_xi} ** i_{n_xi}
                    Psi[row, col] *= xi_Sj[row][j] ** self.i_norm_le_pj[pmax][col][j]

        return Psi

    def w_j(self, xi, c_jl, pmax):
        """
        Compute the surrogate local interpolation at point xi.

        # TODO: right now this assumes a scalar output. Modify the
        code for vector-valued outputs.

        Parameters
        ----------
        xi : array, shape (n_xi,)
            A point inside the stochastic input domain.
        c_jl : array, shape (N + 1,)
            The interpolation coefficients of the j-th stencil, with
            l = 0, ..., N.
        pmax : int
            The max polynomial order of the local stencil.

        Returns
        -------
        w_j_at_xi : float
            The surrogate prediction at xi.

        """

        # number of points in the j-th interpolation stencil
        Np1 = c_jl.shape[0]

        # vector of interpolation monomials
        Psi_xi = np.ones([Np1, 1])
        for i in range(Np1):
            for j in range(self.n_xi):
                # take the power of xi to multi index entries
                Psi_xi[i] *= xi[j] ** self.i_norm_le_pj[pmax][i][j]

        # surrogate prediction
        w_j_at_xi = np.sum(c_jl * Psi_xi)

        return w_j_at_xi

    def check_LEC(self, p_j, v, S_j, n_mc, max_jobs=4):
        """
        Check the Local Extremum Conserving propery of all simplex elements.

        Parameters
        ----------
        p_j : array, shape (n_e,)
            The polynomial order of each element.
        v : array, shape (N + 1,)
            The (scalar) code outputs. #TODO:modify when vectors are allowed
        S_j : array, shape (n_e, n_s)
            The indices of all nearest neighbours points of each simplex j=1,..,n_e,
            ordered from closest to the neighbour that furthest away. The first
            n_xi + 1 indeces belong to the j-th simplex itself.
        n_mc : int
            The number of Monte Carlo samples to use in checking the LEC
            conditions.
        max_jobs : int
            The number of LEC check (one per element) that can be run in
            parallel.

        Returns
        -------
        None.

        """

        n_e = self.tri.nsimplex
        print('Checking LEC condition of ' + str(n_e) + ' stencils...')

        # multi-processing pool which will hold the check_LEC_j jobs
        jobs = []
        queues = []

        running_jobs = 0
        j = 0
        n_jobs = n_e

        el_idx = {}

        # r = np.array(list(product([0.25, 0.75], repeat=self.n_xi)))

        while n_jobs > 0:

            # check how many processes are still alive
            for p in jobs:
                if p.is_alive() == False:
                    jobs.remove(p)

            # number of processes still running
            running_jobs = len(jobs)

            # re-fill jobs with max max_jobs processes
            while running_jobs < max_jobs and n_jobs > 0:
                queue = mp.Queue()
                prcs = mp.Process(target=self.check_LEC_j,
                                  args=(p_j[j], v, S_j[j, :], n_mc, queue))
                prcs.start()
                running_jobs += 1
                n_jobs -= 1
                j += 1
                jobs.append(prcs)
                queues.append(queue)

        # retrieve results
        for j in range(n_e):
            # jobs[j].join()
            tmp = queues[j].get()
            p_j[j] = tmp['p_j[j]']
            el_idx[j] = tmp['el_idx_j']

    #    singular_idx = (p_j == -99).nonzero()[0]
    #
    #    jobs = []
    #    queues = []
    #    n_jobs = singular_idx.size
    #
    #    if singular_idx.size > 0:
    #        nnS_j = compute_stencil_j(tri)
    #
    #    k = 0
    #    while n_jobs > 0:
    #
    #        #check how many processes are still alive
    #        for p in jobs:
    #            if p.is_alive() == False:
    #                jobs.remove(p)
    #
    #        #number of processes still running
    #        running_jobs = len(jobs)
    #
    #        while running_jobs < max_jobs and n_jobs > 0:
    #            #print 'Re-computing S_j for j = ' + str(j)
    #            queue = mp.Queue()
    #            #S_j[j,:], p_j[j], el_idx[j] = \
    #            j = singular_idx[k]
    #            k += 1
    #            prcs = mp.Process(target=non_singular_stencil_j, \
    #            args = (tri, p_j, S_j, j, nnS_j, i_norm_le_pj, el_idx, queue,))
    #            prcs.start()
    #            jobs.append(prcs)
    #            queues.append(queue)
    #
    #            running_jobs += 1
    #            n_jobs -= 1
    #
    #    #retrieve results
    #    idx = 0
    #    for j in singular_idx:
    #        #jobs[idx].join()
    #        tmp = queues[idx].get()
    #        S_j[j,:] = tmp['S_j[j,:]']
    #        p_j[j] = tmp['p_j[j]']
    #        el_idx[j] = tmp['el_idx[j]']
    #        idx += 1

        print('done.')
        return {'p_j': p_j, 'S_j': S_j, 'el_idx': el_idx}

    def find_simplices(self, S_j):
        """
        Find the simplex element indices that are in point stencil S_j.

        Parameters
        ----------
        S_j : array, shape (N + 1,)
            The interpolation stencil of the j-th simplex element, expressed
            as the indices of the simplex points.

        Returns
        -------
        idx : array
            The element indices of stencil S_j.

        """
        n_e = self.tri.nsimplex
        # if the overlap between element i and S_j = n_xi + 1, element i
        # is in S_j
        idx = [np.in1d(self.tri.simplices[i], S_j).nonzero()[0].size for i in range(n_e)]
        idx = (np.array(idx) == self.n_xi + 1).nonzero()[0]

        return idx

    def check_LEC_j(self, p_j, v, S_j, n_mc, queue):
        """
        Check the LEC conditin of the j-th interpolation stencil.

        Parameters
        ----------
        p_j : int
            The polynomial order of the j-th stencil.
        v : array
            The code samples.
        S_j : array, shape (N + 1,)
            The interpolation stencil of the j-th simplex element, expressed
            as the indices of the simplex points.
        n_mc : int
            The number of Monte Carlo samples to use in checking the LEC
            conditions.
        queue : multiprocessing queue object
            Used to store the results.

        Returns
        -------
        None, results (polynomial order and element indices are stored
                       in the queue)

        """
        n_xi = self.n_xi
        # n_e = self.tri.nsimplex
        N = v[0, :].size

        # the number of points in S_j
        Np1_j = int(factorial(n_xi + p_j) / (factorial(n_xi) * factorial(p_j)))
        # select the vertices of stencil S_j
        xi_Sj = self.tri.points[S_j[0:Np1_j]]
        # find the corresponding indices of v
        v_Sj = v[S_j[0:Np1_j], :]

        # the element indices of the simplices in stencil S_j
        el_idx_j = self.find_simplices(S_j[0:Np1_j])

        # compute sample matrix
        Psi = self.compute_Psi(xi_Sj, p_j)

        # check if Psi is well poised
        # det_Psi = np.linalg.det(Psi)
        # if det_Psi == 0:
        #    #print 'Warning: determinant Psi is zero.'
        #    #print 'Reducing local p_j from ' + str(p_j[j]) + ' to a lower value.'
        #    #return an error code
        #    return queue.put({'p_j[j]':-99, 'el_idx_j':el_idx_j})

        # compute the coefficients c_jl
        # c_jl = np.linalg.solve(Psi, v_Sj)
        c_jl = DAFSILAS(Psi, v_Sj)

        # check the LEC condition for all simplices in the STENCIL S_j
        k = 0
        LEC_checked = False

        while LEC_checked == False and p_j != 1:
            # sample the simplices in stencil S_j
            xi_samples = self.sample_simplex(n_mc, self.tri.points[self.tri.simplices[el_idx_j[k]]])

            # function values at the edges of the k-th simplex in S_j
            v_min = np.min(v[self.tri.simplices[el_idx_j[k]]])
            v_max = np.max(v[self.tri.simplices[el_idx_j[k]]])

            # compute interpolation values at MC sample points
            w_j_at_xi = np.zeros([n_mc, N])
            for i in range(n_mc):
                w_j_at_xi[i, :] = self.w_j(xi_samples[i], c_jl, p_j)

            k += 1

            # if LEC is violated in any of the simplices
            # TODO: make work for vector-valued outputs
            eps = 0
            if (w_j_at_xi.min() <= v_min - eps or w_j_at_xi.max() >= v_max + eps) and p_j > 1:

                p_j -= 1

                # the new number of points in S_j
                Np1_j = int(factorial(n_xi + p_j) / (factorial(n_xi) * factorial(p_j)))
                # select the new vertices of stencil S_j
                xi_Sj = self.tri.points[S_j[0:Np1_j]]
                # find the new corresponding indices of v
                v_Sj = v[S_j[0:Np1_j], :]
                # the new element indices of the simplices in stencil S_j
                el_idx_j = self.find_simplices(S_j[0:Np1_j])
                k = 0

                if p_j == 1:
                    return queue.put({'p_j[j]': p_j, 'el_idx_j': el_idx_j})

                # recompute sample matrix
                Psi = self.compute_Psi(xi_Sj, p_j)

                # check if Psi is well poised
                # det_Psi = np.linalg.det(Psi)
                # if det_Psi == 0:
                #    #print 'Warning: determinant Psi is zero.'
                #    #print 'Reducing local p_j from ' + str(p_j[j]) + ' to a lower value.'
                #    #return an error code
                #    return queue.put({'p_j[j]':-99, 'el_idx_j':el_idx_j})

                # compute the coefficients c_jl
                # c_jl = np.linalg.solve(Psi, v_Sj)
                c_jl = DAFSILAS(Psi, v_Sj, False)

            if k == el_idx_j.size:
                LEC_checked = True

        queue.put({'p_j[j]': p_j, 'el_idx_j': el_idx_j})

    def compute_stencil_j(self):
        """
        Compute the nearest neighbor stencils of all simplex elements. The
        distance to all points are measured with respect to the cell center
        of each element.

        Returns
        -------
        S_j : array, shape (n_e, n_s)
            The indices of all nearest neighbours points of each simplex j=1,..,n_e,
            ordered from closest to the neighbour that furthest away. The first
            n_xi + 1 indeces belong to the j-th simplex itself.

        """

        n_e = self.tri.nsimplex
        n_s = self.tri.npoints
        n_xi = self.n_xi
        S_j = np.zeros([n_e, n_s])
        # compute the center of each element
        xi_center_j = self.compute_xi_center_j()

        for j in range(n_e):
            # the number of points in S_j
            # Np1_j = factorial(n_xi + p_j[j])/(factorial(n_xi)*factorial(p_j[j]))
            # k = {1,...,n_s}\{k_j0, ..., k_jn_xi}
            idx = np.delete(range(n_s), self.tri.simplices[j])
            # store the vertex indices of the element itself
            S_j[j, 0:n_xi + 1] = np.copy(self.tri.simplices[j])
            # loop over the set k
            dist = np.zeros(n_s - n_xi - 1)
            for i in range(n_s - n_xi - 1):
                # ||xi_k - xi_center_j||
                dist[i] = np.linalg.norm(self.tri.points[idx[i]] - xi_center_j[j, :])
            # store the indices of the points, sorted based on distance wrt
            # simplex center j. Store only the amount of indices allowed by p_j.
            S_j[j, n_xi + 1:] = idx[np.argsort(dist)]

        return S_j.astype('int')

    def compute_ENO_stencil(self, p_j, S_j, el_idx, max_jobs=4):
        """
        Compute the Essentially Non-Oscillatory stencils. The idea behind ENO
        stencils is to have higher degree interpolation stencils up to a thin
        layer of simplices containing the discontinuity. For a given simplex,
        its ENO stencil is created by locating all the nearest-neighbor
        stencils that contain element j , and subsequently selecting the one
        with the highest polynomial order p_j . This leads to a Delaunay
        triangulation which captures the discontinuity better than its
        nearest-neighbor counterpart.

        Parameters
        ----------
        p_j : array, shape (n_e,)
            The polynomial order of each simplex element.
        S_j : array, shape (n_e, n_s)
            The indices of all nearest neighbours points of each simplex j=1,..,n_e,
            ordered from closest to the neighbour that furthest away. The first
            n_xi + 1 indeces belong to the j-th simplex itself.
        el_idx : dict
            The element indices for each interpolation stencil.
            el_idx[2] gives the elements indices of the 3rd interpolation
            stencil. The number of elements is determined by the local
            polynomial order.
        max_jobs : int, optional
            The number of ENO stencils that are computed in parallel.
            The default is 4.

        Returns
        -------
        ENO_S_j : array, shape (n_e, n_s)
            The ENO stencils for each element.
        p_j : array, shape (n_e,)
            The new polynomial order of each element.
        el_idx : dict
            The new element indices for each interpolation stencil.

        """

        n_e = self.tri.nsimplex
        n_s = self.tri.npoints

        # array to store the ENO stencils
        ENO_S_j = np.zeros([n_e, n_s]).astype('int')
        # the center of each simplex
        xi_centers = self.compute_xi_center_j()

        jobs = []
        queues = []
        running_jobs = 0
        j = 0
        n_jobs = n_e

        print('Computing ENO stencils...')

        while n_jobs > 0:

            # check how many processes are still alive
            for p in jobs:
                if p.is_alive() == False:
                    jobs.remove(p)

            # number of processes still running
            running_jobs = len(jobs)

            # compute the ENO stencils (in parallel)
            while running_jobs < max_jobs and n_jobs > 0:
                queue = mp.Queue()
                prcs = mp.Process(target=self.compute_ENO_stencil_j,
                                  args=(p_j, S_j, xi_centers, j, el_idx, queue))

                # print check_LEC_j(tri, p_j, v, S_j, n_mc, j)
                jobs.append(prcs)
                queues.append(queue)
                prcs.start()
                n_jobs -= 1
                running_jobs += 1
                j += 1

        # retrieve results
        for j in range(n_e):
            tmp = queues[j].get()
            ENO_S_j[j, :] = tmp['ENO_S_j']
            p_j[j] = tmp['p_j_new']
            el_idx[j] = tmp['el_idx[j]']

        print('done.')

        return ENO_S_j, p_j, el_idx

    def compute_ENO_stencil_j(self, p_j, S_j, xi_centers, j, el_idx, queue):
        """
        Compute the ENO stencil of the j-th element.

        Parameters
        ----------
        p_j : array, shape (n_e,)
            The polynomial order of each simplex element.
        S_j : array, shape (n_e, n_s)
            The indices of all nearest neighbours points of each simplex j=1,..,n_e,
            ordered from closest to the neighbour that furthest away. The first
            n_xi + 1 indeces belong to the j-th simplex itself.
        xi_centers : array, shape (n_e, )
            The center of each simplex.
        j : int
            The index of the current simplex.
        el_idx : dict
            The element indices for each interpolation stencil.
            el_idx[2] gives the elements indices of the 3rd interpolation
            stencil. The number of elements is determined by the local
            polynomial order.
        queue : multiprocessing queue object
            Used to store the results.

        Returns
        -------
        None, results (polynomial order and element indices are stored
                       in the queue)

        """
        n_e = self.tri.nsimplex

        # set the stencil to the nearest neighbor stencil
        ENO_S_j = np.copy(S_j[j, :])
        p_j_new = np.copy(p_j[j])

        # loop to find alternative candidate stencils S_ji with p_j>1 that contain k_jl
        idx = (p_j == 1).nonzero()[0]
        all_with_pj_gt_1 = np.delete(range(n_e), idx)

        for i in all_with_pj_gt_1:
            # found a candidate stencil S_ji
            if np.in1d(j, el_idx[i]):
                # the candidate stencil has a higher polynomial degree: accept
                if p_j[i] > p_j_new:
                    ENO_S_j = np.copy(S_j[i, :])
                    p_j_new = np.copy(p_j[i])
                    el_idx[j] = np.copy(el_idx[i])
                # the candidate stencil has the same polynomial degree: accept
                # the one with smallest avg Euclidian distance to the cell center
                elif p_j_new == p_j[i]:

                    dist_i = np.linalg.norm(xi_centers[el_idx[i]] - xi_centers[j], 2, axis=1)

                    dist_j = np.linalg.norm(xi_centers[el_idx[j]] - xi_centers[j], 2, axis=1)

                    # if the new distance is smaller than the old one: accept
                    if np.sum(dist_i) < np.sum(dist_j):
                        ENO_S_j = np.copy(S_j[i, :])
                        el_idx[j] = np.copy(el_idx[i])

        queue.put({'ENO_S_j': ENO_S_j, 'p_j_new': p_j_new, 'el_idx[j]': np.copy(el_idx[j])})

    def sample_simplex(self, n_mc, xi_k_jl, check=False):
        """
        Use an analytical map from n_mc uniformly distributed points in the
        n_xi-dimensional hypercube, to uniformly distributed points in the
        target simplex described by the nodes xi_k_jl.

        Derivation: Edeling, W. N., Dwight, R. P., & Cinnella, P. (2016).
        Simplex-stochastic collocation method with improved scalability.
        Journal of Computational Physics, 310, 301-328.

        Parameters
        ----------
        n_mc : int
            The number of Monte Carlo samples.
        xi_k_jl : array, shape (n_xi + 1, n_xi)
            The nodes of the target simplex.
        check : bool, optional
            Check is the random samples actually all lie insiide the
            target simplex. The default is False.

        Returns
        -------
        P : array, shape (n_mc, n_xi)
            Uniformly distributed points inside the target simplex.

        """

        n_xi = self.n_xi
        P = np.zeros([n_mc, n_xi])
        for k in range(n_mc):
            # random points inside the hypercube
            r = np.random.rand(n_xi)

            # the term of the map is \xi_k_j0
            sample = np.copy(xi_k_jl[0])
            for i in range(1, n_xi + 1):
                prod_r = 1.
                # compute the product of r-terms: prod(r_{n_xi-j+1}^{1/(n_xi-j+1)})
                for j in range(1, i + 1):
                    prod_r *= r[n_xi - j]**(1. / (n_xi - j + 1))
                # compute the ith term of the sum: prod_r*(\xi_i-\xi_{i-1})
                sample += prod_r * (xi_k_jl[i] - xi_k_jl[i - 1])
            P[k, :] = sample

        # check if any of the samples are outside the simplex
        if check:
            outside_simplex = 0
            avg = np.sum(xi_k_jl, 0) / (n_xi + 1.)
            el = self.tri.find_simplex(avg)
            for i in range(n_mc):
                if self.tri.find_simplex(P[i, :]) != el:
                    outside_simplex += 1
            print('Number of samples outside target simplex = ' + str(outside_simplex))

        return P

    def sample_simplex_edge(self, simplex_idx, refined_edges):
        """
        Refine the longest edge of a simplex.

        # TODO: is allright for 2D, but does this make sense in higher dims?

        Parameters
        ----------
        simplex_idx : int
            The index of the simplex.
        refined_edges : list
            Contains the pairs of the point indices, corresponding to edges that
            have been refined in the current iteration. Simplices share edges,
            and this list is used to prevent refining the same edge twice within
            the same iteration of the SSC algorihm.

        Returns
        -------
        xi_new : array, shape (n_xi,)
            The newly added point (along the longest edge).
        refined_edges : list
            The updated refined_edges list.
        already_refined : bool
            Returns True if the edge already has been refined.

        """

        # the point indices of the simplex selected for refinement
        simplex_point_idx = self.tri.simplices[simplex_idx]
        # the points of the simplex selected for refinement
        xi_k_jl = self.tri.points[simplex_point_idx]

        # find the indices of all edges, i.e. the combination of all possible
        # 2 distinct elements from range(n_xi + 1)
        comb = list(combinations(range(self.n_xi + 1), 2))

        # compute all edge lengths, select the largest
        edge_lengths = np.zeros(len(comb))
        for i in range(len(comb)):
            edge_lengths[i] = np.linalg.norm(xi_k_jl[comb[i][1], :] - xi_k_jl[comb[i][0], :])
        idx = np.argmax(edge_lengths)

        # if there are 2 or more edge lengths that are the same, select the 1st
        if idx.size > 1:
            idx = idx[0]

        # edge points
        xi_0 = xi_k_jl[comb[idx][0], :]
        xi_1 = xi_k_jl[comb[idx][1], :]

        # simplices share edges, make sure it was not already refined during
        # this iteration
        current_edge = np.array([simplex_point_idx[comb[idx][0]],
                                 simplex_point_idx[comb[idx][1]]])
        already_refined = False

        for edge in refined_edges:
            if set(edge) == set(current_edge):
                already_refined = True

        if not already_refined:
            refined_edges.append(current_edge)

        # place random sample at +/- 10% of edge center
        b = 0.6
        a = 0.4
        U = np.random.rand() * (b - a) + a
        xi_new = xi_0 + U * (xi_1 - xi_0)

        return xi_new, refined_edges, already_refined

    def compute_surplus_k(self, xi_k_jref, S_j, p_j, v, v_k_jref):
        """
        Compute the hierachical surplus at xi_k_jref (the refinement location),
        defined as the difference between the new code sample and the (old)
        surrogate  prediction at the refinement location.

        Parameters
        ----------
        xi_k_jref : array, shape (n_xi,)
            The refinement location.
        S_j : array, shape (n_e, n_s)
            The indices of all nearest neighbours points of each simplex j=1,..,n_e,
            ordered from closest to the neighbour that furthest away. The first
            n_xi + 1 indeces belong to the j-th simplex itself.
        p_j : array, shape (n_e,)
            The polynomial order of each simplex element.
        v : array, shape (N + 1,)
            The (scalar) code outputs. #TODO:modify when vectors are allowed
        v_k_jref : float #TODO:modify when vectors are allowed
            The code prediction at the refinement location.

        Returns
        -------
        surplus : float #TODO:modify when vectors are allowed
            The hierarchical suplus

        """

        w_k_jref = self.surrogate(xi_k_jref, S_j, p_j, v)

        # compute the hierarcical surplus between old interpolation and new v value
        surplus = w_k_jref - v_k_jref

        return surplus

    def surrogate(self, xi, S_j, p_j, v):
        """
        Evaluate the SSC surrogate at xi.

        Parameters
        ----------
        xi : array, shape (n_xi,)
            The location in the input space at which to evaluate the surrogate.
        S_j : array, shape (n_e, n_s)
            The indices of all nearest neighbours points of each simplex j=1,..,n_e,
            ordered from closest to the neighbour that furthest away. The first
            n_xi + 1 indeces belong to the j-th simplex itself.
        p_j : array, shape (n_e,)
            The polynomial order of each simplex element.
        v : array, shape (N + 1,)
            The (scalar) code outputs. #TODO:modify when vectors are allowed

        Returns
        -------
        None.

        """
        n_xi = self.n_xi
        idx = int(self.tri.find_simplex(xi))

        # the number of points in S_j
        Np1_j = int(factorial(n_xi + p_j[idx]) / (factorial(n_xi) * factorial(p_j[idx])))
        # the vertices of the stencil S_j
        xi_Sj = self.tri.points[S_j[idx, 0:Np1_j]]
        # find the corresponding indices of v
        v_Sj = v[S_j[idx, 0:Np1_j], :]
        # compute sample matrix
        Psi = self.compute_Psi(xi_Sj, p_j[idx])

    #    #check if Psi is well poised, at this point all stencils should be well-poised
    #    det_Psi = np.linalg.det(Psi)
    #    if det_Psi == 0:
    #        print 'Error, det(Psi)=0 in compute_surplus_k() method, should not be possible'

        # compute the coefficients c_jl
        # c_jl = np.linalg.solve(Psi, v_Sj)
        c_jl = DAFSILAS(Psi, v_Sj, False)

        # compute the interpolation on the old grid
        w_j = self.w_j(xi, c_jl, p_j[idx])

        return w_j

    def compute_eps_bar_j(self, p_j, prob_j):
        """
        Compute the geometric refinement measure \bar{\\eps}_j for all elements,
        Elements with the largest values will be selected for refinement.

        Parameters
        ----------
        p_j : array, shape (n_e,)
            The polynomial order of each simplex element.
        prob_j : array, shape (n_e,)
            The probability of each simplex element.

        Returns
        -------
        eps_bar_j : array, shape (n_e,)
            The geometric refinement measure.
        vol_j : array, shape (n_e,)
            The volume of each simplex element.

        """

        n_e = self.tri.nsimplex
        eps_bar_j = np.zeros(n_e)
        n_xi = self.tri.ndim
        vol_j = self.compute_vol()
        vol = np.sum(vol_j)

        for j in range(n_e):
            O_j = (p_j[j] + 1.0) / n_xi
            eps_bar_j[j] = prob_j[j] * (vol_j[j] / vol) ** (2 * O_j)

        return eps_bar_j, vol_j

    def find_boundary_simplices(self):
        """
        Find the simplices that are on the boundary of the hypercube   .

        Returns
        -------
        idx : array
            Indices of the boundary simplices.

        """

        idx = (self.tri.neighbors == -1).nonzero()[0]
        return idx

    def update_Delaunay(self, new_points):
        """
        Update the Delaunay triangulation with P new points.

        Parameters
        ----------
        new_points : array, shape (P, n_xi)
            P new n_xi-dimensional points.

        Returns
        -------
        None.

        """

        xi_k_jl = np.append(self.tri.points, new_points, 0)
        if self.n_xi > 1:
            self.tri = Delaunay(xi_k_jl)
        else:
            self.tri = Tri1D(xi_k_jl)

        self._n_samples = self.tri.npoints

    def get_Delaunay(self):
        """
        Return the SciPy Delaunay triangulation.
        """
        return self.tri

    def is_finite(self):
        return True

    @property
    def n_samples(self):
        """
        Returns the number of samples code samples.
        """
        return self._n_samples

    @property
    def n_dimensions(self):
        """
        Returns the number of uncertain random variables
        """
        return self.n_xi

    @property
    def n_elements(self):
        """
        Returns the number of simplex elements
        """
        return self.tri.nsimplex

    def __next__(self):
        if self.count < self._n_samples:
            run_dict = {}
            i_par = 0
            for param_name in self.vary.get_keys():
                run_dict[param_name] = self.tri.points[self.count][i_par]
                i_par += 1
            self.count += 1
            return run_dict
        else:
            raise StopIteration

    def save_state(self, filename):
        """
        Save the state of the sampler to a pickle file.

        Parameters
        ----------
        filename : string
            File name.

        Returns
        -------
        None.

        """
        print("Saving sampler state to %s" % filename)
        with open(filename, 'wb') as fp:
            pickle.dump(self.__dict__, fp)

    def load_state(self, filename):
        """
        Load the state of the sampler from a pickle file.

        Parameters
        ----------
        filename : string
            File name.

        Returns
        -------
        None.

        """
        print("Loading sampler state from %s" % filename)
        with open(filename, 'rb') as fp:
            self.__dict__ = pickle.load(fp)


def DAFSILAS(A, b, print_message=False):
    """
    Direct Algorithm For Solving Ill-conditioned Linear Algebraic Systems,

    solves the linear system when Ax = b when A is ill conditioned.

    Solves for x in the non-null subspace of the solution as described in
    the reference below. This method utilizes Gauss–Jordan elimination with
    complete pivoting to identify the null subspace of a (almost) singular
    matrix.

    X. J. Xue, Kozaczek, K. J., Kurtzl, S. K., & Kurtz, D. S. (2000). A direct
    algorithm for solving ill-conditioned linear algebraic systems.
    Adv. X-Ray Anal, 42.
    """

    # The matrix A' as defined in Xue
    b = b.reshape(b.size)
    Ap = np.zeros([A.shape[0], 2 * A.shape[0] + 1])
    Ap[:, 0:A.shape[0]] = np.copy(A)
    Ap[:, A.shape[0]] = np.copy(b)
    Ap[:, A.shape[0] + 1:] = np.eye(A.shape[0])
    n, m = Ap.shape

    # permutation matrix
    P = np.eye(n)

    # the ill-condition control parameter
    # epsilon = np.finfo(np.float64).eps
    epsilon = 10**-14

    for i in range(n - 1):
        # calc sub matrix Ai
        Ai = np.copy(Ap[i:n, i:n])

        # find the complete pivot in sub matrix Ai
        api = np.max(np.abs(Ai))

        if api == 0:
            break

        # find the location of the complete pivot in Ai
        row, col = np.unravel_index(np.abs(Ai).argmax(), Ai.shape)

        # interchange rows and columns to exchange position of api and aii
        tmp = np.copy(Ap[i, :])
        Ap[i, :] = np.copy(Ap[i + row, :])
        Ap[i + row, :] = tmp

        tmp = np.copy(Ap[:, i])
        Ap[:, i] = np.copy(Ap[:, i + col])
        Ap[:, i + col] = tmp

        # Also interchange the entries in b
        # tmp = A[i, n]
        # A[i, n] = A[i+col, n]Ap[i+1+j, i:m]
        # A[i+col, n] = tmp

        # keep track of column switches via a series of permuation matrices P =
        # P1*P2*...*Pi*...*Pn ==> at each iteration x = P*xi
        Pi = np.eye(n)
        tmp = np.copy(Pi[i, :])
        Pi[i, :] = np.copy(Pi[i + col, :])
        Pi[i + col, :] = tmp
        P = np.dot(P, Pi)

        # Calculate multipliers
        if Ai[row, col] < 0:
            api = api * -1.  # sign is important in multipliers

        M = Ap[i + 1:n, i] / np.double(api)

        # start row reduction
        for j in range(M.size):
            Ap[i + 1 + j, i:m] = Ap[i + 1 + j, i:m] - M[j] * Ap[i, i:m]

    # the largest complete pivot
    eta = np.max(np.abs(np.diag(Ap))) * 1.0
    # test if |aii/nc| <= epsilon
    idx = (np.abs(np.diag(Ap) / eta) <= epsilon).nonzero()[0]

    # Perform zeroing operation if necessary
    if idx.size > 0:
        nullity = idx.size
        Arange = Ap[0:n - nullity, 0:n - nullity]
        if print_message:
            print('Matrix is ill-conditioned, performing zeroing operation')
            print('nullity = ' + str(nullity) + ', rank = ' + str(n - nullity) +
                  ', cond(A) = ' + str(np.linalg.cond(A)) +
                  ', cond(Arange) = ' + str(np.linalg.cond(Arange)))

        # ajj = 1, aij = 0 for j = i...n
        Ap[idx[0]:n, idx[0]:n] = np.eye(nullity)
        # bj = 0
        Ap[idx[0]:n, n] = 0
        # ejj = 1, eij = 0
        Ap[idx[0]:n, idx[0] + n + 1:m] = np.eye(nullity)

    # Back substitution
    for i in range(n, 0, -1):
        Ai = Ap[0:i, :]

        # Calculate multipliers
        M = Ai[0:i - 1, i - 1] / np.double(Ai[i - 1, i - 1])

        # start back substitution
        for j in range(M.size):
            Ai[j, :] = Ai[j, :] - M[j] * Ai[i - 1, :]

        # store result in A
        Ap[0:i, :] = Ai

    # turn A into eye(n)
    D = (1. / np.diag(Ap)).reshape([n, 1])
    Ap = np.multiply(D, Ap)
    # Calculated solution
    return np.dot(P, Ap[:, n]).reshape([n, 1])


class Tri1D:
    """
    1D "triangulation" that mimics the following SciPy Delaunay properties:
        * ndim
        * points
        * npoints
        * nsimplex
        * simplices
        * neighbours
        * the find_simplex subroutine
    """

    def __init__(self, points):
        """
        Create a 1D Triangulation object that can we used by the SSCSampler
        in the same way as the SciPy Delaunay triangulation.

        Parameters
        ----------
        points : array, shape (n_s, )
            A 1D array of nodes.

        Returns
        -------
        None.

        """
        self.ndim = 1
        self.points = points
        self.npoints = points.size
        self.nsimplex = points.size - 1

        points_sorted = np.sort(self.points.reshape(self.npoints))
        self.simplices = np.zeros([self.nsimplex, 2])
        for i in range(self.nsimplex):
            self.simplices[i, 0] = (self.points == points_sorted[i]).nonzero()[0]
            self.simplices[i, 1] = (self.points == points_sorted[i + 1]).nonzero()[0]
        self.simplices = self.simplices.astype('int')

        self.neighbors = np.zeros([self.nsimplex, 2])
        for i in range(self.nsimplex):
            self.neighbors[i, 0] = i - 1
            self.neighbors[i, 1] = i + 1
        self.neighbors[-1, 1] = -1
        self.neighbors = self.neighbors.astype('int')

    def find_simplex(self, xi):
        """
        Find the simplex indices of nodes xi

        Parameters
        ----------
        xi : array, shape (S,)
            An array if S 1D points.

        Returns
        -------
        array
            An array containing the simplex indices of points xi.

        """
        Idx = np.zeros(xi.shape[0])
        points_sorted = np.sort(self.points.reshape(self.npoints))

        for i in range(xi.shape[0]):
            idx = (points_sorted < xi[i]).argmin() - 1
            # if xi = 0 idx will be -1
            if idx == -1:
                Idx[i] = 0
            else:
                Idx[i] = idx

        return Idx.astype('int')
