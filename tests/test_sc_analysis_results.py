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
    # Select the MC sampler
    sampler = uq.sampling.SCSampler(vary)
    data = []
    for run_id, sample in enumerate(sampler):
        data.append({
            'run_id': run_id,
            'x1': sample['x1'],
            'x2': sample['x2'],
            'f': sobol_g_func([sample['x1'], sample['x2']], d=2)
        })

    df = pd.DataFrame(data)
    return sampler, df


@pytest.fixture
def results(data):
    # Post-processing analysis
    mc_sampler, df = data
    analysis = uq.analysis.SCAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    results = analysis.analyse(df)
    return results


def test_results(results):
    assert(isinstance(results, SCAnalysisResults))
    sobols_first_x1 = results._get_sobols_first('f', 'x1')
    sobols_first_x2 = results._get_sobols_first('f', 'x2')
    assert(sobols_first_x1 == pytest.approx(0.610242, 0.001))
    assert(sobols_first_x2 == pytest.approx(0.26096511, 0.001))


def test_results_conf(results):
    sobols_first_x1_conf = results._get_sobols_first_conf('f', 'x1')
    assert(math.isnan(sobols_first_x1_conf[0]))
    assert(math.isnan(sobols_first_x1_conf[1]))
    sobols_first_x2_conf = results._get_sobols_first_conf('f', 'x2')
    assert(math.isnan(sobols_first_x2_conf[0]))
    assert(math.isnan(sobols_first_x2_conf[1]))


def test_full_results(results):
    assert(results.sobols_first().shape == (1, 6))


def test_describe(results):
    assert(results.describe().to_dict()['f'] == pytest.approx({
        'mean': 0.9101117102420444,
        'std': 0.8184617581393419,
        'var': 0.6698796495365424
    }))
