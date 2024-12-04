import chaospy as cp
import easyvvuq as uq
import pytest
import yaml
import pickle
import numpy as np

# No longer required
# def test_l_n_exception():
#     vary = {
#         "gravity": cp.Uniform(9.8, 1.0),
#         "mass": cp.Uniform(2.0, 10.0),
#     }
#     with pytest.raises(RuntimeError):
#         sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=1, sparse=True)


def test_lagrange_poly():
    assert (uq.analysis.sc_analysis.lagrange_poly(2.0, [8, 4, 9], 0) == -3.5)
    assert (uq.analysis.sc_analysis.lagrange_poly(2.0, [8, 4, 9], 1) == 2.0999999999999996)
    assert (uq.analysis.sc_analysis.lagrange_poly(2.0, [8, 4, 9], 2) == 2.4000000000000004)
    with pytest.raises(IndexError):
        uq.analysis.sc_analysis.lagrange_poly(2.0, [8, 4, 9], 3)
