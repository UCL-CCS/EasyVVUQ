from easyvvuq.sampling import ReplicaSampler
from easyvvuq.sampling import BasicSweep
from easyvvuq.sampling import EmptySampler
import pytest


@pytest.fixture
def replica_sampler():
    return ReplicaSampler(BasicSweep({'a': [1, 2], 'b': [3, 4]}))


def test_infite_exception():
    with pytest.raises(RuntimeError):
        ReplicaSampler(EmptySampler())


def test_is_finite(replica_sampler):
    assert(not replica_sampler.is_finite())


def test_element_version(replica_sampler):
    assert(replica_sampler.element_version() == '0.1')


def test_n_samples(replica_sampler):
    with pytest.raises(RuntimeError):
        replica_sampler.n_samples()


def test_replica_sampler_ensemble(replica_sampler):
    params = next(replica_sampler)
    assert(params == {'a': 1, 'b': 3, 'ensemble': 0})
    params = next(replica_sampler)
    assert(params == {'a': 1, 'b': 4, 'ensemble': 1})
    params = next(replica_sampler)
    assert(params == {'a': 2, 'b': 3, 'ensemble': 2})
    params = next(replica_sampler)
    assert(params == {'a': 2, 'b': 4, 'ensemble': 3})
    params = next(replica_sampler)
    assert(params == {'a': 1, 'b': 3, 'ensemble': 0})
    params = next(replica_sampler)
    assert(params == {'a': 1, 'b': 4, 'ensemble': 1})
