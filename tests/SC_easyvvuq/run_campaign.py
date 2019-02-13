import numpy as np
import matplotlib.pyplot as plt
import easyvvuq as uq

# Input file containing information about parameters of interest
input_json = "ade_input.json"

# 1. Initialize `Campaign` object which information on parameters to be sampled
#    and the values used for all sampling runs
my_campaign = uq.Campaign(state_filename=input_json)

# 2. Set which parameters we wish to include in the analysis and the
#    distribution from which to draw samples
my_campaign.vary_param("Pe", dist=uq.distributions.uniform(-1.0, 1.0))
my_campaign.vary_param("f", dist=uq.distributions.uniform(-1.0, 1.0))

# First we create three samples where the varying parameter ()"mu", the mean)
# is chosen directly from the selected distribution. If multiple parameters
# were allowed to vary then all would be sampled independently.
number_of_samples = 3
random_sampler = uq.elements.sampling.RandomSampler(my_campaign)
my_campaign.add_runs(random_sampler, max_num=number_of_samples)

# 4. Create directories containing inputs for each run containing the
#    parameters determined by the `Sampler`(s).
#    This makes use of the `Encoder` specified in the input file.
my_campaign.populate_runs_dir()

# 5. Run execution - note this method of running all jobs is just for demo
#    purposes.
my_campaign.apply_for_each_run_dir(
        uq.actions.ExecuteLocal("run_ADE.py ade_in.json"))

# 6. Aggregate the results from all runs.
#    This makes use of the `Decoder` selected in the input file to interpret the
#    run output and produce data that can be integrated in a summary pandas
#    dataframe.

output_filename = my_campaign.params_info['out_file']['default']
output_columns = ['u']

aggregate = uq.elements.collate.AggregateSamples(
                                                my_campaign,
                                                output_filename=output_filename,
                                                output_columns=output_columns,
                                                header=0,
                                                )
aggregate.apply()