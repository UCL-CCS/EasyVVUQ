import os
import easyvvuq as uq
import chaospy as cp
import pickle
import time
import numpy as np
import matplotlib.pylab as plt
from pprint import pprint
import glob
import subprocess
import pytest


###@pytest.mark.skip(reason="fipy nonsense")
def test_action_replace():
    params = {
        "Qe_tot": {"type": "float", "min": 1.0e6, "max": 50.0e6, "default": 2e6},
        "H0": {"type": "float", "min": 0.00, "max": 1.0, "default": 0},
        "Hw": {"type": "float", "min": 0.01, "max": 100.0, "default": 0.1},
        "Te_bc": {"type": "float", "min": 10.0, "max": 1000.0, "default": 100},
        "chi": {"type": "float", "min": 0.01, "max": 100.0, "default": 1},
        "a0": {"type": "float", "min": 0.2, "max": 10.0, "default": 1},
        "R0": {"type": "float", "min": 0.5, "max": 20.0, "default": 3},
        "E0": {"type": "float", "min": 1.0, "max": 10.0, "default": 1.5},
        "b_pos": {"type": "float", "min": 0.95, "max": 0.99, "default": 0.98},
        "b_height": {"type": "float", "min": 3e19, "max": 10e19, "default": 6e19},
        "b_sol": {"type": "float", "min": 2e18, "max": 3e19, "default": 2e19},
        "b_width": {"type": "float", "min": 0.005, "max": 0.025, "default": 0.01},
        "b_slope": {"type": "float", "min": 0.0, "max": 0.05, "default": 0.01},
        "nr": {"type": "integer", "min": 10, "max": 1000, "default": 100},
        "dt": {"type": "float", "min": 1e-3, "max": 1e3, "default": 100},
        "out_file": {"type": "string", "default": "output.csv"}
    }

    encoder = uq.encoders.GenericEncoder(
        template_fname='tutorials/fusion.template',
        delimiter='$',
        target_filename='fusion_in.json')
    decoder = uq.decoders.SimpleCSV(
        target_filename="output.csv",
        output_columns=["te", "ne", "rho", "rho_norm"])
    execute = uq.actions.ExecuteLocal(
        'python3 %s/fusion_model.py fusion_in.json' % (os.getcwd()))
    actions = uq.actions.Actions(
        uq.actions.CreateRunDirectory('.'),
        uq.actions.Encode(encoder))
    vary = {
        "Qe_tot": cp.Uniform(1.8e6, 2.2e6),
        "Te_bc": cp.Uniform(80.0, 120.0)
    }
    campaign = uq.Campaign(name='fusion_pce.')
    campaign.add_app(name="fusion", params=params, actions=actions)
    campaign.set_sampler(uq.sampling.PCESampler(vary=vary, polynomial_order=2))
    campaign.execute().collate()
    input_json_files_PATH = [
        os.path.dirname(p)
        for p in glob.glob(
            campaign._campaign_dir + '/**/fusion_in.json',
            recursive=True
        )]
    curr_dir = os.getcwd()
    for run_dir in input_json_files_PATH:
        subprocess.call(
            ["python3 {}/tutorials/fusion_model.py  fusion_in.json".format(curr_dir)],
            cwd=run_dir,
            shell=True
        )
        print("executes fusion_model.py in directory {}".format(run_dir))
    actions = uq.actions.Actions(uq.actions.Decode(decoder))
    campaign.replace_actions("fusion", actions)
    campaign.execute().collate()
    results_df = campaign.get_collation_result()
    results = campaign.analyse(qoi_cols=["te", "ne", "rho", "rho_norm"])
    rho = results.describe('rho', 'mean')
    rho_norm = results.describe('rho_norm', 'mean')
