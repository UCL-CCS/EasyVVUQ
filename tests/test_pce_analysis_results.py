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
    sampler = uq.sampling.PCESampler(vary)
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
    analysis = uq.analysis.PCEAnalysis(sampler=sampler, qoi_cols=['g', 'h'])
    results = analysis.analyse(df)
    return results


def test_results(results):
    assert (isinstance(results, PCEAnalysisResults))
    sobols_first_x1 = results._get_sobols_first('f', 'x1')
    sobols_first_x2 = results._get_sobols_first('f', 'x2')
    sobols_second_x1 = results._get_sobols_second('f', 'x1')
    sobols_second_x2 = results._get_sobols_second('f', 'x2')
    sobols_total_x1 = results._get_sobols_total('f', 'x1')
    sobols_total_x2 = results._get_sobols_total('f', 'x2')
    assert (sobols_first_x1 == pytest.approx(0.62644867, 0.001))
    assert (sobols_first_x2 == pytest.approx(0.26789576, 0.001))
    assert (sobols_second_x1['x2'] == pytest.approx(0.10565556484738273, 0.001))
    assert (sobols_second_x2['x1'] == pytest.approx(0.10565556484738273, 0.001))
    assert (sobols_total_x1 == pytest.approx(0.73210424, 0.001))
    assert (sobols_total_x2 == pytest.approx(0.37355133, 0.001))


def test_full_results(results):
    with pytest.raises(RuntimeError):
        results.sobols_first('z')
    with pytest.raises(RuntimeError):
        results.sobols_first('f', 'y')
    with pytest.raises(AssertionError):
        results.sobols_first(None, 'x1')
    assert (results.sobols_first()['f']['x1'][0] == pytest.approx(0.6264486733708418))
    assert (results.sobols_first()['f']['x2'][0] == pytest.approx(0.2678957617817755))
    assert (results.sobols_first('f')['x1'][0] == pytest.approx(0.6264486733708418))
    assert (results.sobols_first('f')['x2'][0] == pytest.approx(0.2678957617817755))
    assert (results.sobols_first('f', 'x1')[0] == pytest.approx(0.6264486733708418))
    assert (results.sobols_first('f', 'x2')[0] == pytest.approx(0.2678957617817755))


def test_distribution(results):
    with pytest.raises(RuntimeError):
        results.get_distribution('z')
    assert (results.get_distribution('f').pdf([0, 0]) == pytest.approx([0.44296863, 0.44296863]))


def test_describe(results_vectors):
    assert (
        results_vectors.describe()[
            ('g',
             1)].to_dict() == {
            'mean': pytest.approx(0.5000000000000001, 0.001),
            'var': pytest.approx(0.08333333333333348, 0.001),
            'std': pytest.approx(0.28867513459481314, 0.001),
            '1%': pytest.approx(0.00918264783704714, 0.001),
            '10%': pytest.approx(0.09946223131463872, 0.001),
            'median': pytest.approx(0.49494477064098824, 0.001),
            '90%': pytest.approx(0.9004983440179313, 0.001),
            '99%': pytest.approx(0.9905999521854744, 0.001),
            'min': pytest.approx(-0.775685017772766, 0.001),
            'max': pytest.approx(1.775781592068878, 0.001)})
    assert (
        results_vectors.describe('g').to_dict()[
            ('g',
             1)] == {
            'mean': pytest.approx(0.5000000000000001, 0.001),
            'var': pytest.approx(0.08333333333333348, 0.001),
            'std': pytest.approx(0.28867513459481314, 0.001),
            '1%': pytest.approx(0.00918264783704714, 0.001),
            '10%': pytest.approx(0.09946223131463872, 0.001),
            'median': pytest.approx(0.49494477064098824, 0.001),
            '90%': pytest.approx(0.9004983440179313, 0.001),
            '99%': pytest.approx(0.9905999521854744, 0.001),
            'min': pytest.approx(-0.7756850177727665, 0.001),
            'max': pytest.approx(1.775781592068878, 0.001)})
    assert (isinstance(results_vectors.describe('g', 'min'), np.ndarray))
