import pytest
import chaospy as cp
from easyvvuq.sampling import MCSampler


def test_sampling():
    vary = {'a': cp.Uniform(-5, 0), 'b': cp.Uniform(2, 10)}
    sampler = MCSampler(vary, 100)
    assert (sampler.n_samples() == 400)
    for _ in range(sampler.n_samples()):
        sample = next(sampler)
        assert (sample['a'] >= -5 and sample['a'] <= 0)
        assert (sample['b'] >= 2 and sample['b'] <= 10)
    with pytest.raises(StopIteration):
        next(sampler)


def test_sampling_1D():
    vary = {'a': cp.Uniform(-1, 1)}
    sampler = MCSampler(vary, 100)
    # This used to fail in the saltelli subroutine if there was only 1 input
    for _ in range(sampler.n_samples()):
        sample = next(sampler)
