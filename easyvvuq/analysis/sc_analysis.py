import numpy as np
import chaospy as cp
from itertools import product, chain, combinations
import pickle
import copy
from easyvvuq import OutputType
from .base import BaseAnalysisElement
import logging
from scipy.special import comb
import pandas as pd
from numba import jit

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
            self.std_history = []
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
        #make a copy of the state, and do not store the sampler as well
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

    def analyse(self, data_frame=None, compute_moments=True, compute_Sobols=True):
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
        elif type(data_frame) == pd.DataFrame and data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        # the number of uncertain parameters
        self.N = self.sampler.N
        #tensor grid
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
            #multi indices (stored in l_norm) for isotropic sparse grid or
            #dimension-adaptive grid before the 1st refinement.
            #If dimension_adaptive and number_of_adaptations > 0: l_norm
            #is computed in self.adaptation_metric
            if not self.dimension_adaptive or self.sampler.number_of_adaptations == 0:
                # the maximum level (quad order) of the (sparse) grid
                self.l_norm = self.sampler.compute_sparse_multi_idx(self.L, self.N)

            self.l_norm_min = np.ones(self.N, dtype=int)

        # #compute generalized combination coefficients
        self.compute_comb_coef()

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
        if type(data_frame) == pd.DataFrame:
            for run_id in data_frame.run_id.unique():
                for k in qoi_cols:
                    values = data_frame.loc[data_frame['run_id'] == run_id][k].values
                    samples[k].append(values)
        elif type(data_frame) == dict:
            #dict is not sorted, make sure the runs are processed in ascending order
            for k in qoi_cols:
                run_id_int = [int(run_id.split('Run_')[-1]) for run_id in data_frame[k].keys()]
                for run_id in range(1, np.max(run_id_int) + 1):
                        samples[k].append(data_frame[k]['Run_' + str(run_id)])
        self.samples = samples
        print('done')

        # size of one code sample
        self.N_qoi = self.samples[qoi_cols[0]][0].size

        # Compute descriptive statistics for each quantity of interest
        results = {'statistical_moments': {},
                   'sobols_first': {k: {} for k in self.qoi_cols},
                   'sobols': {k: {} for k in self.qoi_cols}}
 
        if compute_moments:
            for qoi_k in qoi_cols:
                mean_k, var_k = self.get_moments(qoi_k)
                std_k = np.sqrt(var_k)
                # compute statistical moments
                results['statistical_moments'][qoi_k] = {'mean': mean_k,
                                                         'var': var_k,
                                                         'std': std_k}

        if compute_Sobols:
            for qoi_k in qoi_cols:
                if not self.sparse:
                    results['sobols'][qoi_k], _ = self.get_sobol_indices(qoi_k, 'first_order')
                else:
                    _, _, _, results['sobols'][qoi_k] = self.get_pce_sobol_indices(qoi_k, 'first_order')

                for idx, param_name in enumerate(self.sampler.vary.get_keys()):
                    results['sobols_first'][qoi_k][param_name] = \
                        results['sobols'][qoi_k][(idx,)]

        self.results = results
        return results

    def compute_comb_coef(self):
        """
        Compute general combination coefficients. These are the coefficients
        multiplying the tensor products associated to each multi index l,
        see page 12 Gerstner & Griebel, numerical integration using sparse grids
        """
        self.comb_coef = {}
        print('Computing combination coefficients...')
        for k in self.l_norm:
            coef = 0.0
            #for every k, subtract all multi indices
            for l in self.l_norm:
                z = l - k
                #if the results contains only 0's and 1's, then z is the
                #vector that can be formed from a tensor product of unit vectors
                #for which k+z is in self.l_norm
                if np.array_equal(z, z.astype(bool)):
                    coef += (-1)**(np.sum(z))
            self.comb_coef[tuple(k)] = coef
        print('done')

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

    def adapt_dimension(self, qoi, data_frame, store_stats_history=True):
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
        print('Refining sampling plan...')
        #load the code samples
        samples = []
        if type(data_frame) == pd.DataFrame:
            for run_id in data_frame.run_id.unique():
                values = data_frame.loc[data_frame['run_id'] == run_id][qoi].values
                samples.append(values)
        elif type(data_frame) == dict:
            #dict is not sorted, make sure the runs are processed in ascending order
            run_id_int = [int(run_id.split('Run_')[-1]) for run_id in data_frame[qoi].keys()]
            for run_id in range(1, np.max(run_id_int) + 1):
                values = data_frame[qoi]['Run_' + str(run_id)]
                samples.append(values)

        #the currently accepted grid points
        xi_d_accepted = self.sampler.generate_grid(self.l_norm)

        #compute the hierarchical surplus based error for every admissible l
        error = {}
        for l in self.sampler.admissible_idx:
            error[tuple(l)] = []
            # collocation points of current level index l
            X_l = [self.sampler.xi_1d[n][l[n]] for n in range(self.N)]
            X_l = np.array(list(product(*X_l)))
            #only consider new points, subtract the accepted points
            X_l = setdiff2d(X_l, xi_d_accepted)
            for xi in X_l:
                #find the location of the current xi in the global grid
                idx = np.where((xi == self.sampler.xi_d).all(axis=1))[0][0]
                #hierarchical surplus error at xi
                hier_surplus = samples[idx] - self.surrogate(qoi, xi)
                error[tuple(l)].append(np.linalg.norm(hier_surplus, np.inf))
            #compute mean error over all points in X_l
            error[tuple(l)] = np.mean(error[tuple(l)])
        for key in error.keys():
            print("Surplus error when l =", key, "=", error[key])
        #find the admissble index with the largest error
        l_star = np.array(max(error, key=error.get)).reshape([1, self.N])
        print('Selecting', l_star, 'for refinement.')
        #add max error to list
        self.adaptation_errors.append(max(error.values()))

        #add l_star to the current accepted level indices
        self.l_norm = np.concatenate((self.l_norm, l_star))
        #if someone executes this function twice for some reason,
        #remove the duplicate l_star entry. Keep order unaltered
        idx = np.unique(self.l_norm, axis=0, return_index=True)[1]
        self.l_norm = np.array([self.l_norm[i] for i in sorted(idx)])

        #if l_norm changes, the interpolation must be reinitialized
        # self.init_interpolation = True

        #peform the analyse step, but do not compute moments and Sobols
        self.analyse(data_frame, compute_moments=False, compute_Sobols=False)

        if store_stats_history:
            mean_f, var_f = self.get_moments(qoi)
            self.mean_history.append(mean_f)
            self.std_history.append(var_f**0.5)

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

    def plot_stat_convergence(self):
        """
        Plots the convergence of the statistical mean and std dev over the different
        refinements in a dimension-adaptive setting. Specifically the inf norm
        of the difference between the stats of iteration i and iteration i-1
        is plotted.

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
            differ_mean = np.zeros(K - 1)
            differ_std = np.zeros(K - 1)
            for i in range(1, K):
                differ_mean[i - 1] = np.linalg.norm(self.mean_history[i] -
                                                    self.mean_history[i - 1], np.inf)

                differ_std[i - 1] = np.linalg.norm(self.std_history[i] -
                                                   self.std_history[i - 1], np.inf)

        import matplotlib.pyplot as plt
        fig = plt.figure('stat_conv')
        ax1 = fig.add_subplot(111, title='moment convergence')
        ax1.set_xlabel('refinement step')
        ax1.set_ylabel(r'$ ||\mathrm{mean}_i - \mathrm{mean}_{i - 1}||_\infty$',
                       color='r', fontsize=12)
        ax1.plot(range(2, K + 1), differ_mean, color='r', marker='+')
        ax1.tick_params(axis='y', labelcolor='r')

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        ax2.set_ylabel(r'$ ||\mathrm{std}_i - \mathrm{std}_{i - 1}||_\infty$',
                       color='b', fontsize=12)
        ax2.plot(range(2, K + 1), differ_std, color='b', marker='*')
        ax2.tick_params(axis='y', labelcolor='b')

        plt.tight_layout()
        plt.show()

    def surrogate(self, qoi, x, L=None, recursive=False):
        """
        Use sc_expansion UQP as a surrogate

        Parameters
        ----------
        - qoi (str): name of the qoi
        - x (array): location at which to evaluate the surrogate
        - L (int): level of the (sparse) grid, default = self.L
        - recursive (boolean): use the recursive implementation of the
          SC expansion, default = False.

        Returns
        -------
        the interpolated value of qoi at x (float, (N_qoi,))
        """

        if L is None:
            L = self.L

        if not recursive:
            return self.sc_expansion(self.samples[qoi], x=x)
        else:
            return self.sc_expansion_recursive(L, self.samples[qoi], x=x)

    def quadrature(self, qoi, samples=None, combination_technique=True):
        """
        Computes a (Smolyak) quadrature

        Parameters
        ----------
        - qoi (str): name of the qoi

        - samples: Default: compute the mean
          by setting samples = self.samples. To compute the variance,
          set samples = (self.samples - mean)**2

        - combination_technique: compute the (sparse) grid quadrature by
          using the general combination technique, default = True. If False,
          the quadrature is computed by a brute force expansion of quadrature
          difference formulas, which is inefficient in high dimensions.

        Returns: the quadrature of qoi
        -------
        """
        if samples is None:
            samples = self.samples[qoi]

        if combination_technique:
            return self.combination_technique(qoi, samples)
        else:
            #brute force quad computation
            return np.array([self.compute_Q_diff(l, samples) for l in self.l_norm]).sum(axis=0)

    def combination_technique(self, qoi, samples=None):
        """
        Efficient quadrature formulation for (sparse) grids. See:

            Gerstner, Griebel, "Numerical integration using sparse grids"
            Uses the general combination technique (page 12).

        Parameters
        ----------
        - qoi (str): name of the qoi

        - samples (optional in kwargs): Default: compute the mean
          by setting samples = self.samples. To compute the variance,
          set samples = (self.samples - mean)**2
        """

        if samples is None:
            samples = self.samples[qoi]

        #quadrature Q
        Q = 0.0

        #loop over l
        for l in self.l_norm:

            # compute the tensor product of parameter and weight values
            X_k = [self.xi_1d[n][l[n]] for n in range(self.N)]
            W_k = [self.wi_1d[n][l[n]] for n in range(self.N)]

            X_k = np.array(list(product(*X_k)))
            W_k = np.array(list(product(*W_k)))
            W_k = np.prod(W_k, axis=1)
            W_k = W_k.reshape([W_k.shape[0], 1])

            # scaling factor of combination technique
            W_k *= self.comb_coef[tuple(l)]

            # find corresponding code values
            f_k = np.array([samples[np.where((x == self.xi_d).all(axis=1))[0][0]] for x in X_k])

            # quadrature of Q^1_{k1} X ... X Q^1_{kN} product
            Q += np.sum(f_k * W_k, axis=0).T

        return Q

    def compute_Q_diff(self, l, samples):
        """
        Brute force computation of quadrature difference operators \Delta_l
        Note: superseded by combination_technique. Becomes slow though
        for a large number of parameters.
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

    def get_moments(self, qoi, combination_technique=True):
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
        mean_f = self.quadrature(qoi, combination_technique=combination_technique)
        # compute variance
        variance_samples = [(sample - mean_f)**2 for sample in self.samples[qoi]]
        var_f = self.quadrature(qoi, samples=variance_samples,
                                combination_technique=combination_technique)
        print('done')
        return mean_f, var_f

    def sc_expansion(self, samples, x):
        """
        -------------------------------------------------
        Non recursive implementation of the SC expansion.
        (Default setting of surrogate)
        -------------------------------------------------
        Performs interpolation for both full and sparse grids.

        Parameters
        ----------
        - samples: array of code samples
        - x (float (N,)): location in stochastic space at which to eval
          the surrogate

        Returns
        -------

        surr (float, (N_qoi,)): the interpolated value of qoi at x

        """
        #TODO: xi_d, idx are computed every time, but only depend upon
        #self.l_norm. Makes it slow, store globally, and only recompute when
        #self.l_norm has changed
        
        # if self.init_interpolation:
        #     self.xi_d_per_l = {}
        #     for l in self.l_norm:
        #         #all points corresponding to l
        #         xi = [self.xi_1d[n][l[n]] for n in range(self.N)]
        #         self.xi_d_per_l[tuple(l)] = np.array(list(product(*xi)))
        #     self.init_interpolation = False
        
        surr = 0.0
        for l in self.l_norm:
            #all points corresponding to l
            xi = [self.xi_1d[n][l[n]] for n in range(self.N)]
            xi_d = np.array(list(product(*xi)))

            for xi in xi_d:
                # indices of current collocation point
                # in corresponding 1d colloc points (self.xi_1d[n][l[n]])
                # These are the j of the 1D lagrange polynomials l_j(x), see
                # lagrange_poly subroutine
                idx = [(self.xi_1d[n][l[n]] == xi[n]).nonzero()[0][0] for n in range(self.N)]
                # values of Lagrange polynomials at x
                weight = [lagrange_poly(x[n], self.xi_1d[n][l[n]], idx[n]) for n in range(self.N)]

                idx = np.where((xi == self.xi_d).all(axis=1))[0][0]
                surr += self.comb_coef[tuple(l)] * samples[idx] * np.prod(weight)

        return surr

    def sc_expansion_recursive(self, L, samples, x):
        """
        --------------------------------------------
        Recursive implementation of the SC expansion.
        --------------------------------------------

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
                #In case of sparse grid: level = sum(l) - N + 1
                #so prev level is sum(l) - N
                Lm1 = np.sum(l) - self.N
            else:
                #previous level of full tensor grid = L - 1, will yield a zero
                Lm1 = self.L - 1

            if k in self.surr_lm1[L]:
                #print('surrogate already computed')
                surr_lm1 = self.surr_lm1[L][k]
            else:
                surr_lm1 = self.sc_expansion_recursive(Lm1, samples, x=Map[k]['X'])
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

        fig = plt.figure('adapt_hist', figsize=[4, 8])
        ax = fig.add_subplot(111, ylabel='max quadrature order',
                             title='Number of refinements = %d'
                             % self.sampler.number_of_adaptations)
        #find max quad order for every parameter
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

    def SC2PCE(self, samples):
        """
        Computes the Polynomials Chaos Expansion coefficients from the SC
        expansion via a transformation of basis (Lagrange polynomials basis -->
        orthonomial basis).

        Parameters
        ----------
        samples : array of SC code samples from which to compute the PCE coefficients

        Returns
        -------
        pce_coefs : dict of PCE coefficients per multi index l

        """
        pce_coefs = {}

        count_l = 1
        for l in self.l_norm:
            #pce coefficients for current multi-index l        
            pce_coefs[tuple(l)] = {}

            #1d points generated by l
            x_1d = [self.xi_1d[n][l[n]] for n in range(self.N)]
            #1d Lagrange polynomials generated by l
            #EDIT: do not use chaospy for Largrange, converts lagrange into monomial, requires
            #Vandermonde matrix inversion to find coefficients, which becomes
            #very ill conditioned rather quickly. Can no longer use cp.E to compute
            #integrals, use GQ instead
            # a_1d = [cp.lagrange_polynomial(sampler.xi_1d[n][l[n]]) for n in range(d)]

            #N-dimensional grid generated by l
            x_l = np.array(list(product(*x_1d)))

            #all multi indices of the PCE expansion: k <= l
            k_norm = list(product(*[np.arange(1, l[n] + 1) for n in range(self.N)]))

            if self.comb_coef[tuple(l)] != 0:
                print('Computing PCE coefficients of refinement %d / %d' % (count_l, self.l_norm.shape[0]))
            else:
                print('Skipping PCE coefficients of refinement %d / %d' % (count_l, self.l_norm.shape[0]))

            for k in k_norm:
                if self.comb_coef[tuple(l)] != 0:
                    #product of the PCE basis function or order k - 1 and all
                    #Lagrange basis functions in a_1d, per dimension
                    #[[phi_k[0]*a_1d[0]], ..., [phi_k[N-1]*a_1d[N-1]]]

                    #orthogonal polynomial generated by chaospy
                    phi_k = [cp.orth_ttr(k[n] - 1,
                                        dist=self.sampler.params_distribution[n],
                                        normed=True)[-1] for n in range(self.N)]

                    #the polynomial order of each integrand phi_k*a_j = (k - 1) + (number of colloc. points - 1) 
                    orders = [(k[n] - 1) + (self.xi_1d[n][l[n]].size - 1) for n in range(self.N)]

                    #will hold the products of PCE basis functions phi_k and lagrange interpolation polynomials a_1d 
                    cross_prod = []

                    for n in range(self.N):
                        #GQ using n points can exactly integrate polynomials of order 2n-1:
                        #solve for required number of points when given order
                        n_quad_points = int(np.ceil((orders[n] + 1) / 2))

                        #generate Gaussian quad rule
                        if isinstance(self.sampler.params_distribution[n], cp.DiscreteUniform):
                            xi = self.xi_1d[n][l[n]]
                            wi = self.wi_1d[n][l[n]]
                            #TODO: remove when chaospy discrete weights have been fixed
                            # wi = np.ones(xi.size)/xi.size
                        else:
                            xi, wi = cp.generate_quadrature(n_quad_points - 1, self.sampler.params_distribution[n], rule="G")
                            xi = xi[0]

                        #number of colloc points = number of Lagrange polynomials
                        n_lagrange_poly = int(self.xi_1d[n][l[n]].size)

                        #compute the v coefficients = coefficients of SC2PCE mapping
                        v_coefs_n = []
                        for j in range(n_lagrange_poly):
                            #compute values of Lagrange polys at quadrature points
                            l_j = np.array([lagrange_poly(xi[i], self.xi_1d[n][l[n]], j) for i in range(xi.size)])
                            #each coef is the integral of the lagrange poly times the current orthogonal PCE poly
                            v_coefs_n.append(np.sum(l_j*phi_k[n](xi)*wi))
                        cross_prod.append(v_coefs_n)

                    #tensor product of all integrals
                    integrals = np.array(list(product(*cross_prod)))
                    #multiply over the number of parameters: v_prod = v_k1_j1 * ... * v_kd_jd
                    v_prod = np.prod(integrals, axis=1)
                    v_prod = v_prod.reshape([v_prod.size, 1])

                    # find corresponding code values
                    f_k = np.array([samples[np.where((x == self.xi_d).all(axis=1))[0][0]] for x in x_l])

                    #the sum of all code sample * v_{k,j_1} * ... * v_{k,j_N}
                    #equals the PCE coefficient 
                    eta_k = np.sum(f_k * v_prod, axis=0).T

                    # #find corresponding point in global grid
                    # idx = np.where((x_l[count] == self.xi_d).all(axis=1))[0][0]
                    # #multiply v_{k,j_1} * ... * v_{k,j_N} with the code output
                    # v_prod = v_prod * samples[idx]
                    # count += 1
                    # eta_k = eta_k + v_prod
                else:
                    eta_k = np.zeros(samples[0].size) 
    
                pce_coefs[tuple(l)][tuple(k)] = eta_k
            count_l += 1

        print('done')
        self.pce_coefs = pce_coefs
        return pce_coefs

    #REMOVE THIS LATER
    # def SC2PCE_old(self, samples):
    #     """
    #     Computes the Polynomials Chaos Expansion coefficients from the SC
    #     expansion via a transformation of basis (Lagrange polynomials basis -->
    #     orthonomial basis).

    #     Parameters
    #     ----------
    #     samples : array of SC code samples from which to compute the PCE coefficients

    #     Returns
    #     -------
    #     pce_coefs : dict of PCE coefficients per multi index l

    #     """
    #     pce_coefs = {}
    #     self.foo2 = {}

    #     count_l = 1
    #     for l in self.l_norm:
    #         #pce coefficients for current multi-index l        
    #         pce_coefs[tuple(l)] = {}

    #         #1d points generated by l
    #         x_1d = [self.xi_1d[n][l[n]] for n in range(self.N)]
    #         #1d Lagrange polynomials generated by l
    #         a_1d = [cp.lagrange_polynomial(self.xi_1d[n][l[n]]) for n in range(self.N)]
    #         #N-dimensional grid generated by l
    #         x_l = np.array(list(product(*x_1d)))

    #         #all multi indices of the PCE expansion: k <= l
    #         k_norm = list(product(*[np.arange(1, l[n] + 1) for n in range(self.N)]))

    #         if self.comb_coef[tuple(l)] != 0:
    #             print('Computing PCE coefficients of refinement %d / %d' % (count_l, self.l_norm.shape[0]))
    #         else:
    #             print('Skipping PCE coefficients of refinement %d / %d' % (count_l, self.l_norm.shape[0]))

    #         for k in k_norm:
    #             if self.comb_coef[tuple(l)] != 0:
    #                 #product of the PCE basis function or order k - 1 and all
    #                 #Lagrange basis functions in a_1d, per dimension
    #                 #[[phi_k[0]*a_1d[0]], ..., [phi_k[N-1]*a_1d[N-1]]]
    #                 cross_prod = [cp.orth_ttr(k[n] - 1,
    #                                           dist=self.sampler.params_distribution[n],
    #                                           normed=True)[-1] * a_1d[n] for n in range(self.N)]

    #                 #the tensor product of cross prod gives all the integrands
    #                 #for which we must compute the integral
    #                 integrands = list(product(*cross_prod))

    #                 #eta_k = the PCE coef corresponding to multi index k
    #                 eta_k = 0.0
    #                 count = 0
                    
    #                 if k == tuple(np.ones(self.N, dtype=int)):
    #                     self.foo2[tuple(l)] = []
                    
    #                 for integrand in integrands:
    #                     v_prod = 1.0
    #                     #compute v_{k,j_1} * ... * v_{k,j_N}, where each v is
    #                     #the integral
    #                     for n in range(self.N):
    #                         v_kj_n = cp.E(integrand[n],
    #                                       self.sampler.params_distribution[n])
    #                         v_prod = v_prod * v_kj_n
    #                     if k == tuple(np.ones(self.N, dtype=int)):
    #                         self.foo2[tuple(l)].append(v_prod)                          

    #                     #find corresponding point in global grid
    #                     idx = np.where((x_l[count] == self.xi_d).all(axis=1))[0][0]
    #                     #multiply v_{k,j_1} * ... * v_{k,j_N} with the code output
    #                     v_prod = v_prod * samples[idx]
    #                     count += 1

    #                     #the sum of all code sample * v_{k,j_1} * ... * v_{k,j_N}
    #                     #equals the PCE coefficient
    #                     eta_k = eta_k + v_prod
    #             else:
    #                eta_k = np.zeros(self.N_qoi) 

    #             pce_coefs[tuple(l)][tuple(k)] = eta_k
    #         count_l += 1

    #     print('done')
    #     self.pce_coefs = pce_coefs
    #     return pce_coefs

    def get_pce_sobol_indices(self, qoi, typ='first_order', **kwargs):
        """
        Computes Sobol indices using Polynomials Chaos coefficients. These
        coefficients are computed from the SC expansion via a transformation
        of basis (SC2PCE subroutine). This works better than computing the
        Sobol indices directly from the SC expansion in the case of the
        dimension-adaptive sampler.

        Method: J.D. Jakeman et al, "Adaptive multi-index collocation
        for uncertainty quantification and sensitivity analysis", 2019.
        (Page 18)

        Parameters
        ----------
        - qoi (str): name of the Quantity of Interest for which to compute the indices
        - typ (str): Default = 'first_order'. 'all' is also possible
        - **kwargs: if this contains 'samples', use these instead of the SC samples 
          in the database

        Returns
        -------
        - Mean: PCE mean
        - Var: PCE variance
        - S_u: PCE Sobol indices, either the first order indices or all indices
        """
        
        if 'samples' in kwargs:
            samples = kwargs['samples']
            N_qoi = samples[0].size
        else:
            samples = self.samples[qoi]
            N_qoi = self.N_qoi

        #compute the PCE coefficients
        self.SC2PCE(samples)

        #Compute the PCE mean (not really required)
        k1 = tuple(np.ones(self.N, dtype=int))
        mean = 0.0
        for l in self.l_norm:
            mean = mean + self.comb_coef[tuple(l)] * self.pce_coefs[tuple(l)][k1]

        #dict to hold the variance per multi index k
        var = {}
        #D = total PCE variance
        D = 0.0
        for k in self.l_norm[1:]:
            var_k = 0.0
            for l in self.l_norm[1:]:
                if tuple(k) in self.pce_coefs[tuple(l)].keys():
                    eta_k = self.pce_coefs[tuple(l)][tuple(k)]
                    var_k = var_k + self.comb_coef[tuple(l)] * eta_k
            var[tuple(k)] = var_k**2
            D = D + var[tuple(k)]

        print('Computing Sobol indices...')
        # Universe = (0, 1, ..., N - 1)
        U = np.arange(self.N)

        #the powerset of U for either the first order or all Sobol indices
        if typ == 'first_order':
            P = [()]
            for i in range(self.N):
                P.append((i,))
        else:
            # all indices u
            P = list(powerset(U))

        #dict to hold the partial Sobol variances and Sobol indices
        D_u = {}; S_u = {}
        for u in P[1:]:
            # complement of u
            u_prime = np.delete(U, u)
            k = []
            D_u[u] = np.zeros(N_qoi)
            S_u[u] = np.zeros(N_qoi)

            #compute the set of multi indices corresponding to varying ONLY
            #the inputs indexed by u
            for l in self.l_norm:
                #assume l_i = 1 for all i in u' until found otherwise
                all_ones = True
                for i_up in u_prime:
                    if l[i_up] != 1:
                        all_ones = False
                        break
                #if l_i = 1 for all i in u'
                if all_ones:
                    #assume all l_i for i in u are > 1
                    all_gt_one = True
                    for i_u in u:
                        if l[i_u] == 1:
                            all_gt_one = False
                            break
                    #if both conditions above are True, the current l varies
                    #only inputs indexed by u, add this l to k
                    if all_gt_one:
                        k.append(l)

            print('Multi indices of dimension u =', u, 'are', k)
            #the partial variance of u is the sum of all variances index by k
            for k_u in k:
                D_u[u] = D_u[u] + var[tuple(k_u)]

            #normalize D_u by total variance D to get the Sobol index
            S_u[u] = D_u[u] / D

        print('done')
        return mean, D, D_u, S_u

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

                #Below: old implementation using compute_Q_diff subroutine
                # # expand the multi-index indices of the tensor product
                # # (Q^1_{i1} - Q^1_{i1-1}) X ... X (Q^1_{id) - Q^1_{id-1})
                # diff_idx = np.array(list(product(*[[k, -(k - 1)] for k in l])))

                # # perform analysis on each Q^1_l1 X ... X Q^1_l_N tensor prod
                # for diff in diff_idx:

                #     # if any Q^1_li is below the minimim level, Q^1_li is defined
                #     # as zero: do not compute this Q^1_l1 X ... X Q^1_l_N tensor prod
                #     if not (np.abs(diff) < self.l_norm_min).any():

                #         # mariginal integral h, integrate over dimensions u'
                #         h, wi_d_u = self.compute_marginal(qoi, u, u_prime, diff)

                #         # square result and integrate over remaining dimensions u
                #         for i_u in range(wi_d_u.shape[0]):
                #             D_u[u] += np.sign(np.prod(diff)) * h[i_u]**2 * wi_d_u[i_u].prod()

                # #D_u[u] = D_u[u].flatten()

                #New implementation using combination coefficients
                # mariginal integral h, integrate over dimensions u'
                h, wi_d_u = self.compute_marginal(qoi, u, u_prime, l)
                # square result and integrate over remaining dimensions u
                for i_u in range(wi_d_u.shape[0]):      
                    D_u[u] += h[i_u]**2 * wi_d_u[i_u].prod()
                D_u[u] *= self.comb_coef[tuple(l)]**3

            # all subsets of u
            W = list(powerset(u))[0:-1]

            # partial variance of u
            for w in W:
                D_u[u] = D_u[u] - D_u[w]

            # compute Sobol index, only include points where D > 0
            # sobol[u] = D_u[u][idx_gt0]/D[idx_gt0]
            sobol[u] = D_u[u] / D
        print('done.')
        return sobol, D_u

    def get_confidence_intervals(self, qoi, n_samples, conf=0.9, **kwargs):
        """
        Compute the confidence intervals based upon samples of the SC surrogate.
        Uses a non-parametric approach based upon the empirical cumulative
        distribution function.

        Parameters:
        -----------
        - qoi (str): name of the Quantity of Interest for which to compute the intervals
        - n_samples (int): number of surrogate samples to be used in the computation
          conf (float in [0, 1]): the confidence interval magnitude
        - kwargs: can contain 'surr_samples' key if you want to use precomputed
          surrogate samples. Should be an array of dimension [n_samples, N_qoi],
          where N_qoi is the size of the quantity of interest

        Returns:
        --------
        lower, upper (array of floats): the lower and upper bound of the interval
        """

        #ake sure conf is in [0, 1]
        if conf < 0.0 or conf > 1.0:
            print('conf must be specified within [0, 1]')
            return
        #lower bound = alpha, upper bound = 1 - alpha 
        alpha = 0.5*(1.0 - conf)

        #use precomputed surrogate samples or not
        if 'surr_samples' in kwargs:
            surr_samples = kwargs['surr_samples']
        else:
            #draw n_samples draws from the input distributions
            xi_mc = np.zeros([n_samples, self.N])
            idx = 0
            for dist in self.sampler.vary.get_values():
                xi_mc[:, idx] = dist.sample(n_samples)
                idx += 1

            #sample the surrogate n_samples times
            surr_samples = np.zeros([n_samples, self.N_qoi])
            print('Sampling surrogate %d times to compute %.2f % confidence interval' % (n_samples, conf*100))
            for i in range(n_samples):
                surr_samples[i, :] = self.surrogate(qoi, xi_mc[i])
                if np.mod(i, 10) == 0:
                    print('%d of %d' % (i + 1, n_samples))
            print('done')

        #arrays for lower and upper bound of the interval
        lower = np.zeros(self.N_qoi)
        upper = np.zeros(self.N_qoi)

        #the probabilities of the ecdf
        prob = np.linspace(0, 1, n_samples)
        #the closest locations in prob that correspond to the interval bounds
        idx0 = np.where(prob <= alpha)[0][-1]
        idx1 = np.where(prob <= 1.0 - alpha)[0][-1]

        #for every location of qoi compute the ecdf-based confidence interval
        for i in range(self.N_qoi):
            #the sorted surrogate samples at the current location
            samples_sorted = np.sort(surr_samples[:, i])
            #the corresponding confidence interval
            lower[i] = samples_sorted[idx0]
            upper[i] = samples_sorted[idx1]

        return lower, upper

    def get_uncertainty_blowup(self, qoi):
        """
        Computes a measure that signifies the ratio of output to input 
        uncertainty. It is computed as the (mean) Coefficient of Variation (V)
        of the output divided by the (mean) CV of the input.

        Parameters
        ----------
        qoi (string): name of the Quantity of Interest 

        Returns
        -------
        blowup (float): the ratio output CV / input CV

        """

        mean_f, var_f = self.get_moments(qoi)
        std_f = np.sqrt(var_f)

        mean_xi = []; std_xi = []; CV_xi = []
        for param in self.sampler.params_distribution:
            E = cp.E(param); Std = cp.Std(param)
            mean_xi.append(E)
            std_xi.append(Std)
            CV_xi.append(Std/E)

        CV_in = np.mean(CV_xi)
        CV_out = std_f/mean_f
        idx = np.where(np.isnan(CV_out) == False)[0]
        CV_out = np.mean(CV_out[idx])
        blowup = CV_out / CV_in

        print('-----------------')
        print('Mean CV input = %.4f %%' % (100*CV_in, ))
        print('Mean CV output = %.4f %%' % (100*CV_out, ))
        print('Uncertainty blowup factor = %.4f/%.4f = %.4f %%' % (100*CV_out, 100*CV_in, 100*blowup))
        print('-----------------')

        return blowup


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
    #implementation below is more beautiful, but slower
    # x_i_ = np.delete(x_i, j)
    # return np.prod((x - x_i_) / (x_i[j] - x_i_))


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
