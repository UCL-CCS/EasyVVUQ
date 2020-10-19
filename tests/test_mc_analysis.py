import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import pytest
import logging
import pandas as pd
from tests.sc.sobol_model import sobol_g_func


def exact_sobols_g_func(d=2, a=[0.0, 0.5, 3.0, 9.0, 99.0]):
    # for the Sobol g function, the exact (1st-order)
    # Sobol indices are known analytically
    V_i = np.zeros(d)
    for i in range(d):
        V_i[i] = 1.0 / (3.0 * (1 + a[i])**2)
    V = np.prod(1 + V_i) - 1
    logging.debug('Exact 1st-order Sobol indices: ', V_i / V)
    return V_i / V


# author: Wouter Edeling
__license__ = "LGPL"

HOME = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def data():
    # fix random seed to make this test deterministic
    np.random.seed(10000000)
    # Create the sampler
    vary = {
        "x1": cp.Uniform(0.0, 1.0),
        "x2": cp.Uniform(0.0, 1.0)
    }
    # Select the MC sampler
    mc_sampler = uq.sampling.MCSampler(vary, n_mc_samples=100)
    data = []
    for run_id, sample in enumerate(mc_sampler):
        data.append({
            'run_id': run_id,
            'x1': sample['x1'],
            'x2': sample['x2'],
            'f': sobol_g_func([sample['x1'], sample['x2']], d=2)
        })

    df = pd.DataFrame(data)
    return mc_sampler, df


@pytest.fixture
def results(data):
    # Post-processing analysis
    mc_sampler, df = data
    analysis = uq.analysis.QMCAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    results = analysis.analyse(df)
    return results


def test_mc_analysis(results):
    # analytic Sobol indices
    ref_sobols = exact_sobols_g_func()
    sobol_x1 = results._get_sobols_first('f', 'x1')
    sobol_x2 = results._get_sobols_first('f', 'x2')
    assert sobol_x1 == pytest.approx(ref_sobols[0], abs=0.1)
    assert sobol_x2 == pytest.approx(ref_sobols[1], abs=0.1)


def test_sobol_bootstrap(data):
    mc_sampler, df = data
    analysis = uq.analysis.QMCAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    s1, s1_conf, st, st_conf = analysis.sobol_bootstrap(list(df['f']))
    assert(s1['x1'] == pytest.approx(0.5569058947880715, 0.01))
    assert(s1['x2'] == pytest.approx(0.20727553481694053, 0.01))
    assert(st['x1'] == pytest.approx(0.8132793654841785, 0.01))
    assert(st['x2'] == pytest.approx(0.3804962894947435, 0.01))
    assert(s1_conf['x1']['low'][0] == pytest.approx(0.14387035, 0.01))
    assert(s1_conf['x1']['high'][0] == pytest.approx(0.89428774, 0.01))
    assert(s1_conf['x2']['low'][0] == pytest.approx(-0.11063341, 0.01))
    assert(s1_conf['x2']['high'][0] == pytest.approx(0.46752829, 0.01))
    assert(st_conf['x1']['low'][0] == pytest.approx(0.61368887, 0.01))
    assert(st_conf['x1']['high'][0] == pytest.approx(1.01858671, 0.01))
    assert(st_conf['x2']['low'][0] == pytest.approx(0.24361207, 0.01))
    assert(st_conf['x2']['high'][0] == pytest.approx(0.49214117, 0.01))


def test_separate_output_values(data):
    mc_sampler, df = data
    analysis = uq.analysis.QMCAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    f_M2, f_M1, f_Ni = analysis._separate_output_values(df['f'], 2, 100)
    assert(f_M2.shape == (100,))
    assert(f_M1.shape == (100,))
    assert(f_Ni.shape == (100, 2))


def test_get_samples(data):
    pass
