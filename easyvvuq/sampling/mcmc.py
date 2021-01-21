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
    def __init__(self, init, q, qoi):
        self.init = init
        self.x = init
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
        for i, key in enumerate(self.x.keys()):
            y[key] = y_[i]
        return y

    def update(self, y, f_y, q):
        r = min(1.0, (self.f_y / self.f_x) * q)
        if np.random.random() < r:
            self.x = self.y
            self.y = y
            self.f_x = self.f_x
            self.f_y = f_y

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {"init": self.x}

    def mcmc_sampling(self, campaign, iterations=100):
        """Performs the MCMC sampling procedure on the campaign.

        Parameters
        ----------
        campaign: Campaign
            campaign instance
        iterations: int
            Number of iterations.
        """
        ignored_runs = []
        for _ in range(iterations):
            campaign.draw_samples(1)
            campaign.populate_runs_dir()
            campaign.apply_for_each_run_dir(action)
            campaign.collate()
            result = campaign.get_collation_result()
            last_row = result.iloc[-1]
            y = dict((key, last_row[key][0]) for key in init.keys())
            if self.f_x is None:
                self.f_x = last_row[self.qoi][0]
            else:
                f_y = last_row[self.qoi][0]
                q_xy = self.q(self.y).pdf([self.x[key] for key in self.init.keys()])
                q_yx = self.q(self.x).pdf([y[key] for key in self.init.keys()])
                r = min(1.0, (f_y / self.f_x) * (q_xy / q_yx))
                if r < np.random.random():
                    self.x = y
                    self.f_x = f_y
                else:
                    ignored_runs.append(last_row['id'])
        self.campaign.ignore_runs(ignored_runs)
