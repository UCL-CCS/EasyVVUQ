import chaospy as cp
import easyvvuq as uq
import pytest


def test_l_n_exception():
    vary = {
        "gravity": cp.Uniform(9.8, 1.0),
        "mass": cp.Uniform(2.0, 10.0),
    }
    with pytest.raises(RuntimeError):
        sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=1, sparse=True)
