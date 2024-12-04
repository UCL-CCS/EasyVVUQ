import easyvvuq as uq
from easyvvuq.actions import Actions, Encode, Decode, CreateRunDirectory
import chaospy as cp
import os
import pytest

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

CANNONSIM_PATH = os.path.realpath(os.path.expanduser("tests/cannonsim/bin/cannonsim"))


def setup_cannonsim_app():
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

    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/cannonsim/test_input/cannonsim.template',
        delimiter='#',
        target_filename='in.cannon')
    decoder = uq.decoders.SimpleCSV(
        target_filename='output.csv', output_columns=[
            'Dist', 'lastvx', 'lastvy'])

    vary = {
        "gravity": cp.Uniform(1.0, 9.8),
        "mass": cp.Uniform(2.0, 10.0),
    }
    cannon_sampler = uq.sampling.RandomSampler(vary=vary, max_num=5)
    cannon_action = uq.actions.ExecuteLocal(os.path.abspath("tests/cannonsim/bin/cannonsim") +
                                            " in.cannon output.csv")
    cannon_stats = uq.analysis.BasicStats(qoi_cols=['Dist', 'lastvx', 'lastvy'])
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), cannon_action, Decode(decoder))
    return params, cannon_sampler, actions, cannon_stats


def setup_cooling_app():
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
    cooling_sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=3)
    cooling_action = uq.actions.ExecuteLocal(os.path.abspath("tests/cooling/cooling_model.py") +
                                             " cooling_in.json")
    cooling_stats = uq.analysis.PCEAnalysis(sampler=cooling_sampler, qoi_cols=output_columns)
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), cooling_action, Decode(decoder))
    return params, cooling_sampler, actions, cooling_stats


def test_multiapp(tmpdir):

    campaign = uq.Campaign(name='multiapp', work_dir=tmpdir, db_location='sqlite:///')

    # Add the cannonsim app to the campaign
    (params, cannon_sampler, cannon_action, cannon_stats) = setup_cannonsim_app()
    campaign.add_app(name="cannonsim",
                     params=params,
                     actions=cannon_action)

    campaign.set_app("cannonsim")
    campaign.set_sampler(cannon_sampler)

    # Add the cooling app to the campaign
    (params, cooling_sampler, cooling_action, cooling_stats) = setup_cooling_app()
    campaign.add_app(name="cooling",
                     params=params,
                     actions=cooling_action)

    # Populate the runs dirs for runs belonging to the cannonsim app
    campaign.set_app("cannonsim")
    campaign.set_sampler(cannon_sampler)
    campaign.execute().collate()

    # Populate the runs dirs for runs belonging to the cooling app
    campaign.set_app("cooling")
    campaign.set_sampler(cooling_sampler)
    campaign.execute().collate()

    campaign.set_app("cannonsim")

    campaign.set_app("cooling")

    # Apply analysis for cannon app
    campaign.set_app("cannonsim")
    campaign.set_sampler(cannon_sampler, True)
    campaign.apply_analysis(cannon_stats)

    cannonsim_df = campaign.get_collation_result()

    # Apply analysis for cooling app
    campaign.set_app("cooling")
    campaign.set_sampler(cooling_sampler, True)
    campaign.apply_analysis(cooling_stats)

    cooling_df = campaign.get_collation_result

    assert (not cannonsim_df.equals(cooling_df))


if __name__ == "__main__":
    test_multiapp("/tmp/")
