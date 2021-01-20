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
    vary_init = {
        "x1": 0.0,
        "x2": 0.0
    }
    sampler = uq.sampling.MCMCSampler(vary_init)
    campaign.set_sampler(sampler)
    action = uq.actions.ExecuteLocal("tutorials/rosenbrock.py input.json")
    qoi = 'value'
    def get_q_xy(x, y):
        pass
    def get_q_yx(x, y):
        pass
    for _ in range(100):
        campaign.draw_samples(1)
        campaign.populate_runs_dir()
        campaign.apply_for_each_run_dir(action)
        campaign.collate()
        result = campaign.get_collation_result()
        last_row = result.iloc[-1]
        y = dict((key, last_row[key][0]) for key in vary_init.keys())
        sampler.update(y, last_row[qoi][0], get_q_xy(sampler.x, y), get_q_yx(sampler.x, y))
        
