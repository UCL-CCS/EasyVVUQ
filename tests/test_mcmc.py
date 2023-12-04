import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import json
import pytest
import sys
from easyvvuq.actions import ExecutePython, Actions
from dask.distributed import Client
import matplotlib.pyplot as plt


HOME = os.path.abspath(os.path.dirname(__file__))


def rosenbrock(inputs):
    x1 = float(inputs['x1'])
    x2 = float(inputs['x2'])
    y = (1.0 - x1) ** 2 + 100.0 * (x2 - x1 ** 2) ** 2
    return {'value': 300.0 - y}


###@pytest.mark.skip(reason="Broke due to pandas update. See issue #393.")
def test_mcmc(tmp_path):
    campaign = uq.Campaign(name="mcmc", work_dir=tmp_path)
    params = {
        "x1": {"type": "float", "default": 0.0},
        "x2": {"type": "float", "default": 0.0},
        "chain_id": {"type": "integer", "default": 0}
    }
    encoder = uq.encoders.GenericEncoder(template_fname=os.path.abspath(
        "tutorials/rosenbrock.template"), delimiter="$", target_filename="input.json")
    decoder = uq.decoders.JSONDecoder("output.json", ["value"])
    actions = Actions(ExecutePython(rosenbrock))
    campaign.add_app(name="mcmc", params=params, actions=actions)
    vary_init = {
        "x1": [-1.0, 0.0, 1.0, 0.5, 0.1],
        "x2": [1.0, 0.0, 0.5, 1.0, 0.2]
    }

    def q(x, b=1):
        return cp.J(cp.Normal(x['x1'], b), cp.Normal(x['x2'], b))
    np.random.seed(1969)
    sampler = uq.sampling.MCMCSampler(vary_init, q, 'value', 5)
    campaign.set_sampler(sampler)
    iterator = campaign.iterate(pool=Client())
    for _ in range(200):
        next(iterator).collate(progress_bar=True)
    df = campaign.get_collation_result()
    analysis = uq.analysis.MCMCAnalysis(sampler)
    result = analysis.analyse(df)
    plt.clf(); result.plot_hist('x1'); plt.savefig('/tmp/test_mcmc_hist_x1.png')
    plt.clf(); result.plot_hist('x2'); plt.savefig('/tmp/test_mcmc_hist_x2.png')
    plt.clf(); result.plot_chains('x1'); plt.savefig('/tmp/test_mcmc_chains_x1.png')
    plt.clf(); result.plot_chains('x2'); plt.savefig('/tmp/test_mcmc_chains_x2.png')
