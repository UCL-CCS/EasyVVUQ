import easyvvuq as uq
import chaospy as cp
import os
import sys
import pytest
import itertools
import tempfile

@pytest.mark.parametrize(
    'encoder,decoder,sampler_analysis',
    itertools.product(
        [uq.encoders.GenericEncoder(
            template_fname='tests/cooling/cooling.template',
            delimiter='$',
            target_filename='cooling_in.json')],
        [uq.decoders.SimpleCSV(
            target_filename='output.csv',
            output_columns=['te']),
         uq.decoders.JSONDecoder(
            target_filename='output.json',
            output_columns=['te'])],
        [(uq.sampling.PCESampler, uq.analysis.PCEAnalysis),
         (uq.sampling.SCSampler, uq.analysis.SCAnalysis)]))
def test_full_campaign(encoder, decoder, sampler_analysis):
    with tempfile.TemporaryDirectory() as tmp_path:
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
                "default": "output.csv"
            }
        }
        vary = {
            "kappa": cp.Uniform(0.025, 0.075),
            "t_env": cp.Uniform(15, 25)
        }
        sampler, analysis = sampler_analysis
        sampler = sampler(vary)
        analysis = analysis(sampler, qoi_cols=['te'])
        actions = uq.actions.ExecuteLocal("tests/cooling/cooling_model.py cooling_in.json")
        campaign = uq.Campaign(
            name='test_campaign', work_dir=tmp_path, db_location='sqlite:///:memory:')
        campaign.add_app(name='test_app',
                         params=params,
                         encoder=encoder,
                         decoder=decoder)
        campaign.set_app('test_app')
        campaign.set_sampler(sampler)
        campaign.draw_samples()
        campaign.populate_runs_dir()
        campaign.apply_for_each_run_dir(actions)
        campaign.collate()
        df = campaign.get_collation_result()
        result = analysis.analyse(df)
    
