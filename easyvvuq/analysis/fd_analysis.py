"""Analysis element for polynomial chaos expansion (PCE). We use ChaosPy
under the hood for this functionality.
"""
import logging
import chaospy as cp
import numpy as np
import numpoly
import warnings
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from .results import AnalysisResults
from .qmc_analysis import QMCAnalysisResults

__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"

logger = logging.getLogger(__name__)


class PCEAnalysisResults(QMCAnalysisResults):
    """Analysis results for the FDAnalysis class.
    """

    def _get_derivatives_first(self, qoi, input_):
        """Returns the first order derivative-based index for a given qoi wrt input variable.

        Parameters
        ----------
        qoi : str
           Quantity of interest
        input_ : str
           Input variable

        Returns
        -------
        float
            First order derivative-based index.
        """

        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['derivatives_first'])
        return raw_dict[AnalysisResults._to_tuple(qoi)][input_]

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

    def supported_stats(self):
        """Types of statistics supported by the describe method.

        Returns
        -------
        list of str
        """
        return ['min', 'max', '10%', '90%', '1%', '99%', 'median',
                'mean', 'var', 'std']

    def _describe(self, qoi, statistic):
        """Returns descriptive statistics, similar to pandas describe.

        Parameters
        ----------
        qoi : str
            Name of quantity of interest.
        statistic : str
            One of 'min', 'max', '10%', '90%', 'median', 'mean', 'var', 'std'

        Returns
        -------
        float
            Value of the requested statistic.
        """
        if statistic not in self.supported_stats():
            raise NotImplementedError
        if statistic == 'min':
            return np.array([v.lower[0] for _, v in enumerate(
                self.raw_data['output_distributions'][qoi])])
        elif statistic == 'max':
            return np.array([v.upper[0] for _, v in enumerate(
                self.raw_data['output_distributions'][qoi])])
        elif statistic == '1%':
            return self.raw_data['percentiles'][qoi]['p01']
        elif statistic == '10%':
            return self.raw_data['percentiles'][qoi]['p10']
        elif statistic == '90%':
            return self.raw_data['percentiles'][qoi]['p90']
        elif statistic == '99%':
            return self.raw_data['percentiles'][qoi]['p99']
        elif statistic == 'median':
            return self.raw_data['percentiles'][qoi]['p50']
        else:
            try:
                return self.raw_data['statistical_moments'][qoi][statistic]
            except KeyError:
                raise NotImplementedError

    def surrogate(self):
        """Return a PCE surrogate model.

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
            values = np.array([inputs[key] for key in self.inputs])
            results = dict([(qoi, swap((self.raw_data['fit'][qoi](*values)).T)) for qoi in self.qois])
            return results
        return surrogate_fn

    def get_distribution(self, qoi):
        """Returns a distribution for the given qoi.

        Parameters
        ----------
        qoi: str
            QoI name

        Returns
        -------
        A ChaosPy PDF
        """
        if qoi not in self.qois:
            raise RuntimeError('no such quantity of interest - {}'.format(qoi))
        return self.raw_data['output_distributions'][qoi]


class FDAnalysis(BaseAnalysisElement):

    def __init__(self, sampler=None, qoi_cols=None):
        """Analysis element for polynomial chaos expansion (PCE).

        Parameters
        ----------
        sampler : PCESampler
            Sampler used to initiate the PCE analysis.
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        """

        if sampler is None:
            msg = 'FD analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)

        # Flag specifing if we should scale the runs with the nominal base run
        self.relative_analysis = sampler.relative_analysis

        if qoi_cols is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

    def element_name(self):
        """Name for this element for logging purposes.

        Returns
        -------
        str
            "FD_Analysis"
        """
        return "FD_Analysis"

    def element_version(self):
        """Version of this element for logging purposes.

        Returns
        -------
        str
            Element version.
        """
        return "0.6"

    def analyse(self, data_frame=None):
        """Perform PCE analysis on input `data_frame`.

        Parameters
        ----------
        data_frame : pandas DataFrame
            Input data for analysis.

        Returns
        -------
        PCEAnalysisResults
            Use it to get the sobol indices and other information.
        """

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")
        elif data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        qoi_cols = self.qoi_cols
        T = len(data_frame[qoi_cols[0]].values[-1])

        results = {'statistical_moments': {k: {'mean':np.zeros(T),
                                               'var':np.zeros(T),
                                               'std':np.zeros(T)} for k in qoi_cols},
                   'percentiles': {k: {'p01': np.zeros(T),
                                       'p10': np.zeros(T),
                                       'p50': np.zeros(T),
                                       'p90': np.zeros(T),
                                       'p99': np.zeros(T)} for k in qoi_cols},
                   'sobols_first': {k: {p: np.zeros(T) for p in self.sampler.vary.vary_dict} for k in qoi_cols},
                   'sobols_second': {k: {p: np.zeros(T) for p in self.sampler.vary.vary_dict} for k in qoi_cols},
                   'sobols_total': {k: {p: np.zeros(T) for p in self.sampler.vary.vary_dict} for k in qoi_cols},
                   'correlation_matrices': {k: {} for k in qoi_cols},
                   'output_distributions': {k: {} for k in qoi_cols},
                   'fit': {k: cp.polynomial(np.zeros(T)) for k in qoi_cols},
                   'Fourier_coefficients': {k: {p: np.zeros(T) for p in self.sampler.vary.vary_dict} for k in qoi_cols},
                   'derivatives_first': {k: {p: np.zeros(T) for p in self.sampler.vary.vary_dict} for k in qoi_cols},
                   }

        # Get sampler informations
        nodes = self.sampler._nodes
        perturbations = self.sampler._perturbations
        if self.sampler._is_dependent:
            nodes_dep = self.sampler._nodes_dep
            #perturbations_dep = self.sampler._perturbations_dep
            

        for k in qoi_cols:

            base = data_frame[k].values[0]
            if self.relative_analysis:
                if np.all(np.array(base) == 0):
                    warnings.warn(f"Removing QoI {k} from the analysis, contains all zeros", RuntimeWarning)
                    continue
                if np.any(np.array(base) == 0):
                    warnings.warn(f"Removing QoI {k} from the analysis, contains some zeros", RuntimeWarning)
                    continue

            results['statistical_moments'][k] = {'mean': np.mean(data_frame[k].values, axis=0),
                                                     'var': np.var(data_frame[k].values, axis=0),
                                                     'std': np.std(data_frame[k].values, axis=0)}

            # Get the QoI value for the base value of the parameters
            y_base = data_frame[k].values[0]

            # Compute FD approximation
            offset = 1
            for pi, p in enumerate(self.sampler.vary.vary_dict):
                
                # assumes ordering of the nodes [0, ..., +delta, -delta, ...]
                y_pos = data_frame[k].values[offset]
                y_neg = data_frame[k].values[offset+1]
                
                if self.relative_analysis:
                    d_pos = perturbations[pi][offset]
                    d_neg = perturbations[pi][offset+1]
                    #d_pos = nodes[pi][offset]/nodes[pi][0] - 1
                    #d_neg = nodes[pi][offset+1]/nodes[pi][0] - 1

                    results["derivatives_first"][k][p] = 0.5*(y_pos/y_base-1)/(d_pos) + 0.5*(y_neg/y_base - 1)/(d_neg)

                    # scale the derivatives to the absolute values
                    x_base = nodes[pi][0] # base value of the parameter
                    scaling_factor = y_base/x_base
                    results["derivatives_first"][k][p] *= scaling_factor
                else:
                    d_pos = nodes[pi][offset] - nodes[pi][0]
                    d_neg = nodes[pi][offset+1] - nodes[pi][0]

                    # norm([dg, 0, 0]) = delta_g
                    results["derivatives_first"][k][p] = 0.5*(y_pos - y_base)/(d_pos) + 0.5*(y_neg - y_base)/(d_neg)

                offset = offset + 2

        return PCEAnalysisResults(raw_data=results, samples=data_frame,
                                  qois=self.qoi_cols, inputs=list(self.sampler.vary.get_keys()))
