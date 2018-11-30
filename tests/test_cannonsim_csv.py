import easyvvuq as uq
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
    pytest.skip("Skipping cannonsim test (cannonsim is not installed in tests/cannonsim/bin/)",
                allow_module_level=True)


def test_cannonsim_csv(tmpdir):

    # Params for testing
    input_json = "tests/cannonsim/test_input/test_cannonsim_csv.json"
    output_json = os.path.join(tmpdir, "out_cannonsim.json")
    number_of_samples = 15

    assert(os.path.exists(input_json))

    my_campaign = uq.Campaign(state_filename=input_json, workdir=tmpdir)

    assert(my_campaign is not None)
    assert("angle" in my_campaign.params_info)
    assert("air_resistance" in my_campaign.params_info)
    assert("height" in my_campaign.params_info)
    assert("time_step" in my_campaign.params_info)
    assert("gravity" in my_campaign.params_info)
    assert("mass" in my_campaign.params_info)
    assert("velocity" in my_campaign.params_info)

    my_campaign.vary_param("angle",    dist=uq.distributions.uniform(0.0, 1.0))
    my_campaign.vary_param("height",   dist=uq.distributions.uniform_integer(0, 10))
    my_campaign.vary_param("velocity", dist=uq.distributions.normal(10.0, 1.0))
    my_campaign.vary_param(
        "mass",
        dist=uq.distributions.custom_histogram("tests/cannonsim/test_input/mass_distribution.csv")
    )

    assert("angle" in my_campaign.vars)
    assert("height" in my_campaign.vars)
    assert("velocity" in my_campaign.vars)
    assert("mass" in my_campaign.vars)

    uq.uqp.sampling.random_sampler(my_campaign, num_samples=number_of_samples)

    assert(len(my_campaign.runs) == number_of_samples)

    my_campaign.populate_runs_dir()

    assert(len(my_campaign.runs_dir) > 0)
    assert(os.path.exists(my_campaign.runs_dir))
    assert(os.path.isdir(my_campaign.runs_dir))

    my_campaign.apply_for_each_run_dir(
            uq.actions.ExecuteLocal("tests/cannonsim/bin/cannonsim input.cannon output.csv"))

    output_filename = 'output.csv'
    output_columns = ['Dist', 'lastvx', 'lastvy']
    uq.collate.aggregate_samples(my_campaign,
                                 output_filename=output_filename,
                                 output_columns=output_columns,
                                 header=0)

    assert(len(my_campaign.data) > 0)

    stats = uq.uqp.analysis.BasicStats(my_campaign, value_cols=output_columns)
    results, output_file = stats.run_analysis()

    my_campaign.save_state(output_json)

    assert(os.path.exists(output_json))
    assert(os.path.isfile(output_json))

if __name__ == "__main__":
    test_cannonsim_csv("/tmp/")
