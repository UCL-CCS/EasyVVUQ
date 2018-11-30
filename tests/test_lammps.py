import os, sys
import easyvvuq as uq
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


# If lammps is not installed (at present only checks for /usr/bin/lammps) then skip this test
if not os.path.exists("/usr/bin/lammps"):
    pytest.skip("Skipping lammps test (lammps is not installed in /usr/bin/lammps", allow_module_level=True)

def test_lammps(tmpdir):

    # Params for testing
    input_json = "tests/lammps/test_lammps.json"
    output_json = os.path.join(tmpdir, "out_lammps.json")
    number_of_samples = 15

    assert(os.path.exists(input_json))

    my_campaign = uq.Campaign(state_filename=input_json, workdir=tmpdir)

    assert(my_campaign is not None)
    assert("seed" in my_campaign.params_info)

    my_campaign.vary_param("seed",    dist=uq.distributions.uniform_integer(0, 10000000))

    assert("seed" in my_campaign.vars)

    uq.uqp.sampling.random_sampler(my_campaign, num_samples=number_of_samples)

    assert(len(my_campaign.runs) == number_of_samples)

    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal("/usr/bin/lammps -i in.CG.lammps"))

    assert(len(my_campaign.runs_dir) > 0)
    assert(os.path.exists(my_campaign.runs_dir))
    assert(os.path.isdir(my_campaign.runs_dir))

    output_filename = 'output_replica.csv'
    output_columns = ['pe', 'temp', 'pres']

    uq.collate.aggregate_samples(my_campaign, average=True,
                                 output_filename=output_filename,
                                 output_columns=output_columns)

    assert(len(my_campaign.data) > 0)

    stats = uq.uqp.analysis.BasicStats(my_campaign)
    results, output_file = stats.run_analysis()

    my_campaign.save_state(output_json)

    assert(os.path.exists(output_json))
    assert(os.path.isfile(output_json))

if __name__ == "__main__":
    test_lammps("/tmp/")
