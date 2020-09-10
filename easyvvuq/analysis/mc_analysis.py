
import logging
import numpy as np
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from easyvvuq.sampling import RandomSampler

__author__ = 'Wouter Edeling'
__license__ = "LGPL"

logger = logging.getLogger(__name__)


class MCAnalysis(BaseAnalysisElement):

    def __init__(self, sampler, qoi_cols=None):
        """Analysis element for Quasi-Monte Carlo (QMC).

        Parameters
        ----------
        sampler : easyvvuq.sampling.random
            MC Sampler used to evaluate the model
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        """
        if not isinstance(sampler, RandomSampler):
            raise RuntimeError(
                'MCAnalysis class relies on the RandomSampler as its sampling component')
        if qoi_cols is None:
            self.qoi_cols = list(sampler.vary.get_keys())
        else:
            self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

    def element_name(self):
        """Name for this element"""
        return "MC_Analysis"

    def element_version(self):
        """Version of this element"""
        return "0.1"

    def analyse(self, data_frame):
        """Perform MC analysis on a given pandas DataFrame.

        Parameters
        ----------
        data_frame : pandas DataFrame
            Input data for analysis.

        Returns
        -------
        dict:
            Contains analysis results in sub-dicts with keys -
            ['statistical_moments', 'sobols_first', 'sobols_total']
        """
        if data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        qoi_cols = self.qoi_cols

        results = {
            'sobols_first': {k: {} for k in qoi_cols},
            'sobols_total': {k: {} for k in qoi_cols}
        }

        # Extract output values for each quantity of interest from Dataframe
        self.N_qoi = {}  # the size of the QoIs
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                data = data_frame.loc[data_frame['run_id'] == run_id][k]
                samples[k].append(data.values)
                self.N_qoi[k] = samples[k][0].size

        # Compute descriptive statistics for each quantity of interest
        for k in qoi_cols:
            # Sensitivity Analysis: First and Total Sobol indices
            sobols_first_dict = {}
            sobols_total_dict = {}
            sobols_first, sobols_total = self.get_sobol_indices(k, samples)
            i_par = 0
            for param_name in self.sampler.vary.get_keys():
                sobols_first_dict[param_name] = sobols_first[i_par]
                sobols_total_dict[param_name] = sobols_total[i_par]
                i_par += 1
            results['sobols_first'][k] = sobols_first_dict
            results['sobols_total'][k] = sobols_total_dict

        return results

    def get_sobol_indices(self, qoi, samples):
        """
        Compute the first-order and total-order Sobol indices for qoi.

        Method: A. Saltelli, Making best use of model evaluations to compute
        sensitivity indices, Computer Physics Communications, 2002.

        Parameters
        ----------
        + qoi : The name of the QoI
        + samples : The EasyVVUQ dataframe.

        Returns
        -------
        sobols_first : array of first-order indices.
        sobols_total : array of total-order indices.

        """
        print('Computing Sobol indices...')
        # #the starting index of the sobol samples in the dataframe
        # sobol_start = self.sampler.sobol_start
        # #the end index of the sobol samples in the dataframe
        # sobol_count = self.sampler.sobol_count
        # #the samples to be used to compute the Sobol indices
        # sobol_samples = np.array(samples[qoi][sobol_start:sobol_count])
        sobol_samples = np.array(samples[qoi])
        # the number of input parameters
        n_params = self.sampler.n_params
        # the total variance
        var = np.var(sobol_samples, axis=0)
        # Saltelli: cost = n_mc*(n_params + 2), find n_mc
        cost = self.sampler.max_num
        n_mc = int(cost / (n_params + 2))
        # the size of the QoI
        n_qoi = self.N_qoi[qoi]
        # seperate the samples into contribution due to M1, M2 and the Ni matrices
        sobol_samples = sobol_samples.reshape([n_params + 2, n_mc, n_qoi])
        # function evaluations on the inputs of matrix M1
        f_M_1 = sobol_samples[0].reshape([n_mc, n_qoi])
        # function evaluations on the inputs of matrix M2
        f_M_2 = sobol_samples[1].reshape([n_mc, n_qoi])
        # function evaluations on the inputs of matrix Ni, i=1,...,n_params
        f_N_i = np.zeros([n_params, n_mc, n_qoi])
        for i in range(n_params):
            f_N_i[i] = sobol_samples[i + 2].reshape([n_mc, n_qoi])
        # the estimate of the squared mean
        E_squared = np.dot(f_M_1.T, f_M_2) / n_mc
        # U_j for the 1st order indices (integral of sqaured condition mean)
        U_j = np.zeros([n_params, n_qoi])
        for i in range(n_params):
            U_j[i] = np.dot(f_M_1.T, f_N_i[i]) / (n_mc - 1)
        # first-order sobol indices
        sobols_first = (U_j - E_squared) / var
        # U_j for the total order indices (integral of sqaured condition mean)
        U_j = np.zeros([n_params, n_qoi])
        for i in range(n_params):
            U_j[i] = np.dot(f_M_2.T, f_N_i[i]) / (n_mc - 1)
        # total-order sobol indices
        sobols_total = 1.0 - (U_j - E_squared) / var
        print('done.')
        return sobols_first, sobols_total
