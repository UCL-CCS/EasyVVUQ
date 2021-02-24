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

    replica_col : string
        a parameter name for the replica id
    """

    def __init__(self, sampler, replica_col='replica_id', replicas=0):
        if not sampler.is_finite():
            raise RuntimeError("Replica sampler only works with finite samplers")
        self.sampler = sampler
        self.replica_col = replica_col
        self.replicas = replicas
        self.history = []
        for sample in sampler:
            self.history.append(sample)
        self.size = len(self.history)
        self.cycle = cycle(self.history)
        self.counter = 0

    def is_finite(self):
        if self.replicas == 0:
            return False
        else:
            return True

    def element_version(self):
        return '0.1'

    def n_samples(self):
        if self.replicas == 0:
            raise RuntimeError("You can't get the number of samples in an infinite sampler")
        else:
            return self.replicas * self.sampler.n_samples()

    def __next__(self):
        params = dict(next(self.cycle))
        params[self.replica_col] = self.counter
        self.counter = (self.counter + 1) % self.size
        return params

    def is_restartable(self):
        return False
