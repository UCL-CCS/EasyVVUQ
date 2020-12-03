"""Analysis element for polynomial chaos expansion (PCE).
"""
import logging
import chaospy as cp
import pandas as pd
import numpy as np
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from .results import AnalysisResults
from .qmc_analysis import QMCAnalysisResults

__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"

logger = logging.getLogger(__name__)


class PCEAnalysisResults(QMCAnalysisResults):
    implemented = ['sobols_first', 'sobols_total', 'describe']

    def _get_sobols_first(self, qoi, input_):
        """Returns the first order sobol index for a given qoi wrt input variable.

        Parameters
        ----------
        qoi : str
           Quantity of interest
        input_ : str
           Input variable

        Returns
        -------
        float
            First order sobol index.
        """
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_first'])
        return raw_dict[AnalysisResults._to_tuple(qoi)][input_]

    def _get_sobols_second(self, qoi, input_):
        """Returns the second order sobol index for a given qoi wrt input variable.

        Parameters
        ----------
        qoi : str
           Quantity of interest
        input_ : str
           Input variable

        Returns
        -------
        float
            Second order sobol index.
        """
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_second'])
        return dict([(in_, raw_dict[AnalysisResults._to_tuple(qoi)][input_][i])
                     for i, in_ in enumerate(self.inputs) if in_ != input_])

    def _get_sobols_total(self, qoi, input_):
        """Returns the total order sobol index for a given qoi wrt input variable.

        Parameters
        ----------
        qoi : str
           Quantity of interest
        input_ : str
           Input variable

        Returns
        -------
        float
            Total order sobol index.
        """
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_total'])
        return raw_dict[AnalysisResults._to_tuple(qoi)][input_]

    def _describe(self, qoi, statistic):
        """Returns descriptive statistics, similar to pandas describe.

        Examples
        --------


        Returns
        -------
        pandas DataFrame with descriptive statistics
        """
        if statistic == 'min':
            return np.array([v.lower[0] for _, v in enumerate(
                self.raw_data['output_distributions'][qoi])])
        elif statistic == 'max':
            return np.array([v.upper[0] for _, v in enumerate(
                self.raw_data['output_distributions'][qoi])])
        elif statistic == '10%':
            return self.raw_data['percentiles'][qoi]['p10']
        elif statistic == '90%':
            return self.raw_data['percentiles'][qoi]['p90']
        else:
            try:
                return self.raw_data['statistical_moments'][qoi][statistic]
            except KeyError:
                raise NotImplementedError


class PCEAnalysis(BaseAnalysisElement):

    def __init__(self, sampler=None, qoi_cols=None):
        """Analysis element for polynomial chaos expansion (PCE).

        Parameters
        ----------
        sampler : :obj:`easyvvuq.sampling.pce.PCESampler`
            Sampler used to initiate the PCE analysis
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        """

        if sampler is None:
            msg = 'PCE analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)

        if qoi_cols is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

    def element_name(self):
        """Name for this element for logging purposes"""
        return "PCE_Analysis"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.6"

    def analyse(self, data_frame=None):
        """Perform PCE analysis on input `data_frame`.

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
                   'sobols_first': {k: {} for k in qoi_cols},
                   'sobols_second': {k: {} for k in qoi_cols},
                   'sobols_total': {k: {} for k in qoi_cols},
                   'correlation_matrices': {},
                   'output_distributions': {},
                   }

        # Get sampler informations
        P = self.sampler.P
        nodes = self.sampler._nodes
        weights = self.sampler._weights
        regression = self.sampler.regression

        # Extract output values for each quantity of interest from Dataframe
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame[('run_id', 0)].unique():
            for k in qoi_cols:
                data = data_frame.loc[data_frame[('run_id', 0)] == run_id][k]
                samples[k].append(data.values.flatten())

        # Compute descriptive statistics for each quantity of interest
        for k in qoi_cols:
            # Approximation solver
            if regression:
                fit = cp.fit_regression(P, nodes, samples[k])
            else:
                fit = cp.fit_quadrature(P, nodes, weights, samples[k])

            # Statistical moments
            mean = cp.E(fit, self.sampler.distribution)
            var = cp.Var(fit, self.sampler.distribution)
            std = cp.Std(fit, self.sampler.distribution)
            results['statistical_moments'][k] = {'mean': mean,
                                                 'var': var,
                                                 'std': std}

            # Percentiles: 10% and 90%
            P10 = cp.Perc(fit, 10, self.sampler.distribution)
            P90 = cp.Perc(fit, 90, self.sampler.distribution)
            results['percentiles'][k] = {'p10': P10, 'p90': P90}

            # Sensitivity Analysis: First, Second and Total Sobol indices
            sobols_first_narr = cp.Sens_m(fit, self.sampler.distribution)
            sobols_second_narr = cp.Sens_m2(fit, self.sampler.distribution)
            sobols_total_narr = cp.Sens_t(fit, self.sampler.distribution)
            sobols_first_dict = {}
            sobols_second_dict = {}
            sobols_total_dict = {}
            for i, param_name in enumerate(self.sampler.vary.vary_dict):
                sobols_first_dict[param_name] = sobols_first_narr[i]
                sobols_second_dict[param_name] = sobols_second_narr[i]
                sobols_total_dict[param_name] = sobols_total_narr[i]

            results['sobols_first'][k] = sobols_first_dict
            results['sobols_second'][k] = sobols_second_dict
            results['sobols_total'][k] = sobols_total_dict

            # Correlation matrix
            results['correlation_matrices'][k] = cp.Corr(
                fit, self.sampler.distribution)

            # Output distributions
            results['output_distributions'][k] = cp.QoI_Dist(
                fit, self.sampler.distribution)

        return PCEAnalysisResults(raw_data=results, samples=data_frame,
                                  qois=self.qoi_cols, inputs=list(self.sampler.vary.get_keys()))
