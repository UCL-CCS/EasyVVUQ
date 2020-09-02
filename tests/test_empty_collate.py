import easyvvuq as uq
import chaospy as cp
import os
import sys
import pytest
from pprint import pprint

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


def test_empty_collate(tmpdir):

    # Set up a fresh campaign called "cannon"
    my_campaign = uq.Campaign(name='cannon', work_dir=tmpdir)

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

    # Create an encoder, decoder and collater for the cannonsim app
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/cannonsim/test_input/cannonsim.template',
        delimiter='#',
        target_filename='in.cannon')
    decoder = uq.decoders.SimpleCSV(
        target_filename='output.csv', output_columns=[
            'Dist', 'lastvx', 'lastvy'], header=0)
    collater = uq.collate.AggregateSamples(average=False)

    # Add the cannonsim app
    my_campaign.add_app(name="cannonsim",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)

    # Set the active app to be cannonsim (this is redundant when only one app
    # has been added)
    my_campaign.set_app("cannonsim")

    # Set up samplers
    vary = {
        "gravity": cp.Uniform(9.8, 1.0),
        "mass": cp.Uniform(2.0, 10.0),
    }
    sampler = uq.sampling.RandomSampler(vary=vary, max_num=5)

    # Set the campaign to use this sampler
    my_campaign.set_sampler(sampler)

    # Test reloading
    my_campaign.save_state(tmpdir + "test_multisampler.json")
    reloaded_campaign = uq.Campaign(state_file=tmpdir + "test_multisampler.json", work_dir=tmpdir)

    # Draw all samples
    my_campaign.draw_samples()

    # Encode
    my_campaign.populate_runs_dir()

    # Do an early collation, before anything has been executed. This means the collation element
    # may attempt to add an empty dataframe to the database (which will cause issues upon subsequent
    # collates due to an empty set of columns (Issue 163).
    my_campaign.collate()

    # Execute
    my_campaign.apply_for_each_run_dir(
        uq.actions.ExecuteLocal("tests/cannonsim/bin/cannonsim in.cannon output.csv"))

    # Attempt to collate() again, now that the runs have been executed. If Issue 163 is not
    # fixed then an error will occur here.
    my_campaign.collate()
    print("data:", my_campaign.get_collation_result())

    pprint(my_campaign._log)


if __name__ == "__main__":
    test_empty_collate("/tmp/")
