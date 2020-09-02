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


def test_multiencoder(tmpdir):

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

    # Specify a complicated directory hierarchy to test the DirectoryBuilder encoder
    directory_tree = {'dir1': {'dir2': {'dir3': None, 'dir4': None}}, 'dir5': {'dir6': None}}

    # Create a multiencoder combining a directory build, and two template encodes
    multiencoder = uq.encoders.MultiEncoder(

        uq.encoders.DirectoryBuilder(tree=directory_tree),

        uq.encoders.GenericEncoder(
            template_fname='tests/cannonsim/test_input/cannonsim.template',
            delimiter='#',
            target_filename='dir1/dir2/dir3/in.cannon'
        ),

        uq.encoders.GenericEncoder(
            template_fname='tests/cannonsim/test_input/cannonsim.template',
            delimiter='#',
            target_filename='dir5/dir6/in.cannon.2'
        )
    )

    # Create decoder and collater for the cannonsim app
    decoder = uq.decoders.SimpleCSV(
        target_filename='output.csv', output_columns=[
            'Dist', 'lastvx', 'lastvy'], header=0)
    collater = uq.collate.AggregateSamples(average=False)

    # Add the cannonsim app
    my_campaign.add_app(name="cannonsim",
                        params=params,
                        encoder=multiencoder,
                        decoder=decoder,
                        collater=collater)

    # Set the active app to be cannonsim (this is redundant when only one app
    # has been added)
    my_campaign.set_app("cannonsim")

    # Set up sampler
    sweep1 = {
        "angle": [0.1, 0.2, 0.3],
        "height": [2.0, 10.0],
        "velocity": [10.0, 10.1, 10.2]
    }
    sampler = uq.sampling.BasicSweep(sweep=sweep1)

    # Set the campaign to use this sampler
    my_campaign.set_sampler(sampler)

    # Test reloading
    my_campaign.save_state(tmpdir + "test_multiencoder.json")
    reloaded_campaign = uq.Campaign(state_file=tmpdir + "test_multiencoder.json", work_dir=tmpdir)

    # Draw all samples
    my_campaign.draw_samples()

    # Print the list of runs now in the campaign db
    print("List of runs added:")
    pprint(my_campaign.list_runs())
    print("---")

    # Encode and execute.
    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(
        uq.actions.ExecuteLocal("tests/cannonsim/bin/cannonsim dir5/dir6/in.cannon.2 output.csv"))

    print("Runs list after encoding and execution:")
    pprint(my_campaign.list_runs())

    # Collate all data into one pandas data frame
    my_campaign.collate()
    print("data:", my_campaign.get_collation_result())

    # Create a BasicStats analysis element and apply it to the campaign
    stats = uq.analysis.BasicStats(qoi_cols=['Dist', 'lastvx', 'lastvy'])
    my_campaign.apply_analysis(stats)
    print("stats:\n", my_campaign.get_last_analysis())

    # Print the campaign log
    pprint(my_campaign._log)

    print("All completed?", my_campaign.all_complete())


if __name__ == "__main__":
    test_multiencoder("/tmp/")
