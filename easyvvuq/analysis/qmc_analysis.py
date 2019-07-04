"""Analysis element for Quasi-Monte Carlo (QMC).
"""
import logging
import numpy as np
from easyvvuq import OutputType
from .base import BaseAnalysisElement

__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"

logger = logging.getLogger(__name__)


class QMCAnalysis(BaseAnalysisElement):

    def __init__(self, sampler=None, qoi_cols=None):
        """Analysis element for Quasi-Monte Carlo (QMC).

        Parameters
        ----------
        sampler : :obj:`easyvvuq.sampling.qmc.QMCSampler`
            Sampler used to initiate the QMC analysis
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        """

        if sampler is None:
            msg = 'QMC analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)

        if qoi_cols is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

    def element_name(self):
        """Name for this element for logging purposes"""
        return "QMC_Analysis"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.1"

    def analyse(self, data_frame=None):
        """Perform QMC analysis on input `data_frame`.

        Parameters
        ----------
        data_frame : :obj:`pandas.DataFrame`
            Input data for analysis.

        Returns
        -------
        dict:
            Contains analysis results in sub-dicts with keys -
            ['statistical_moments', 'percentiles', 'sobol_indices',
             'correlation_matrices', 'output_distributions']
        """

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")
        elif data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        qoi_cols = self.qoi_cols

        results = {'statistical_moments': {},
                   'percentiles': {},
                   'correlation_matrices': {},
                   }

        # Get the number of samples: TODO for SA
        number_of_samples = self.sampler.number_of_samples

        # Extract output values for each quantity of interest from Dataframe
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == run_id][k]
                samples[k].append(values)

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
            P10 = np.percentile(samples[k], 10, 0)
            P90 = np.percentile(samples[k], 90, 0)
            results['percentiles'][k] = {'p10': P10, 'p90': P90}

            # Sensitivity Analysis: First and Total Sobol indices
            # TODO use saltelli method

            # Correlation matrix
            results['correlation_matrices'][k] = np.corrcoef(samples[k])

        return results
