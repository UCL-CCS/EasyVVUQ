import os, sys
import easyvvuq as uq

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


my_campaign = uq.Campaign(state_filename="test_input/test_gauss.json")

my_campaign.vary_param("mu", dist=uq.distributions.uniform(1.0, 100.0))
uq.uqp.sampling.random_sampler(my_campaign, num_samples=2)
uq.uqp.sampling.add_replicas(my_campaign, replicates=5)

my_campaign.populate_runs_dir()
my_campaign.apply_for_each_run(uq.execute_local)

# Apply replica aggregation UQP (using decoder)
# Apply ensemble bootstrap UQP

print(my_campaign)
my_campaign.save_state("out_gauss.json")

