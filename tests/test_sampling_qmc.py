import pytest
import chaospy as cp
from easyvvuq.sampling import QMCSampler
from easyvvuq.sampling.base import Vary


def test_init():
    with pytest.raises(RuntimeError):
        QMCSampler({}, 100)
    with pytest.raises(RuntimeError):
        QMCSampler([], 100)


def test_is_finite():
    vary = {'a': cp.Uniform(-5, 3), 'b': cp.Uniform(2, 10)}
    sampler = QMCSampler(vary, 100)
    assert(sampler.is_finite())


def test_is_restartable():
    vary = {'a': cp.Uniform(-5, 3), 'b': cp.Uniform(2, 10)}
    sampler = QMCSampler(vary, 100)
    assert(sampler.is_restartable())


def test_restart_dict():
    vary = {'a': cp.Uniform(-5, 0), 'b': cp.Uniform(2, 10)}
    sampler = QMCSampler(vary, 100)
    for _ in range(10):
        next(sampler)
    restart = sampler.get_restart_dict()
    assert(restart['vary'] == Vary(vary).serialize())
    assert(restart['count'] == 10)
    assert(restart['n_mc_samples'] == 100)


def test_sampling():
    vary = {'a': cp.Uniform(-5, 0), 'b': cp.Uniform(2, 10)}
    sampler = QMCSampler(vary, 100)
    assert(sampler.n_samples == 400)
    for _ in range(sampler.n_samples):
        sample = next(sampler)
        assert(sample['a'] >= -5 and sample['a'] <= 0)
        assert(sample['b'] >= 2 and sample['b'] <= 10)
    with pytest.raises(StopIteration):
        next(sampler)


def test_resume():
    vary = {'a': cp.Uniform(-5, 0), 'b': cp.Uniform(2, 10)}
    sampler = QMCSampler(vary, 100, 390)
    for _ in range(10):
        sample = next(sampler)
    with pytest.raises(StopIteration):
        next(sampler)
