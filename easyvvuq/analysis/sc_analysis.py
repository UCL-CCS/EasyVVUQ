import numpy as np
import chaospy as cp
from itertools import product, chain, combinations
import pickle
import copy
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from .results import AnalysisResults
import logging
from scipy.special import comb
import pandas as pd

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


class SCAnalysisResults(AnalysisResults):
    implemented = ['sobols_first', 'describe']

    def _get_sobols_first(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_first'])
        return raw_dict[AnalysisResults._to_tuple(qoi)][input_][0]

    def _get_sobols_first_conf(self, qoi, input_):
        return [float('nan'), float('nan')]

    def describe(self):
        result = {}
        for qoi in self.qois:
            result[qoi] = {
                'mean': self.raw_data['statistical_moments'][qoi]['mean'],
                'var': self.raw_data['statistical_moments'][qoi]['var'],
                'std': self.raw_data['statistical_moments'][qoi]['std']
            }
        return pd.DataFrame(result)


class SCAnalysis(BaseAnalysisElement):

    def __init__(self, sampler=None, qoi_cols=None):
        """
        Parameters
        ----------
        sampler : :obj:`easyvvuq.sampling.stochastic_collocation.SCSampler`
            Sampler used to initiate the SC analysis
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
        self.dimension_adaptive = sampler.dimension_adaptive
        if self.dimension_adaptive:
            self.adaptation_errors = []
            self.mean_history = []
        self.sparse = sampler.sparse

    def element_name(self):
        """Name for this element for logging purposes"""
        return "SC_Analysis"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.5"

    def save_state(self, filename):
        """
        Saves the complete state of the analysis object to a pickle file,
        except the sampler object (self.samples).

        Parameters
        ----------
        filename : (string) name to the file to write the state to

        Returns
        -------
        None.

        """
        print("Saving analysis state to %s" % filename)
        # make a copy of the state, and do not store the sampler as well
        state = copy.copy(self.__dict__)
        del state['sampler']
        file = open(filename, 'wb')
        pickle.dump(state, file)
        file.close()

    def load_state(self, filename):
        """
        Loads the complete state of the analysis object from a
        pickle file, stored using save_state.

        Parameters
        ----------
        filename : (string) name of the file to load

        Returns
        -------
        None.

        """
        print("Loading analysis state from %s" % filename)
        file = open(filename, 'rb')
        state = pickle.load(file)
        for key in state.keys():
            self.__dict__[key] = state[key]
        file.close()

    def analyse(self, data_frame=None, compute_results=True):
        """Perform SC analysis on input `data_frame`.

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

        # the number of uncertain parameters
        self.N = self.sampler.N
        # tensor grid
        self.xi_d = self.sampler.xi_d
        # the maximum level (quad order) of the (sparse) grid
        self.L = self.sampler.L

        # if L < L_min: quadratures and interpolations are zero
        # For full tensor grid: there is only one level: L_min = L
        if not self.sparse:
            self.L_min = self.L
            self.l_norm = np.array([self.sampler.polynomial_order])
            self.l_norm_min = self.l_norm
        # For sparse grid: one or more levels
        else:
            self.L_min = 1
            # multi indices (stored in l_norm) for isotropic sparse grid or
            # dimension-adaptive grid before the 1st refinement.
            # If dimension_adaptive and number_of_adaptations > 0: l_norm
            # is computed in self.adaptation_metric
            if not self.dimension_adaptive or self.sampler.number_of_adaptations == 0:
                # the maximum level (quad order) of the (sparse) grid
                self.l_norm = self.sampler.compute_sparse_multi_idx(self.L, self.N)

            self.l_norm_min = np.ones(self.N, dtype=int)

        # 1d weights and points per level
        self.xi_1d = self.sampler.xi_1d
        self.wi_1d = self.compute_SC_weights(rule=self.sampler.quad_rule)

        # per level, map a unique index k to all (level multi indices, colloc points)
        # combinations. Will differ for sparse or full tensor grids.
        # All interpolation/quadrature subroutines loop over the entries in Map
        self.Map = {}
        self.surr_lm1 = {}

        print('Computing collocation points and level indices...')
        for level in range(self.L_min, self.L + 1):
            self.Map[level] = self.create_map(level)
        print('done.')
        self.clear_surr_lm1()

        # Extract output values for each quantity of interest from Dataframe
        print('Loading samples...')
        qoi_cols = self.qoi_cols
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == run_id][k].values
                samples[k].append(values)
        self.samples = samples
        print('done')

        # size of one code sample
        self.N_qoi = self.samples[qoi_cols[0]][0].size

        if compute_results:
            results = {'statistical_moments': {},
                       'sobols_first': {k: {} for k in self.qoi_cols},
                       'sobols': {k: {} for k in self.qoi_cols}}

            # Compute descriptive statistics for each quantity of interest
            for qoi_k in qoi_cols:
                mean_k, var_k = self.get_moments(qoi_k)
                std_k = np.sqrt(var_k)
                # compute statistical moments
                results['statistical_moments'][qoi_k] = {'mean': mean_k,
                                                         'var': var_k,
                                                         'std': std_k}
                # compute all Sobol indices
                results['sobols'][qoi_k] = self.get_sobol_indices(qoi_k, 'first_order')
                for idx, param_name in enumerate(self.sampler.vary.get_keys()):
                    results['sobols_first'][qoi_k][param_name] = \
                        results['sobols'][qoi_k][(idx,)]

            return SCAnalysisResults(raw_data=results, samples=data_frame,
                                     qois=qoi_cols, inputs=list(self.sampler.vary.get_keys()))

    def create_map(self, L):
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
        logging.debug('Creating multi-index map for level %d', L)
        # full tensor product
        if not self.sparse:
            # l = (np.ones(N) * L).astype('int')
            l = (self.sampler.polynomial_order)
            # map_ = [{'l': l, 'X': x, 'f': k} for k, x in enumerate(self.xi_d)]
            k = 0
            map_ = {}
            for x in self.xi_d:
                map_[k] = {'l': l, 'X': x, 'f': k}
                k += 1
        # sparse grid
        else:
            # all sparse grid multi indices l
            # l_norm_le_L = self.sampler.compute_sparse_multi_idx(L, N)
            idx_le_L = np.where(np.sum(self.l_norm, axis=1) - self.N + 1 <= L)
            l_norm_le_L = self.l_norm[idx_le_L]
            k = 0
            map_ = {}
            # loop over all multi indices
            for l in l_norm_le_L:
                # colloc point of current level index l
                X_l = [self.xi_1d[n][l[n]] for n in range(self.N)]
                X_l = np.array(list(product(*X_l)))
                for x in X_l:
                    j = np.where((x == self.xi_d).all(axis=1))[0][0]
                    map_[k] = {'l': l, 'X': x, 'f': j}
                    k += 1
        logging.debug('done.')
        return map_

    def adapt_dimension(self, qoi, data_frame, store_mean_history=False):
        """
        Compute the adaptation metric and decide which of the admissible
        level indices to include in next iteration of the sparse grid. The
        adaptation metric is based on the hierarchical surplus, defined as the
        difference between the new code values of the admissible level indices,
        and the SC surrogate of the previous iteration. Important: this
        subroutine must therefore be called AFTER the code is evaluated at
        the new points, but BEFORE the analysis is performed.

        Parameters
        ----------
        qoi : (string) the name of the quantity of interest which is used
                       to base the adaptation metric on.
        data_frame : the data frame from the EasyVVUQ Campaign

        Returns
        -------
        None.

        """
        # load the code samples
        samples = []
        for run_id in data_frame.run_id.unique():
            values = data_frame.loc[data_frame['run_id'] == run_id][qoi].values
            samples.append(values)

        # the currently accepted grid points
        xi_d_accepted = self.sampler.generate_grid(self.l_norm)

        # compute the hierarchical surplus based error for every admissible l
        error = {}
        for l in self.sampler.admissible_idx:
            error[tuple(l)] = []
            # collocation points of current level index l
            X_l = [self.sampler.xi_1d[n][l[n]] for n in range(self.N)]
            X_l = np.array(list(product(*X_l)))
            # only consider new points, subtract the accepted points
            X_l = setdiff2d(X_l, xi_d_accepted)
            for xi in X_l:
                # find the location of the current xi in the global grid
                idx = np.where((xi == self.sampler.xi_d).all(axis=1))[0][0]
                # hierarchical surplus error at xi
                hier_surplus = samples[idx] - self.surrogate(qoi, xi)
                error[tuple(l)].append(np.linalg.norm(hier_surplus, np.inf))
            # compute mean error over all points in X_l
            error[tuple(l)] = np.mean(error[tuple(l)])
        for key in error.keys():
            print("Surplus error when l =", key, "=", error[key])
        # find the admissble index with the largest error
        l_star = np.array(max(error, key=error.get)).reshape([1, self.N])
        print('Selecting', l_star, 'for refinement.')
        # add max error to list
        self.adaptation_errors.append(max(error.values()))

        # add l_star to the current accepted level indices
        self.l_norm = np.concatenate((self.l_norm, l_star))
        # if someone executes this function twice for some reason,
        # remove the duplicate l_star entry. Keep order unaltered
        idx = np.unique(self.l_norm, axis=0, return_index=True)[1]
        self.l_norm = self.l_norm[idx]

        # peform the analyse step, but do not compute moments and Sobols
        self.analyse(data_frame, compute_results=False)

        if store_mean_history:
            self.mean_history.append(self.quadrature(qoi))

        # self.L = np.max(np.sum(self.l_norm, axis = 1) - self.N + 1)
        # self.xi_d = self.sampler.generate_grid(self.l_norm)
        # self.run_id = []

        # #names of the uncertain variables
        # uncertain_vars = list(self.sampler.vary.get_keys())
        # #loop over all samples in the data frame
        # for run_id in data_frame["run_id"].unique():
        #     #find the value of the input params at current run_id
        #     xi = data_frame.loc[data_frame["run_id"] == run_id][uncertain_vars].values[0]
        #     #see if this point is also in self.xi_d
        #     idx = np.where((xi == self.xi_d).all(axis = 1))[0]
        #     #if so, add run_id to self.run_id
        #     if idx.size != 0:
        #         self.run_id.append(run_id)

    def get_adaptation_errors(self):
        """
        Returns self.adaptation_errors
        """
        return self.adaptation_errors

    def plot_mean_convergence(self):
        """
        Plots the convergence of the statistical mean over the different
        refinements in a dimension-adaptive setting.

        Returns
        -------
        None.

        """
        if not self.dimension_adaptive:
            print('Only works for the dimension adaptive sampler.')
            return

        K = len(self.mean_history)
        if K < 2:
            print('Means from at least two refinements are required')
            return
        else:
            differ = np.zeros(K - 1)
            for i in range(1, K):
                differ[i - 1] = np.linalg.norm(self.mean_history[i] -
                                               self.mean_history[i - 1], np.inf)
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=[4, 4])
        ax = fig.add_subplot(111, xlabel=r'refinement step',
                             ylabel=r'$ ||\mathrm{mean}_i - \mathrm{mean}_{i - 1}||_\infty$')
        ax.plot(range(2, K + 1), differ, '-b+')
        plt.tight_layout()
        plt.show()

    def surrogate(self, qoi, x, L=None):
        """
        Use sc_expansion UQP as a surrogate

        Parameters
        ----------
        - qoi (str): name of the qoi

        Returns
        -------
        the interpolated value of qoi at x (float, (N_qoi,))

        """

        if L is None:
            L = self.L

        return self.sc_expansion(L, self.samples[qoi], x=x)

    def quadrature(self, qoi, samples=None):
        """
        Computes a (Smolyak) quadrature

        Parameters
        ----------
        - qoi (str): name of the qoi

        - samples (optional in kwargs): Default: compute the mean
          by setting samples = self.samples. To compute the variance,
          set samples = (self.samples - mean)**2
        """
        if samples is None:
            samples = self.samples[qoi]
        # compute the Delta Q :=
        # (Q^1_l_1 - Q^1_{l_1 - 1}) X ... X (Q^1_{l_N} - Q^1_{L_N - 1})
        # tensor product

        if not self.sparse or self.dimension_adaptive:
            return np.array([self.compute_Q_diff(l, samples) for l in self.l_norm]).sum(axis=0)
        else:
            return self.combination_technique(qoi, samples)

    def combination_technique(self, qoi, samples=None):
        """
        Efficient quadrature formulation for isotropic sparse grids. See:

            Gerstner, Griebel, "Numerical integration using sparse grids"
            page 7.

        Parameters
        ----------
        - qoi (str): name of the qoi

        - samples (optional in kwargs): Default: compute the mean
          by setting samples = self.samples. To compute the variance,
          set samples = (self.samples - mean)**2
        """

        if samples is None:
            samples = self.samples[qoi]

        # quadrature Q
        Q = 0.0

        # loop over l
        for l in self.l_norm:

            # for sum(l) < L, combination technique formula shows that weights
            # are zero
            if np.sum(l) >= self.L:

                # compute the tensor product of parameter and weight values
                X_k = [self.xi_1d[n][l[n]] for n in range(self.N)]
                W_k = [self.wi_1d[n][l[n]] for n in range(self.N)]

                X_k = np.array(list(product(*X_k)))
                W_k = np.array(list(product(*W_k)))
                W_k = np.prod(W_k, axis=1)
                W_k = W_k.reshape([W_k.shape[0], 1])

                # scaling factor of combination technique
                scaling_factor = (-1)**(self.L + self.N - np.sum(l) - 1) * \
                    comb(self.N - 1, np.sum(l) - self.L)
                W_k *= scaling_factor

                # find corresponding code values
                f_k = np.array([samples[np.where((x == self.xi_d).all(axis=1))[0][0]] for x in X_k])

                # quadrature of Q^1_{k1} X ... X Q^1_{kN} product
                Q += np.sum(f_k * W_k, axis=0).T

        return Q

    def compute_Q_diff(self, l, samples):
        """
        Brute force computation of quadrature difference operators \Delta_l
        Note: superseded by combination_technique for sparse grids, but might
        still be useful for anisotropic sparse grids. Becomes very slow though
        for a large number of parameters, and is therefore in need of
        replacement.
        =======================================================================
        For every multi index l = (l1, l2, ..., ld), Smolyak sums over
        tensor products difference quadrature rules:
        (Q^1_{l1} - Q^1_{l1-1}) X ... X (Q^1_{lN) - Q^1_{lN-1})
        Below this product is expanded into individual tensor products, each
        of which is then computed as:
        Q^1_{k1} X ... X Q^1_{kN} = sum...sum w_{k1}*...*w_{kN}*f(x_{k1},...,x_{kN})
        =======================================================================
        Parameters
        - l : multi index of quadrature orders
        - samples: array of samples to use in the quadrature

        Returns: value of the difference operator
        """

        # expand the multi-index indices of the tensor product
        # (Q^1_{i1} - Q^1_{i1-1}) X ... X (Q^1_{id) - Q^1_{id-1})
        diff_idx = np.array(list(product(*[[k, -(k - 1)] for k in l])))

        # Delta will be the sum of all expanded tensor products
        # Q^1_{k1} X ... X Q^1_{kd} = sum...sum w_{k1}*...*w_{kN}*f(x_{k1},...,x_{kd})
        Delta = 0.0

        # each diff contains the level indices of to a single
        # Q^1_{k1} X ... X Q^1_{kN} product
        for diff in diff_idx:
            # if any Q^1_{ki} is below the minimim level, Q^1_{ki} is defined
            # as zero: do not compute this Q^1_{k1} X ... X Q^1_{kN} product
            if not (np.abs(diff) < self.l_norm_min).any():

                # compute the tensor product of parameter and weight values
                X_k = [self.xi_1d[n][np.abs(diff)[n]] for n in range(self.N)]
                W_k = [self.wi_1d[n][np.abs(diff)[n]] for n in range(self.N)]

                X_k = np.array(list(product(*X_k)))
                W_k = np.array(list(product(*W_k)))
                W_k = np.prod(W_k, axis=1)
                W_k = W_k.reshape([W_k.shape[0], 1])

                # find corresponding code values
                f_k = np.array([samples[np.where((x == self.xi_d).all(axis=1))[0][0]] for x in X_k])

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
        print('Computing moments...')
        # compute mean
        mean_f = self.quadrature(qoi)
        # compute variance
        variance_samples = [(sample - mean_f)**2 for sample in self.samples[qoi]]
        var_f = self.quadrature(qoi, samples=variance_samples)
        print('done')
        return mean_f, var_f

    def sc_expansion(self, L, samples, x):
        """
        -----------------------------------------
        This is the UQ Pattern for the SC method.
        -----------------------------------------

        Can perform interpolation for both full and sparse grids.

        For a qoi q, it computes the following tensor product:

        $\\approx \\sum_{l in \\Lambda} \\Delta_{l}[q](x)$

        where $\\Delta_{l}$ is the difference at x between surrogates / quadratues
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
                # In case of sparse grid: level = sum(l) - N + 1
                # so prev level is sum(l) - N
                Lm1 = np.sum(l) - self.N
            else:
                # previous level of full tensor grid = L - 1, will yield a zero
                Lm1 = self.L - 1

            if k in self.surr_lm1[L]:
                #print('surrogate already computed')
                surr_lm1 = self.surr_lm1[L][k]
            else:
                surr_lm1 = self.sc_expansion(Lm1, samples, x=Map[k]['X'])
                self.surr_lm1[L][k] = surr_lm1

            s_k = q_k - surr_lm1

            # indices of current collocation point (Map[k]['X'][n]),
            # in corresponding 1d colloc points (self.xi_1d[n][l[n]])
            # These are the j of the 1D lagrange polynomials l_j(x), see
            # lagrange_poly subroutine
            idx = [(self.xi_1d[n][l[n]] == Map[k]['X'][n]).nonzero()[0][0] for n in range(self.N)]
            # interpolate
            # add values of Lagrange polynomials at x
            weight = [lagrange_poly(x[n], self.xi_1d[n][l[n]], idx[n]) for n in range(self.N)]
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
        return np.array([self.samples[qoi][k] for k in range(len(self.samples[qoi]))])

    def adaptation_histogram(self):
        """
        Parameters
        ----------
        None

        Returns
        -------
        Plots a bar chart of the maximum order of the quadrature rule
        that is used in each dimension. Use in case of the dimension adaptive
        sampler to get an idea of which parameters were more refined than others.
        This gives only a first-order idea, as it only plots the max quad
        order independently per input parameter, so higher-order refinements
        that were made do not show up in the bar chart.
        """
        import matplotlib.pyplot as plt

        fig = plt.figure(figsize=[4, 8])
        ax = fig.add_subplot(111, ylabel='max quadrature order',
                             title='Number of refinements = %d'
                             % self.sampler.number_of_adaptations)
        # find max quad order for every parameter
        adapt_measure = np.max(self.l_norm, axis=0)
        ax.bar(range(adapt_measure.size), height=adapt_measure)
        params = list(self.sampler.vary.get_keys())
        ax.set_xticks(range(adapt_measure.size))
        ax.set_xticklabels(params)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    def plot_grid(self):
        """
        Plots the collocation points for 2 and 3 dimensional problems
        """
        import matplotlib.pyplot as plt

        if self.N == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, xlabel=r'$x_1$', ylabel=r'$x_2$')
            ax.plot(self.xi_d[:, 0], self.xi_d[:, 1], 'ro')
            plt.tight_layout()
            plt.show()
        elif self.N == 3:
            from mpl_toolkits.mplot3d import Axes3D
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d', xlabel=r'$x_1$',
                                 ylabel=r'$x_2$', zlabel=r'$x_3$')
            ax.scatter(self.xi_d[:, 0], self.xi_d[:, 1], self.xi_d[:, 2])
            plt.tight_layout()
            plt.show()
        else:
            print('Will only plot for N = 2 or N = 3.')

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
        xi_u = [xi[key] for key in u]
        wi_u = [wi[key] for key in u]

        xi_d_u = np.array(list(product(*xi_u)))
        wi_d_u = np.array(list(product(*wi_u)))

        # tensor products with dimension of u' (complement of u)
        xi_u_prime = [xi[key] for key in u_prime]
        wi_u_prime = [wi[key] for key in u_prime]

        xi_d_u_prime = np.array(list(product(*xi_u_prime)))
        wi_d_u_prime = np.array(list(product(*wi_u_prime)))

        return xi_d_u, wi_d_u, xi_d_u_prime, wi_d_u_prime

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
        xi_d_u, wi_d_u, xi_d_u_prime, wi_d_u_prime =\
            self.compute_tensor_prod_u(xi, wi, u, u_prime)

        idxs = np.argsort(np.concatenate((u, u_prime)))
        # marginals h = f*w' integrated over u', so cardinality is that of u
        h = [0.0] * xi_d_u.shape[0]
        for i_u, xi_d_u_ in enumerate(xi_d_u):
            for i_up, xi_d_u_prime_ in enumerate(xi_d_u_prime):
                xi_s = np.concatenate((xi_d_u_, xi_d_u_prime_))[idxs]
                # find the index of the corresponding code sample
                idx = np.where(np.prod(self.xi_d == xi_s, axis=1))[0][0]
                # perform quadrature
                q_k = self.samples[qoi][idx]
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
        print('Computing Sobol indices...')
        # multi indices
        U = np.arange(self.N)

        if typ == 'first_order':
            P = list(powerset(U))[0:self.N + 1]
        elif typ == 'all':
            # all indices u
            P = list(powerset(U))

        # get first two moments
        mu, D = self.get_moments(qoi)

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

                    # if any Q^1_li is below the minimim level, Q^1_li is defined
                    # as zero: do not compute this Q^1_l1 X ... X Q^1_l_N tensor prod
                    if not (np.abs(diff) < self.l_norm_min).any():

                        # mariginal integral h, integrate over dimensions u'
                        h, wi_d_u = self.compute_marginal(qoi, u, u_prime, diff)

                        # square result and integrate over remaining dimensions u
                        for i_u in range(wi_d_u.shape[0]):
                            D_u[u] += np.sign(np.prod(diff)) * h[i_u]**2 * wi_d_u[i_u].prod()

                #D_u[u] = D_u[u].flatten()

            # all subsets of u
            W = list(powerset(u))[0:-1]

            # partial variance of u
            for w in W:
                D_u[u] -= D_u[w]

            # compute Sobol index, only include points where D > 0
            # sobol[u] = D_u[u][idx_gt0]/D[idx_gt0]
            sobol[u] = D_u[u] / D
        print('done.')
        return sobol


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
    x_i_ = np.delete(x_i, j)
    return np.prod((x - x_i_) / (x_i[j] - x_i_))


def setdiff2d(X, Y):
    """
    Computes the difference of two 2D arrays X \ Y

    Parameters
    ----------
    X : 2D numpy array
    Y : 2D numpy array

    Returns
    -------
    The difference X \ Y as a 2D array

    """
    diff = set(map(tuple, X)) - set(map(tuple, Y))
    return np.array(list(diff))
