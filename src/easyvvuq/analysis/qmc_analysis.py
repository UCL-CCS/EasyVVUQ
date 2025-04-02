"""Analysis element for Quasi-Monte Carlo (QMC) sensitivity analysis.

Please refer to the article below for the basic approach used here.
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
    """Analysis results for the QMCAnalysis Method. Refer to the AnalysisResults base class
    documentation for details on using it.
    """

    def _get_sobols_first(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_first'])
        return raw_dict[AnalysisResults._to_tuple(qoi)][input_][0]

    def _get_sobols_total(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['sobols_total'])
        return raw_dict[AnalysisResults._to_tuple(qoi)][input_][0]

    def _get_sobols_second(self, qoi, input_):
        raise NotImplementedError

    def _get_sobols_first_conf(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['conf_sobols_first'])
        return [raw_dict[AnalysisResults._to_tuple(qoi)][input_]['low'][0],
                raw_dict[AnalysisResults._to_tuple(qoi)][input_]['high'][0]]

    def _get_sobols_total_conf(self, qoi, input_):
        raw_dict = AnalysisResults._keys_to_tuples(self.raw_data['conf_sobols_total'])
        return [raw_dict[AnalysisResults._to_tuple(qoi)][input_]['low'][0],
                raw_dict[AnalysisResults._to_tuple(qoi)][input_]['high'][0]]

    def supported_stats(self):
        """Types of statistics supported by the describe method.

        Returns
        -------
        list of str
        """
        return ['mean', 'var', 'std', 'min', 'max', 'median', 'percentiles', '1%', '10%', '50%', '90%', '99%']

    def _describe(self, qoi, statistic):
        if statistic not in self.supported_stats():
            raise NotImplementedError
        if statistic == '1%':
            return self.raw_data['percentiles'][qoi]['p1']
        if statistic == '10%':
            return self.raw_data['percentiles'][qoi]['p10']
        elif statistic == '50%':
            return self.raw_data['percentiles'][qoi]['p50']
        elif statistic == '90%':
            return self.raw_data['percentiles'][qoi]['p90']
        elif statistic == '99%':
            return self.raw_data['percentiles'][qoi]['p99']
        else:
            return self.raw_data['statistical_moments'][qoi][statistic][0]


class QMCAnalysis(BaseAnalysisElement):
    def __init__(self, sampler, qoi_cols=None):
        """Analysis element for Quasi-Monte Carlo (QMC).

        Parameters
        ----------
        sampler : easyvvuq.sampling.qmc.QMCSampler
            Sampler used to initiate the QMC analysis
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is to be
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
        """Name for this element.

        Return
        ------
        str:
            "QMC_Analysis"
        """
        return "QMC_Analysis"

    def element_version(self):
        """Version of this element.

        Return
        ------
        str:
            Element version.
        """
        return "0.2"

    def contains_nan(self, values):
        """
        Checks if ``None`` or ``numpy.nan`` exists in `values`. Returns ``True`` if
        any there are at least one occurrence of ``None`` or ``numpy.nan``.
        Parameters
        ----------
        values : array_like, list, number
            `values` where to check for occurrences of ``None`` or ``np.nan``.
            Can be irregular and have any number of nested elements.
        Returns
        -------
        bool
            ``True`` if `values` has at least one occurrence of ``None`` or
            ``numpy.nan``.
        """
        # To speed up we first try the fast option np.any(np.isnan(values))
        try:
            return np.any(np.isnan(values))
        except (ValueError, TypeError):
            if values is None or values is np.nan:
                return True
            # To solve the problem of float/int as well as numpy int/flaot
            elif np.isscalar(values) and np.isnan(values):
                return True
            elif hasattr(values, "__iter__"):
                for value in values:
                    if self.contains_nan(value):
                        return True

                return False
            else:
                return False

    def create_mask(self, samples):
        """
        Mask samples that do not give results (anything but np.nan or None).
        Parameters
        ----------
        samples : array_like
            Evaluations for the model.
        Returns
        -------
        masked_samples : list
            The evaluations that have results (not numpy.nan or None).
        mask : boolean array
            The mask itself, used to create the masked arrays.
        """
        masked_samples = []
        mask = np.ones(len(samples), dtype=bool)

        for i, result in enumerate(samples):
            # if np.any(np.isnan(result)):
            if self.contains_nan(result):
                mask[i] = False
            else:
                masked_samples.append(result)

        return masked_samples, mask     

    def analyse(self, data_frame):
        """Perform QMC analysis on a given pandas DataFrame.

        Parameters
        ----------
        data_frame : pandas DataFrame
            Input data for analysis.

        Returns
        -------
        easyvvuq.analysis.qmc.QMCAnalysisResults
            AnalysisResults object for QMC.
        """
        if data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        qoi_cols = self.qoi_cols

        results = {
            'statistical_moments': {k: {} for k in qoi_cols},
            'percentiles': {k: {} for k in qoi_cols},
            'sobols_first': {k: {} for k in qoi_cols},
            'sobols_total': {k: {} for k in qoi_cols},
            'conf_sobols_first': {k: {} for k in qoi_cols},
            'conf_sobols_total': {k: {} for k in qoi_cols}
        }

        # Extract output values for each quantity of interest from Dataframe
        samples = self.get_samples(data_frame)

        # Compute descriptive statistics for each quantity of interest
        for k in qoi_cols:
            # Find NaNs and create a mask excluding these samples from the analysis
            # https://github.com/simetenn/uncertainpy/blob/ffb2400289743066265b9a8561cdf3b72e478a28/src/uncertainpy/core/uncertainty_calculations.py#L1532
            masked_samples, mask = self.create_mask(samples[k])

            results['statistical_moments'][k] = {'mean': np.mean(masked_samples, axis=0),
                                                 'var': np.var(masked_samples, axis=0),
                                                 'std': np.std(masked_samples, axis=0),
                                                 'min': np.min(masked_samples, axis=0),
                                                 'max': np.max(masked_samples, axis=0),
                                                 'median': np.median(masked_samples, axis=0),
                                                 }
            results['percentiles'][k] = {'p1': np.percentile(masked_samples, 1, 0)[0],
                                         'p10': np.percentile(masked_samples, 10, 0)[0],
                                         'p50': np.percentile(masked_samples, 50, 0)[0],
                                         'p90': np.percentile(masked_samples, 90, 0)[0],
                                         'p99': np.percentile(masked_samples, 99, 0)[0]}

            # Replace Nan values by the mean before proceeding with the SA
            indices = np.where(mask == 0)[0] # samples[~mask] = results[k].mean
            for i in indices:
                samples[k][i] = results['statistical_moments'][k]['mean']

            if not np.all(mask):
                print("Warning: QoI \"{}\" only yields ".format(k) +
                    "results for {}/{} ".format(sum(mask), len(mask)) +
                    "parameter combinations. " +
                    "Runs {} are not valid. ".format(indices+1) +
                    "NaN results are set to the mean when calculating the Sobol indices. " +
                    "This might affect the Sobol indices.")
            
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
        data_frame : pandas DataFrame
            the EasyVVUQ Pandas dataframe from collation.

        Returns
        -------
        dict :
            A dictionary with the QoI names as keys.
            Each element is a list of code evaluations.
        """
        samples = {k: [] for k in self.qoi_cols}
        for run_id in data_frame['run_id'].squeeze().unique():
            for k in self.qoi_cols:
                data = data_frame.loc[data_frame['run_id'].squeeze() == run_id][k]
                samples[k].append(data.values)
        return samples

    def sobol_bootstrap_(self, samples, alpha=0.05, n_samples=1000):
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
    
    def sobol_bootstrap(self, samples, alpha=0.05, n_bootstrap=1000):
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
        assert n_bootstrap > 0

        # convert to array
        samples = np.array(samples)
        # the number of parameter and the number of MC samples in n_mc * (n_params + 2)
        # and the size of the QoI
        n_params = self.sampler.n_params
        # n_mc = self.sampler.n_mc_samples
        n_mc = int(samples.shape[0]/(n_params + 2))
        n_qoi = samples[0].size
        sobols_first_dict = {}
        conf_first_dict = {}
        sobols_total_dict = {}
        conf_total_dict = {}

        # code evaluations of input matrices M1, M2 and Ni, i = 1,...,n_params
        # see reference above.
        f_M2, f_M1, f_Ni = self._separate_output_values(samples, n_params, n_mc)
        r = np.random.randint(n_mc, size=(n_mc, n_bootstrap))

        for j, param_name in enumerate(self.sampler.vary.get_keys()):

            # our point estimate for the 1st and total order Sobol indices
            value_first = self._first_order(f_M2, f_M1, f_Ni[:, j])
            value_total = self._total_order(f_M2, f_M1, f_Ni[:, j])

            # sobols computed from resampled data points
            if n_mc * n_bootstrap * n_qoi <= 10**7:
                #this is a vectorized computation, Is fast, but f_M2[r] will be of size
                #(n_mc, n_bootstrap, n_qoi), this can become too large and cause a crash, 
                #especially when dealing with large QoI (n_qoi >> 1). So this is only done
                #when n_mc * n_bootstrap * n_qoi <= 10**7
                print("Vectorized bootstrapping")
                sobols_first = self._first_order(f_M2[r], f_M1[r], f_Ni[r, j])
                sobols_total = self._total_order(f_M2[r], f_M1[r], f_Ni[r, j])
            else:
                #array for resampled estimates
                sobols_first = np.zeros([n_bootstrap, n_qoi])
                sobols_total = np.zeros([n_bootstrap, n_qoi])
                print("Sequential bootstrapping")
                #non-vectorized implementation
                for i in range(n_bootstrap):
                    #resampled sample matrices of size (n_mc, n_qoi)
                    sobols_first[i] = self._first_order(f_M2[r[i]], f_M1[r[i]], f_Ni[r[i], j])
                    sobols_total[i] = self._total_order(f_M2[r[i]], f_M1[r[i]], f_Ni[r[i], j])

            # compute confidence intervals based on percentiles
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
