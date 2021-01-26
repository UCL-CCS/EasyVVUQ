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
        self.x = dict(init)
        self.f_x = None
        self.q = q
        self.qoi = qoi

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return False

    def __next__(self):
        if self.f_x is None:
            return self.x
        y = {}
        y_ = self.q(self.x).sample()
        for i, key in enumerate(self.init.keys()):
            y[key] = y_[i][0]
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
            campaign.draw_samples(1)
            campaign.populate_runs_dir()
            campaign.apply_for_each_run_dir(action)
            campaign.collate()
            result = campaign.get_collation_result()
            last_row = result.iloc[-1]
            y = dict((key, last_row[key][0]) for key in self.init.keys())
            if self.f_x is None:
                self.f_x = last_row[self.qoi][0]
            else:
                f_y = last_row[self.qoi][0]
                q_xy = self.q(y).pdf([self.x[key] for key in self.init.keys()])
                q_yx = self.q(self.x).pdf([y[key] for key in self.init.keys()])
                r = min(1.0, (f_y / self.f_x) * (q_xy / q_yx))
                if np.random.random() < r:
                    self.x = dict(y)
                    self.f_x = f_y
                else:
                    ignored_runs.append(last_row['run_id'][0])
        campaign.ignore_runs(ignored_runs)
        return ignored_runs
