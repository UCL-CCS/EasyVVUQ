from easyvvuq.sampling import BaseSamplingElement
from itertools import cycle


class ReplicaSampler(BaseSamplingElement, sampler_name='replica_sampler'):
    def __init__(self, sampler, ensemble_col='ensemble'):
        if not sampler.is_finite():
            raise RuntimeError("Replica sampler only works with finite samplers")
        self.sampler = sampler
        self.ensemble_col = ensemble_col
        self.history = []
        for sample in sampler:
            self.history.append(sample)
        self.size = len(self.history)
        self.cycle = cycle(self.history)
        self.ensemble = 0
        self.counter = 0

    def is_finite(self):
        return False

    def element_version(self):
        return '0.1'

    def n_samples(self):
        raise RuntimeError("You can't get the number of samples in an infinite sampler")

    def __next__(self):
        params = dict(next(self.cycle))
        if self.counter < self.size - 1:
            self.counter += 1
        else:
            self.counter = 0
            self.ensemble += 1
        params[self.ensemble_col] = self.ensemble
        return params

    def is_restartable(self):
        return False
