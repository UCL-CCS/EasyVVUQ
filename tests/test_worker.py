import easyvvuq as uq
import chaospy as cp
import os
import sys
import pytest
from easyvvuq.constants import default_campaign_prefix, Status
from pprint import pprint
import subprocess

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


def test_worker(tmpdir):

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
            "type": "integer",
            "min": 0,
            "max": 1000,
            "default": 1},
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

    # Make a random sampler
    vary = {
        "angle": cp.Uniform(0.0, 1.0),
        "height": cp.DiscreteUniform(0, 100),
        "velocity": cp.Normal(10.0, 1.0),
        "mass": cp.Uniform(5.0, 1.0)
    }
    sampler1 = uq.sampling.RandomSampler(vary=vary)

    print("Serialized sampler:", sampler1.serialize())

    # Set the campaign to use this sampler
    my_campaign.set_sampler(sampler1)

    # Draw 5 samples
    my_campaign.draw_samples(num_samples=5)

    # Print the list of runs now in the campaign db
    print("List of runs added:")
    pprint(my_campaign.list_runs())
    print("---")

    # User defined function
    def encode_and_execute_cannonsim(run_id, run_data):
        enc_args = [
            my_campaign.db_type,
            my_campaign.db_location,
            'FALSE',
            "cannon",
            "cannonsim",
            run_id
        ]
        encoder_path = os.path.realpath(os.path.expanduser("easyvvuq/tools/external_encoder.py"))
        try:
            subprocess.run(['python3', encoder_path] + enc_args, check=True)
        except subprocess.CalledProcessError as e:
            sys.exit(f"Failed during encoding of run: f{e}")

        try:
            subprocess.run([CANNONSIM_PATH, "in.cannon", "output.csv"],
                           cwd=run_data['run_dir'], check=True)
        except subprocess.CalledProcessError as e:
            sys.exit(f"Failed during execution of run: f{e}")

        my_campaign.campaign_db.set_run_statuses([run_id], Status.ENCODED)  # see note further down

    # Encode and execute. Note to call function for all runs with status NEW (and not ENCODED)
    my_campaign.call_for_each_run(encode_and_execute_cannonsim, status=uq.constants.Status.NEW)

    ####
    # Important note: In this example the execution is done with subprocess which is blocking.
    # However, in practice this will be some sort of middleware (e.g. PJM) which is generally
    # non-blocking. In such a case it is the job of the middleware section to keep track of
    # which runs have been encoded, and updating the database (all at the end if need be) to
    # indicate this to EasyVVUQ _before_ trying to run the collation/analysis section. If
    # EasyVVUQ has not been informed that runs have been encoded, it will most likely just tell
    # you that 'nothing has been collated' or something to that effect.
    ####

    print("Runs list after encoding and execution:")
    pprint(my_campaign.list_runs())

    # Collate all data into one pandas data frame
    my_campaign.collate()
    print("data:", my_campaign.get_collation_result())

    # Create a BasicStats analysis element and apply it to the campaign
    stats = uq.analysis.BasicStats(qoi_cols=['Dist', 'lastvx', 'lastvy'])
    my_campaign.apply_analysis(stats)
    print("stats:\n", my_campaign.get_last_analysis())

    bootstrap = uq.analysis.EnsembleBoot(groupby=['Dist'], qoi_cols=['lastv'])
    with pytest.raises(RuntimeError, match=r".* lastv"):
        my_campaign.apply_analysis(bootstrap)

    # Print the campaign log
    pprint(my_campaign._log)

    print("All completed?", my_campaign.all_complete())


if __name__ == "__main__":
    test_worker("/tmp/")
