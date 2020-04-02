from easyvvuq.sampling.sampler_of_samplers import MultiSampler
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


def test_iterator():
    pass


def test_is_restartable(multi_sampler):
    assert(multi_sampler.is_restartable())


def test_get_restart_dict():
    pass
