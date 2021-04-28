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

def test_surrogate_workflow():
    campaign = uq.Campaign('surrogate')
=======
from easyvvuq.actions import CreateRunDirectory, Encode, Decode, ExecuteLocal, Actions

def test_surrogate_workflow(tmpdir):
    campaign = uq.Campaign(name='sc', work_dir=tmpdir)
    params = {
        "Pe": {
            "type": "float",
            "min": 1.0,
            "max": 2000.0,
            "default": 100.0},
        "f": {
            "type": "float",
            "min": 0.0,
            "max": 10.0,
            "default": 1.0},
        "out_file": {
            "type": "string",
            "default": "output.csv"
        }
    }

    output_filename = params["out_file"]["default"]
    output_columns = ["u"]
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/sc/sc.template',
        delimiter='$',
        target_filename='ade_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns)
    execute = ExecuteLocal("{} ade_in.json".format(os.path.abspath('tests/sc/sc_model.py')))
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))
    campaign.add_app(name="sc", params=params, actions=actions)

    vary = {
        "Pe": cp.Uniform(100.0, 200.0),
        "f": cp.Uniform(0.95, 1.05)
    }
    sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=[2, 5], quadrature_rule="G")
    campaign.set_sampler(sampler)

    campaign.execute().collate()

    results = campaign.analyse(qoi_cols=output_columns)