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
    seed_col : string
        a parameter name for the input parameter that specifies the RNG seed
    replicas : int
        number of replicas, if zero will result in an infinite sampler
    """

    def __init__(self, sampler, replica_col='ensemble_id', seed_col=None, replicas=0):
        if not sampler.is_finite():
            raise RuntimeError("Replica sampler only works with finite samplers")
        self.sampler = sampler
        self.replica_col = replica_col
        self.replicas = replicas
        self.sampler.n_replicas = replicas
        self.reset()

    def reset(self):
        self.history = []
        for sample in self.sampler:
            self.history.append(sample)
        self.size = len(self.history)
        self.cycle = cycle(self.history)
        self.counter = 0
        if isinstance(self.sampler.n_samples, int):
            self.total_counter = self.replicas * self.sampler.n_samples
        else:
            self.total_counter = self.replicas * self.sampler.n_samples()

    def is_finite(self):
        if self.replicas == 0:
            return False
        else:
            return True

    def n_samples(self):
        if self.replicas == 0:
            raise RuntimeError("You can't get the number of samples in an infinite sampler")
        else:
            return self.replicas * self.sampler.n_samples()

    def __next__(self):
        if self.replicas != 0:
            self.total_counter -= 1
            if self.total_counter < 0:
                raise StopIteration
        params = dict(next(self.cycle))
        params[self.replica_col] = self.counter
        self.counter = (self.counter + 1) % self.size
        return params

    def update(self, result, invalid):
        self.reset()
        return self.sampler.update(result, invalid)

    @property
    def iteration(self):
        return self.sampler.iteration

    @property
    def analysis_class(self):
        return self.sampler.analysis_class

    @property
    def inputs(self):
        return self.sampler.inputs

    @property
    def qoi(self):
        return self.sampler.qoi
