import easyvvuq as uq
import chaospy as cp
import os
import sys
import pytest
import logging
from pprint import pformat, pprint
from gauss.encoder_gauss import GaussEncoder
from gauss.decoder_gauss import GaussDecoder

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


# If cannonsim has not been built (to do so, run the Makefile in tests/cannonsim/src/)
# then skip this test
if not os.path.exists("tests/cannonsim/bin/cannonsim"):
    pytest.skip(
        "Skipping cannonsim test (cannonsim is not installed in tests/cannonsim/bin/)",
        allow_module_level=True)


logging.basicConfig(level=logging.CRITICAL)

@pytest.fixture
def campaign():
    def _campaign(work_dir, campaign_name, app_name, params, encoder, decoder, sampler,
                      collater, actions, stats, vary, num_samples, replicas, db_type):
        my_campaign = uq.Campaign(name='cannon', work_dir=work_dir, db_type=db_type)
        print("Serialized encoder:", encoder.serialize())
        print("Serialized decoder:", decoder.serialize())
        # Add the cannonsim app
        my_campaign.add_app(name="cannonsim",
                            params=params,
                            encoder=encoder,
                            decoder=decoder)
        my_campaign.set_app("cannonsim")
        my_campaign.set_collater(collater)
        print("Serialized collation:", collater.serialize())
        print("Serialized sampler:", sampler.serialize())
        # Set the campaign to use this sampler
        my_campaign.set_sampler(sampler)
        # Draw 5 samples
        my_campaign.draw_samples(num_samples=num_samples, replicas=replicas)
        # Print the list of runs now in the campaign db
        print("List of runs added:")
        pprint(my_campaign.list_runs())
        print("---")
        # Encode all runs into a local directory
        pprint(
            f"Encoding all runs to campaign runs dir {my_campaign.get_campaign_runs_dir()}")
        my_campaign.populate_runs_dir()
        #assert(len(my_campaign.get_campaign_runs_dir()) > 0)
        #assert(os.path.exists(my_campaign.get_campaign_runs_dir()))
        #assert(os.path.isdir(my_campaign.get_campaign_runs_dir()))
        # Local execution
        my_campaign.apply_for_each_run_dir(actions)
        # Collate all data into one pandas data frame
        my_campaign.collate()
        print("data:", my_campaign.get_collation_result())
        # Save the state of the campaign
        state_file = work_dir + "cannonsim_state.json"
        my_campaign.save_state(state_file)
        my_campaign = None
        # Load state in new campaign object
        reloaded_campaign = uq.Campaign(state_file=state_file, work_dir=work_dir)
        reloaded_campaign.set_app("cannonsim")
        # Draw 3 more samples, execute, and collate onto existing dataframe
        print("Running 3 more samples...")
        reloaded_campaign.draw_samples(num_samples=num_samples, replicas=replicas)
        print("List of runs added:")
        pprint(reloaded_campaign.list_runs())
        print("---")
        reloaded_campaign.populate_runs_dir()
        reloaded_campaign.apply_for_each_run_dir(actions)
        print("Completed runs:")
        pprint(reloaded_campaign.scan_completed())
        print("All completed?", reloaded_campaign.all_complete())
        reloaded_campaign.collate()
        print("data:\n", reloaded_campaign.get_collation_result())
        print(reloaded_campaign)
        # Create a BasicStats analysis element and apply it to the campaign
        reloaded_campaign.apply_analysis(stats)
        print("stats:\n", reloaded_campaign.get_last_analysis())
        # Print the campaign log
        pprint(reloaded_campaign._log)
        print("All completed?", reloaded_campaign.all_complete())
    return _campaign


def test_cannonsim_csv(tmpdir, campaign):

    # Set up a fresh campaign called "cannon"

    # Define parameter space for the cannonsim app
    params = {
        "angle": {
            "type": "float",
            "min": 0.0,
            "max": 6.28,
            "default": 0.79},
        "air_resistance": {
            "type": "float",
            "min": 0.0,
            "max": 1.0,
            "default": 0.2},
        "height": {
            "type": "float",
            "min": 0.0,
            "max": 1000.0,
            "default": 1.0},
        "time_step": {
            "type": "float",
            "min": 0.0001,
            "max": 1.0,
            "default": 0.01},
        "gravity": {
            "type": "float",
            "min": 0.0,
            "max": 1000.0,
            "default": 9.8},
        "mass": {
            "type": "float",
            "min": 0.0001,
            "max": 1000.0,
            "default": 1.0},
        "velocity": {
            "type": "float",
            "min": 0.0,
            "max": 1000.0,
            "default": 10.0}}

    # Create an encoder and decoder for the cannonsim app
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/cannonsim/test_input/cannonsim.template',
        delimiter='#',
        target_filename='in.cannon')
    decoder = uq.decoders.SimpleCSV(
        target_filename='output.csv', output_columns=[
            'Dist', 'lastvx', 'lastvy'], header=0)
    # Create a collation element for this campaign
    collater = uq.collate.AggregateSamples(average=False)
    actions = uq.actions.ExecuteLocal("tests/cannonsim/bin/cannonsim in.cannon output.csv")
    stats = uq.analysis.BasicStats(qoi_cols=['Dist', 'lastvx', 'lastvy'])
    # Make a random sampler
    vary = {
        "angle": cp.Uniform(0.0, 1.0),
        "height": cp.Uniform(2.0, 10.0),
        "velocity": cp.Normal(10.0, 1.0),
        "mass": cp.Uniform(5.0, 1.0)
    }
    sampler = uq.sampling.RandomSampler(vary=vary)
    campaign(tmpdir, 'cannon', 'cannonsim', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 5, 1, db_type='sql')
    campaign(tmpdir, 'cannon', 'cannonsim', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 5, 1, db_type='json')


def test_gauss(tmpdir, campaign):
    params = {
        "sigma": {
            "type": "real",
            "min": "0.0",
            "max": "100000.0",
            "default": "0.25"
        },
        "mu": {
            "type": "real",
            "min": "0.0",
            "max": "100000.0",
            "default": "1"
        },
        "num_steps": {
            "type": "int",
            "min": "0",
            "max": "100000",
            "default": "10"
        },
        "out_file": {
            "type": "str",
            "default": "output.csv"
        }
    }
    encoder = uq.encoders.GenericEncoder(template_fname='tests/gauss/gauss.template',
                                         target_filename='gauss_in.json')
    decoder = GaussDecoder(target_filename=params['out_file']['default'])
    collater = uq.collate.AggregateSamples(average=False)
    actions = uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_in.json")
    stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
    vary = {
        "mu": cp.Uniform(1.0, 100.0),
    }
    sampler = uq.sampling.RandomSampler(vary=vary)
    campaign(tmpdir, 'gauss', 'gauss', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 3, 5, db_type='sql')
    campaign(tmpdir, 'gauss', 'gauss', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 3, 5, db_type='json')


def test_gauss_custom_encoder(tmpdir, campaign):
    params = {
        "sigma": {"type": "real", "min": "0.0", "max": "100000.0",
                  "default": "0.25"},
        "mu": {"type": "real", "min": "0.0", "max": "100000.0",
               "default": "1"},
        "num_steps": {"type": "int", "min": "0", "max": "100000",
                      "default": "10"},
        "out_file": {"type": "str", "default": "output.csv"}
    }
    # Create an encoder and decoder for the gauss app
    encoder = GaussEncoder(target_filename='gauss_in.json')
    decoder = GaussDecoder(target_filename=params['out_file']['default'])
    # Create a collation element for this campaign
    collater = uq.collate.AggregateSamples(average=False)
    actions = uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_in.json")
    stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
    vary = {
        "mu": cp.Uniform(1.0, 100.0),
    }
    sampler = uq.sampling.RandomSampler(vary=vary)
    campaign(tmpdir, 'gauss', 'gauss', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 3, 5, db_type='sql')
    campaign(tmpdir, 'gauss', 'gauss', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 3, 5, db_type='json')


def test_gauss_fix(tmpdir, campaign):
    params = {
        "sigma": {"type": "real", "min": "0.0", "max": "100000.0",
                  "default": "0.25"},
        "mu": {"type": "real", "min": "0.0", "max": "100000.0",
               "default": "1"},
        "num_steps": {"type": "int", "min": "0", "max": "100000",
                      "default": "10"},
        "out_file": {"type": "str", "default": "output.csv"},
        "bias": {"type": "fixture", "options": ["bias1", "bias2"],
                 "default": "bias1"}
    }
    fixtures = {
        "bias1": {"type": "file", "path": "tests/gauss/bias1.txt",
                  "common": False, "exists_local": True,
                  "target": "", "group": ""},
        "bias2": {"type": "file", "path": "tests/gauss/bias2.txt",
                  "common": False, "exists_local": True,
                  "target": "", "group": ""}
    }
    number_of_samples = 2
    number_of_replicas = 2
    encoder = uq.encoders.GenericEncoder(template_fname='tests/gauss/gauss.template',
                                         target_filename='gauss_in.json')
    decoder = GaussDecoder(target_filename=params['out_file']['default'])
    collater = uq.collate.AggregateSamples(average=False)
    actions = uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_in.json")
    stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
    vary = {
        "mu": cp.Uniform(1.0, 100.0),
    }
    sampler = uq.sampling.RandomSampler(vary=vary)
    campaign(tmpdir, 'gauss', 'gauss', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 3, 5, db_type='sql')
    campaign(tmpdir, 'gauss', 'gauss', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 3, 5, db_type='json')


def test_pce(tmpdir, campaign):
    # Define parameter space
    params = {
        "kappa": {
            "type": "real",
            "min": "0.0",
            "max": "0.1",
            "default": "0.025"},
        "t_env": {
            "type": "real",
            "min": "0.0",
            "max": "40.0",
            "default": "15.0"},
        "out_file": {
            "type": "str",
            "default": "output.csv"}}
    output_filename = params["out_file"]["default"]
    output_columns = ["te", "ti"]
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/pce/pce.template',
        delimiter='$',
        target_filename='pce_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns,
                                    header=0)
    # Create a collation element for this campaign
    collater = uq.collate.AggregateSamples(average=False)
    # Create the sampler
    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }
    sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=3)
    actions = uq.actions.ExecuteLocal("tests/pce/pce_model.py pce_in.json")
    # Post-processing analysis
    stats = uq.analysis.PCEAnalysis(sampler=sampler,
                                        qoi_cols=output_columns)
    campaign(tmpdir, 'pce', 'pce', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 0, 1, db_type='sql')
    #campaign(tmpdir, 'pce', 'pce', params, encoder, decoder, sampler,
    #             collater, actions, stats, vary, 0, 1, db_type='json')


def test_sc(tmpdir, campaign):
    params = {
        "Pe": {
            "type": "real",
            "min": "1.0",
            "max": "2000.0",
            "default": "100.0"},
        "f": {
            "type": "real",
            "min": "0.0",
            "max": "10.0",
            "default": "1.0"},
        "out_file": {
            "type": "str",
            "default": "output.csv"}}
    output_filename = params["out_file"]["default"]
    output_columns = ["u"]
    encoder = uq.encoders.GenericEncoder(
        template_fname=f'tests/sc/sc.template',
        delimiter='$',
        target_filename='sc_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns,
                                    header=0)
    collater = uq.collate.AggregateSamples(average=False)
    vary = {
        "Pe": cp.Uniform(100.0, 200.0),
        "f": cp.Normal(1.0, 0.1)
    }
    sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=1)
    actions = uq.actions.ExecuteLocal(f"tests/sc/sc_model.py sc_in.json")
    stats = uq.analysis.SCAnalysis(sampler=sampler, qoi_cols=output_columns)
    campaign(tmpdir, 'sc', 'sc', params, encoder, decoder, sampler,
             collater, actions, stats, vary, 0, 1, db_type='sql')
    #campaign(tmpdir, 'sc', 'sc', params, encoder, decoder, sampler,
    #             collater, actions, stats, vary, 0, 1, db_type='json')
    
