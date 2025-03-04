import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import pytest
import logging
import pandas as pd
import math
from tests.sc.sobol_model import sobol_g_func
from easyvvuq.analysis.sc_analysis import SCAnalysisResults


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
    sampler = uq.sampling.SCSampler(vary)
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
    sampler, df = data
    analysis = uq.analysis.SCAnalysis(sampler=sampler, qoi_cols=['f'])
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
    assert (isinstance(results, SCAnalysisResults))
    sobols_first_x1 = results._get_sobols_first('f', 'x1')
    sobols_first_x2 = results._get_sobols_first('f', 'x2')
    assert (sobols_first_x1 == pytest.approx(0.610242, 0.001))
    assert (sobols_first_x2 == pytest.approx(0.26096511, 0.001))
    with pytest.raises(RuntimeError):
        results.sobols_total()


def test_results_conf(results):
    with pytest.raises(NotImplementedError):
        results._get_sobols_first_conf('f', 'x1')


def test_full_results(results):
    with pytest.raises(RuntimeError):
        results.sobols_first('z')
    with pytest.raises(RuntimeError):
        results.sobols_first('f', 'y')
    with pytest.raises(AssertionError):
        results.sobols_first(None, 'x1')
    assert (results.sobols_first()['f']['x1'][0] == pytest.approx(0.6102419965318732, 0.001))
    assert (results.sobols_first()['f']['x2'][0] == pytest.approx(0.2609651061314295, 0.001))
    assert (results.sobols_first('f')['x1'][0] == pytest.approx(0.6102419965318732, 0.001))
    assert (results.sobols_first('f')['x2'][0] == pytest.approx(0.2609651061314295, 0.001))
    assert (results.sobols_first('f', 'x1')[0] == pytest.approx(0.6102419965318732, 0.001))
    assert (results.sobols_first('f', 'x2')[0] == pytest.approx(0.2609651061314295, 0.001))


def test_describe(results):
    assert (results.describe().to_dict()[('f', 0)] == {
        'mean': pytest.approx(0.9101117102420444, 0.001),
        'std': pytest.approx(0.8184617581393419, 0.001),
        'var': pytest.approx(0.6698796495365424, 0.001)
    })


def test_vectors(results_vectors):
    assert (results_vectors.sobols_first(('g', 0), 'x1') == pytest.approx(1.0))
    assert (results_vectors.sobols_first(('g', 0), 'x2') == pytest.approx(0.0))
    assert (results_vectors.sobols_first(('g', 1), 'x1') == pytest.approx(0.0))
    assert (results_vectors.sobols_first(('g', 1), 'x2') == pytest.approx(1.0))
    assert (results_vectors.sobols_first(('g', 2), 'x1') == pytest.approx(0.5))
    assert (results_vectors.sobols_first(('g', 2), 'x2') == pytest.approx(0.5))
