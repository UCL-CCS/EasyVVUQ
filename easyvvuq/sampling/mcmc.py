from .base import BaseSamplingElement, Vary
import numpy as np
import chaospy as cp


class MCMCSampler(BaseSamplingElement, sampler_name='mcmc_sampler'):
    def __init__(self):
        pass

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def n_samples(self):
        return 1

    def __next__(self):
        return 0.0

    def update(self, y1, y2, q1, q2):
        pass

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {"vary": self.vary.serialize(), "prev": self.prev, "qoi": qoi}
