"""
Summary
-------
This module provides classes based on RandomSampler but modified in such a way
that the output of the sampler is not random but is meant to be used in place
of uniformly random number sequences. Usually this is used to cover the sampling
space more "evenly" than a uniform random distribution would. Two methods are
implemented:

https://en.wikipedia.org/wiki/Latin_hypercube_sampling
https://en.wikipedia.org/wiki/Halton_sequence

"""


from .random import RandomSampler
import numpy as np
import chaospy as cp


class LHCSampler(RandomSampler, sampler_name='lhc_sampler'):
    def __next__(self):
        if self.is_finite():
            if self.count >= self.max_num:
                raise StopIteration

        run_dict = {}
        for param_name, dist in self.vary.get_items():
            run_dict[param_name] = dist.sample(1, rule='L')[0]

        self.count += 1
        return run_dict


class HaltonSampler(RandomSampler, sampler_name='halton_sampler'):
    def __next__(self):
        if self.is_finite():
            if self.count >= self.max_num:
                raise StopIteration

        run_dict = {}
        for param_name, dist in self.vary.get_items():
            run_dict[param_name] = dist.sample(1, rule='H')[0]

        self.count += 1
        return run_dict
