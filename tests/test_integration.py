import easyvvuq as uq
import chaospy as cp
import os
import sys
import pytest
import logging
from pprint import pformat, pprint
from .gauss.encoder_gauss import GaussEncoder
from .gauss.decoder_gauss import GaussDecoder
from easyvvuq.actions import CreateRunDirectory, Encode, ExecuteLocal, Decode, Actions


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

cannonsim_path = os.path.realpath(os.path.expanduser("tests/cannonsim/bin/cannonsim"))


def execute_cannonsim(path, params):
    os.system(f"cd {path} && {cannonsim_path} in.cannon output.csv")


logging.basicConfig(level=logging.CRITICAL)


@pytest.fixture
def campaign():
    def _campaign(work_dir, campaign_name, app_name, params, encoder, decoder, sampler,
                  actions, stats, vary, num_samples=0, replicas=1, db_type='sql',
                  call_fn=None):
        my_campaign = uq.Campaign(name=campaign_name, work_dir=work_dir)
        db_location = my_campaign.db_location
        # Add the cannonsim app
        actions_ = Actions(CreateRunDirectory('/tmp'), Encode(encoder), actions, Decode(decoder))
        my_campaign.add_app(name=app_name,
                            params=params,
                            actions=actions_)
        my_campaign.set_app(app_name)
        # Set the campaign to use this sampler
        my_campaign.set_sampler(sampler)
        my_campaign.execute(nsamples=num_samples, sequential=True).collate()
        my_campaign = None
        # Load state in new campaign object
        reloaded_campaign = uq.Campaign(name=campaign_name, db_location=db_location)
        reloaded_campaign.set_app(app_name)
        reloaded_campaign.execute(nsamples=num_samples).collate()
        # Draw 3 more samples, execute, and collate onto existing dataframe
        # reloaded_campaign.draw_samples(num_samples=num_samples, replicas=replicas)
        # reloaded_campaign.collate()
        if stats is not None:
            reloaded_campaign.apply_analysis(stats)
    return _campaign


def test_cannonsim(tmpdir, campaign):
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
            'Dist', 'lastvx', 'lastvy'])
    # Create a collation element for this campaign
    actions = uq.actions.ExecuteLocal(
        os.path.abspath("tests/cannonsim/bin/cannonsim") +
        " in.cannon output.csv")
    stats = uq.analysis.BasicStats(qoi_cols=['Dist', 'lastvx', 'lastvy'])
    # Make a random sampler
    vary = {
        "angle": cp.Uniform(0.0, 1.0),
        "height": cp.Uniform(2.0, 10.0),
        "velocity": cp.Normal(10.0, 1.0),
        "mass": cp.Uniform(1.0, 5.0)
    }
    sampler = uq.sampling.RandomSampler(vary=vary)
    campaign(
        work_dir=tmpdir,
        campaign_name='cannon',
        app_name='cannonsim',
        params=params,
        encoder=encoder,
        decoder=decoder,
        sampler=sampler,
        actions=actions,
        stats=stats,
        vary=vary,
        num_samples=5,
        replicas=1)
    # Make a sweep sampler
    sweep = {
        "angle": [0.1, 0.2, 0.3],
        "height": [2.0, 10.0],
        "velocity": [10.0, 10.1, 10.2]
    }
    sampler = uq.sampling.BasicSweep(sweep=sweep)
    campaign(
        work_dir=tmpdir,
        campaign_name='cannonsim',
        app_name='cannonsim',
        params=params,
        encoder=encoder,
        decoder=decoder,
        sampler=sampler,
        actions=actions,
        stats=None,
        vary=sweep,
        num_samples=5,
        replicas=1)


# def test_gauss(tmpdir, campaign):
#     params = {
#         "sigma": {
#             "type": "float",
#             "min": 0.0,
#             "max": 100000.0,
#             "default": 0.25
#         },
#         "mu": {
#             "type": "float",
#             "min": 0.0,
#             "max": 100000.0,
#             "default": 1
#         },
#         "num_steps": {
#             "type": "integer",
#             "min": 0,
#             "max": 100000,
#             "default": 10
#         },
#         "out_file": {
#             "type": "string",
#             "default": "output.csv"
#         },
#         "bias": {
#             "type": "fixture",
#             "allowed": ["bias1", "bias2"],
#             "default": "bias1"
#         }
#     }
#     fixtures = {
#         "bias1": {
#             "type": "file", "path": "tests/gauss/bias1.txt",
#             "common": False, "exists_local": True,
#             "target": "",
#             "group": ""
#         },
#         "bias2": {
#             "type": "file", "path": "tests/gauss/bias2.txt",
#             "common": False, "exists_local": True,
#             "target": "",
#             "group": ""
#         }
#     }
#     encoder = uq.encoders.GenericEncoder(template_fname='tests/gauss/gauss.template',
#                                          target_filename='gauss_in.json')
#     fixtures_encoder = uq.encoders.ApplyFixtures(fixtures=fixtures)
#     encoder_with_fixtures = uq.encoders.MultiEncoder(encoder, fixtures_encoder)

#     decoder = GaussDecoder(target_filename=params['out_file']['default'])
#     actions = uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_in.json")
#     stats = uq.analysis.EnsembleBoot(groupby=[("mu", 0)], qoi_cols=[("numbers", 0)])
#     vary = {
#         "mu": cp.Uniform(1.0, 100.0),
#     }
#     sampler = uq.sampling.RandomSampler(vary=vary)
#     campaign(tmpdir, 'gauss', 'gauss', params, encoder, decoder,
#              sampler, actions, stats, vary, 2, 2)
#     encoder = GaussEncoder(target_filename='gauss_in.json')
#     campaign(tmpdir, 'gauss', 'gauss', params, encoder, decoder,
#              sampler, actions, stats, vary, 2, 2)
#     campaign(tmpdir, 'gauss', 'gauss', params, encoder_with_fixtures, decoder,
#              sampler, actions, stats, vary, 2, 2)


def test_pce(tmpdir, campaign):
    # Define parameter space
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
    # Create the sampler
    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }
    sampler = uq.sampling.PCESampler(vary=vary,
                                     polynomial_order=3)
    actions = uq.actions.ExecuteLocal(
        os.path.abspath("tests/cooling/cooling_model.py") +
        " cooling_in.json")
    stats = uq.analysis.PCEAnalysis(sampler=sampler,
                                    qoi_cols=output_columns)
    campaign(tmpdir, 'pce', 'pce', params, encoder, decoder, sampler, actions, stats, vary, 0, 1)


def test_sc(tmpdir, campaign):
    params = {
        "Pe": {
            "type": "float",
            "min": "1.0",
            "max": "2000.0",
            "default": "100.0"},
        "f": {
            "type": "float",
            "min": "0.0",
            "max": "10.0",
            "default": "1.0"},
        "out_file": {
            "type": "string",
            "default": "output.csv"}}
    output_filename = params["out_file"]["default"]
    output_columns = ["u"]
    encoder = uq.encoders.GenericEncoder(
        template_fname=f'tests/sc/sc.template',
        delimiter='$',
        target_filename='sc_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns)
    vary = {
        "Pe": cp.Uniform(100.0, 200.0),
        "f": cp.Normal(1.0, 0.1)
    }
    sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=1)
    actions = uq.actions.ExecuteLocal(os.path.abspath("tests/sc/sc_model.py") + " sc_in.json")
    stats = uq.analysis.SCAnalysis(sampler=sampler, qoi_cols=output_columns)
    campaign(tmpdir, 'sc', 'sc', params, encoder, decoder, sampler, actions, stats, vary, 0, 1)


# def test_qmc(tmpdir, campaign):
#     # Define parameter space
#     params = {
#         "temp_init": {
#             "type": "float",
#             "min": 0.0,
#             "max": 100.0,
#             "default": 95.0},
#         "kappa": {
#             "type": "float",
#             "min": 0.0,
#             "max": 0.1,
#             "default": 0.025},
#         "t_env": {
#             "type": "float",
#             "min": 0.0,
#             "max": 40.0,
#             "default": 15.0},
#         "out_file": {
#             "type": "string",
#             "default": "output.csv"}}
#     output_filename = params["out_file"]["default"]
#     output_columns = ["te"]
#     # Create an encoder and decoder for QMC test app
#     encoder = uq.encoders.GenericEncoder(
#         template_fname='tests/cooling/cooling.template',
#         delimiter='$',
#         target_filename='cooling_in.json')
#     decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
#                                     output_columns=output_columns,
#                                     header=0)
#     # Create a collation element for this campaign
#     collater = uq.collate.AggregateSamples(average=False)
#     # Create the sampler
#     vary = {
#         "kappa": cp.Uniform(0.025, 0.075),
#         "t_env": cp.Uniform(15, 25)
#     }
#     sampler = uq.sampling.QMCSampler(vary=vary,
#                                      n_mc_samples=10)
#     actions = uq.actions.ExecuteLocal("tests/cooling/cooling_model.py cooling_in.json")
#     stats = uq.analysis.QMCAnalysis(sampler=sampler,
#                                     qoi_cols=output_columns)
#     campaign(tmpdir, 'qmc2', 'qmc2', params, encoder, decoder, sampler,
#              collater, actions, stats, vary, 10, 1)
