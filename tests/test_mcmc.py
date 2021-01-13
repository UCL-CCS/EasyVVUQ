import os
import easyvvuq as uq
import numpy as np
import chaospy as cp

def test_mcmc(tmp_path):
    campaign = uq.Campaign(name="mcmc", work_dir=tmp_path)
    params = {
        "x1": {"type": "float", "min": -5.0, "max": 5.0, "default": 0.0},
        "x2": {"type": "float", "min": -5.0, "max": 5.0, "default": 0.0},
        "outfile": {"type": "string", "default": "output.json"}
    }
    encoder = uq.encoders.GenericEncoder(
        template_fname=HOME + "ronsenbrock.template", delimiter="$", target_filename="input.json")
    decoder = uq.decoders.JSONDecoder("input.json", ["value"])
    campaign.add_app(name="mcmc", params=params, encoder=encoder, decoder=decoder)
    
