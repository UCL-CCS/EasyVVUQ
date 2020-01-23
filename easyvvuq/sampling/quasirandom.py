from .base import BaseSamplingElement
import numpy as np
import chaospy as cp

class LHCSampler(BaseSamplingElement, sampler_name='lhc_sampler'):
    def __init__(self, vary=None, order=1):
        """
            Expects dict of var names, and their ranges
        """
        self.vary = vary
        self.samples = np.array([vary[param][0] + row * (vary[param][1] - vary[param][0])
                                     for row, param in
                                     zip(cp.create_latin_hypercube_samples(order=order, dim=len(vary.keys())), vary)])
        self.order = order
        self.dim = len(vary)
        def sample_generator():
            for sample in zip(*self.samples):
                yield {key : value for key, value in zip(vary.keys(), sample)}
        self.sample_generator = sample_generator()

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def __next__(self):
        return next(self.sample_generator)

    def is_restartable(self):
        return False


class HaltonSampler(BaseSamplingElement, sampler_name='halton_sampler'):
    def __init__(self, vary=None, order=1):
        """
            Expects dict of var names, and their ranges
        """
        self.vary = vary
        self.samples = np.array([vary[param][0] + row * (vary[param][1] - vary[param][0])
                                     for row, param in
                                     zip(cp.distributions.sampler.sequences.halton.create_halton_samples(order=order, dim=len(vary.keys())), vary)])
        self.order = order
        self.dim = len(vary)
        def sample_generator():
            for sample in zip(*self.samples):
                yield {key : value for key, value in zip(vary.keys(), sample)}
        self.sample_generator = sample_generator()

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def __next__(self):
        return next(self.sample_generator)

    def is_restartable(self):
        return False
