import easyvvuq as uq
from .base import BaseSamplingElement
import numpy as np


class MCMCSampler(BaseSamplingElement, sampler_name='mcmc_sampler'):
    """A Metropolis-Hastings MCMC Sampler.

    Parameters
    ----------
    init: dict
       Initial values for each input parameter. Of the form {'input1': value, ...}
    q: function
       A function of one argument X (dictionary) that returns the proposal distribution conditional on
    the X.
    qoi: str
       Name of the quantity of interest
    n_chains: int
       Number of MCMC chains to run in paralle.
    replica_col: str or None
       Name of the replica_id column when used with ReplicaSampler. 
       None when ReplicaSampler is not used.
    estimator: function
       To be used with replica_col argument. Outputs an estimate of some 
       parameter when given a sample array.
    """

    def __init__(self, init, q, qoi, n_chains=1, n_replicas=1,
                 replica_col=None, estimator=None):
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
        if n_replicas != 1:
            assert(replica_col is not None)
            assert(estimator is not None)
        self.n_replicas = n_replicas
        self.replica_col = replica_col
        self.estimator = estimator

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def n_samples(self):
        return self.n_chains

    def __iter__(self):
        self.current_chain = 0
        return self

    def __next__(self):
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

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {"init": self.init}

    def update(self, campaign):
        """Performs the MCMC sampling procedure on the campaign.

        Parameters
        ----------
        campaign: Campaign
            campaign instance

        Returns
        -------
        list of rejected run ids, for testing purposes mainly
        """
        self.stop = False
        result = campaign.get_collation_result()
        last_rows = result.iloc[-self.n_chains * self.n_replicas:]
        ignored_runs = []
        for chain_id, last_row in enumerate(last_rows.iterrows()):
            last_row = last_row[1]
            y = dict([(key, last_row[key][0]) for key in self.inputs])
            if self.f_x[chain_id] is None:
                self.f_x[chain_id] = last_row[self.qoi][0]
            else:
                f_y = last_row[self.qoi][0]
                q_xy = self.q(y).pdf([self.x[chain_id][key] for key in self.inputs])
                q_yx = self.q(self.x[chain_id]).pdf([y[key] for key in self.inputs])
                r = min(1.0, (f_y / self.f_x[chain_id]) * (q_xy / q_yx))
                if np.random.random() < r:
                    self.x[chain_id] = dict(y)
                    self.f_x[chain_id] = f_y
                else:
                    ignored_runs.append(last_row['run_id'][0])
        for run_id in ignored_runs:
            campaign.campaign_db.session.query(uq.db.sql.RunTable).\
                filter(uq.db.sql.RunTable.id == run_id).\
                update({'status': uq.constants.Status.IGNORED})
        return ignored_runs
