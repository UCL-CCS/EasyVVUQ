from easyvvuq.sampling.sampler_of_samplers import MultiSampler
from easyvvuq.sampling.sweep import BasicSweep
import pytest
import unittest.mock as mock


@pytest.fixture
def multi_sampler():
    sampler1 = mock.MagicMock()
    sampler2 = mock.MagicMock()
    sampler1.is_finite.return_value = True
    sampler2.is_finite.return_value = True
    multi_sampler = MultiSampler(sampler1, sampler2)
    return multi_sampler


def test_init_exceptions():
    # All samplers must be finite
    sampler1 = mock.MagicMock()
    sampler2 = mock.MagicMock()
    sampler1.is_finite.return_value = True
    sampler2.is_finite.return_value = False
    with pytest.raises(RuntimeError):
        multi_sampler = MultiSampler(sampler1, sampler2)
    with pytest.raises(RuntimeError):
        MultiSampler()


def test_element_version(multi_sampler):
    assert(isinstance(multi_sampler.element_version(), str))


def test_is_finite(multi_sampler):
    assert(multi_sampler.is_finite())


def test_n_samples():
    sampler1 = BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]})
    sampler2 = BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]})
    multi = MultiSampler(sampler1, sampler2)
    assert(multi.n_samples() == 81)


def test_iterator():
    def popper(values):
        if len(values):
            values.pop()
        else:
            raise StopIteration
    sampler1 = mock.MagicMock()
    values1 = [3, 2, 1]
    sampler1.__next__.return_value = values1[-1]
    sampler1.__next__.side_effect = popper(values1)
    sampler2 = mock.MagicMock()
    values2 = [3, 2, 1]
    sampler2.__next__.return_value = values2[-1]
    sampler2.__next__.side_effect = popper(values2)
    sampler1.is_finite.return_value = True
    sampler2.is_finite.return_value = True


def test_is_restartable(multi_sampler):
    assert(multi_sampler.is_restartable())


def test_get_restart_dict(multi_sampler):
    assert(isinstance(multi_sampler.get_restart_dict(), dict))
