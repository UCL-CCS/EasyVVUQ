"""
ANALYSIS CLASS FOR THE SSC SAMPLER
"""

import numpy as np
import pickle
import copy
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from .results import AnalysisResults
# import logging
# from scipy.special import comb
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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


class SSCAnalysisResults(AnalysisResults):
    # def _get_sobols_first(self, qoi, input_):
    #     raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_first'])
    #     result = raw_dict[AnalysisResults._to_tuple(qoi)][input_]
    #     try:
    #         return np.array([float(result)])
    #     except TypeError:
    #         return np.array(result)

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
        """Return a SSC surrogate model.

        Returns
        -------
        A function that takes a dictionary of parameter - value pairs and returns
        a dictionary with the results (same output as decoder).
        """
        def surrogate_fn(inputs):
            def swap(x):
                if x.size > 1:
                    return list(x)
                else:
                    return x[0]
            values = np.squeeze(np.array([inputs[key] for key in self.inputs])).T
            results = dict([(qoi, swap(self.surrogate_(qoi, values))) for qoi in self.qois])
            return results
        return surrogate_fn


class SSCAnalysis(BaseAnalysisElement):
    """
    SSc analysis class.
    """

    def __init__(self, sampler=None, qoi_cols=None):
        """
        Parameters
        ----------
        sampler : SSCSampler
            Sampler used to initiate the SSC analysis
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        """

        if sampler is None:
            msg = 'SSC analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)

        if qoi_cols is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

    def element_name(self):
        """Name for this element for logging purposes"""
        return "SSC_Analysis"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.1"

    def save_state(self, filename):
        """
        Saves the complete state of the analysis object to a pickle file,
        except the sampler object (self.sampler).

        Parameters
        ----------
        filename : string
            name to the file to write the state to
        """
        print("Saving analysis state to %s" % filename)
        # make a copy of the state, and do not store the sampler as well
        state = copy.copy(self.__dict__)
        del state['sampler']
        with open(filename, 'wb') as fp:
            pickle.dump(state, fp)

    def load_state(self, filename):
        """
        Loads the complete state of the analysis object from a
        pickle file, stored using save_state.

        Parameters
        ----------
        filename : string
            name of the file to load
        """
        print("Loading analysis state from %s" % filename)
        with open(filename, 'rb') as fp:
            state = pickle.load(fp)
        for key in state.keys():
            self.__dict__[key] = state[key]

    def analyse(self, data_frame=None, compute_moments=True, n_mc=20000):
        """
        Perform SSC analysis on input `data_frame`.

        Parameters
        ----------
        data_frame : pandas.DataFrame
            Input data for analysis.
        compute_moments : bool, optional.
            Compute the first 2 moments. Default is True.

        Returns
        -------
        results : dict
            A dictionary containing the statistical moments.
        """

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")
        elif isinstance(data_frame, pd.DataFrame) and data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        self.load_samples(data_frame)
        # # size of one code sample
        # # TODO: change this to include QoI of different size
        # self.N_qoi = self.samples[qoi_cols[0]][0].size

        # Compute descriptive statistics for each quantity of interest
        results = {'statistical_moments': {}}

        if compute_moments:
            for qoi_k in self.qoi_cols:
                mean_k, var_k = self.get_moments(qoi_k, n_mc=n_mc)
                std_k = var_k ** 0.5
                # compute statistical moments
                results['statistical_moments'][qoi_k] = {'mean': mean_k,
                                                         'var': var_k,
                                                         'std': std_k}

        results = SSCAnalysisResults(raw_data=results, samples=data_frame,
                                     qois=self.qoi_cols, inputs=list(self.sampler.vary.get_keys()))
        results.surrogate_ = self.surrogate
        return results

    def load_samples(self, data_frame):
        """
        Extract output values for each quantity of interest from Dataframe.

        Parameters
        ----------
        data_frame : EasyVVUQ (pandas) data frame
            The code samples from the EasyVVUQ data frame.

        Returns
        -------
        None.

        """
        print('Loading samples...')
        qoi_cols = self.qoi_cols
        samples = {k: [] for k in qoi_cols}
        for k in qoi_cols:
            for run_id in data_frame[('run_id', 0)].unique():
                values = data_frame.loc[data_frame[('run_id', 0)] == run_id][k].values
                samples[k].append(values.flatten())
            samples[k] = np.array(samples[k])
        self.samples = samples
        print('done')

    def get_moments(self, qoi, n_mc):
        """
        Compute the mean and variance through Monte Carlo sampling of the SSC
        surrogate. Independent random inputs samples are drawn though the
        SSC sampler object.

        Parameters
        ----------
        qoi : string
            The name of the QoI.
        n_mc : int
            The number of Monte Carlo samples.

        Returns
        -------
        mean : array
            The mean of qoi.
        var : array
            The variance of qoi.

        """
        print('Computing mean and variance...')
        Xi = self.sampler.sample_inputs(n_mc)
        rvs = [self.surrogate(qoi, xi) for xi in Xi]
        mean = np.mean(rvs)
        var = np.var(rvs)
        print('done.')
        return np.array([mean]), np.array([var])

    def update_surrogate(self, qoi, data_frame, max_LEC_jobs=4, n_mc_LEC=5,
                         max_ENO_jobs=4):
        """
        Update the SSC surrogate given new data. Given an EasyVVUQ dataframe,
        check the LEC condition, and compute the ENO interpolation stencils.

        Parameters
        ----------
        qoi : string
            The name of the QoI on the basis of which the sampling plan
            is refined.
        data_frame : EasyVVUQ (pandas) data frame
            The code samples from the EasyVVUQ data frame.
        max_LEC_jobs : int, optional
            The number of LEC checks to perform in parallel. The default is 4.
        n_mc_LEC : int, optional
            The number of surrogate evaluations used in the LEC check.
            The default is 5.
        max_LEC_jobs : int, optional
            The number of ENO stencils to compute in parallel. The default is 4.

        Returns
        -------
        None. Stores the polynomials orders, interpolation stencils and
        the simplex probabilities in analysis.p_j, analysis.S_j and
        analysis.prob_j respectively.

        """

        # the number of code evaluations
        n_s = self.sampler.n_samples
        # the number of simplex elements
        n_e = self.sampler.n_elements

        # load the EasyVVUQ data frame
        self.load_samples(data_frame)
        # code outputs
        # v = np.array(self.samples[qoi])
        v = self.samples[qoi]

        # find the max polynomial order and set the p_j = pmax
        pmax = self.sampler.find_pmax(n_s)
        if pmax > self.sampler.pmax_cutoff:
            pmax = self.sampler.pmax_cutoff
            print('Max. polynomial order set by hand to = ' + str(pmax))
        else:
            print('Max. polynomial order allowed by n_s = ' + str(pmax))

        # polynomial order per simplex elememt
        p_j = (np.ones(n_e) * pmax).astype('int')

        # compute nearest neighbour stencils
        S_j = self.sampler.compute_stencil_j()

        # check the LEC condition of all stencil
        res_LEC = self.sampler.check_LEC(p_j, v, S_j,
                                         n_mc=n_mc_LEC,
                                         max_jobs=max_LEC_jobs)
        # updated polynomial order, stencil and el_idx are the element indices
        # per interpolation stencil
        p_j = res_LEC['p_j']
        S_j = res_LEC['S_j']
        el_idx = res_LEC['el_idx']

        # convert the nearest-neighbour stencils to ENO stencils
        S_j, p_j, el_idx = self.sampler.compute_ENO_stencil(p_j, S_j, el_idx,
                                                            max_jobs=max_ENO_jobs)
        # store polynomial orders and stencils
        self.p_j = p_j
        self.S_j = S_j

        print("Updated polynomials orders = %s" % p_j)

        # compute the simplex probabilities
        self.prob_j = self.sampler.compute_probability()

    def adapt_locally(self, n_new_samples=1):
        """
        Locally refine the sampling plan based on the SSC geometric
        refinement measure.

        Parameters
        ----------
        n_new_samples : int, optional
            The number of new code evaulations to perform. The default is 1.

        Returns
        -------
        None. Updates the Delaunay triangulation of the SSC sampler with
        the new points. A new ensemble must be executed next.

        """

        if n_new_samples > self.sampler.n_elements:
            n_new_samples = self.sampler.n_elements

        # compute the refinement measures
        eps_bar_j, vol_j = self.sampler.compute_eps_bar_j(self.p_j, self.prob_j)

        # rank elements according to eps_bar_j
        refine_idx = np.flipud(np.argsort(eps_bar_j))

        # find the elements at the hypercube boundaries
        bound_simplices = self.sampler.find_boundary_simplices()

        # store which edges are refined, to prevent refining the same edge twice
        # during the same interation
        refined_edges = []

        # the refinement locations
        xi_k_jref = np.zeros([n_new_samples, self.sampler.n_dimensions])

        i = 0
        j = 0

        # determine n_new_samples locations
        while i < n_new_samples:

            if np.in1d(refine_idx[j], bound_simplices) == False:
                # compute the subvertices of the element chosen for refinement
                sub_vertices = self.sampler.compute_sub_simplex_vertices(refine_idx[j])
                # draw a random sample from the sub simplex
                xi_k_jref[i, :] = self.sampler.sample_simplex(1, sub_vertices)
                # if interior is refined: no danger of refining the same edge twice
                already_refined = False
            else:
                print('refining edge')

                xi_k_jref[i, :], refined_edges, already_refined =  \
                    self.sampler.sample_simplex_edge(refine_idx[j], refined_edges)

            if not already_refined:
                i += 1
                j += 1
            else:
                print('Edge already refined, selecting another sample.')
                j += 1

        self.sampler.update_Delaunay(xi_k_jref)

    def surrogate(self, qoi, xi):
        """
        Evaluate the SSC surrogate at xi.

        Parameters
        ----------
        qoi : string
            Name of the QoI.
        xi : array, shape (n_xi,)
            The location in the input space at which to evaluate the
            surrogate.

        Returns
        -------
        array
            The surrogate output at xi

        """

        if not isinstance(xi, np.ndarray):
            xi = np.array([xi])

        surr = self.sampler.surrogate(xi, self.S_j, self.p_j, self.samples[qoi])
        return np.array([surr])

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

        return self.samples[qoi]

    def plot_grid(self):
        """
        Plot the 1D or 2D sampling plan and color code the simplices according
        to their polynomial order.

        Returns
        -------
        None.

        """

        assert self.sampler.n_xi == 1 or self.sampler.n_xi == 2, \
            "Only works for 1D and 2D problems"

        tri = self.sampler.tri
        colors = ["#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3",
                  "#fdb462", "#b3de69", "#fccde5", "#d9d9d9"]

        if self.sampler.n_xi == 2:
            # plot the delaunay grid and color it according to the local p_j
            fig = plt.figure()
            ax = fig.add_subplot(111, xlabel=r'$\xi_1$', ylabel=r'$\xi_2$',
                                 xlim=[self.sampler.corners[0][0],
                                       self.sampler.corners[0][1]],
                                 ylim=[self.sampler.corners[1][0],
                                       self.sampler.corners[1][1]])

            for p in range(np.max(self.p_j)):
                idx = (self.p_j == p + 1).nonzero()[0]
                first = True
                for i in idx:
                    vertices = tri.points[tri.simplices[i]]
                    if first:
                        pg = Polygon(vertices, facecolor=colors[p], edgecolor='k',
                                     label=r'$p_j = %d$' % (p + 1))
                        first = False
                    else:
                        pg = Polygon(vertices, facecolor=colors[p], edgecolor='k')

                    ax.add_patch(pg)

            leg = plt.legend(loc=0)
            leg.set_draggable(True)

        elif self.sampler.n_xi == 1:
            fig = plt.figure()
            ax = fig.add_subplot(111, xlabel='cell center',
                                 ylabel=r'polynomial order %s' % '$p_j$')
            ax.plot(self.sampler.compute_xi_center_j(), self.p_j, 'o')
            ax.vlines(self.sampler.compute_xi_center_j(), np.zeros(self.sampler.n_elements),
                      self.p_j, linestyles='dashed')
            ax.vlines(self.sampler.tri.points, -0.05 * np.max(self.p_j),
                      0.05 * np.max(self.p_j))

        plt.tight_layout()
        plt.show()
