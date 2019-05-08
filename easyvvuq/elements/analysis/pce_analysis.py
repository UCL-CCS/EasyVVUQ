import chaospy as cp
from easyvvuq import OutputType
from .base import BaseAnalysisElement

# author: Jalal Lakhlili
__license__ = "LGPL"

# TODO:
# 1. Add pd.read_hdf (https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-hdf5).
# 2. Add STORE flag (False by default) to allow the user to store output_file or no.
# 3. Test cp.fit_regression to approximate solver.


class PCEAnalysis(BaseAnalysisElement):

    def element_name(self):
        return "PCE_Analysis"

    def element_version(self):
        return "0.3"

    def __init__(self, params_cols=None, sampler=None):

        if sampler is None:
            msg = 'PCE analysis requires a paired sampler to be passed'
            raise RuntimeError(msg)

        self.params_cols = params_cols
        self.output_type = OutputType.SUMMARY
        self.sampler = sampler

        self._statistical_moments = {}
        self._percentiles = {}
        self._sobol_indices = {}
        self._correlation_matrices = {}
        self._output_distributions = {}

    def analyse(self, data_frame=None, qoi_cols=None):

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")

        if qoi is None:
            raise RuntimeError("Analysis element requires a list of "
                               "quantities of interest (qoi)")

        # TODO: refactor the rest of this

        # Get the Polynomial
        P = self.sampler.P

        # Compute nodes and weights
        nodes, weights = cp.generate_quadrature(order=self.sampler.quad_order,
                                                domain=self.sampler.distribution,
                                                rule=self.sampler.quad_rule,
                                                sparse=self.sampler.quad_sparse)

        # Extract output values for each quantity of interest from Dataframe
        samples = {k: [] for k in qoi_cols}
        for i in range(self.campaign.run_number):
            for k in qoi_cols:
                values = data_frame.loc[data_frame['run_id'] == 'Run_' + str(i)][k].to_numpy()
                samples[k].append(values)

        output_distributions = {}

        # Compute descriptive statistics for each quantity of interest
        for k in qoi_cols:
            # Approximation solver
            fit = cp.fit_quadrature(P, nodes, weights, samples[k])

            # Statistical moments
            mean = cp.E(fit, self.sampler.distribution)
            var = cp.Var(fit, self.sampler.distribution)
            std = cp.Std(fit, self.sampler.distribution)
            self._statistical_moments[k] = {'mean': mean,
                                            'var': var,
                                            'std': std}

            # Percentiles (Pxx)
            P10 = cp.Perc(fit, 10, self.sampler.distribution)
            P90 = cp.Perc(fit, 90, self.sampler.distribution)
            self._percentiles[k] = {'p10': P10, 'p90': P90}

            # First Sobol indices
            sobol_first_narr = cp.Sens_m(fit, self.sampler.distribution)
            sobol_first_dict = {}
            i_par = 0
            for param_name in self.sampler.vary.keys():
                sobol_first_dict[param_name] = sobol_first_narr[i_par]
                i_par += 1
            self._sobol_indices[k] = sobol_first_dict

            # Correlation matrix
            self._correlation_matrices[k] = cp.Corr(fit, self.sampler.distribution)

            # Ouput distributions
            output_distributions[k] = cp.QoI_Dist(fit, self.sampler.distribution)

        return

    # Descriptive statistics
    def statistical_moments(self, qoi):
        """
        Returns a dictionary object containing mean, variation and standard deviation
        of the given quantity of interset.
        keys: 'mean', 'var' and 'std'
        values: ndarrays
        """

        if qoi not in self._statistical_moments:
            raise NameError("Unknown quantity of interset " + qoi)

        return self._statistical_moments[qoi]

    def percentiles(self, qoi):
        """
        Returns a dictionary object containing 10% and 90% percentiles
        of the given quantity of interset.
        keys: 'p10' and 'p90'
        values: ndarrays
        """

        if qoi not in self._percentiles:
            raise NameError("Unknown quantity of interest " + qoi)

        return self._percentiles[qoi]

    def sobol_indices(self, qoi, typ):
        """
        Returns a dictionary object containing the sobol indices of the given quantity of interest
        for each uncertain parameter (typ='first_order').
        keys: uncertain parameters names
        values: ndarray
        """

        if qoi not in self._sobol_indices:
            raise NameError("Unknown quantity of interest " + qoi)

        if typ == 'first_order':
            return self._sobol_indices[qoi]
        else:
            raise RuntimeError('Calculation of higher order '
                               'indices not implemented')

    def correlation_matrix(self, qoi):
        """
        Returns the correlation matrix of the given quantity of interest.
        """

        if qoi not in self._correlation_matrices:
            raise NameError("Unknown quantity of interest " + qoi)

        return self._correlation_matrices[qoi]

    def output_distributions(self, qoi):
        """
        Returns the constructed quantity of interest distributions.
        """

        if qoi not in self._output_distributions:
            raise NameError("Unknown quantity of interest " + qoi)

        return self._output_distributions[qoi]
