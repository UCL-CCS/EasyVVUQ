"""Analysis element for Quasi-Monte Carlo (QMC) sensitivity analysis.

Please refer to the article below for further references.
https://en.wikipedia.org/wiki/Variance-based_sensitivity_analysis
"""
import logging
import numpy as np
from easyvvuq import OutputType
from .base import BaseAnalysisElement
from easyvvuq.sampling import QMCSampler
from .results import AnalysisResults
from easyvvuq.sampling import MCSampler
from .ensemble_boot import confidence_interval

__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"

logger = logging.getLogger(__name__)


class QMCAnalysisResults(AnalysisResults):
    implemented = ['sobols_first', 'sobols_total', 'describe']

    def _get_sobols_first(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_first'])
        return raw_dict[AnalysisResults._to_tuple(qoi)][input_][0]

    def _get_sobols_total(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_total'])
        return raw_dict[AnalysisResults._to_tuple(qoi)][input_][0]

    def _get_sobols_first_conf(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['conf_sobols_first'])
        return [raw_dict[AnalysisResults._to_tuple(qoi)][input_]['low'][0],
                raw_dict[AnalysisResults._to_tuple(qoi)][input_]['high'][0]]

    def _get_sobols_total_conf(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['conf_sobols_total'])
        return [raw_dict[AnalysisResults._to_tuple(qoi)][input_]['low'][0],
                raw_dict[AnalysisResults._to_tuple(qoi)][input_]['high'][0]]


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
        if not isinstance(sampler, QMCSampler) and not isinstance(sampler, MCSampler):
            raise RuntimeError(
                'QMCAnalysis class relies on the QMCSampler or MCSampler as its sampling component')
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

        results = {
            'statistical_moments': {k: {} for k in qoi_cols},
            'sobols_first': {k: {} for k in qoi_cols},
            'sobols_total': {k: {} for k in qoi_cols},
            'conf_sobols_first': {k: {} for k in qoi_cols},
            'conf_sobols_total': {k: {} for k in qoi_cols}
        }

        # Extract output values for each quantity of interest from Dataframe
        samples = self.get_samples(data_frame)

        # Compute descriptive statistics for each quantity of interest
        for k in qoi_cols:
            results['statistical_moments'][k] = {'mean': np.mean(samples[k], axis=0),
                                                 'var': np.var(samples[k], axis=0),
                                                 'std': np.std(samples[k], axis=0)}
            sobols_first, conf_first, sobols_total, conf_total = \
                self.sobol_bootstrap(samples[k])
            results['sobols_first'][k] = sobols_first
            results['sobols_total'][k] = sobols_total
            results['conf_sobols_first'][k] = conf_first
            results['conf_sobols_total'][k] = conf_total

        return QMCAnalysisResults(raw_data=results, samples=data_frame,
                                  qois=self.qoi_cols, inputs=list(self.sampler.vary.get_keys()))

    def get_samples(self, data_frame):
        """
        Converts the Pandas dataframe into a dictionary.

        Parameters
        ----------
        data_frame : the EasyVVUQ Pandas dataframe.

        Returns
        -------
        samples : A dictionary with the QoI names as keys. Each samples[qoi_name]
        is a list of code evaluations.

        """
        samples = {k: [] for k in self.qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in self.qoi_cols:
                data = data_frame.loc[data_frame['run_id'] == run_id][k]
                samples[k].append(data.values)
        return samples

    def sobol_bootstrap(self, samples, alpha=0.05, n_samples=1000):
        """
        Computes the first order and total order Sobol indices using Saltelli's
        method. To assess the sampling inaccuracy, bootstrap confidence intervals
        are also computed.

        Reference: A. Saltelli, Making best use of model evaluations to compute
        sensitivity indices, Computer Physics Communications, 2002.

        Parameters
        ----------
        samples : list
            The samples for a given QoI.
        alpha: float
            The (1 - alpha) * 100 confidence interval parameter. The default is 0.05.
        n_samples: int
            The number of bootstrap samples. The default is 1000.

        Returns
        -------
        sobols_first_dict, conf_first_dict, sobols_total_dict, conf_total_dict:
        dictionaries containing the first- and total-order Sobol indices for all
        parameters, and (1-alpha)*100 lower and upper confidence bounds.

        """
        assert len(samples) > 0
        assert alpha > 0.0
        assert alpha < 1.0
        assert n_samples > 0

        # convert to array
        samples = np.array(samples)
        # the number of parameter and the number of MC samples in n_mc * (n_params + 2)
        # and the size of the QoI
        n_params = self.sampler.n_params
        n_mc = self.sampler.n_mc_samples
        n_qoi = samples[0].size
        sobols_first_dict = {}
        conf_first_dict = {}
        sobols_total_dict = {}
        conf_total_dict = {}

        for j, param_name in enumerate(self.sampler.vary.get_keys()):
            # code evaluations of input matrices M1, M2 and Ni, i = 1,...,n_params
            # see reference above.
            f_M2, f_M1, f_Ni = self._separate_output_values(samples, n_params, n_mc)
            # our point estimate for the 1st and total order Sobol indices
            value_first = self._first_order(f_M2, f_M1, f_Ni[:, j])
            value_total = self._total_order(f_M2, f_M1, f_Ni[:, j])
            # array for resampled estimates
            sobols_first = np.zeros([n_samples, n_qoi])
            sobols_total = np.zeros([n_samples, n_qoi])
            for i in range(n_samples):
                # resample, must be done on already seperated output due to
                # the specific order in samples
                idx = np.random.randint(0, n_mc - 1, n_mc)
                f_M2_resample = f_M2[idx]
                f_M1_resample = f_M1[idx]
                f_Ni_resample = f_Ni[idx]
                # recompute Sobol indices
                sobols_first[i] = self._first_order(f_M2_resample, f_M1_resample,
                                                    f_Ni_resample[:, j])
                sobols_total[i] = self._total_order(f_M2_resample, f_M1_resample,
                                                    f_Ni_resample[:, j])
            # compute confidence intervals
            _, low_first, high_first = confidence_interval(sobols_first, value_first,
                                                           alpha, pivotal=True)
            _, low_total, high_total = confidence_interval(sobols_total, value_total,
                                                           alpha, pivotal=True)
            # store results
            sobols_first_dict[param_name] = value_first
            conf_first_dict[param_name] = {'low': low_first, 'high': high_first}
            sobols_total_dict[param_name] = value_total
            conf_total_dict[param_name] = {'low': low_total, 'high': high_total}

        return sobols_first_dict, conf_first_dict, sobols_total_dict, conf_total_dict

    # Adapted from SALib
    @staticmethod
    def _separate_output_values(samples, n_params, n_mc_samples):
        """There are n_params + 2 different input matrices: M1, M2, N_i,
        i=1,...,n_params.  (see reference under sobol_bootstrap). The
        EasyVVUQ dataframe is stored in the order:

        [sample from M2, sample from N1, N2, ... sample from N_n_params,
         sample from M1, repeat].

        This subroutine separates the output values into the contributions
        of the different input matrices.

        Parameters
        ----------
        samples: list
            The samples for a given QoI
        n_params: int
            The number of uncertain input parameters.
        n_mc_samples: int
            The number of MC samples per input matrix, i.e. the
          number of rows in M1, M2 or Ni.

        Returns
        -------
        NumPy arrays of the separated code evaluations: f_M2, f_M1, f_Ni, where
        f_Ni contains n_params entries corresponding to the n_params Ni matrices.

        """
        evaluations = np.array(samples)

        shape = (n_mc_samples, n_params) + evaluations[0].shape
        step = n_params + 2
        f_Ni = np.zeros(shape)

        f_M2 = evaluations[0:evaluations.shape[0]:step]
        f_M1 = evaluations[(step - 1):evaluations.shape[0]:step]

        for i in range(n_params):
            f_Ni[:, i] = evaluations[(i + 1):evaluations.shape[0]:step]

        return f_M2, f_M1, f_Ni

    @staticmethod
    def _first_order(f_M2, f_M1, f_Ni):
        """Calculate first order sensitivity indices.

        Parameters
        ----------
        f_M2: NumPy array
            Array of code evaluations on input array M2
        f_M1: NumPy array
            Array of code evaluations on input array M1
        f_Ni: NumPy array
            Array of code evaluations on input array Ni, i=1,...,n_params

        Returns
        -------
        A NumPy array of the n_params first-order Sobol indices.
        """
        V = np.var(np.r_[f_M2, f_M1], axis=0)
        return np.mean(f_M1 * (f_Ni - f_M2), axis=0) / (V + (V == 0)) * (V != 0)

    @staticmethod
    def _total_order(f_M2, f_M1, f_Ni):
        """Calculate total order sensitivity indices. See also:

        A Saltelli et al, Variance based sensitivity analysis of model output.
        Design and estimator for the total sensitivity index, 2009.

        Parameters
        ----------
        f_M2: NumPy array
            Array of code evaluations on input array M2 (matrix A in ref above)
        f_M1: NumPy array
            Array of code evaluations on input array M1 (matrix B in ref above)
        f_Ni: NumPy array
            Array of code evaluations on input array Ni, i=1,...,n_params
          (matrix AB in ref above)

        Returns
        -------
        A NumPy array of the n_params total-order Sobol indices.
        """
        V = np.var(np.r_[f_M2, f_M1], axis=0)
        return 0.5 * np.mean((f_M2 - f_Ni) ** 2, axis=0) / (V + (V == 0)) * (V != 0)
