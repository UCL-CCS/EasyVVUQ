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
my_campaign = uq.Campaign(state_filename="test_input/test_cannonsim.json")

# Specify names of parameters that are variable, and their (prior) distributions.
my_campaign.vary_param("angle",    dist=uq.distributions.uniform(0.0, 1.0))
my_campaign.vary_param("velocity", dist=uq.distributions.normal(10.0, 1.0))
my_campaign.vary_param("mass",     dist=uq.distributions.customHistogram("test_input/mass_distribution.csv"))

# Apply the randomSampler UQP, generating 15 runs
uq.uqp.sampling.randomSampler(my_campaign, num_samples=15)

# Execute and analyse
my_campaign.populate_runs_dir()
my_campaign.apply_for_each_run(uq.execute_local)
my_campaign.apply_for_each_run(uq.uqp.analysis.basicStats(reader=uq.reader.csvReader('output.csv', 0)))

# Output
print(my_campaign)
my_campaign.save_state("out_cannonsim.json")
