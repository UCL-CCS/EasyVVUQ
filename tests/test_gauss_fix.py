import os
import sys
import easyvvuq as uq
import chaospy as cp
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


def test_gauss_fix(tmpdir):

    # Params for testing
    input_json = "tests/gauss/test_gauss_fix.json"
    output_json = os.path.join(tmpdir, "out_gauss.json")
    number_of_samples = 2
    number_of_replicas = 5

    assert(os.path.exists(input_json))

    my_campaign = uq.Campaign(state_filename=input_json, workdir=tmpdir)

    assert(my_campaign is not None)
    assert("sigma" in my_campaign.params_info)
    assert("mu" in my_campaign.params_info)
    assert("num_steps" in my_campaign.params_info)
    assert("out_file" in my_campaign.params_info)

    my_campaign.vary_param("mu", dist=cp.Uniform(1.0, 100.0))

    assert("mu" in my_campaign.vars)

    random_sampler = uq.elements.sampling.RandomSampler(my_campaign)
    my_campaign.add_runs(random_sampler, max_num=number_of_samples)

    assert(len(my_campaign.runs) == number_of_samples)

    replicator = uq.elements.sampling.Replicate(
        my_campaign, replicates=number_of_replicas)
    my_campaign.add_runs(replicator)

    assert(len(my_campaign.runs) == number_of_samples * number_of_replicas)

    print(my_campaign)

    my_campaign.populate_runs_dir()

    assert(len(my_campaign.runs_dir) > 0)
    assert(os.path.exists(my_campaign.runs_dir))
    assert(os.path.isdir(my_campaign.runs_dir))

    my_campaign.apply_for_each_run_dir(
        uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_in.json"))

    aggregate = uq.elements.collate.AggregateSamples(my_campaign, average=True)
    aggregate.apply()

    assert(len(my_campaign.data) > 0)

    ensemble_boot = uq.elements.analysis.EnsembleBoot(my_campaign)
    results, output_file = ensemble_boot.apply()

    my_campaign.save_state(output_json)

    assert(os.path.exists(output_json))
    assert(os.path.isfile(output_json))


if __name__ == "__main__":
    test_gauss_fix("/tmp/")
