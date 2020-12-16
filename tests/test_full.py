import easyvvuq as uq
import chaospy as cp
import os
import sys
import pytest
import itertools

VARY = {
    "kappa": cp.Uniform(0.025, 0.075),
    "t_env": cp.Uniform(15, 25)
}

@pytest.mark.parametrize(
    'encoder,decoder,sampler_analysis',
    itertools.product(
        [uq.encoders.GenericEncoder(
            template_fname='tests/cooling/cooling.template',
            delimiter='$',
            target_filename='cooling_in.json')],
        [uq.decoders.SimpleCSV(
            target_filename='output.csv',
            output_columns=['te'])],
        [(uq.sampling.PCESampler(vary=VARY, polynomial_order=3), uq.analysis.PCEAnalysis),
         (uq.sampling.SCSampler(vary=VARY), uq.analysis.SCAnalysis)]))
def test_full_campaign(tmp_path, encoder, decoder, sampler_analysis):
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
    sampler, analysis = sampler_analysis
    actions = uq.actions.ExecuteLocal("tests/cooling/cooling_model.py cooling_in.json")
    campaign = uq.Campaign(name='test_campaign', work_dir=tmp_path)
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
    campaign.get_collation_result()
