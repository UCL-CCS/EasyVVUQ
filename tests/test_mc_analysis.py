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
    sampler = uq.sampling.MCSampler(vary, n_mc_samples=100)
    data = {('run_id', 0): [], ('x1', 0): [], ('x2', 0): [], ('f', 0): []}
    for run_id, sample in enumerate(sampler):
        data[('run_id', 0)].append(run_id)
        data[('x1', 0)].append(sample['x1'])
        data[('x2', 0)].append(sample['x2'])
        data[('f', 0)].append(sobol_g_func([sample['x1'], sample['x2']], d=2))
    df = pd.DataFrame(data)
    return sampler, df


@pytest.fixture
def results(data):
    # Post-processing analysis
    mc_sampler, df = data
    analysis = uq.analysis.QMCAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    results = analysis.analyse(df)
    return results

@pytest.fixture
def results_vectors(data_vectors):
    # Post-processing analysis
    mc_sampler, df = data_vectors
    analysis = uq.analysis.QMCAnalysis(sampler=mc_sampler, qoi_cols=['g', 'h'])
    results = analysis.analyse(df)
    return results

@pytest.fixture
def data_vectors():
    np.random.seed(10000000)
    vary = {
        "x1": cp.Uniform(0.0, 1.0),
        "x2": cp.Uniform(0.0, 1.0)
    }
    sampler = uq.sampling.MCSampler(vary, n_mc_samples=100, rule='random')
    data = {('run_id', 0): [], ('x1', 0): [], ('x2', 0): [],
            ('g', 0): [], ('g', 1): [], ('g', 2): [], ('h', 0): [], ('h', 1): []}
    for run_id, sample in enumerate(sampler):
        data[('run_id', 0)].append(run_id)
        data[('x1', 0)].append(sample['x1'])
        data[('x2', 0)].append(sample['x2'])
        data[('g', 0)].append(sample['x1'])
        data[('g', 1)].append(sample['x2'])
        data[('g', 2)].append(sample['x1'] + sample['x2'])
        data[('h', 0)].append(sample['x1'] * sample['x2'])
        data[('h', 1)].append(sample['x1'] ** sample['x2'])
    df = pd.DataFrame(data)
    return sampler, df


def test_mc_analysis(results):
    # analytic Sobol indices
    ref_sobols = exact_sobols_g_func()
    sobol_x1 = results._get_sobols_first('f', 'x1')
    sobol_x2 = results._get_sobols_first('f', 'x2')
    assert sobol_x1 == pytest.approx(ref_sobols[0], abs=0.15)
    assert sobol_x2 == pytest.approx(ref_sobols[1], abs=0.15)


def test_sobol_bootstrap(data):
    mc_sampler, df = data
    analysis = uq.analysis.QMCAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    s1, s1_conf, st, st_conf = analysis.sobol_bootstrap(df['f'])
    print('================================')
    print(s1)
    assert (s1['x1'] == pytest.approx(0.52678798, 0.01))
    assert (s1['x2'] == pytest.approx(0.21411798, 0.01))
    assert (st['x1'] == pytest.approx(0.76100627, 0.01))
    assert (st['x2'] == pytest.approx(0.31407034, 0.01))
    assert (s1_conf['x1']['low'][0] == pytest.approx(0.09359582, 0.01))
    assert (s1_conf['x1']['high'][0] == pytest.approx(0.90002346, 0.01))
    # assert (s1_conf['x2']['low'][0] == pytest.approx(-0.11063341, 0.01))
    # assert (s1_conf['x2']['high'][0] == pytest.approx(0.46752829, 0.01))
    # assert (st_conf['x1']['low'][0] == pytest.approx(0.61368887, 0.01))
    # assert (st_conf['x1']['high'][0] == pytest.approx(1.01858671, 0.01))
    # assert (st_conf['x2']['low'][0] == pytest.approx(0.24361207, 0.01))
    # assert (st_conf['x2']['high'][0] == pytest.approx(0.49214117, 0.01))


def test_separate_output_values(data):
    mc_sampler, df = data
    analysis = uq.analysis.QMCAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    f_M2, f_M1, f_Ni = analysis._separate_output_values(df['f'], 2, 100)
    assert (f_M2.shape == (100, 1))
    assert (f_M1.shape == (100, 1))
    assert (f_Ni.shape == (100, 2, 1))


def test_get_samples(data):
    pass

def test_describe(results_vectors):

    assert (results_vectors.describe(qoi='g', statistic='mean')[0] == pytest.approx(0.44925539, 0.01))
    assert (results_vectors.describe(qoi='g', statistic='mean')[1] == pytest.approx(0.48683778, 0.01))
    assert (results_vectors.describe(qoi='g', statistic='mean')[2] == pytest.approx(0.93609317, 0.01))
                 
    assert (isinstance(results_vectors.describe('h', 'std'), np.ndarray))
