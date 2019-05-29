import os
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


def test_gauss(tmpdir):

    # Set up a fresh campaign called "cannon"
    my_campaign = uq.Campaign(name='gauss', work_dir=tmpdir)

    params = {
        "sigma": {"type": "real", "min": "0.0", "max": "100000.0",
                  "default": "0.25"},
        "mu": {"type": "real", "min": "0.0", "max": "100000.0",
               "default": "1"},
        "num_steps": {"type": "int", "min": "0", "max": "100000",
                      "default": "10"},
        "out_file": {"type": "str", "default": "output.csv"}
    }

    number_of_samples = 3
    number_of_replicas = 5

    # Create an encoder, decoder and collation element for the cannonsim app
    encoder = uq.encoders.GenericEncoder(template_fname='tests/gauss/gauss.template',
                                         target_filename='gauss_in.json')
    decoder = GaussDecoder(target_filename=params['out_file']['default'])
    collation = uq.collate.AggregateSamples(average=True)

    my_campaign.add_app(name="gauss",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collation=collation
                        )

    # Make a random sampler
    vary = {
        "mu": cp.Uniform(1.0, 100.0),
    }
    sampler1 = uq.sampling.RandomSampler(vary=vary)

    # Set the campaign to use this sampler
    my_campaign.set_sampler(sampler1)

    # Draw samples
    my_campaign.draw_samples(num_samples=number_of_samples,
                             replicas=number_of_replicas)

    # TODO: Assert no. samples in db = number_of_samples*number_of_replicas

    my_campaign.populate_runs_dir()

    assert(len(my_campaign.get_campaign_runs_dir()) > 0)
    runs_dir = my_campaign.get_campaign_runs_dir()
    assert(os.path.exists(runs_dir))
    assert(os.path.isdir(runs_dir))

    my_campaign.apply_for_each_run_dir(
        uq.actions.ExecuteLocal("tests/gauss/gauss_json.py gauss_in.json"))

    my_campaign.collate()

    # Create a BasicStats analysis element and apply it to the campaign
    stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
    my_campaign.apply_analysis(stats)
    print("stats:", my_campaign.get_last_analysis())


if __name__ == "__main__":
    test_gauss("/tmp/")
