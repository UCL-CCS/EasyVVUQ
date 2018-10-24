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

# Get app and param info about cannonsim
my_campaign = uq.Campaign(state_filename="test_input/test_lammps.json")

# Specify which parameters can vary, and their (prior) distributions.
my_campaign.vary_param("seed",    dist=uq.distributions.uniform_integer(0, 10000000))

# Apply the randomSampler UQP, generating 15 runs
uq.uqp.sampling.random_sampler(my_campaign, num_samples=15)

# Populate runs dir and execute
my_campaign.populate_runs_dir()
my_campaign.apply_for_each_run(uq.execute_local)

output_filename = 'output_replica.csv'
output_columns = ['pe', 'temp', 'pres']

# Aggregate results from all runs
uq.collate.aggregate_samples(my_campaign, average=True,
                             output_filename=output_filename,
                             output_columns=output_columns)

# Apply ensemble bootstrap UQP
stats = uq.uqp.analysis.BasicStats(my_campaign)
results, output_file = stats.run_analysis()

# Output
print(my_campaign)
my_campaign.save_state("out_lammps.json")
