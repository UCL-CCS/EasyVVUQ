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
