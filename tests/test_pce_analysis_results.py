import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import pytest
import logging
import pandas as pd
import math
from tests.sc.sobol_model import sobol_g_func
from easyvvuq.analysis.pce_analysis import PCEAnalysisResults


def exact_sobols_g_func(d=2, a=[0.0, 0.5, 3.0, 9.0, 99.0]):
    # for the Sobol g function, the exact (1st-order)
    # Sobol indices are known analytically
    V_i = np.zeros(d)
    for i in range(d):
        V_i[i] = 1.0 / (3.0 * (1 + a[i])**2)
    V = np.prod(1 + V_i) - 1
    logging.debug('Exact 1st-order Sobol indices: ', V_i / V)
    return V_i / V


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
    sampler = uq.sampling.PCESampler(vary)
    data = {('run_id', 0): [], ('x1', 0): [], ('x2', 0): [], ('f', 0): []}
    for run_id, sample in enumerate(sampler):
        data[('run_id', 0)].append(run_id)
        data[('x1', 0)].append(sample['x1'])
        data[('x2', 0)].append(sample['x2'])
        data[('f', 0)].append(sobol_g_func([sample['x1'], sample['x2']], d=2))
    df = pd.DataFrame(data)
    return sampler, df


@pytest.fixture
def data_vectors():
    np.random.seed(10000000)
    vary = {
        "x1": cp.Uniform(0.0, 1.0),
        "x2": cp.Uniform(0.0, 1.0)
    }
    sampler = uq.sampling.SCSampler(vary)
    data = {('run_id', 0): [], ('x1', 0): [], ('x2', 0): [],
            ('g', 0): [], ('g', 1): [], ('g', 2): []}
    for run_id, sample in enumerate(sampler):
        data[('run_id', 0)].append(run_id)
        data[('x1', 0)].append(sample['x1'])
        data[('x2', 0)].append(sample['x2'])
        data[('g', 0)].append(sample['x1'])
        data[('g', 1)].append(sample['x2'])
        data[('g', 2)].append(sample['x1'] + sample['x2'])
    df = pd.DataFrame(data)
    return sampler, df


@pytest.fixture
def results(data):
    # Post-processing analysis
    mc_sampler, df = data
    analysis = uq.analysis.PCEAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    results = analysis.analyse(df)
    return results


@pytest.fixture
def results_vectors(data_vectors):
    # Post-processing analysis
    sampler, df = data_vectors
    analysis = uq.analysis.SCAnalysis(sampler=sampler, qoi_cols=[('g', 0), ('g', 1), ('g', 2)])
    results = analysis.analyse(df)
    return results


def test_results(results):
    assert(isinstance(results, PCEAnalysisResults))
    sobols_first_x1 = results._get_sobols_first('f', 'x1')
    sobols_first_x2 = results._get_sobols_first('f', 'x2')
    sobols_second_x1 = results._get_sobols_second('f', 'x1')
    sobols_second_x2 = results._get_sobols_second('f', 'x2')
    sobols_total_x1 = results._get_sobols_total('f', 'x1')
    sobols_total_x2 = results._get_sobols_total('f', 'x2')
    assert(sobols_first_x1 == pytest.approx(0.62644867, 0.001))
    assert(sobols_first_x2 == pytest.approx(0.26789576, 0.001))
    assert(sobols_second_x1 == {'x1': 0.0, 'x2': 0.10565556484738273})
    assert(sobols_second_x2 == {'x1': 0.10565556484738273, 'x2': 0.0})
    assert(sobols_total_x1 == pytest.approx(0.73210424, 0.001))
    assert(sobols_total_x2 == pytest.approx(0.37355133, 0.001))


def test_full_results(results):
    with pytest.raises(RuntimeError):
        results.sobols_first('z')
    with pytest.raises(RuntimeError):
        results.sobols_first('f', 'y')
    with pytest.raises(AssertionError):
        results.sobols_first(None, 'x1')
    assert(results.sobols_first()['f']['x1'][0] == pytest.approx(0.6264486733708418))
    assert(results.sobols_first()['f']['x2'][0] == pytest.approx(0.2678957617817755))
    assert(results.sobols_first('f')['x1'][0] == pytest.approx(0.6264486733708418))
    assert(results.sobols_first('f')['x2'][0] == pytest.approx(0.2678957617817755))
    assert(results.sobols_first('f', 'x1')[0] == pytest.approx(0.6264486733708418))
    assert(results.sobols_first('f', 'x2')[0] == pytest.approx(0.2678957617817755))


def test_describe(results):
    assert(results.describe().to_dict()['f'] == pytest.approx({
        '10%': 0.009410762945528006,
        '90%': 2.1708835276870935,
        'count': 25.0,
        'mean': 0.91011171024204,
        'std': 0.807805287287411,
        'var': 0.6525493821694965
    }))
