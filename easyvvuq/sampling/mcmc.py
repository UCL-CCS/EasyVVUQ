from .base import BaseSamplingElement
import numpy as np
import os

class MCMCSampler(BaseSamplingElement, sampler_name='mcmc_sampler'):
    """A Metropolis-Hastings MCMC Sampler.

    Parameters
    ----------
    init: dict
       Initial values for each input parameter. Of the form {'input1': value, ...}
    q: function
       A function of one argument X (dictionary) that returns the proposal distribution conditional on
       the `X`.
    qoi: str
       Name of the quantity of interest
    n_chains: int
       Number of MCMC chains to run in paralle.
    estimator: function
       To be used with replica_col argument. Outputs an estimate of some
       parameter when given a sample array.
    """

    def __init__(self, init, q, qoi, n_chains=1, likelihood=lambda x: x[0], estimator=None):
        for param in init:
            if not hasattr(init[param], '__iter__'):
                raise RuntimeError(
                    'all input intializations should be iterables of same length as there are chains')
            if len(init[param]) != n_chains:
                raise RuntimeError(
                    'initialization dictionary should have separate values for each chain')
        self.init = dict(init)
        self.inputs = list(self.init.keys())
        for input_ in self.inputs:
            if len(self.init[input_]) != n_chains:
                raise RuntimeError("The init dictionary must contains the same number \
                                    of values for each input as there are chains.")
        self.n_chains = n_chains
        self.x = []
        self.q = q
        self.qoi = qoi
        self.current_chain = 0
        for chain in range(self.n_chains):
            self.x.append(dict([(key, self.init[key][chain]) for key in self.inputs]))
            self.x[chain]['chain_id'] = chain
        self.f_x = [None] * n_chains
        self.stop = False
        self.likelihood = lambda x: np.exp(likelihood(x))
        self.n_replicas = None
        self.estimator = estimator
        self.acceptance_ratios = []
        self.iteration = 0

    def is_finite(self):
        return True

    def n_samples(self):
        return self.n_chains

    def __iter__(self):
        self.current_chain = 0
        return self

    def __next__(self):
        """Returns next MCMC sample.

        Returns
        -------
        dict
           A dictionary where keys are input variables names and values are input values.
        """
        if self.stop:
            raise StopIteration
        if self.f_x[self.current_chain] is None:
            try:
                return self.x[self.current_chain]
            finally:
                self.current_chain = (self.current_chain + 1) % self.n_chains
                if self.current_chain == 0:
                    self.stop = True
        y = {}
        y_ = self.q(self.x[self.current_chain]).sample()
        for i, key in enumerate(self.inputs):
            y[key] = y_[i][0]
        y['chain_id'] = self.current_chain
        self.current_chain = (self.current_chain + 1) % self.n_chains
        if self.current_chain == 0:
            self.stop = True
        return y

    def update(self, result, invalid):
        """Performs the MCMC sampling procedure on the campaign.

        Parameters
        ----------
        result: pandas DataFrame
            run information from previous iteration (same as collation DataFrame)
        invalid: pandas DataFrame
            invalid run information (runs that cannot be executed for some reason)

        Returns
        -------
        list of rejected run ids
        """
        self.stop = False
        if (self.estimator is not None) and (len(result) > 0):
            result_grouped = result.groupby(('chain_id', 0)).apply(self.estimator)
        else:
            result_grouped = result
        if (self.estimator is not None) and (len(invalid) > 0):
            invalid_grouped = invalid.groupby(('chain_id', 0)).apply(lambda x: x.mean())
        else:
            invalid_grouped = invalid
        ignored_chains = []
        ignored_runs = []
        # process normal runs
        for row in result_grouped.iterrows():
            row = row[1]
            chain_id = int(row['chain_id'].values[0])
            y = dict([(key, row[key][0]) for key in self.inputs])
            if self.f_x[chain_id] is None:
                self.f_x[chain_id] = self.likelihood(row[self.qoi].values)
            else:
                f_y = self.likelihood(row[self.qoi].values)
                q_xy = self.q(y).pdf([self.x[chain_id][key] for key in self.inputs])
                q_yx = self.q(self.x[chain_id]).pdf([y[key] for key in self.inputs])
                if self.f_x[chain_id] == 0.0:
                    r = 1.0
                else:
                    r = min(1.0, (f_y / self.f_x[chain_id]) * (q_xy / q_yx))
                if np.random.random() < r:
                    self.x[chain_id] = dict(y)
                    self.f_x[chain_id] = f_y
                else:
                    ignored_chains.append(chain_id)
        for row in invalid_grouped.iterrows():
            row = row[1]
            chain_id = int(row['chain_id'].values[0])
            ignored_chains.append(chain_id)
        for chain_id in ignored_chains:
            try:
                ignored_runs += list(result.loc[result[('chain_id', 0)]
                                                == chain_id]['run_id'].values)
            except KeyError:
                if os.getenv("EasyVVUQ_Debug"): print('KeyError raised and ignored')
            try:
                ignored_runs += list(invalid.loc[invalid[('chain_id', 0)]
                                                 == chain_id]['run_id'].values)
            except KeyError:
                if os.getenv("EasyVVUQ_Debug"): print('KeyError raised and ignored')
        ignored_runs = [run[0] for run in ignored_runs]
        self.iteration += 1
        return ignored_runs

    @property
    def analysis_class(self):
        """Returns a corresponding analysis class for this sampler.

        Returns
        -------
        class
        """
        from easyvvuq.analysis import MCMCAnalysis
        return MCMCAnalysis
