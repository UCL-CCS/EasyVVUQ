import os
import sys
import easyvvuq as uq
from flee.encoder_flee import FleeEncoder
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


def test_flee(tmpdir):

    my_campaign = uq.Campaign(state_filename="tests/flee/flee_application.json", workdir=tmpdir)

    my_campaign.vary_param("MaxMoveSpeed", dist=uq.distributions.normal(200.0, 5.0))

    random_sampler = uq.elements.sampling.RandomSampler(my_campaign)

    my_campaign.add_runs(random_sampler, max_num=5)

    my_campaign.populate_runs_dir()

    my_campaign.apply_for_each_run_dir(
            uq.actions.ExecuteLocal("/bin/bash run_flee.sh\n"))

    output_filename = 'out.csv'
    output_columns = ['Total error']

    aggregate = uq.elements.collate.AggregateSamples(
                                my_campaign,
                                output_filename=output_filename,
                                output_columns=output_columns,
                                header=0)
    aggregate.apply()

    my_campaign.save_state("test_flee.json")

    sys.exit(0)

#    stats = uq.elements.analysis.BasicStats(my_campaign, value_cols=output_columns)
#    results, output_file = stats.apply()
#
#    my_campaign.save_state(output_json)
#
#    print(results)


if __name__ == "__main__":
    test_flee("/tmp/")
