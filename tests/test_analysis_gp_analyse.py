import easyvvuq as uq
import chaospy as cp
import os
import pytest
import shutil
from easyvvuq.actions import CreateRunDirectory, Encode, ExecuteLocal, Decode, Actions


def test_gp(tmp_path):
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
    execute = ExecuteLocal("{} cooling_in.json".format(
        os.path.abspath("tests/cooling/cooling_model.py")))
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))
    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }
    sampler = uq.sampling.quasirandom.LHCSampler(vary=vary)

    campaign.add_app(name='test_app', params=params, actions=actions)
    campaign.set_app('test_app')
    campaign.set_sampler(sampler)
    campaign.execute(nsamples=100).collate()
    df = campaign.get_collation_result()
    analysis = uq.analysis.gp_analyse.GaussianProcessSurrogate(sampler, ['te'])
    result = analysis.analyse(df)
