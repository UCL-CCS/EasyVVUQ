"""Replica Sampler

Summary
-------

Primarily intended for sampling the same paramater values but with
different random seed. Other uses may be possible. It takes a finite
sampler and produces an infinite sampler from it. This infinite
sampler loops through the parameters produced by the finite sampler
and at each cycle adds a unique id number for that cycle to the
parameter dictionary.
"""

from easyvvuq.sampling import BaseSamplingElement
from itertools import cycle


class ReplicaSampler(BaseSamplingElement, sampler_name='replica_sampler'):
    """Replica Sampler

    Parameters
    ----------
    sampler : an instance of a class derived from  BaseSamplingElement
        a finite sampler to loop over

    ensemble_col : string
        a parameter name for the ensemble id
    """

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
        self.counter = 0

    def is_finite(self):
        return False

    def element_version(self):
        return '0.1'

    def n_samples(self):
        raise RuntimeError("You can't get the number of samples in an infinite sampler")

    def __next__(self):
        params = dict(next(self.cycle))
        params[self.ensemble_col] = self.counter
        self.counter = (self.counter + 1) % self.size
        return params

    def is_restartable(self):
        return False
