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


# If cannonsim has not been built (to do so, run the Makefile in
# tests/cannonsim/src/) then skip this test
if not os.path.exists("tests/cannonsim/bin/cannonsim"):
    pytest.skip(
        "Skipping cannonsim test (cannonsim is not installed in "
        "tests/cannonsim/bin/)",
        allow_module_level=True)


def test_cannonsim_csv_jsondb(tmpdir):

    # Set up a fresh campaign called "cannon"
    my_campaign = uq.Campaign(name='cannon', work_dir=tmpdir, db_type="json")

    # Define parameter space for the cannonsim app
    params = {
        "angle": {
            "type": "real",
            "min": "0.0",
            "max": "6.28",
            "default": "0.79",
            "variable": "True"},
        "air_resistance": {
            "type": "real",
            "min": "0.0",
            "max": "1.0",
            "default": "0.2",
            "variable": "True"},
        "height": {
            "type": "real",
            "min": "0.0",
            "max": "1000.0",
            "default": "1.0",
            "variable": "True"},
        "time_step": {
            "type": "real",
                    "min": "0.0001",
                    "max": "1.0",
                    "default": "0.01",
                    "variable": "True"},
        "gravity": {
            "type": "real",
            "min": "0.0",
            "max": "1000.0",
            "default": "9.8",
            "variable": "True"},
        "mass": {
            "type": "real",
            "min": "0.0001",
            "max": "1000.0",
            "default": "1.0",
            "variable": "True"},
        "velocity": {
            "type": "real",
            "min": "0.0",
            "max": "1000.0",
            "default": "10.0",
            "variable": "True"}}

    # Create an encoder, decoder and collation element for the cannonsim app
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/cannonsim/test_input/cannonsim.template',
        delimiter='#',
        target_filename='in.cannon')
    decoder = uq.decoders.SimpleCSV(
        target_filename='output.csv', output_columns=[
            'Dist', 'lastvx', 'lastvy'], header=0)
    collation = uq.collate.AggregateSamples(average=False)

    print("Serialized encoder:", encoder.serialize())
    print("Serialized decoder:", decoder.serialize())
    print("Serialized collation:", collation.serialize())

    # Add the cannonsim app
    my_campaign.add_app(name="cannonsim",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collation=collation
                        )

    # Set the active app to be cannonsim
    my_campaign.set_app("cannonsim")

    # Make a random sampler
    vary = {
        "angle": cp.Uniform(0.0, 1.0),
        "height": cp.Uniform(2.0, 10.0),
        "velocity": cp.Normal(10.0, 1.0),
        "mass": cp.Uniform(5.0, 1.0)
    }
    sampler1 = uq.sampling.RandomSampler(vary=vary)

    # Set the campaign to use this sampler
    my_campaign.set_sampler(sampler1)

    # Draw 5 samples
    my_campaign.draw_samples(num_samples=5)

    # Print the list of runs now in the campaign db
    print("List of runs added:")
    pprint(my_campaign.list_runs())
    print("---")

    # Encode all runs into a local directory
    print(
        f"Encoding all runs to campaign runs "
        f"dir {my_campaign.get_campaign_runs_dir()}")
    my_campaign.populate_runs_dir()

    assert(len(my_campaign.get_campaign_runs_dir()) > 0)
    assert(os.path.exists(my_campaign.get_campaign_runs_dir()))
    assert(os.path.isdir(my_campaign.get_campaign_runs_dir()))

    # Local execution
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
        "tests/cannonsim/bin/cannonsim in.cannon output.csv"))

    # Collate all data into one pandas data frame
    my_campaign.collate(store=False)
    print("data:", my_campaign.get_last_collation())

    # Create a BasicStats analysis element and apply it to the campaign
    stats = uq.analysis.BasicStats(
        params_cols=['Dist', 'lastvx', 'lastvy'])
    my_campaign.apply_analysis(stats)
    print("stats:", my_campaign.get_last_analysis())


if __name__ == "__main__":
    test_cannonsim_csv_jsondb("/tmp/")
