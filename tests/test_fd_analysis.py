import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import pytest
import logging
import pandas as pd
import math
from easyvvuq.analysis.fd_analysis import PCEAnalysisResults

def my_func1(x):
    # for the function, the exact (1st-order)
    # derivative indices are known analytically

    assert(len(x) == 2)
    
    f = x[0]**2 +2*x[0]*x[1] + 4*x[1]**2

    #df_dx1 = 2*x[0] + 2*x[1]
    #df_dx2 = 2*x[0] + 8*x[1]

    return f


@pytest.fixture
def sampler():
    # Create the sampler
    vary = {
        "x1": cp.Normal(0.0, 1.0),
        "x2": cp.Normal(0.0, 1.0)
    }

    nominal_value = {
        "x1": 1.,
        "x2": 1.
    }

    s = uq.sampling.FDSampler(vary=vary, perturbation=0.05, nominal_value=nominal_value, relative_analysis=False)
    return s

@pytest.fixture
def sampler_relative():
    # Create the sampler
    vary = {
        "x1": cp.Normal(0.0, 1.0),
        "x2": cp.Normal(0.0, 1.0)
    }

    nominal_value = {
        "x1": 1.,
        "x2": 1.
    }

    s = uq.sampling.FDSampler(vary=vary, perturbation=0.05, nominal_value=nominal_value, relative_analysis=True)
    return s

@pytest.fixture
def data(sampler):
    # fix random seed to make this test deterministic
    np.random.seed(10000000)
    
    data = {('run_id', 0): [], ('x1', 0): [], ('x2', 0): [], ('f', 0): []}
    for run_id, sample in enumerate(sampler):
        data[('run_id', 0)].append(run_id)
        data[('x1', 0)].append(sample['x1'])
        data[('x2', 0)].append(sample['x2'])

        f = my_func1([sample['x1'], sample['x2']])
        data[('f', 0)].append(f)
    df = pd.DataFrame(data)
    return sampler, df


@pytest.fixture
def data_vectors(sampler):
    np.random.seed(10000000)
    
    data = {('run_id', 0): [], ('x1', 0): [], ('x2', 0): [],
            ('g', 0): [], ('g', 1): [], ('g', 2): [], ('h', 0): [], ('h', 1): []}
    for run_id, sample in enumerate(sampler):
        data[('run_id', 0)].append(run_id)
        data[('x1', 0)].append(sample['x1'])
        data[('x2', 0)].append(sample['x2'])

        f = my_func1([sample['x1'], sample['x2']])
        data[('g', 0)].append(f)
        data[('g', 1)].append(f + 5)
        data[('g', 2)].append(f + 10)
        data[('h', 0)].append(2*f)
        data[('h', 1)].append(4*f)
    df = pd.DataFrame(data)
    return sampler, df

@pytest.fixture
def data_vectors_relative(sampler_relative):
    np.random.seed(10000000)
    
    data = {('run_id', 0): [], ('x1', 0): [], ('x2', 0): [],
            ('g', 0): [], ('g', 1): [], ('g', 2): [], ('h', 0): [], ('h', 1): []}
    for run_id, sample in enumerate(sampler_relative):
        data[('run_id', 0)].append(run_id)
        data[('x1', 0)].append(sample['x1'])
        data[('x2', 0)].append(sample['x2'])

        f = my_func1([sample['x1'], sample['x2']])
        data[('g', 0)].append(f)
        data[('g', 1)].append(f + 5)
        data[('g', 2)].append(f + 10)
        data[('h', 0)].append(2*f)
        data[('h', 1)].append(4*f)
    df = pd.DataFrame(data)
    return sampler_relative, df


@pytest.fixture
def results(data):
    # Post-processing analysis
    mc_sampler, df = data
    analysis = uq.analysis.FDAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    results = analysis.analyse(df)
    return results


@pytest.fixture
def results_vectors(data_vectors):
    # Post-processing analysis
    sampler, df = data_vectors
    analysis = uq.analysis.FDAnalysis(sampler=sampler, qoi_cols=['g', 'h'])
    results = analysis.analyse(df)
    return results


@pytest.fixture
def results_vectors_relative(data_vectors_relative):
    # Post-processing analysis
    sampler, df = data_vectors_relative
    analysis = uq.analysis.FDAnalysis(sampler=sampler, qoi_cols=['g', 'h'])
    results = analysis.analyse(df)
    return results


def test_results(results):
    assert (isinstance(results, PCEAnalysisResults))
    sobols_first_x1 = results._get_sobols_first('f', 'x1')
    sobols_first_x2 = results._get_sobols_first('f', 'x2')
    sobols_total_x1 = results._get_sobols_total('f', 'x1')
    sobols_total_x2 = results._get_sobols_total('f', 'x2')
    assert (sobols_first_x1 == pytest.approx(0.0, 0.001))
    assert (sobols_first_x2 == pytest.approx(0.0, 0.001))
    assert (sobols_total_x1 == pytest.approx(0.0, 0.001))
    assert (sobols_total_x2 == pytest.approx(0.0, 0.001))

    derivatives_first_x1 = results._get_derivatives_first('f', 'x1')
    derivatives_first_x2 = results._get_derivatives_first('f', 'x2')
    assert (derivatives_first_x1 == pytest.approx(4.0, 0.001))
    assert (derivatives_first_x2 == pytest.approx(10.0, 0.001))

def test_results_vec(results_vectors):
    assert (isinstance(results_vectors, PCEAnalysisResults))
    
    # Different access modes
    assert (results_vectors.derivatives_first()['g']['x1'][0] == pytest.approx(results_vectors.derivatives_first('g')['x1'][0]))
    assert (results_vectors.derivatives_first()['g']['x1'][0] == pytest.approx(results_vectors.derivatives_first('g', 'x1')[0]))

    # Numerical values
    assert (results_vectors.derivatives_first('g')['x1'][0] == pytest.approx(4.0))
    assert (results_vectors.derivatives_first('g')['x2'][0] == pytest.approx(10.0))
    assert (results_vectors.derivatives_first('g')['x1'][1] == pytest.approx(4.0))
    assert (results_vectors.derivatives_first('g')['x2'][1] == pytest.approx(10.0))
    assert (results_vectors.derivatives_first('g')['x1'][2] == pytest.approx(4.0))
    assert (results_vectors.derivatives_first('g')['x2'][2] == pytest.approx(10.0))

    # since h[0] = my_func1(p)*2
    assert (results_vectors.derivatives_first('h')['x1'][0] == pytest.approx(2*4.0))
    assert (results_vectors.derivatives_first('h')['x2'][0] == pytest.approx(2*10.0))
    # since h[0] = my_func1(p)*4
    assert (results_vectors.derivatives_first('h')['x1'][1] == pytest.approx(4*4.0))
    assert (results_vectors.derivatives_first('h')['x2'][1] == pytest.approx(4*10.0))


def test_results_vec_relative(results_vectors_relative, sampler_relative):
    assert (isinstance(results_vectors_relative, PCEAnalysisResults))
    
    # Different access modes
    assert (results_vectors_relative.derivatives_first()['g']['x1'][0] == pytest.approx(results_vectors_relative.derivatives_first('g')['x1'][0]))
    assert (results_vectors_relative.derivatives_first()['g']['x1'][0] == pytest.approx(results_vectors_relative.derivatives_first('g', 'x1')[0]))

    # Numerical values
    assert (results_vectors_relative.derivatives_first('g')['x1'][0] == pytest.approx(4.0))
    assert (results_vectors_relative.derivatives_first('g')['x2'][0] == pytest.approx(10.0))
    assert (results_vectors_relative.derivatives_first('g')['x1'][1] == pytest.approx(4.0))
    assert (results_vectors_relative.derivatives_first('g')['x2'][1] == pytest.approx(10.0))
    assert (results_vectors_relative.derivatives_first('g')['x1'][2] == pytest.approx(4.0))
    assert (results_vectors_relative.derivatives_first('g')['x2'][2] == pytest.approx(10.0))


    assert (results_vectors_relative.derivatives_first('h')['x1'][0] == pytest.approx(2*4.0))
    assert (results_vectors_relative.derivatives_first('h')['x2'][0] == pytest.approx(2*10.0))
    assert (results_vectors_relative.derivatives_first('h')['x1'][1] == pytest.approx(4*4.0))
    assert (results_vectors_relative.derivatives_first('h')['x2'][1] == pytest.approx(4*10.0))

