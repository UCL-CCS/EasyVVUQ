import easyvvuq as uq
from .base import BaseSamplingElement, Vary
import numpy as np
import chaospy as cp


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
    """
    def __init__(self, init, q, qoi, n_chains=1):
        self.init = dict(init)
        self.inputs = list(self.init.keys())
        self.n_chains = n_chains
        self.x = []
        for chain in range(self.n_chains):
            self.x.append(dict([(key, self.init[key][chain]) for key in self.inputs]))
        self.f_x = [None] * n_chains
        self.q = q
        self.qoi = qoi
        self.current_chain = 0

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return False

    def __next__(self):
        if self.f_x[self.current_chain] is None:
            return self.x[self.current_chain]
        y = {}
        y_ = self.q(self.x[self.current_chain]).sample()
        for i, key in enumerate(self.inputs):
            y[key] = y_[i][0]
        self.current_chain = (self.current_chain + 1) % self.current_chain
        return y

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {"init": self.init}

    def mcmc_sampling(self, campaign, action, iterations=100):
        """Performs the MCMC sampling procedure on the campaign.

        Parameters
        ----------
        campaign: Campaign
            campaign instance
        action: BaseAction
            An action to be executed for each sample.
        iterations: int
            Number of iterations.

        Returns
        -------
        list of rejected run ids, for testing purposes mainly
        """
        ignored_runs = []
        for _ in range(iterations):
            campaign.draw_samples(self.n_chains)
            campaign.populate_runs_dir()
            campaign.apply_for_each_run_dir(action)
            campaign.collate()
            result = campaign.get_collation_result()
            last_rows = result.iloc[-self.n_chains:]
            for chain_id, last_row in enumerate(last_rows.iterrows()):
                y = dict((key, last_row[key][0]) for key in self.inputs)
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
