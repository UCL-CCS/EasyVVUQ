import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import json
import matplotlib.pyplot as plt
import sys

HOME = os.path.abspath(os.path.dirname(__file__))

def rosenbrock(directory):
    json_input = os.path.join(directory, 'input.json')
    if not os.path.isfile(json_input):
        sys.exit(json_input + " does not exist.")
    with open(json_input, "r") as fd:
        inputs = json.load(fd)
    x1 = float(inputs['x1'])
    x2 = float(inputs['x2'])
    output_filename = os.path.join(directory, inputs['outfile'])
    y = (1.0 - x1) ** 2 + 100.0 * (x2 - x1 ** 2) ** 2
    with open(output_filename, 'w') as fd:
        json.dump({'value': -y}, fd)

def test_mcmc(tmp_path):
    campaign = uq.Campaign(name="mcmc", work_dir=tmp_path)
    params = {
        "x1": {"type": "float", "default": 0.0},
        "x2": {"type": "float", "default": 0.0},
        "out_file": {"type": "string", "default": "output.json"}
    }
    encoder = uq.encoders.GenericEncoder(
        template_fname=os.path.abspath("tutorials/rosenbrock.template"), delimiter="$", target_filename="input.json")
    decoder = uq.decoders.JSONDecoder("output.json", ["value"])
    campaign.add_app(name="mcmc", params=params, encoder=encoder, decoder=decoder)
    vary_init = {
        "x1": -3.0,
        "x2": 2.0
    }
    def q(x, b=0.1):
        return cp.J(cp.Normal(x['x1'], b), cp.Normal(x['x2'], b))
    sampler = uq.sampling.MCMCSampler(vary_init, q, 'value')
    campaign.set_sampler(sampler)
    action = uq.actions.ExecutePython(rosenbrock)
    ignored = sampler.mcmc_sampling(campaign, action, 200)
    df = campaign.get_collation_result()
    analysis = uq.analysis.MCMCAnalysis(sampler, 'value')
    result = analysis.analyse(df)
    distribution = result.distribution()

