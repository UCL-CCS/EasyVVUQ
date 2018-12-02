import os
import sys
import easyvvuq as uq
from gauss.encoder_gauss import GaussEncoder
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


def test_gauss_custom_encoder(tmpdir):

    # Params for testing
    input_json = "tests/gauss/test_gauss_custom_encoder.json"
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

    my_campaign.vary_param("mu", dist=uq.distributions.uniform(1.0, 100.0))

    assert("mu" in my_campaign.vars)

    uq.elements.sampling.random_sampler(my_campaign, num_samples=number_of_samples)
    uq.elements.sampling.add_replicas(my_campaign, replicates=number_of_replicas)

    assert(len(my_campaign.runs) == number_of_samples * number_of_replicas)

    my_campaign.populate_runs_dir()

    assert(len(my_campaign.runs_dir) > 0)
    assert(os.path.exists(my_campaign.runs_dir))
    assert(os.path.isdir(my_campaign.runs_dir))

    my_campaign.apply_for_each_run_dir(
            uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_input.json"))

    uq.collate.aggregate_samples(my_campaign, average=True)

    assert(len(my_campaign.data) > 0)

    ensemble_boot = uq.elements.analysis.EnsembleBoot(my_campaign)
    results, output_file = ensemble_boot.run_analysis()

    my_campaign.save_state(output_json)

    assert(os.path.exists(output_json))
    assert(os.path.isfile(output_json))

if __name__ == "__main__":
    test_gauss_custom_encoder("/tmp/")
