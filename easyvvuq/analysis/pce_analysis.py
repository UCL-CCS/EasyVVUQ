"""Analysis element for polynomial chaos expansion (PCE).
"""
import logging
import chaospy as cp
from easyvvuq import OutputType
from .base import BaseAnalysisElement

__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"

logger = logging.getLogger(__name__)

# TODO: Enhancements - issue #101
#       - Work out how to get multiple Sobol indices
#         + Note that may require different orders for different qoi?
#       - Add pd.read_hdf (https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-hdf5)
#       - Test cp.fit_regression to approximate solver


class PCEAnalysis(BaseAnalysisElement):

    def __init__(self, sampler=None, qoi_cols=None, sobol_order=1):
        """Analysis element for polynomial chaos expansion (PCE).

        Parameters
        ----------
        sampler : :obj:`easyvvuq.sampling.pce.PCESampler`
            Sampler used to initiate the PCE analysis
        qoi_cols : list or None
            Column names for quantities of interest (for which analysis is
            performed).
        sobol_order : int, default=1
            Order of Sobol indices to calculate.
        """

        if sampler is None:
            msg = 'PCE analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)
        # TODO: Check that this is a viable PCE sampler?

        if qoi_cols is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        if sobol_order > len(sampler.vary.vary_dict):
            logger.warning("sobol_order too high - set to number of "
                           "variables from sampler")
            sobol_order = len(sampler.vary.vary_dict)

        self.sobol_order = sobol_order
        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

    def element_name(self):
        """Name for this element for logging purposes"""
        return "PCE_Analysis"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.3"

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
                   'sobol_indices': {k: {} for k in qoi_cols},
                   'correlation_matrices': {},
                   'output_distributions': {},
                   }

        # Get the Polynomial
        P = self.sampler.P

        # Compute nodes and weights
        nodes, weights = cp.generate_quadrature(order=self.sampler.quad_order,
                                                domain=self.sampler.distribution,
                                                rule=self.sampler.quad_rule,
                                                sparse=self.sampler.quad_sparse)

        # Extract output values for each quantity of interest from Dataframe
        samples = {k: [] for k in qoi_cols}
        for run_id in data_frame.run_id.unique():
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == run_id][k]
                samples[k].append(values)

        # Compute descriptive statistics for each quantity of interest
        for k in qoi_cols:
            # Approximation solver
            fit = cp.fit_quadrature(P, nodes, weights, samples[k])

            # Statistical moments
            mean = cp.E(fit, self.sampler.distribution)
            var = cp.Var(fit, self.sampler.distribution)
            std = cp.Std(fit, self.sampler.distribution)
            results['statistical_moments'][k] = {'mean': mean,
                                                 'var': var,
                                                 'std': std}

            # Percentiles (Pxx)
            P10 = cp.Perc(fit, 10, self.sampler.distribution)
            P90 = cp.Perc(fit, 90, self.sampler.distribution)
            results['percentiles'][k] = {'p10': P10, 'p90': P90}

            # First Sobol indices
            # TODO: Implement higher order indices
            logger.warning('Only first order Sobol indices implemented')
            sobol_first_narr = cp.Sens_m(fit, self.sampler.distribution)
            sobol_first_dict = {}
            i_par = 0
            for param_name in self.sampler.vary.get_keys():
                sobol_first_dict[param_name] = sobol_first_narr[i_par]
                i_par += 1
            # 1 here = order
            results['sobol_indices'][k][1] = sobol_first_dict

            # Correlation matrix
            results['correlation_matrices'][k] = cp.Corr(
                fit, self.sampler.distribution)

            # Output distributions
            results['output_distributions'][k] = cp.QoI_Dist(
                fit, self.sampler.distribution)

        return results
