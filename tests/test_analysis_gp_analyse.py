import easyvvuq as uq
import chaospy as cp
import os
import pytest
import shutil

def test_relocate_full(tmp_path):
    campaign = uq.Campaign(name='test', work_dir=tmp_path)
    params = {
        "temp_init": {
            "type": "float",
            "min": 0.0,
            "max": 100.0,
            "default": 95.0},
        "kappa": {
            "type": "float",
            "min": 0.0,
            "max": 0.1,
            "default": 0.025},
        "t_env": {
            "type": "float",
            "min": 0.0,
            "max": 40.0,
            "default": 15.0},
        "out_file": {
            "type": "string",
            "default": "output.csv"}}
    output_filename = params["out_file"]["default"]
    output_columns = ["te"]
    # Create an encoder and decoder for PCE test app
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/cooling/cooling.template',
        delimiter='$',
        target_filename='cooling_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns)
    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }
    sampler = uq.sampling.quasirandom.LHCSampler(vary=vary)
    actions = uq.actions.ExecuteLocal("tests/cooling/cooling_model.py cooling_in.json")
    campaign.add_app(name='test_app', params=params, encoder=encoder, decoder=decoder)
    campaign.set_app('test_app')
    campaign.set_sampler(sampler)
    campaign.draw_samples(100)
    campaign.populate_runs_dir()
    campaign.apply_for_each_run_dir(actions)
    campaign.collate()
    df = campaign.get_collation_result()
    analysis = uq.analysis.gp_analyse.GaussianProcessSurrogate(['kappa', 't_env'], ['te'])
    result = analysis.analyse(df)
