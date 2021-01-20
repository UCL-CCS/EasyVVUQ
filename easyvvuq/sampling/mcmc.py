from .base import BaseSamplingElement, Vary
import numpy as np
import chaospy as cp


class MCMCSampler(BaseSamplingElement, sampler_name='mcmc_sampler'):
    def __init__(self, init):
        self.x = init
        self.f_y = None
        self.f_x = None
        self.q_xy = None
        self.q_yx = None

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return False

    def __next__(self):
        if self.f_x is None:
            return self.x
        r = min(1.0, (self.f_y / self.f_x) * (self.q_xy / self.q_yx))
        if np.random.random() < r:
            return self.y
        else:
            return self.x

    def update(self, y, f_y, q_xy, q_yx):
        self.x = self.y
        self.y = y
        self.f_x = self.f_x
        self.f_y = f_y
        self.q_xy = q_xy
        self.q_yx = q_yx

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
