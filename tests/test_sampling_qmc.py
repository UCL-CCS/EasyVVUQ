import pytest
import chaospy as cp
from easyvvuq.sampling import QMCSampler


def test_init():
    with pytest.raises(RuntimeError):
        QMCSampler({}, 128)
    with pytest.raises(RuntimeError):
        QMCSampler([], 128)


def test_is_finite():
    vary = {'a': cp.Uniform(-5, 3), 'b': cp.Uniform(2, 10)}
    sampler = QMCSampler(vary, 128)
    assert (sampler.is_finite())


def test_sampling():
    vary = {'a': cp.Uniform(-5, 0), 'b': cp.Uniform(2, 10)}
    sampler = QMCSampler(vary, 128)
    assert (sampler.n_samples == 512)
    for _ in range(sampler.n_samples):
        sample = next(sampler)
        assert (sample['a'] >= -5 and sample['a'] <= 0)
        assert (sample['b'] >= 2 and sample['b'] <= 10)
    with pytest.raises(StopIteration):
        next(sampler)


def test_resume():
    vary = {'a': cp.Uniform(-5, 0), 'b': cp.Uniform(2, 10)}
    sampler = QMCSampler(vary, 128, 500)
    for _ in range(12):
        sample = next(sampler)
    with pytest.raises(StopIteration):
        next(sampler)
