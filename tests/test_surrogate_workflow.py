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
from easyvvuq.actions import CreateRunDirectory, Encode, Decode, ExecuteLocal, Actions, ExecutePython
import matplotlib.pyplot as plt

VARY = {
    "Pe": cp.Uniform(100.0, 200.0),
    "f": cp.Uniform(0.95, 1.05)
}


###@pytest.mark.skip(reason="Broke due to pandas update. See issue #395.")
@pytest.mark.parametrize('sampler', [
    uq.sampling.RandomSampler(
        vary=VARY, max_num=100, analysis_class=uq.analysis.GaussianProcessSurrogate),
    uq.sampling.SCSampler(
        vary=VARY, polynomial_order=[2, 5], quadrature_rule="G"),
    #    uq.sampling.PCESampler(
    #        vary=VARY, polynomial_order=[2, 5], rule="G")
])
def test_surrogate_workflow(tmpdir, sampler):
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
        },
        "chain_id": {
            "type": "integer",
            "default": 0
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
    campaign.set_sampler(sampler)
    campaign.execute().collate()
    results = campaign.analyse(qoi_cols=output_columns)
    surrogate = results.surrogate()

    df = campaign.get_collation_result()
    for index, row in df.iterrows():
        surrogate_y = surrogate({'Pe': row['Pe'][0], 'f': row['f'][0]})['u']
        model_y = row['u'].values
        # assert(pytest.approx(surrogate_y == model_y))
        assert np.max(np.abs(surrogate_y - model_y)) < 1e-6

    # Attempt callibration with MCMC
    del params['out_file']  # eliminate this (now) nuisance field
    campaign.add_app(name='surrogate', params=params, actions=Actions(ExecutePython(surrogate)))
    db_location = campaign.db_location
    campaign = None
    reloaded_campaign = uq.Campaign('sc', db_location=db_location)
    assert (reloaded_campaign._active_app_name == 'surrogate')
    u = np.array([0., 0.00333333, 0.00666667, 0.01, 0.01333333,
                  0.01666667, 0.02, 0.02333333, 0.02666667, 0.03,
                  0.03333333, 0.03666667, 0.04, 0.04333333, 0.04666667,
                  0.05, 0.05333333, 0.05666667, 0.06, 0.06333333,
                  0.06666667, 0.07, 0.07333333, 0.07666667, 0.08,
                  0.08333333, 0.08666667, 0.09, 0.09333333, 0.09666667,
                  0.1, 0.10333333, 0.10666667, 0.11, 0.11333333,
                  0.11666667, 0.12, 0.12333333, 0.12666667, 0.13,
                  0.13333333, 0.13666667, 0.14, 0.14333333, 0.14666667,
                  0.15, 0.15333333, 0.15666667, 0.16, 0.16333333,
                  0.16666667, 0.17, 0.17333333, 0.17666667, 0.18,
                  0.18333333, 0.18666667, 0.19, 0.19333333, 0.19666667,
                  0.2, 0.20333333, 0.20666667, 0.21, 0.21333333,
                  0.21666667, 0.22, 0.22333333, 0.22666667, 0.23,
                  0.23333333, 0.23666667, 0.24, 0.24333333, 0.24666667,
                  0.25, 0.25333333, 0.25666667, 0.26, 0.26333333,
                  0.26666667, 0.27, 0.27333333, 0.27666667, 0.28,
                  0.28333333, 0.28666667, 0.29, 0.29333333, 0.29666667,
                  0.3, 0.30333333, 0.30666667, 0.31, 0.31333333,
                  0.31666667, 0.32, 0.32333333, 0.32666667, 0.33,
                  0.33333333, 0.33666667, 0.34, 0.34333333, 0.34666667,
                  0.35, 0.35333333, 0.35666667, 0.36, 0.36333333,
                  0.36666667, 0.37, 0.37333333, 0.37666667, 0.38,
                  0.38333333, 0.38666667, 0.39, 0.39333333, 0.39666667,
                  0.4, 0.40333333, 0.40666667, 0.41, 0.41333333,
                  0.41666667, 0.42, 0.42333333, 0.42666667, 0.43,
                  0.43333333, 0.43666667, 0.44, 0.44333333, 0.44666667,
                  0.45, 0.45333333, 0.45666667, 0.46, 0.46333333,
                  0.46666667, 0.47, 0.47333333, 0.47666667, 0.48,
                  0.48333333, 0.48666667, 0.49, 0.49333333, 0.49666667,
                  0.5, 0.50333333, 0.50666667, 0.51, 0.51333333,
                  0.51666667, 0.52, 0.52333333, 0.52666667, 0.53,
                  0.53333333, 0.53666667, 0.54, 0.54333333, 0.54666667,
                  0.55, 0.55333333, 0.55666667, 0.56, 0.56333333,
                  0.56666667, 0.57, 0.57333333, 0.57666667, 0.58,
                  0.58333333, 0.58666667, 0.59, 0.59333333, 0.59666667,
                  0.6, 0.60333333, 0.60666667, 0.61, 0.61333333,
                  0.61666667, 0.62, 0.62333333, 0.62666667, 0.63,
                  0.63333333, 0.63666667, 0.64, 0.64333333, 0.64666667,
                  0.65, 0.65333333, 0.65666667, 0.66, 0.66333333,
                  0.66666667, 0.67, 0.67333333, 0.67666667, 0.68,
                  0.68333333, 0.68666667, 0.69, 0.69333333, 0.69666667,
                  0.7, 0.70333333, 0.70666667, 0.71, 0.71333333,
                  0.71666667, 0.72, 0.72333333, 0.72666667, 0.73,
                  0.73333333, 0.73666667, 0.74, 0.74333333, 0.74666667,
                  0.75, 0.75333333, 0.75666667, 0.76, 0.76333333,
                  0.76666667, 0.77, 0.77333333, 0.77666667, 0.78,
                  0.78333333, 0.78666667, 0.79, 0.79333333, 0.79666667,
                  0.8, 0.80333333, 0.80666667, 0.81, 0.81333333,
                  0.81666667, 0.82, 0.82333333, 0.82666667, 0.83,
                  0.83333333, 0.83666667, 0.84, 0.84333333, 0.84666667,
                  0.85, 0.85333333, 0.85666667, 0.86, 0.86333333,
                  0.86666667, 0.87, 0.87333333, 0.87666666, 0.87999999,
                  0.88333332, 0.88666664, 0.88999995, 0.89333325, 0.89666653,
                  0.89999978, 0.90333296, 0.90666605, 0.90999898, 0.91333163,
                  0.91666382, 0.91999526, 0.92332544, 0.9266535, 0.92997806,
                  0.93329677, 0.93660573, 0.93989844, 0.94316407, 0.94638456,
                  0.94952982, 0.95254969, 0.9553606, 0.95782322, 0.95970536,
                  0.96062005, 0.9599223, 0.95653717, 0.94867307, 0.933344,
                  0.90557333, 0.85706667, 0.774, 0.63333333, 0.39666667,
                  0.])

    def proposal(x):
        return cp.J(cp.Normal(x['Pe'], 1.0),
                    cp.Normal(x['f'], 0.001))

    def loglikelihood(x):
        return -((u - x) ** 2).sum()

    init = {'Pe': [110.0], 'f': [2.0]}
    reloaded_campaign.set_sampler(uq.sampling.MCMCSampler(init, proposal, 'u', 1, loglikelihood))
    iterator = reloaded_campaign.iterate(mark_invalid=True)
    for _ in range(100):
        next(iterator).collate()
    df = reloaded_campaign.get_collation_result()
    assert (len(df) > 0)
    assert (len(df) <= 100)
    results = reloaded_campaign.analyse()
    plt.clf(); results.plot_hist('Pe'); plt.savefig('/tmp/test_mcmc_hist_Pe.png')
    plt.clf(); results.plot_hist('f'); plt.savefig('/tmp/test_mcmc_hist_f.png')
    plt.clf(); results.plot_chains('Pe'); plt.savefig('/tmp/test_mcmc_chains_Pe.png')
    plt.clf(); results.plot_chains('f'); plt.savefig('/tmp/test_mcmc_chains_f.png')
