"""Analysis element for Stochastic Collocation (SC).

Method: 'Global Sensitivity Analysis for Stochastic Collocation'
        G. Tang and G. Iaccarino, AIAA 2922, 2010
"""
import numpy as np
import chaospy as cp
from itertools import product, chain, combinations
from easyvvuq import OutputType
from .base import BaseAnalysisElement

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


class SCAnalysis(BaseAnalysisElement):

    def __init__(self, sampler=None, qoi_cols=None):
        """Analysis element for Stochastic Collocation (SC).

        Method: 'Global Sensitivity Analysis for Stocastic Collocation'
                G. Tang and G. Iaccarino, AIAA 2922, 2010

        Parameters
        ----------
        sampler : :obj:`easyvvuq.sampling.stochastic_collocation.SCSampler`
            Sampler used to initiate the PCE analysis
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        """

        if sampler is None:
            msg = 'SC analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)

        if qoi_cols is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler
        self._number_of_samples = sampler._number_of_samples
        self.sparse = sampler.sparse

    def element_name(self):
        """Name for this element for logging purposes"""
        return "SC_Analysis"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.3"

    def analyse(self, data_frame=None):
        """Perform PCE analysis on input `data_frame`.

        Parameters
        ----------
        data_frame : :obj:`pandas.DataFrame`
            Input data for analysis.

        Returns
        -------
        dict
            Results dictionary with sub-dicts with keys:
            ['statistical_moments', 'sobol_indices'].
            Each dict has an entry for each item in `qoi_cols`.
        """

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")
        elif data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        # the maximum level (quad order) of the (sparse) grid
        self.L = self.sampler.L

        # the number of uncertain parameters
        self.N = self.sampler.N

        # if L < L_min: quadratures and interpolations are zero
        # For full tensor grid: there is only one level: L_min = L
        if not self.sparse:
            self.L_min = self.L
            self.l_norm = np.array([self.sampler.polynomial_order])
            self.l_norm_min = self.l_norm
        # For sparse grid: multiple levels, L >= N must hold
        else:
            self.L_min = 1
            self.l_norm = self.sampler.compute_sparse_multi_idx(self.L, self.N)
            self.l_norm_min = np.ones(self.N, dtype=int)

        # full tensor grid
        self.xi_d = self.sampler.xi_d

        # 1d weights and points per level
        self.xi_1d = self.sampler.xi_1d
        self.wi_1d = self.compute_SC_weights(rule=self.sampler.quad_rule)

        # per level, map a unique index k to all (level multi indices, colloc points)
        # combinations. Will differ for sparse or full tensor grids.
        # All interpolation/quadrature subroutines loop over the entries in Map
        self.Map = {}
        self.surr_lm1 = {}

        self.foo = []

        for level in range(self.L_min, self.L + 1):
            self.Map[level] = self.create_map(self.N, level)

        self.clear_surr_lm1()

        # Extract output values for each quantity of interest from Dataframe
        qoi_cols = self.qoi_cols
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == run_id][k].values
                samples[k].append(values)
        self.samples = samples

        # size of one code sample
        self.N_qoi = self.samples[qoi_cols[0]][0].size

        results = {'statistical_moments': {},
                   'sobols_first': {k: {} for k in self.qoi_cols},
                   'sobols': {k: {} for k in self.qoi_cols}}

        # Compute descriptive statistics for each quantity of interest
        for qoi_k in qoi_cols:
            mean_k, var_k = self.get_moments(qoi_k)
            std_k = var_k**0.5

            # compute statistical moments
            results['statistical_moments'][qoi_k] = {'mean': mean_k,
                                                     'var': var_k,
                                                     'std': std_k}
            # compute all Sobol indices
            results['sobols'][qoi_k] = self.get_sobol_indices(qoi_k, 'all')

            idx = 0
            for param_name in self.sampler.vary.get_keys():
                results['sobols_first'][qoi_k][param_name] = \
                    results['sobols'][qoi_k][(idx,)]
                idx += 1

        return results

    def create_map(self, N, L):
        """
        Create a map from a unique integer k to each
        (level multi index l, collocation point X) combination. Also
        compute the index of X (f) in the global (sparse) grid xi_d

        Parameters
        ----------
        - N (int) = number of parameters
        - L (int) = max level of grid

        Returns
        --------
        - Map: a dict for level L containing k, l, X, and f
        """

        # unique index
        k = 0
        Map = {}

        print('Creating multi-index map for level', L, '...')

        # full tensor product
        if not self.sparse:

            # l = (np.ones(N) * L).astype('int')
            l = (self.sampler.polynomial_order)

            for x in self.xi_d:
                Map[k] = {'l': l, 'X': x, 'f': k}
                k += 1
        # sparse grid
        else:

            # all sparse grid multi indices l with |l| <= L
            l_norm_le_L = self.sampler.compute_sparse_multi_idx(L, N)

            # loop over all multi indices
            for l in l_norm_le_L:

                # colloc point of current level index l
                X_l = [self.xi_1d[n][l[n]] for n in range(N)]
                X_l = np.array(list(product(*X_l)))

                for x in X_l:
                    j = np.where((x == self.xi_d).all(axis=1))[0][0]
                    Map[k] = {'l': l, 'X': x, 'f': j}
                    k += 1

        print('done.')

        return Map

    def surrogate(self, qoi, x, **kwargs):
        """
        Use sc_expansion UQP as a surrogate

        Parameters
        ----------
        - qoi (str): name of the qoi

        Returns
        -------
        the interpolated value of qoi at x (float, (N_qoi,))

        """

        if 'L' in kwargs:
            L = kwargs['L']
        else:
            L = self.L

        return self.sc_expansion(L, self.samples[qoi], x=x)

    def quadrature(self, qoi, **kwargs):
        """
        Computes a (Smolyak) quadrature

        Parameters
        ----------
        - qoi (str): name of the qoi

        - samples (optional in kwargs): Default: compute the mean
          by setting samples = self.samples. To compute the variance,
          set samples = (self.samples - mean)**2
        """

        if 'samples' in kwargs:
            samples = kwargs['samples']
        else:
            samples = self.samples[qoi]

        Delta = np.zeros([self.l_norm.shape[0], self.N_qoi])
        idx = 0
        for l in self.l_norm:
            # compute the Delta Q :=
            # (Q^1_l_1 - Q^1_{l_1 - 1}) X ... X (Q^1_{l_N} - Q^1_{L_N - 1})
            # tensor product
            Delta[idx, :] = self.compute_Q_diff(l, samples)
            idx += 1

        quadrature_approx = np.sum(Delta, axis=0)

        return quadrature_approx

    def compute_Q_diff(self, l, samples, **kwargs):
        """
        =======================================================================
        For every multi index l = (l1, l2, ..., ld), Smolyak sums over
        tensor products difference quadrature rules:
        (Q^1_{l1} - Q^1_{l1-1}) X ... X (Q^1_{lN) - Q^1_{lN-1})
        Below this product is expanded into individual tensor products, each
        of which is then computed as:
        Q^1_{k1} X ... X Q^1_{kN} = sum...sum w_{k1}*...*w{kN}*f(x_{k1},...,x_{kN})
        =======================================================================
        """

        # expand the multi-index indices of the tensor product
        # (Q^1_{i1} - Q^1_{i1-1}) X ... X (Q^1_{id) - Q^1_{id-1})
        diff_idx = np.array(list(product(*[[k, -(k - 1)] for k in l])))

        # Delta will be the sum of all expanded tensor products
        # Q^1_{k1} X ... X Q^1_{kd} = sum...sum w_{k1}*...*w{kN}*f(x_{k1},...,x_{kd})
        Delta = 0.0

        # each diff contains the level indices of to a single
        # Q^1_{k1} X ... X Q^1_{kN} product
        for diff in diff_idx:
            #if any Q^1_{ki} is below the minimim level, Q^1_{ki} is defined
            #as zero: do not compute this Q^1_{k1} X ... X Q^1_{kN} product
            if not (np.abs(diff) < self.l_norm_min).any():

                # compute the tensor product of parameter and weight values
                X_k = []
                W_k = []
                for n in range(self.N):
                    X_k.append(self.xi_1d[n][np.abs(diff)[n]])
                    W_k.append(self.wi_1d[n][np.abs(diff)[n]])

                X_k = np.array(list(product(*X_k)))
                W_k = np.array(list(product(*W_k)))
                W_k = np.prod(W_k, axis=1)
                W_k = W_k.reshape([W_k.shape[0], 1])

                # find corresponding code values
                f_k = []
                for x in X_k:
                    j = np.where((x == self.xi_d).all(axis=1))[0][0]
                    f_k.append(samples[j])
                f_k = np.array(f_k).reshape([len(X_k), self.N_qoi])

                # quadrature of Q^1_{k1} X ... X Q^1_{kN} product
                Q_prod = np.sum(f_k * W_k, axis=0).T
                Delta += np.sign(np.prod(diff)) * Q_prod

        return Delta

    def get_moments(self, qoi):
        """
        Parameters
        ----------
        - qoi (str): name of the qoi

        Returns
        -------
        - mean and variance of qoi (float (N_qoi,))

        """

        # compute mean
        mean_f = self.quadrature(qoi)

        # compute variance
        variance_samples = []
        for sample in self.samples[qoi]:
            variance_samples.append((sample - mean_f)**2)

        var_f = self.quadrature(qoi, samples=variance_samples)

        return mean_f, var_f

    def sc_expansion(self, L, samples, **kwargs):
        """
        -----------------------------------------
        This is the UQ Pattern for the SC method.
        -----------------------------------------

        Can perform interpolation for both full and sparse grids.

        For a qoi q, it computes the following tensor product:

        q \approx \sum_{l\in\Lambda} \Delta_{l}[q](x)

        where Delta_{l} is the difference at x between surrogates / quadratues
        of level L and L-1. See e.g.:

        Dimitrios Loukrezis et. al., "Assessing the Performance of Leja and
        Clenshaw-Curtis Collocation for Computational Electromagnetics with
        Random Input Data."

        Parameters
        ----------

        - x (float (N,)): location in stochastic space at which to eval the surrogate
        - L (int): max level of the surrogate

        Returns
        -------

        surr (float, (N_qoi,)): the interpolated value of qoi at x
        """

        # for L < L_min the surrogate is defined as zero
        if L < self.L_min:
            return 0.0

        surr = np.zeros(self.N_qoi)

        # contains the level multi-indices (l), colloc points x and samples
        # indices f of the (sparse) grid
        Map = self.Map[L]

        for k in Map.keys():

            # the current code samples
            q_k = samples[Map[k]['f']]

            # the current level multi index (l_1,...,l_N)
            l = Map[k]['l']

            # the hierarchical surplus (s_k) between the code output q_k and the
            # previous surrogate of level L-1 evaluated at the same location.
            # Recursively computed.

            if self.sparse:
                Lm1 = np.sum(l) - 1
            else:
                Lm1 = self.L - 1

            if k in self.surr_lm1[L]:
                #                print('surrogate already computed')
                surr_lm1 = self.surr_lm1[L][k]
            else:
                surr_lm1 = self.sc_expansion(Lm1, samples, x=Map[k]['X'])
                self.surr_lm1[L][k] = surr_lm1

            s_k = q_k - surr_lm1

            idx = {}
            # indices of current collocation point (Map[k]['X'][n]),
            # in corresponding 1d colloc points (self.xi_1d[n][l[n]])
            # These are the j of the 1D lagrange polynomials l_j(x), see
            # lagrange_poly subroutine
            for n in range(self.N):
                idx[n] = (self.xi_1d[n][l[n]] == Map[k]['X'][n]).nonzero()[0][0]

            weight = []
            for n in range(self.N):
                # interpolate
                x = kwargs['x']
                # add values of Lagrange polynomials at x
                weight.append(lagrange_poly(x[n], self.xi_1d[n][l[n]], idx[n]))

            # Delta is the interpolation of the hierarchical surplus
            surr += s_k * np.prod(weight)

        return surr

    def clear_surr_lm1(self):
        """
        Clears the interpolation results in surr_lm1[ID].

        surr_lm1 is a dictionary used to store surrogate results at
        previous level (l-1). Used to avoid recomputing the surrogate
        in the recursive sc_expansion subroutine.

        surr_lm1[l][k] stores the interpolation results
        of level l-1 at collocation point X_k

        Parameters
        ----------
        - ID (str): either 'interpolate' or 'quadrature'

        """
        self.surr_lm1 = {}
        for level in range(self.L_min, self.L + 1):
            self.surr_lm1[level] = {}

    def compute_SC_weights(self, rule):
        """
        Computes the 1D quadrature weights w_j of the SC expansion:

            w_j = int L_j(x)p(x) dx                             (1)

        Here L_j is a Lagrange polynomial of the SC expansion.

        Parameters
        ----------
        - rule ("str"): chaospy quadrature rule used to compute (1),


        Returns
        -------
        - wi_1d (dict): wi_1d[n][l] gives an array
          of quadrature weigths for the n-th parameter at level l.

          IMPORTANT:
          If rule is the same as the rule used to compute the SC
          collocation points, these weights will equal the weights
          computed by chaospy, since L_j(x_k) = 1 when j=k and 0
          for the rest. This is the default setting.
        """

        # no need to recompute weights
        if rule == self.sampler.quadrature_rule:
            return self.sampler.wi_1d
        # recompute weights - generally not used
        else:
            wi_1d = {}

            params = self.sampler.params_distribution

            for n in range(self.N):
                # 1d weights for n-th parameter
                wi_1d[n] = {}
                # loop over all level of collocation method
                for level in range(1, self.L + 1):
                    # current SC nodes over dimension n and level
                    xi_1d = self.xi_1d[n][level]
                    wi_1d[n][level] = np.zeros(xi_1d.size)

                    # generate a quadrature rule to compute the SC weights
                    xi_quad, wi_quad = cp.generate_quadrature(level, params[n], rule=rule)
                    xi_quad = xi_quad[0]

                    # compute integral of the lagrange polynomial through xi_1d, weighted
                    # by the input distributions:
                    # w_j = int L_j(xi) p(xi) dxi j = 1,..,xi_1d.size
                    for j in range(xi_1d.size):
                        # values of L_i(xi_quad)
                        lagrange_quad = np.zeros(xi_quad.size)
                        for i in range(xi_quad.size):
                            lagrange_quad[i] = lagrange_poly(xi_quad[i], xi_1d, j)
                        # quadrature
                        wi_1d[n][level][j] = np.sum(lagrange_quad * wi_quad)

            return wi_1d

    def get_sample_array(self, qoi):
        """
        Parameters
        ----------
        - qoi (str): name of quantity of interest

        Returns
        -------
         - array of all samples of qoi
        """

        tmp = np.zeros([self._number_of_samples, self.N_qoi])

        for k in range(self._number_of_samples):
            tmp[k, :] = (self.samples[qoi][k])

        return tmp

    def plot_grid(self):
        """
        If N = 2 or N = 3 plot the (sparse) grid
        """
        import matplotlib.pyplot as plt

        if self.N == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, xlabel=r'$x_1$', ylabel=r'$x_2$')
            ax.plot(self.xi_d[:, 0], self.xi_d[:, 1], 'ro')
        elif self.N == 3:
            from mpl_toolkits.mplot3d import Axes3D
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d', xlabel=r'$x_1$',
                                 ylabel=r'$x_2$', zlabel=r'$x_3$')
            ax.scatter(self.xi_d[:, 0], self.xi_d[:, 1], self.xi_d[:, 2])
        else:
            print('Will only plot for N = 2 or N = 3.')

        plt.tight_layout()
        plt.show()

    # Start SC specific methods

    @staticmethod
    def compute_tensor_prod_u(xi, wi, u, u_prime):
        """
        Calculate tensor products of weights and collocation points
        with dimension of u and u'

        Parameters
        ----------
        xi (array of floats): 1D colloction points
        wi (array of floats): 1D quadrature weights
        u  (array of int): dimensions
        u_prime (array of int): remaining dimensions (u union u' = range(N))

        Returns
        dict of tensor products of weight and points for dimensions u and u'
        -------

        """

        # tensor products with dimension of u
        xi_u = {}
        wi_u = {}
        for key in u:
            xi_u[key] = xi[key]
            wi_u[key] = wi[key]

        xi_d_u = np.array(list(product(*xi_u.values())))
        wi_d_u = np.array(list(product(*wi_u.values())))

        # tensor products with dimension of u' (complement of u)
        xi_u_prime = {}
        wi_u_prime = {}
        for key in u_prime:
            xi_u_prime[key] = xi[key]
            wi_u_prime[key] = wi[key]

        xi_d_u_prime = np.array(list(product(*xi_u_prime.values())))
        wi_d_u_prime = np.array(list(product(*wi_u_prime.values())))

        return {'xi_d_u': xi_d_u, 'wi_d_u': wi_d_u,
                'xi_d_u_prime': xi_d_u_prime, 'wi_d_u_prime': wi_d_u_prime}

    def compute_marginal(self, qoi, u, u_prime, diff):
        """
        Computes a marginal integral of the qoi(x) over the dimension defined
        by u_prime, for every x value in dimensions u

        Parameters
        ----------
        - qoi (str): name of the quantity of interest
        - u (array of int): dimensions which are not integrated
        - u_prime (array of int): dimensions which are integrated
        - diff (array of int): levels

        Returns
        - Values of the marginal integral
        -------

        """

        # 1d weights and points of the levels in diff
        xi = [self.xi_1d[n][np.abs(diff)[n]] for n in range(self.N)]
        wi = [self.wi_1d[n][np.abs(diff)[n]] for n in range(self.N)]

        # compute tensor products and weights in dimension u and u'
        tmp = self.compute_tensor_prod_u(xi, wi, u, u_prime)
        xi_d_u = tmp['xi_d_u']
        wi_d_u = tmp['wi_d_u']
        xi_d_u_prime = tmp['xi_d_u_prime']
        wi_d_u_prime = tmp['wi_d_u_prime']

        S_u = xi_d_u.shape[0]
        S_u_prime = xi_d_u_prime.shape[0]

        # marginals h = f*w' integrated over u', so cardinality is that of u
        h = {}
        for i_u in range(S_u):
            h[i_u] = 0.
            for i_up in range(S_u_prime):

                # collocation point to be evaluated
                xi_s = np.zeros(self.N)

                # add the xi of u (at the correct location k)
                idx = 0
                for k in u:
                    xi_s[k] = xi_d_u[i_u][idx]
                    idx += 1

                # add the xi of u' (at the correct location k)
                idx = 0
                for k in u_prime:
                    xi_s[k] = xi_d_u_prime[i_up][idx]
                    idx += 1

                # find the index of the corresponding code sample
                tmp = np.prod(self.xi_d == xi_s, axis=1)
                idx = np.where(tmp == 1)[0][0]

                # perform quadrature
                q_k = self.samples[qoi][idx].flatten()
                h[i_u] += q_k * wi_d_u_prime[i_up].prod()

        # return marginal and the weights of dimensions u
        return h, wi_d_u

    def get_sobol_indices(self, qoi, typ='first_order'):
        """
        Computes Sobol indices using Stochastic Collocation. Method:
        Tang (2009), GLOBAL SENSITIVITY ANALYSIS  FOR STOCHASTIC COLLOCATION
        EXPANSION.

        Parameters
        ----------
        qoi (str): name of the Quantity of Interest for which to compute the indices
        typ (str): Default = 'first_order'. 'all' is also possible

        Returns
        -------
        Either the first order or all Sobol indices of qoi
        """

        print('Computing', typ, 'Sobol indices')

        # multi indices
        U = list(range(self.N))

        if typ == 'first_order':
            P = list(powerset(U))[0:self.N + 1]
        elif typ == 'all':
            # all indices u
            P = list(powerset(U))

        # get first two moments
        mu, D = self.get_moments(qoi)
        mu = mu.flatten()
        D = D.flatten()

        # partial variances
        D_u = {P[0]: mu**2}

        sobol = {}

        for u in P[1:]:

            # complement of u
            u_prime = np.delete(U, u)
            D_u[u] = 0.0

            for l in self.l_norm:

                # expand the multi-index indices of the tensor product
                # (Q^1_{i1} - Q^1_{i1-1}) X ... X (Q^1_{id) - Q^1_{id-1})
                diff_idx = np.array(list(product(*[[k, -(k - 1)] for k in l])))

                # perform analysis on each Q^1_l1 X ... X Q^1_l_N tensor prod
                for diff in diff_idx:

                    #if any Q^1_li is below the minimim level, Q^1_li is defined
                    #as zero: do not compute this Q^1_l1 X ... X Q^1_l_N tensor prod
                    if not (np.abs(diff) < self.l_norm_min).any():

                        # mariginal integral h, integrate over dimensions u'
                        h, wi_d_u = self.compute_marginal(qoi, u, u_prime, diff)

                        # square result and integrate over remaining dimensions u
                        for i_u in range(wi_d_u.shape[0]):
                            D_u[u] += np.sign(np.prod(diff)) * h[i_u]**2 * wi_d_u[i_u].prod()

                D_u[u] = D_u[u].flatten()

            # all subsets of u
            W = list(powerset(u))[0:-1]

            # partial variance of u
            for w in W:
                D_u[u] -= D_u[w]

            # compute Sobol index, only include points where D > 0
            # sobol[u] = D_u[u][idx_gt0]/D[idx_gt0]
            sobol[u] = D_u[u] / D

        sort = []
        for u in P[1:]:

            sort.append(sobol[u])

        print('done')
        return sobol

    # End SC specific methods


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    Taken from: https://docs.python.org/3/library/itertools.html#recipes

    Parameters
    ----------
    iterable : iterable
        Input sequence

    Returns
    -------

    """

    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def lagrange_poly(x, x_i, j):
    """
    Lagrange polynomials used for interpolation

    l_j(x) = product(x - x_m / x_j - x_m) with 0 <= m <= k
                                               and m !=j

    Parameters
    ----------
    x : (float), location at which to compute the polynomial

    x_i : list or array of float, nodes of the Lagrange polynomials

    j : int, index of node at which l_j(x_j) = 1

    Returns
    -------
    float
        l_j(x) calculated as shown above.
    """

    l_j = 1.0

    for m in range(len(x_i)):

        if m != j:
            denom = x_i[j] - x_i[m]
            nom = x - x_i[m]

            l_j *= nom / denom

    return l_j
