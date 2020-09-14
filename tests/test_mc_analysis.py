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


def run_campaign():
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
            'run_id' : run_id,
            'x1': sample['x1'],
            'x2': sample['x2'],
            'f': sobol_g_func([sample['x1'], sample['x2']], d=2)
        })

    df = pd.DataFrame(data)

     # Post-processing analysis
    analysis = uq.analysis.QMCAnalysis(sampler=mc_sampler, qoi_cols=['f'])
    results = analysis.analyse(df)

    return results

def test_mc_analysis():
    # analytic Sobol indices
    results = run_campaign()
    ref_sobols = exact_sobols_g_func()
    sobol_x1 = results['sobols_first']['f']['x1']
    sobol_x2 = results['sobols_first']['f']['x2']
    assert sobol_x1 == pytest.approx(ref_sobols[0], abs=0.1)
    assert sobol_x2 == pytest.approx(ref_sobols[1], abs=0.1)

