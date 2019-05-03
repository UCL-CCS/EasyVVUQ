import easyvvuq as uq
import chaospy as cp
import os
import sys
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


def test_cannonsim_csv(tmpdir):

    # Params for testing
    number_of_samples = 15

    my_campaign = uq.Campaign(name='cannon', workdir=tmpdir)

    assert(my_campaign is not None)

    # Define parameter space for the cannonsim app
    params = {
        "angle":            {"type": "real", "min": "0.0",    "max": "6.28",   "default": "0.79", "variable": "True"},
        "air_resistance":   {"type": "real", "min": "0.0",    "max": "1.0",    "default": "0.2",  "variable": "True"},
        "height":           {"type": "real", "min": "0.0",    "max": "1000.0", "default": "1.0",  "variable": "True"},
        "time_step":        {"type": "real", "min": "0.0001", "max": "1.0",    "default": "0.01", "variable": "True"},
        "gravity":          {"type": "real", "min": "0.0",    "max": "1000.0", "default": "9.8",  "variable": "True"},
        "mass":             {"type": "real", "min": "0.0001", "max": "1000.0", "default": "1.0",  "variable": "True"},
        "velocity":         {"type": "real", "min": "0.0",    "max": "1000.0", "default": "10.0", "variable": "True"}
    }

    # Add the cannonsim app
    my_campaign.add_app({
                        "name": "cannonsim", # TODO Tell campaign to "use_app('appname')" to declutter this input line
                        "input_encoder":"generic_template", "encoder_options":{"delimiter":'#'}, # TODO Pass the encoder object directly and have it serialize itself rather than the user needing to do it here
                        "output_decoder":"csv", # TODO Pass decoder object directly and have campaign serialize it to store it
                        "params": params # TODO Allow params to be added to app programmatically
                        })

    # Set the active app to be cannonsim
    my_campaign.set_app("cannonsim")

    # Make a random sampler
    vary = {
        "angle": cp.Uniform(0.0, 1.0),
        "height": cp.Uniform(2.0, 10.0),
        "velocity": cp.Normal(10.0, 1.0),
        "mass": cp.Uniform(5.0, 1.0)
    }
    sampler1 = uq.elements.sampling.RandomSampler(vary=vary)

    my_campaign.set_sampler(sampler1)

    sys.exit(0)


    my_campaign.add_runs(random_sampler, max_num=number_of_samples)

    assert(len(my_campaign.runs) == number_of_samples)

    print(my_campaign.log)

    my_campaign.populate_runs_dir()

    assert(len(my_campaign.runs_dir) > 0)
    assert(os.path.exists(my_campaign.runs_dir))
    assert(os.path.isdir(my_campaign.runs_dir))

    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
        "tests/cannonsim/bin/cannonsim input.cannon output.csv"))

    output_filename = 'output.csv'
    output_columns = ['Dist', 'lastvx', 'lastvy']

    aggregate = uq.elements.collate.AggregateSamples(
        my_campaign,
        output_filename=output_filename,
        output_columns=output_columns,
        header=0)
    aggregate.apply()

    assert(len(my_campaign.data) > 0)

    stats = uq.elements.analysis.BasicStats(
        my_campaign, value_cols=output_columns)
    results, output_file = stats.apply()

    my_campaign.save_state(output_json)

    print(results)

    assert(os.path.exists(output_json))
    assert(os.path.isfile(output_json))


if __name__ == "__main__":
    test_cannonsim_csv("/tmp/")
