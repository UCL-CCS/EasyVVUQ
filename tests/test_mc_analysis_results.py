import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import pytest
import logging
import pandas as pd
import json
from tests.sc.sobol_model import sobol_g_func
from easyvvuq.analysis.qmc_analysis import QMCAnalysisResults


DESCRIBE_RESULTS = """{"run_id":{"count":400.0,"mean":199.5,"std":115.6143013068,\
"min":0.0,"25%":99.75,"50%":199.5,"75%":299.25,"max":399.0},"x1":{"count":400.0,\
"mean":0.4669087199,"std":0.2900847389,"min":0.0057789696,"25%":0.2085183865,\
"50%":0.4712230161,"75%":0.7243719834,"max":0.9849714587},"x2":{"count":400.0,\
"mean":0.4691844467,"std":0.2925121512,"min":0.0038532032,"25%":0.2018501193,\
"50%":0.4495551186,"75%":0.6869525315,"max":0.9983981908},"f":{"count":400.0,\
"mean":1.0181029471,"std":0.7757795887,"min":0.0170251,"25%":0.3510339027,\
"50%":0.8822882238,"75%":1.5481160285,"max":3.1529538623}}"""


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


def test_results(results):
    assert(isinstance(results, QMCAnalysisResults))
    sobols_first_x1 = results._get_sobols_first('f', 'x1')
    sobols_first_x2 = results._get_sobols_first('f', 'x2')
    sobols_total_x1 = results._get_sobols_total('f', 'x1')
    sobols_total_x2 = results._get_sobols_total('f', 'x2')
    assert(sobols_first_x1 == pytest.approx(0.55690589, 0.001))
    assert(sobols_first_x2 == pytest.approx(0.20727553, 0.001))
    assert(sobols_total_x1 == pytest.approx(0.81327937, 0.001))
    assert(sobols_total_x2 == pytest.approx(0.38049629, 0.001))


def test_results_conf(results):
    sobols_first_x1_conf = results._get_sobols_first_conf('f', 'x1')
    assert(sobols_first_x1_conf[0] == pytest.approx(0.14387, 0.001))
    assert(sobols_first_x1_conf[1] == pytest.approx(0.894288, 0.001))
    sobols_first_x2_conf = results._get_sobols_first_conf('f', 'x2')
    assert(sobols_first_x2_conf[0] == pytest.approx(-0.110633, 0.001))
    assert(sobols_first_x2_conf[1] == pytest.approx(0.467528, 0.001))
    sobols_total_x1_conf = results._get_sobols_total_conf('f', 'x1')
    assert(sobols_total_x1_conf[0] == pytest.approx(0.613689, 0.001))
    assert(sobols_total_x1_conf[1] == pytest.approx(1.018587, 0.001))
    sobols_total_x2_conf = results._get_sobols_total_conf('f', 'x2')
    assert(sobols_total_x2_conf[0] == pytest.approx(0.243612, 0.001))
    assert(sobols_total_x2_conf[1] == pytest.approx(0.492141, 0.001))


def test_full_results(results):
    assert(results.sobols_first().shape == (1, 6))
    assert(results.sobols_total().shape == (1, 6))


def test_describe(results):
    assert(json.loads(results.describe().astype(float).to_json()) == json.loads(DESCRIBE_RESULTS))
