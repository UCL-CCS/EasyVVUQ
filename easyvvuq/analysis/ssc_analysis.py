"""
ANALYSIS CLASS FOR THE SSC SAMPLER
"""

import numpy as np
import pickle
import copy
from easyvvuq import OutputType
from .base import BaseAnalysisElement
# from .results import AnalysisResults
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


# TODO: complete this
# class SCAnalysisResults(AnalysisResults):
#     def _get_sobols_first(self, qoi, input_):
#         raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_first'])
#         result = raw_dict[AnalysisResults._to_tuple(qoi)][input_]
#         try:
#             return np.array([float(result)])
#         except TypeError:
#             return np.array(result)

#     def supported_stats(self):
#         """Types of statistics supported by the describe method.

#         Returns
#         -------
#         list of str
#         """
#         return ['mean', 'var', 'std']

#     def _describe(self, qoi, statistic):
#         if statistic in self.supported_stats():
#             return self.raw_data['statistical_moments'][qoi][statistic]
#         else:
#             raise NotImplementedError

#     def surrogate(self):
#         """Return an SC surrogate model.

#         Returns
#         -------
#         A function that takes a dictionary of parameter - value pairs and returns
#         a dictionary with the results (same output as decoder).
#         """
#         def surrogate_fn(inputs):
#             def swap(x):
#                 if len(x) > 1:
#                     return list(x)
#                 else:
#                     return x[0]
#             values = np.squeeze(np.array([inputs[key] for key in self.inputs])).T
#             results = dict([(qoi, swap(self.surrogate_(qoi, values))) for qoi in self.qois])
#             return results
#         return surrogate_fn


class SSCAnalysis(BaseAnalysisElement):

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

    def analyse(self, data_frame=None):
        """Perform SSC analysis on input `data_frame`.

        Parameters
        ----------
        data_frame : pandas.DataFrame
            Input data for analysis.

        Returns
        -------
            #TODO: to be completed
        """

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")
        elif isinstance(data_frame, pd.DataFrame) and data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        # # Extract output values for each quantity of interest from Dataframe
        # print('Loading samples...')
        # qoi_cols = self.qoi_cols
        # samples = {k: [] for k in qoi_cols}
        # for run_id in data_frame[('run_id', 0)].unique():
        #     for k in qoi_cols:
        #         values = data_frame.loc[data_frame[('run_id', 0)] == run_id][k].values
        #         samples[k].append(values.flatten())
        # self.samples = samples
        # print('done')

        # # size of one code sample
        # # TODO: change this to include QoI of different size
        # self.N_qoi = self.samples[qoi_cols[0]][0].size

        self.load_samples(data_frame)

        # results = SCAnalysisResults(raw_data=results, samples=data_frame,
        #                             qois=qoi_cols, inputs=list(self.sampler.vary.get_keys()))
        # results.surrogate_ = self.surrogate
        # return results

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
        for run_id in data_frame[('run_id', 0)].unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame[('run_id', 0)] == run_id][k].values
                samples[k].append(values.flatten())
        self.samples = samples
        print('done')

    def adapt_locally(self, qoi, data_frame, n_new_samples=1,
                      max_LEC_jobs=4, n_mc_LEC=5):

        n_s = self.sampler.n_samples
        n_e = self.sampler.n_elements

        self.load_samples(data_frame)
        v = np.array(self.samples[qoi])

        # find the max polynomial order and set the p_j = pmax
        pmax = self.sampler.find_pmax(n_s)
        if pmax > self.sampler.pmax_cutoff:
            pmax = self.sampler.pmax_cutoff
            print('Max. polynomial order set by hand to = ' + str(pmax))
        else:
            print('Max. polynomial order allowed by n_s = ' + str(pmax))

        p_j = (np.ones(n_e) * pmax).astype('int')

        # compute nearest neighbour stencils
        S_j = self.sampler.compute_stencil_j()

        # check the LEC condition of all stencil
        res_LEC = self.sampler.check_LEC(p_j, v, S_j,
                                         n_mc=n_mc_LEC,
                                         max_jobs=max_LEC_jobs)
        p_j = res_LEC['p_j']
        S_j = res_LEC['S_j']
        el_idx = res_LEC['el_idx']

        # convert the nearest-neighbour stencils to ENO stencils
        S_j, p_j, el_idx = self.sampler.compute_ENO_stencil(p_j, S_j, el_idx,
                                                            max_jobs=max_LEC_jobs)
        # store polynomial orders and stencils
        self.p_j = p_j
        self.S_j = S_j

        # compute the simplex probabilities
        self.prob_j = self.sampler.compute_probability()

        # compute the refinement measures
        eps_bar_j, vol_j = self.sampler.compute_eps_bar_j(p_j, self.prob_j)

        # rank elements according to eps_bar_j
        refine_idx = np.flipud(np.argsort(eps_bar_j))

        # find the elements at the hypercube boundaries
        bound_simplices = self.sampler.find_boundary_simplices()

        refined_edges = []
        run_idx = []

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

                # fres = fpool.apply_async(QoI, args = (xi_k_jref[i, :],))
                # fjobs.append(fres)

                run_idx.append(i)
                i += 1
                j += 1
            else:
                print('Edge already refined, selecting another sample.')
                j += 1

        self.sampler.update_Delaunay(xi_k_jref)

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
