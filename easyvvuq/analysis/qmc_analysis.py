"""Analysis element for Quasi-Monte Carlo (QMC) sensitivity analysis.

Please refer to the article below for further references.
https://en.wikipedia.org/wiki/Variance-based_sensitivity_analysis
"""
import logging
import numpy as np
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from easyvvuq.sampling import QMCSampler

__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"

logger = logging.getLogger(__name__)


class QMCAnalysis(BaseAnalysisElement):

    def __init__(self, sampler, qoi_cols=None):
        """Analysis element for Quasi-Monte Carlo (QMC).

        Parameters
        ----------
        sampler : easyvvuq.sampling.qmc.QMCSampler
            Sampler used to initiate the QMC analysis
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        """
        if not isinstance(sampler, QMCSampler):
            raise RuntimeError('QMCAnalysis class relies on the QMCSampler as its sampling component')
        if qoi_cols is None:
            self.qoi_cols = list(sampler.vary.get_keys())
        else:
            self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

    def element_name(self):
        """Name for this element"""
        return "QMC_Analysis"

    def element_version(self):
        """Version of this element"""
        return "0.2"

    def analyse(self, data_frame):
        """Perform QMC analysis on a given pandas DataFrame.

        Parameters
        ----------
        data_frame : pandas DataFrame
            Input data for analysis.

        Returns
        -------
        dict:
            Contains analysis results in sub-dicts with keys -
            ['statistical_moments', 'percentiles', 'sobol_indices',
             'correlation_matrices', 'output_distributions']
        """
        if data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        qoi_cols = self.qoi_cols

        results = {'statistical_moments': {},
                   'percentiles': {},
                   'sobols_first': {k: {} for k in qoi_cols},
                   'sobols_total': {k: {} for k in qoi_cols},
                   'correlation_matrices': {},
                   }

        # Get the number of samples and uncertain parameters
        n_params = self.sampler.n_params
        n_sobol_samples = int(np.round(self.sampler.n_mc_samples / 2.))

        # Extract output values for each quantity of interest from Dataframe
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                data = data_frame.loc[data_frame['run_id'] == run_id][k]
                samples[k].append(data.values)

        # Compute descriptive statistics for each quantity of interest
        for k in qoi_cols:
            # Statistical moments
            mean = np.mean(samples[k], 0)
            var = np.var(samples[k], 0)
            std = np.std(samples[k], 0)
            results['statistical_moments'][k] = {'mean': mean,
                                                 'var': var,
                                                 'std': std}

            # Percentiles (Pxx)
            p_10 = np.percentile(samples[k], 10, 0)
            p_90 = np.percentile(samples[k], 90, 0)
            results['percentiles'][k] = {'p10': p_10, 'p90': p_90}

            # Sensitivity Analysis: First and Total Sobol indices
            A, B, AB = self._separate_output_values(samples[k],
                                                    n_params,
                                                    n_sobol_samples)
            sobols_first_dict = {}
            sobols_total_dict = {}
            i_par = 0
            for param_name in self.sampler.vary.get_keys():
                sobols_first_dict[param_name] = self._first_order(A, B, AB[:, i_par])
                sobols_total_dict[param_name] = self._total_order(A, B, AB[:, i_par])
                i_par += 1
            results['sobols_first'][k] = sobols_first_dict
            results['sobols_total'][k] = sobols_total_dict

            # Correlation matrix
            results['correlation_matrices'][k] = np.corrcoef(samples[k])

        return results

    # Adapted from SALib
    @staticmethod
    def _separate_output_values(evaluations, n_uncertain_params, n_samples):
        """
        Parameters
        ----------
        evaluations: NumPy array
        n_uncertain_params: int
        n_samples: int

        Returns
        -------
        3-tuple of NumPy arrays
        """
        evaluations = np.array(evaluations)

        shape = (n_samples, n_uncertain_params) + evaluations[0].shape
        step = n_uncertain_params + 2
        AB = np.zeros(shape)

        A = evaluations[0:evaluations.shape[0]:step]
        B = evaluations[(step - 1):evaluations.shape[0]:step]

        for i in range(n_uncertain_params):
            AB[:, i] = evaluations[(i + 1):evaluations.shape[0]:step]

        return A, B, AB

    @staticmethod
    def _first_order(A, B, AB):
        """Calculate first order sensitivity indices.

        Parameters
        ----------
        A: NumPy array
        B: NumPy array
        AB: NumPy array

        Returns
        -------
        A NumPy array
        """ 
        V = np.var(np.r_[A, B], axis=0)
        return np.mean(B * (AB - A), axis=0) / (V + (V == 0)) * (V != 0)

    @staticmethod
    def _total_order(A, B, AB):
        """Calculate total order sensitivity indices.

        Parameters
        ----------
        A: NumPy array
        B: NumPy array
        AB: NumPy array

        Returns
        -------
        A NumPy array
        """
        V = np.var(np.r_[A, B], axis=0)
        return 0.5 * np.mean((A - AB) ** 2, axis=0) / (V + (V == 0)) * (V != 0)
