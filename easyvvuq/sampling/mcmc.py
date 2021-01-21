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
    """
    def __init__(self, init, q):
        self.x = init
        self.q = q

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return False

    def __next__(self):
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

    def mcmc_sampling(self, campaign, init, q_xy, q_yx, iterations=100):
        """Performs the MCMC sampling procedure on the campaign.

        Parameters
        ----------
        campaign: Campaign
            campaign instance
        init: dict
            Initial input parameter values. A dictionary where keys are input parameter names and
            values are initial values for those parameters.
        q_xy: function
            A python function that takes as inputs two dictionaries and returns a float.
        q_yx: function
            A python function that takes as inputs two dictionaries and returns a float.
        iterations: int
            Number of iterations.
        """
        for _ in range(iterations):
            campaign.draw_samples(1)
            campaign.populate_runs_dir()
            campaign.apply_for_each_run_dir(action)
            campaign.collate()
            result = campaign.get_collation_result()
            last_row = result.iloc[-1]
            y = dict((key, last_row[key][0]) for key in init.keys())
            self.update(y, last_row[qoi][0], q_xy(self.x, y), q_yx(self.x, y))
