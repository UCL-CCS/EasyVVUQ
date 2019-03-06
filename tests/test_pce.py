import os
import numpy    as np
import chaospy  as cp
import easyvvuq as uq


# ...
#def test_pce(tmpdir):
tmpdir = "/tmp/"
input_json = "tests/pce/pce_in.json"
output_json = os.path.join(tmpdir, "out_pce.json")

assert(os.path.exists(input_json))

# Initialize Campaign object
my_campaign = uq.Campaign(state_filename=input_json, workdir=tmpdir)

# Define the parameters dictionary
my_campaign.vary_param("kappa", dist=cp.Uniform(0.025, 0.075))
my_campaign.vary_param("t_env", dist=cp.Uniform(15, 25))

# Create the sampler
my_sampler  = uq.elements.sampling.PCESampler(my_campaign)

# Use the sampler
my_campaign.add_runs(my_sampler)

assert(len(my_campaign.runs) == my_campaign.n_samples)
print(my_campaign.log)

my_campaign.populate_runs_dir()

# Execute runs
my_campaign.apply_for_each_run_dir(
    uq.actions.ExecuteLocal("tests/pce/pce_model.py pce_in.json"))

# Aggregate the results from all runs.
output_filename = my_campaign.params_info['out_file']['default']
output_columns = ['te']

aggregate = uq.elements.collate.AggregateSamples(
                                                my_campaign,
                                                output_filename=output_filename,
                                                output_columns=output_columns,
                                                header=0,
                                                )

aggregate.apply()

# Post-processing analysis: computes the 1st two statistical moments and
analysis = uq.elements.analysis.PCEAnalysis(my_campaign, value_cols=output_columns)

output_file = analysis.apply()

## ...
#
#if __name__ == "__main__":
#    test_pce("/tmp/")
