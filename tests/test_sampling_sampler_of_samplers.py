from easyvvuq.sampling.sampler_of_samplers import MultiSampler
import pytest
import unittest.mock as mock


def test_init_exceptions():
    # All samplers must be finite
    sampler1 = mock.MagicMock()
    sampler2 = mock.MagicMock()
    sampler1.is_finite.return_value = True
    sampler2.is_finite.return_value = False
    with pytest.raises(RuntimeError):
        multi_sampler = MultiSampler(sampler1, sampler2)
