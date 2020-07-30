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
    assert(uq.analysis.sc_analysis.lagrange_poly(2.0, [8, 4, 9], 0) == -3.5)
    assert(uq.analysis.sc_analysis.lagrange_poly(2.0, [8, 4, 9], 1) == 2.0999999999999996)
    assert(uq.analysis.sc_analysis.lagrange_poly(2.0, [8, 4, 9], 2) == 2.4000000000000004)
    with pytest.raises(IndexError):
        uq.analysis.sc_analysis.lagrange_poly(2.0, [8, 4, 9], 3)


def test_compute_marginal():
    files = ['tests/sc/compute_marginal/0b7b64b4dcea4d5797ce270c685408a7.yml',
             'tests/sc/compute_marginal/a2676d2279224b4f91ffb39501be165d.yml',
             'tests/sc/compute_marginal/f480d6dcf4334471937bf64209c21b7d.yml']
    data = []
    for file_ in files:
        with open(file_, 'r') as fd:
            data.append(yaml.load(fd, Loader=yaml.Loader))
    analysis = pickle.load(open('tests/sc/compute_marginal/analysis.p', 'rb'))
    for datum in data:
        h, wi_d_u = analysis.compute_marginal(datum['qoi'], datum['u'],
                                              datum['u_prime'], datum['diff'])
        for index, row in enumerate(h):
            assert((row == datum['h'][index]).all())
        assert((wi_d_u == datum['wi_d_u']).all())


def test_get_sobol_indices():
    file_ = 'tests/sc/sobol_indices/6e1252d0b17f4a328c1320a390135c6a.yml'
    with open(file_, 'r') as fd:
        data = yaml.load(fd, Loader=yaml.Loader)
    analysis = pickle.load(open('tests/sc/compute_marginal/analysis.p', 'rb'))
    sobol = analysis.get_sobol_indices(data['qoi'], data['typ'])
    for key in sobol:
        assert(((sobol[key] == data['sobol'][key]) |
                (np.isnan(sobol[key]) & np.isnan(data['sobol'][key]))).all())
