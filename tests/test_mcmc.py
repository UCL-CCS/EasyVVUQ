import os
import easyvvuq as uq
import numpy as np
import chaospy as cp

HOME = os.path.abspath(os.path.dirname(__file__))

def test_mcmc(tmp_path):
    campaign = uq.Campaign(name="mcmc", work_dir=tmp_path)
    params = {
        "x1": {"type": "float", "min": -5.0, "max": 5.0, "default": 0.0},
        "x2": {"type": "float", "min": -5.0, "max": 5.0, "default": 0.0},
        "out_file": {"type": "string", "default": "output.json"}
    }
    encoder = uq.encoders.GenericEncoder(
        template_fname=os.path.abspath("tutorials/rosenbrock.template"), delimiter="$", target_filename="input.json")
    decoder = uq.decoders.JSONDecoder("output.json", ["value"])
    campaign.add_app(name="mcmc", params=params, encoder=encoder, decoder=decoder)
    b = 1.0
    vary = {
        "x1": cp.Normal(0.0, b ** 2),
        "x2": cp.Normal(0.0, b ** 2)
    }
    vary_init = {
        "x1": 0.0,
        "x2": 0.0
    }
    sampler = uq.sampling.MCMCSampler(vary_init)
    campaign.set_sampler(sampler)
    action = uq.actions.ExecuteLocal("tutorials/rosenbrock.py input.json")
    for _ in range(100):
        campaign.draw_samples(1)
        campaign.populate_runs_dir()
        campaign.apply_for_each_run_dir(action)
        campaign.collate()
        result = campaign.get_collation_result()

