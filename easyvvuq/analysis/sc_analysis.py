"""
ANALYSIS CLASS FOR THE SC SAMPLER
"""

import numpy as np
import chaospy as cp
from itertools import product, chain, combinations
import pickle
import copy
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from .results import AnalysisResults
import logging
# from scipy.special import comb
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
    def _get_sobols_first(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_first'])
        result = raw_dict[AnalysisResults._to_tuple(qoi)][input_]
        try:
            return np.array([float(result)])
        except TypeError:
            return np.array(result)

    def supported_stats(self):
        """Types of statistics supported by the describe method.

        Returns
        -------
        list of str
        """
        return ['mean', 'var', 'std']

    def _describe(self, qoi, statistic):
        if statistic in self.supported_stats():
            return self.raw_data['statistical_moments'][qoi][statistic]
        else:
            raise NotImplementedError

    def surrogate(self):
        """Return an SC surrogate model.

        Returns
        -------
        A function that takes a dictionary of parameter - value pairs and returns
        a dictionary with the results (same output as decoder).
        """
        def surrogate_fn(inputs):
            def swap(x):
                if len(x) > 1:
                    return list(x)
                else:
                    return x[0]
            values = np.squeeze(np.array([inputs[key] for key in self.inputs])).T
            results = dict([(qoi, swap(self.surrogate_(qoi, values))) for qoi in self.qois])
            return results
        return surrogate_fn


class SCAnalysis(BaseAnalysisElement):

    def __init__(self, sampler=None, qoi_cols=None):
        """
        Parameters
        ----------
        sampler : SCSampler
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
        self.pce_coefs = {}
        self.N_qoi = {}
        for qoi_k in qoi_cols:
            self.pce_coefs[qoi_k] = {}
            self.N_qoi[qoi_k] = 0

    def element_name(self):
        """Name for this element for logging purposes"""
        return "SC_Analysis"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.5"

    def save_state(self, filename):
        """Saves the complete state of the analysis object to a pickle file,
        except the sampler object (self.samples).

        Parameters
        ----------
        filename : string
            name to the file to write the state to
        """
        logging.debug("Saving analysis state to %s" % filename)
        # make a copy of the state, and do not store the sampler as well
        state = copy.copy(self.__dict__)
        del state['sampler']
        file = open(filename, 'wb')
        pickle.dump(state, file)
        file.close()

    def load_state(self, filename):
        """Loads the complete state of the analysis object from a
        pickle file, stored using save_state.

        Parameters
        ----------
        filename : string
            name of the file to load
        """
        logging.debug("Loading analysis state from %s" % filename)
        file = open(filename, 'rb')
        state = pickle.load(file)
        for key in state.keys():
            self.__dict__[key] = state[key]
        file.close()

    def analyse(self, data_frame=None, compute_moments=True, compute_Sobols=True):
        """Perform SC analysis on input `data_frame`.

        Parameters
        ----------
        data_frame : pandas.DataFrame
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
        elif isinstance(data_frame, pd.DataFrame) and data_frame.empty:
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
            # If dimension_adaptive and nadaptations > 0: l_norm
            # is computed in self.adaptation_metric
            if not self.dimension_adaptive or self.sampler.nadaptations == 0:
                # the maximum level (quad order) of the (sparse) grid
                self.l_norm = self.sampler.compute_sparse_multi_idx(self.L, self.N)

            self.l_norm_min = np.ones(self.N, dtype=int)

        # #compute generalized combination coefficients
        self.comb_coef = self.compute_comb_coef()

        # 1d weights and points per level
        self.xi_1d = self.sampler.xi_1d
        # self.wi_1d = self.compute_SC_weights(rule=self.sampler.quad_rule)
        self.wi_1d = self.sampler.wi_1d

        # Extract output values for each quantity of interest from Dataframe
        logging.debug('Loading samples...')
        qoi_cols = self.qoi_cols
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame[('run_id', 0)].unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame[('run_id', 0)] == run_id][k].values
                samples[k].append(values.flatten())
        self.samples = samples
        logging.debug('done')

        # assume that self.l_norm has changed, and that the interpolation
        # must be initialised, see sc_expansion subroutine
        self.init_interpolation = True

        # same pce coefs must be computed for every qoi
        if self.sparse:
            for qoi_k in qoi_cols:
                self.pce_coefs[qoi_k] = self.SC2PCE(samples[qoi_k], qoi_k)
                # size of one code sample
                self.N_qoi[qoi_k] = self.samples[qoi_k][0].size

        # Compute descriptive statistics for each quantity of interest
        results = {'statistical_moments': {},
                   'sobols_first': {k: {} for k in self.qoi_cols},
                   'sobols': {k: {} for k in self.qoi_cols}}

        if compute_moments:
            for qoi_k in qoi_cols:
                if not self.sparse:
                    mean_k, var_k = self.get_moments(qoi_k)
                    std_k = np.sqrt(var_k)
                else:
                    self.pce_coefs[qoi_k] = self.SC2PCE(self.samples[qoi_k], qoi_k)
                    mean_k, var_k, _ = self.get_pce_stats(self.l_norm, self.pce_coefs[qoi_k],
                                                          self.comb_coef)
                    std_k = np.sqrt(var_k)

                # compute statistical moments
                results['statistical_moments'][qoi_k] = {'mean': mean_k,
                                                         'var': var_k,
                                                         'std': std_k}

        if compute_Sobols:
            for qoi_k in qoi_cols:
                if not self.sparse:
                    results['sobols'][qoi_k] = self.get_sobol_indices(qoi_k, 'first_order')
                else:
                    _, _, _, results['sobols'][qoi_k] = self.get_pce_sobol_indices(
                        qoi_k, 'first_order')

                for idx, param_name in enumerate(self.sampler.vary.get_keys()):
                    results['sobols_first'][qoi_k][param_name] = \
                        results['sobols'][qoi_k][(idx,)]

        results = SCAnalysisResults(raw_data=results, samples=data_frame,
                                    qois=qoi_cols, inputs=list(self.sampler.vary.get_keys()))
        results.surrogate_ = self.surrogate
        return results

    def compute_comb_coef(self, **kwargs):
        """Compute general combination coefficients. These are the coefficients
        multiplying the tensor products associated to each multi index l,
        see page 12 Gerstner & Griebel, numerical integration using sparse grids
        """

        if 'l_norm' in kwargs:
            l_norm = kwargs['l_norm']
        else:
            l_norm = self.l_norm

        comb_coef = {}
        logging.debug('Computing combination coefficients...')
        for k in l_norm:
            coef = 0.0
            # for every k, subtract all multi indices
            for l in l_norm:
                z = l - k
                # if the results contains only 0's and 1's, then z is the
                # vector that can be formed from a tensor product of unit vectors
                # for which k+z is in self.l_norm
                if np.array_equal(z, z.astype(bool)):
                    coef += (-1)**(np.sum(z))
            comb_coef[tuple(k)] = coef
        logging.debug('done')
        return comb_coef

    def adapt_dimension(self, qoi, data_frame, store_stats_history=True,
                        method='surplus', **kwargs):
        """Compute the adaptation metric and decide which of the admissible
        level indices to include in next iteration of the sparse grid. The
        adaptation metric is based on the hierarchical surplus, defined as the
        difference between the new code values of the admissible level indices,
        and the SC surrogate of the previous iteration. Alternatively, it can be
        based on the difference between the output mean of the current level,
        and the mean computed with one extra admissible index.

        This subroutine must be called AFTER the code is evaluated at
        the new points, but BEFORE the analysis is performed.

        Parameters
        ----------
        qoi : string
            the name of the quantity of interest which is used
            to base the adaptation metric on.
        data_frame : pandas.DataFrame
        store_stats_history : bool
            store the mean and variance at each refinement in self.mean_history
            and self.std_history. Used for checking convergence in the statistics
            over the refinement iterations
        method : string
            name of the refinement error, default is 'surplus'. In this case the
            error is based on the hierarchical surplus, which is an interpolation
            based error. Another possibility is 'var',
            in which case the error is based on the difference in the
            variance between the current estimate and the estimate obtained
            when a particular candidate direction is added.
        """
        logging.debug('Refining sampling plan...')
        # load the code samples
        samples = []
        if isinstance(data_frame, pd.DataFrame):
            for run_id in data_frame[('run_id', 0)].unique():
                values = data_frame.loc[data_frame[('run_id', 0)] == run_id][qoi].values
                samples.append(values.flatten())

        if method == 'var':
            all_idx = np.concatenate((self.l_norm, self.sampler.admissible_idx))
            self.xi_1d = self.sampler.xi_1d
            self.wi_1d = self.sampler.wi_1d
            self.pce_coefs[qoi] = self.SC2PCE(samples, qoi, verbose=True, l_norm=all_idx,
                                              xi_d=self.sampler.xi_d)
            _, var_l, _ = self.get_pce_stats(self.l_norm, self.pce_coefs[qoi], self.comb_coef)

        # the currently accepted grid points
        xi_d_accepted = self.sampler.generate_grid(self.l_norm)

        # compute the hierarchical surplus based error for every admissible l
        error = {}
        for l in self.sampler.admissible_idx:
            error[tuple(l)] = []
            # compute the error based on the hierarchical surplus (interpolation based)
            if method == 'surplus':
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
                    if 'index' in kwargs:
                        hier_surplus = hier_surplus[kwargs['index']]
                        error[tuple(l)].append(np.abs(hier_surplus))
                    else:
                        error[tuple(l)].append(np.linalg.norm(hier_surplus, np.inf))
                # compute mean error over all points in X_l
                error[tuple(l)] = np.mean(error[tuple(l)])
            # compute the error based on quadrature of the variance
            elif method == 'var':
                # create a candidate set of multi indices by adding the current
                # admissible index to l_norm
                candidate_l_norm = np.concatenate((self.l_norm, l.reshape([1, self.N])))
                # now we must recompute the combination coefficients
                c_l = self.compute_comb_coef(l_norm=candidate_l_norm)
                _, var_candidate_l, _ = self.get_pce_stats(
                    candidate_l_norm, self.pce_coefs[qoi], c_l)
                # error in var
                error[tuple(l)] = np.linalg.norm(var_candidate_l - var_l, np.inf)
            else:
                logging.debug('Specified refinement method %s not recognized' % method)
                logging.debug('Accepted are surplus, mean or var')
                import sys
                sys.exit()

        for key in error.keys():
            # logging.debug("Surplus error when l = %s is %s" % (key, error[key]))
            logging.debug("Refinement error for l = %s is %s" % (key, error[key]))
        # find the admissble index with the largest error
        l_star = np.array(max(error, key=error.get)).reshape([1, self.N])
        # logging.debug('Selecting %s for refinement.' % l_star)
        logging.debug('Selecting %s for refinement.' % l_star)
        # add max error to list
        self.adaptation_errors.append(max(error.values()))

        # add l_star to the current accepted level indices
        self.l_norm = np.concatenate((self.l_norm, l_star))
        # if someone executes this function twice for some reason,
        # remove the duplicate l_star entry. Keep order unaltered
        idx = np.unique(self.l_norm, axis=0, return_index=True)[1]
        self.l_norm = np.array([self.l_norm[i] for i in sorted(idx)])

        # peform the analyse step, but do not compute moments and Sobols
        self.analyse(data_frame, compute_moments=False, compute_Sobols=False)

        # if True store the mean and variance at eacht iteration of the adaptive
        # algorithmn
        if store_stats_history:
            # mean_f, var_f = self.get_moments(qoi)
            logging.debug('Storing moments of iteration %d' % self.sampler.nadaptations)
            pce_coefs = self.SC2PCE(samples, qoi, verbose=True)
            mean_f, var_f, _ = self.get_pce_stats(self.l_norm, pce_coefs, self.comb_coef)
            self.mean_history.append(mean_f)
            self.std_history.append(var_f)
            logging.debug('done')

    def merge_accepted_and_admissible(self, level=0, **kwargs):
        """In the case of the dimension-adaptive sampler, there are 2 sets of
        quadrature multi indices. There are the accepted indices that are actually
        used in the analysis, and the admissible indices, of which some might
        move to the accepted set in subsequent iterations. This subroutine merges
        the two sets of multi indices by moving all admissible to the set of
        accepted indices.
        Do this at the end, when no more refinements will be executed. The
        samples related to the admissble indices are already computed, although
        not used in the analysis. By executing this subroutine at very end, all
        computed samples are used during the final postprocessing stage. Execute
        campaign.apply_analysis to let the new set of indices take effect.
        If further refinements are executed after all via sampler.look_ahead, the
        number of new admissible samples to be computed can be very high,
        especially in high dimensions. It is possible to undo the merge via
        analysis.undo_merge before new refinements are made. Execute
        campaign.apply_analysis again to let the old set of indices take effect.
        """

        if 'include' in kwargs:
            include = kwargs['include']
        else:
            include = np.arange(self.N)

        if self.sampler.dimension_adaptive:
            logging.debug('Moving admissible indices to the accepted set...')
            # make a backup of l_norm, such that undo_merge can revert back
            self.l_norm_backup = np.copy(self.l_norm)
            # merge admissible and accepted multi indices
            if level == 0:
                merged_l = np.concatenate((self.l_norm, self.sampler.admissible_idx))
            else:
                admissible_idx = []
                count = 0
                for l in self.sampler.admissible_idx:
                    L = np.sum(l) - self.N + 1
                    tmp = np.where(l == L)[0]
                    if L <= level and np.in1d(tmp, include)[0]:
                        admissible_idx.append(l)
                        count += 1
                admissible_idx = np.array(admissible_idx).reshape([count, self.N])
                merged_l = np.concatenate((self.l_norm, admissible_idx))
            # make sure final result contains only unique indices and store
            # results in l_norm
            idx = np.unique(merged_l, axis=0, return_index=True)[1]
            # return np.array([merged_l[i] for i in sorted(idx)])
            self.l_norm = np.array([merged_l[i] for i in sorted(idx)])
            logging.debug('done')

    def undo_merge(self):
        """This reverses the effect of the merge_accepted_and_admissble subroutine.
        Execute if further refinement are required after all.
        """
        if self.sampler.dimension_adaptive:
            self.l_norm = self.l_norm_backup
            logging.debug('Restored old multi indices.')

    def get_adaptation_errors(self):
        """Returns self.adaptation_errors
        """
        return self.adaptation_errors

    def plot_stat_convergence(self):
        """Plots the convergence of the statistical mean and std dev over the different
        refinements in a dimension-adaptive setting. Specifically the inf norm
        of the difference between the stats of iteration i and iteration i-1
        is plotted.
        """
        if not self.dimension_adaptive:
            logging.debug('Only works for the dimension adaptive sampler.')
            return

        K = len(self.mean_history)
        if K < 2:
            logging.debug('Means from at least two refinements are required')
            return
        else:
            differ_mean = np.zeros(K - 1)
            differ_std = np.zeros(K - 1)
            for i in range(1, K):
                differ_mean[i - 1] = np.linalg.norm(self.mean_history[i] -
                                                    self.mean_history[i - 1], np.inf)
                # make relative
                differ_mean[i - 1] = differ_mean[i - 1] / np.linalg.norm(self.mean_history[i - 1],
                                                                         np.inf)

                differ_std[i - 1] = np.linalg.norm(self.std_history[i] -
                                                   self.std_history[i - 1], np.inf)
                # make relative
                differ_std[i - 1] = differ_std[i - 1] / np.linalg.norm(self.std_history[i - 1],
                                                                       np.inf)

        import matplotlib.pyplot as plt
        fig = plt.figure('stat_conv')
        ax1 = fig.add_subplot(111, title='moment convergence')
        ax1.set_xlabel('iteration', fontsize=12)
        # ax1.set_ylabel(r'$ ||\mathrm{mean}_i - \mathrm{mean}_{i - 1}||_\infty$',
        # color='r', fontsize=12)
        ax1.set_ylabel(r'relative error mean', color='r', fontsize=12)
        ax1.plot(range(2, K + 1), differ_mean, color='r', marker='+')
        ax1.tick_params(axis='y', labelcolor='r')

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        # ax2.set_ylabel(r'$ ||\mathrm{var}_i - \mathrm{var}_{i - 1}||_\infty$',
        # color='b', fontsize=12)
        ax2.set_ylabel(r'relative error variance', fontsize=12, color='b')
        ax2.plot(range(2, K + 1), differ_std, color='b', marker='*')
        ax2.tick_params(axis='y', labelcolor='b')

        plt.tight_layout()
        plt.show()

    def surrogate(self, qoi, x, L=None):
        """Use sc_expansion UQP as a surrogate

        Parameters
        ----------
        qoi : str
            name of the qoi
        x : array
            location at which to evaluate the surrogate
        L : int
            level of the (sparse) grid, default = self.L

        Returns
        -------
        the interpolated value of qoi at x (float, (N_qoi,))
        """

        return self.sc_expansion(self.samples[qoi], x=x)

    def quadrature(self, qoi, samples=None):
        """Computes a (Smolyak) quadrature

        Parameters
        ----------
        qoi : str
            name of the qoi

        samples: array
            compute the mean by setting samples = self.samples.
            To compute the variance, set samples = (self.samples - mean)**2

        Returns
        -------
        the quadrature of qoi
        """
        if samples is None:
            samples = self.samples[qoi]

        return self.combination_technique(qoi, samples)

    def combination_technique(self, qoi, samples=None, **kwargs):
        """Efficient quadrature formulation for (sparse) grids. See:

            Gerstner, Griebel, "Numerical integration using sparse grids"
            Uses the general combination technique (page 12).

        Parameters
        ----------
        qoi : str
            name of the qoi

        samples : array
            compute the mean by setting samples = self.samples.
            To compute the variance, set samples = (self.samples - mean)**2
        """

        if samples is None:
            samples = self.samples[qoi]

        # In the case of quadrature-based refinement, we need to specify
        # l_norm, comb_coef and xi_d other than the current defualt values
        if 'l_norm' in kwargs:
            l_norm = kwargs['l_norm']
        else:
            l_norm = self.l_norm

        if 'comb_coef' in kwargs:
            comb_coef = kwargs['comb_coef']
        else:
            comb_coef = self.comb_coef

        if 'xi_d' in kwargs:
            xi_d = kwargs['xi_d']
        else:
            xi_d = self.xi_d

        # quadrature Q
        Q = 0.0

        # loop over l
        for l in l_norm:
            # compute the tensor product of parameter and weight values
            X_k = [self.xi_1d[n][l[n]] for n in range(self.N)]
            W_k = [self.wi_1d[n][l[n]] for n in range(self.N)]

            X_k = np.array(list(product(*X_k)))
            W_k = np.array(list(product(*W_k)))
            W_k = np.prod(W_k, axis=1)
            W_k = W_k.reshape([W_k.shape[0], 1])

            # scaling factor of combination technique
            W_k = W_k * comb_coef[tuple(l)]

            # find corresponding code values
            f_k = np.array([samples[np.where((x == xi_d).all(axis=1))[0][0]] for x in X_k])

            # quadrature of Q^1_{k1} X ... X Q^1_{kN} product
            Q = Q + np.sum(f_k * W_k, axis=0).T

        return Q

    def get_moments(self, qoi):
        """
        Parameters
        ----------
        qoi : str
            name of the qoi

        Returns
        -------
        mean and variance of qoi (float (N_qoi,))
        """
        logging.debug('Computing moments...')
        # compute mean
        mean_f = self.quadrature(qoi)
        # compute variance
        variance_samples = [(sample - mean_f)**2 for sample in self.samples[qoi]]
        var_f = self.quadrature(qoi, samples=variance_samples)
        logging.debug('done')
        return mean_f, var_f

    def sc_expansion(self, samples, x):
        """
        Non recursive implementation of the SC expansion. Performs interpolation
        of code output samples for both full and sparse grids.

        Parameters
        ----------
        samples : list
            list of code output samples.
        x : array
            One or more locations in stochastic space at which to evaluate
            the surrogate.

        Returns
        -------
        surr : array
            The interpolated values of the code output at input locations
            specified by x.

        """
        # Computing the tensor grid of each multiindex l (xi_d below)
        # every time is slow. Instead store it globally, and only recompute when
        # self.l_norm has changed, when the flag init_interpolation = True.
        # This flag is set to True when self.analyse is executed
        if self.init_interpolation:
            self.xi_d_per_l = {}
            for l in self.l_norm:
                # all points corresponding to l
                xi = [self.xi_1d[n][l[n]] for n in range(self.N)]
                self.xi_d_per_l[tuple(l)] = np.array(list(product(*xi)))
            self.init_interpolation = False

        surr = 0.0
        for l in self.l_norm:
            # all points corresponding to l
            # xi = [self.xi_1d[n][l[n]] for n in range(self.N)]
            # xi_d = np.array(list(product(*xi)))
            xi_d = self.xi_d_per_l[tuple(l)]

            for xi in xi_d:
                # indices of current collocation point
                # in corresponding 1d colloc points (self.xi_1d[n][l[n]])
                # These are the j of the 1D lagrange polynomials l_j(x), see
                # lagrange_poly subroutine
                idx = [(self.xi_1d[n][l[n]] == xi[n]).nonzero()[0][0] for n in range(self.N)]
                # index of the code sample
                sample_idx = np.where((xi == self.xi_d).all(axis=1))[0][0]

                # values of Lagrange polynomials at x
                if x.ndim == 1:
                    weight = [lagrange_poly(x[n], self.xi_1d[n][l[n]], idx[n])
                              for n in range(self.N)]
                    surr += self.comb_coef[tuple(l)] * samples[sample_idx] * np.prod(weight, axis=0)
                # batch setting, if multiple x values are presribed
                else:
                    weight = [lagrange_poly(x[:, n], self.xi_1d[n][l[n]], idx[n])
                              for n in range(self.N)]
                    surr += self.comb_coef[tuple(l)] * samples[sample_idx] * \
                        np.prod(weight, axis=0).reshape([-1, 1])

        return surr

    def get_sample_array(self, qoi):
        """
        Parameters
        ----------
        qoi : str
            name of quantity of interest

        Returns
        -------
        array of all samples of qoi
        """
        return np.array([self.samples[qoi][k] for k in range(len(self.samples[qoi]))])

    def adaptation_histogram(self):
        """Plots a bar chart of the maximum order of the quadrature rule
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
                             % self.sampler.nadaptations)
        # find max quad order for every parameter
        adapt_measure = np.max(self.l_norm, axis=0)
        ax.bar(range(adapt_measure.size), height=adapt_measure - 1)
        params = list(self.sampler.vary.get_keys())
        ax.set_xticks(range(adapt_measure.size))
        ax.set_xticklabels(params)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    def adaptation_table(self, **kwargs):
        """Plots a color-coded table of the quadrature-order refinement.
        Shows in what order the parameters were refined, and unlike
        adaptation_histogram, this also shows higher-order refinements.

        Parameters
        ----------
        **kwargs: can contain kwarg 'order' to specify the order in which
        the variables on the x axis are plotted (e.g. in order of decreasing
        1st order Sobol index).

        Returns
        -------
        None.

        """

        # if specified, plot the variables on the x axis in a given order
        if 'order' in kwargs:
            order = kwargs['order']
        else:
            order = range(self.N)

        l = np.copy(self.l_norm)[:, order]
        import matplotlib as mpl
        import matplotlib.pyplot as plt

        fig = plt.figure(figsize=[12, 6])
        ax = fig.add_subplot(111)

        # max quad order
        M = np.max(l)
        cmap = plt.get_cmap('Purples', M)
        # plot 'heat map' of refinement
        plt.imshow(l.T, cmap=cmap, aspect='auto')
        norm = mpl.colors.Normalize(vmin=0, vmax=M - 1)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        cb = plt.colorbar(sm)
        # plot the quad order in the middle of the colorbar intervals
        p = np.linspace(0, M - 1, M + 1)
        tick_p = 0.5 * (p[1:] + p[0:-1])
        cb.set_ticks(tick_p)
        cb.set_ticklabels(np.arange(M))
        cb.set_label(r'quadrature order')
        # plot the variables names on the x axis
        ax.set_yticks(range(l.shape[1]))
        params = np.array(list(self.sampler.vary.get_keys()))
        ax.set_yticklabels(params[order], fontsize=12)
        # ax.set_yticks(range(l.shape[0]))
        ax.set_xlabel('iteration')
        # plt.yticks(rotation=90)
        plt.tight_layout()
        plt.show()

    def plot_grid(self):
        """Plots the collocation points for 2 and 3 dimensional problems
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
            logging.debug('Will only plot for N = 2 or N = 3.')

    def SC2PCE(self, samples, qoi, verbose=True, **kwargs):
        """Computes the Polynomials Chaos Expansion coefficients from the SC
        expansion via a transformation of basis (Lagrange polynomials basis -->
        orthonomial basis).

        Parameters
        ----------
        samples : array
            SC code samples from which to compute the PCE coefficients

        qoi : string
            Name of the QoI.

        Returns
        -------
        pce_coefs : dict
            PCE coefficients per multi index l
        """
        pce_coefs = {}

        if 'l_norm' in kwargs:
            l_norm = kwargs['l_norm']
        else:
            l_norm = self.l_norm

        if 'xi_d' in kwargs:
            xi_d = kwargs['xi_d']
        else:
            xi_d = self.xi_d

        # if not hasattr(self, 'pce_coefs'):
        #     self.pce_coefs = {}

        count_l = 1
        for l in l_norm:
            if not tuple(l) in self.pce_coefs[qoi].keys():
                # pce coefficients for current multi-index l
                pce_coefs[tuple(l)] = {}

                # 1d points generated by l
                x_1d = [self.xi_1d[n][l[n]] for n in range(self.N)]
                # 1d Lagrange polynomials generated by l
                # EDIT: do not use chaospy for Lagrange, converts lagrange into monomial, requires
                # Vandermonde matrix inversion to find coefficients, which becomes
                # very ill conditioned rather quickly. Can no longer use cp.E to compute
                # integrals, use GQ instead
                # a_1d = [cp.lagrange_polynomial(sampler.xi_1d[n][l[n]]) for n in range(d)]

                # N-dimensional grid generated by l
                x_l = np.array(list(product(*x_1d)))

                # all multi indices of the PCE expansion: k <= l
                k_norm = list(product(*[np.arange(1, l[n] + 1) for n in range(self.N)]))

                if verbose:
                    logging.debug('Computing PCE coefficients %d / %d' % (count_l, l_norm.shape[0]))

                for k in k_norm:
                    # product of the PCE basis function or order k - 1 and all
                    # Lagrange basis functions in a_1d, per dimension
                    # [[phi_k[0]*a_1d[0]], ..., [phi_k[N-1]*a_1d[N-1]]]

                    # orthogonal polynomial generated by chaospy
                    phi_k = [cp.expansion.stieltjes(k[n] - 1,
                                                    dist=self.sampler.params_distribution[n],
                                                    normed=True)[-1] for n in range(self.N)]

                    # the polynomial order of each integrand phi_k*a_j = (k - 1) + (number of
                    # colloc. points - 1)
                    orders = [(k[n] - 1) + (self.xi_1d[n][l[n]].size - 1) for n in range(self.N)]

                    # will hold the products of PCE basis functions phi_k and lagrange
                    # interpolation polynomials a_1d
                    cross_prod = []

                    for n in range(self.N):
                        # GQ using n points can exactly integrate polynomials of order 2n-1:
                        # solve for required number of points n when given order
                        n_quad_points = int(np.ceil((orders[n] + 1) / 2))

                        # generate Gaussian quad rule
                        if isinstance(self.sampler.params_distribution[n], cp.DiscreteUniform):
                            xi = self.xi_1d[n][l[n]]
                            wi = self.wi_1d[n][l[n]]
                        else:
                            xi, wi = cp.generate_quadrature(
                                n_quad_points - 1, self.sampler.params_distribution[n], rule="G")
                            xi = xi[0]

                        # number of colloc points = number of Lagrange polynomials
                        n_lagrange_poly = int(self.xi_1d[n][l[n]].size)

                        # compute the v coefficients = coefficients of SC2PCE mapping
                        v_coefs_n = []
                        for j in range(n_lagrange_poly):
                            # compute values of Lagrange polys at quadrature points
                            l_j = np.array([lagrange_poly(xi[i], self.xi_1d[n][l[n]], j)
                                            for i in range(xi.size)])
                            # each coef is the integral of the lagrange poly times the current
                            # orthogonal PCE poly
                            v_coefs_n.append(np.sum(l_j * phi_k[n](xi) * wi))
                        cross_prod.append(v_coefs_n)

                    # tensor product of all integrals
                    integrals = np.array(list(product(*cross_prod)))
                    # multiply over the number of parameters: v_prod = v_k1_j1 * ... * v_kd_jd
                    v_prod = np.prod(integrals, axis=1)
                    v_prod = v_prod.reshape([v_prod.size, 1])

                    # find corresponding code values
                    f_k = np.array([samples[np.where((x == xi_d).all(axis=1))[0][0]] for x in x_l])

                    # the sum of all code sample * v_{k,j_1} * ... * v_{k,j_N}
                    # equals the PCE coefficient
                    eta_k = np.sum(f_k * v_prod, axis=0).T

                    pce_coefs[tuple(l)][tuple(k)] = eta_k
            else:
                # pce coefs previously computed, just copy result
                pce_coefs[tuple(l)] = self.pce_coefs[qoi][tuple(l)]
            count_l += 1

        logging.debug('done')
        return pce_coefs

    def generalized_pce_coefs(self, l_norm, pce_coefs, comb_coef):
        """
        Computes the generalized PCE coefficients, defined as the linear combibation
        of PCE coefficients which make it possible to write the dimension-adaptive
        PCE expansion in standard form. See DOI: 10.13140/RG.2.2.18085.58083/1

        Parameters
        ----------
        l_norm : array
            array of quadrature order multi indices
        pce_coefs : tuple
            tuple of PCE coefficients computed by SC2PCE subroutine
        comb_coef : tuple
            tuple of combination coefficients computed by compute_comb_coef

        Returns
        -------
        gen_pce_coefs : tuple
            The generalized PCE coefficients, indexed per multi index.

        """
        assert self.sparse, "Generalized PCE coeffcients are computed only for sparse grids"

        # the set of all forward neighbours of l: {k | k >= l}
        F_l = {}
        # the generalized PCE coefs, which turn the adaptive PCE into a standard PCE expansion
        gen_pce_coefs = {}
        for l in l_norm:
            # {indices of k | k >= l}
            idx = np.where((l <= l_norm).all(axis=1))[0]
            F_l[tuple(l)] = l_norm[idx]

            # the generalized PCE coefs are comb_coef[k] * pce_coefs[k][l], summed over k
            # for a fixed l
            gen_pce_coefs[tuple(l)] = 0.0
            for k in F_l[tuple(l)]:
                gen_pce_coefs[tuple(l)] += comb_coef[tuple(k)] * pce_coefs[tuple(k)][tuple(l)]

        return gen_pce_coefs

    def get_pce_stats(self, l_norm, pce_coefs, comb_coef):
        """Compute the mean and the variance based on the generalized PCE coefficients
        See DOI: 10.13140/RG.2.2.18085.58083/1

        Parameters
        ----------
        l_norm : array
            array of quadrature order multi indices
        pce_coefs : tuple
            tuple of PCE coefficients computed by SC2PCE subroutine
        comb_coef : tuple
            tuple of combination coefficients computed by compute_comb_coef

        Returns
        -------
        tuple with mean and variance based on the PCE coefficients
        """

        gen_pce_coefs = self.generalized_pce_coefs(l_norm, pce_coefs, comb_coef)

        # with the generalized pce coefs, the standard PCE formulas for the mean and var
        # can be used for the dimension-adaptive PCE

        # the PCE mean is just the 1st generalized PCE coef
        l1 = tuple(np.ones(self.N, dtype=int))
        mean = gen_pce_coefs[l1]

        # the variance is the sum of the squared generalized PCE coefs, excluding the 1st coef
        D = 0.0
        for l in l_norm[1:]:
            D += gen_pce_coefs[tuple(l)] ** 2

        return mean, D, gen_pce_coefs

    def get_pce_sobol_indices(self, qoi, typ='first_order', **kwargs):
        """Computes Sobol indices using Polynomials Chaos coefficients. These
        coefficients are computed from the SC expansion via a transformation
        of basis (SC2PCE subroutine). This works better than computing the
        Sobol indices directly from the SC expansion in the case of the
        dimension-adaptive sampler. See DOI: 10.13140/RG.2.2.18085.58083/1

        Method: J.D. Jakeman et al, "Adaptive multi-index collocation
        for uncertainty quantification and sensitivity analysis", 2019.
        (Page 18)

        Parameters
        ----------
        qoi : str
            name of the Quantity of Interest for which to compute the indices
        typ : str
            Default = 'first_order'. 'all' is also possible
        **kwargs : dict
            if this contains 'samples', use these instead of the SC samples ]
            in the database

        Returns
        -------
        Tuple
            Mean: PCE mean
            Var: PCE variance
            S_u: PCE Sobol indices, either the first order indices or all indices
        """

        if 'samples' in kwargs:
            samples = kwargs['samples']
            N_qoi = samples[0].size
        else:
            samples = self.samples[qoi]
            N_qoi = self.N_qoi[qoi]

        # compute the (generalized) PCE coefficients and stats
        self.pce_coefs[qoi] = self.SC2PCE(samples, qoi)
        mean, D, gen_pce_coefs = self.get_pce_stats(
            self.l_norm, self.pce_coefs[qoi], self.comb_coef)

        logging.debug('Computing Sobol indices...')
        # Universe = (0, 1, ..., N - 1)
        U = np.arange(self.N)

        # the powerset of U for either the first order or all Sobol indices
        if typ == 'first_order':
            P = [()]
            for i in range(self.N):
                P.append((i,))
        else:
            # all indices u
            P = list(powerset(U))

        # dict to hold the partial Sobol variances and Sobol indices
        D_u = {}
        S_u = {}
        for u in P[1:]:
            # complement of u
            u_prime = np.delete(U, u)
            k = []
            D_u[u] = np.zeros(N_qoi)
            S_u[u] = np.zeros(N_qoi)

            # compute the set of multi indices corresponding to varying ONLY
            # the inputs indexed by u
            for l in self.l_norm:
                # assume l_i = 1 for all i in u' until found otherwise
                all_ones = True
                for i_up in u_prime:
                    if l[i_up] != 1:
                        all_ones = False
                        break
                # if l_i = 1 for all i in u'
                if all_ones:
                    # assume all l_i for i in u are > 1
                    all_gt_one = True
                    for i_u in u:
                        if l[i_u] == 1:
                            all_gt_one = False
                            break
                    # if both conditions above are True, the current l varies
                    # only inputs indexed by u, add this l to k
                    if all_gt_one:
                        k.append(l)

            logging.debug('Multi indices of dimension  %s are %s' % (u, k))
            # the partial variance of u is the sum of all variances index by k
            for k_u in k:
                D_u[u] = D_u[u] + gen_pce_coefs[tuple(k_u)] ** 2

            # normalize D_u by total variance D to get the Sobol index
            S_u[u] = D_u[u] / D

        logging.debug('done')
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
        logging.debug('Computing Sobol indices...')
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

                # D_u[u] = D_u[u].flatten()

            # all subsets of u
            W = list(powerset(u))[0:-1]

            # partial variance of u
            for w in W:
                D_u[u] -= D_u[w]

            # compute Sobol index, only include points where D > 0
            # sobol[u] = D_u[u][idx_gt0]/D[idx_gt0]
            sobol[u] = D_u[u] / D
        logging.debug('done.')
        return sobol

    def get_uncertainty_amplification(self, qoi):
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

        mean_xi = []
        std_xi = []
        CV_xi = []
        for param in self.sampler.params_distribution:
            E = cp.E(param)
            Std = cp.Std(param)
            mean_xi.append(E)
            std_xi.append(Std)
            CV_xi.append(Std / E)

        CV_in = np.mean(CV_xi)
        CV_out = std_f / mean_f
        idx = np.where(np.isnan(CV_out) == False)[0]
        CV_out = np.mean(CV_out[idx])
        blowup = CV_out / CV_in

        print('-----------------')
        print('Mean CV input = %.4f %%' % (100 * CV_in, ))
        print('Mean CV output = %.4f %%' % (100 * CV_out, ))
        print('Uncertainty amplification factor = %.4f/%.4f = %.4f' %
              (CV_out, CV_in, blowup))
        print('-----------------')

        return blowup


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

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
    """Lagrange polynomials used for interpolation

    l_j(x) = product(x - x_m / x_j - x_m) with 0 <= m <= k
                                               and m !=j

    Parameters
    ----------
    x : float
        location at which to compute the polynomial

    x_i : list or array of float
        nodes of the Lagrange polynomials

    j : int
        index of node at which l_j(x_j) = 1

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
    # implementation below is more beautiful, but slower
    # x_i_ = np.delete(x_i, j)
    # return np.prod((x - x_i_) / (x_i[j] - x_i_))


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
