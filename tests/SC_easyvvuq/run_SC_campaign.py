import numpy as np
import matplotlib.pyplot as plt
import easyvvuq as uq

# Input file containing information about parameters of interest
input_json = "ade_input.json"
output_json = "ade_output.json"

# 1. Initialize `Campaign` object which information on parameters to be sampled
#    and the values used for all sampling runs
my_campaign = uq.Campaign(state_filename=input_json)

# 2. Set which parameters we wish to include in the analysis and the
#    distribution from which to draw samples
m1 = 6
m2 = 6
my_campaign.vary_param("Pe", dist=uq.distributions.legendre(m1))
my_campaign.vary_param("f", dist=uq.distributions.legendre(m2))

# First we create three samples where the varying parameter ()"mu", the mean)
# is chosen directly from the selected distribution. If multiple parameters
# were allowed to vary then all would be sampled independently.
sc_sampler = uq.elements.sampling.SCSampler(my_campaign)
number_of_samples = sc_sampler.number_of_samples

my_campaign.add_runs(sc_sampler, max_num=number_of_samples)

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

# 7. Compute the first two statistical moments using new class which 
#    inherents from the base analysis class
stats = uq.elements.analysis.SCMoments(my_campaign, value_cols=output_columns)
results, output_file = stats.apply()

# 8. Use stochastic collocation expansion as a surrogate, interpolating
#    the samples computed in step 5 to unobserved parameter values.
#    Makes use of a new Analysis class.
surr = uq.elements.analysis.SCSurrogate(my_campaign, value_cols=output_columns)

my_campaign.save_state(output_json)
###############################################################################

#plot some results
plt.close('all')
from collections import OrderedDict

#spatial grid of advection diffusion problem
x = np.linspace(0, 1, surr.N_qoi)

fig = plt.figure(figsize=[10, 5])
ax = fig.add_subplot(121, xlabel='x', ylabel='u', \
                     title=r'code samples and stats')
ax.plot(x, results['mean_f'], 'b', label='mean')
ax.plot(x, results['mean_f'] + results['var_f']**0.5, '--r', label='std-dev')
ax.plot(x, results['mean_f'] - results['var_f']**0.5, '--r')

#plot individual SC samples
for i in range(number_of_samples):
    plt.plot(x, surr.samples[i], 'g', alpha=0.1, label='samples')
   
#display legend, remove duplicate entries
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
leg = plt.legend(by_label.values(), by_label.keys())
leg.draggable(True)

ax = fig.add_subplot(122, xlabel='x', ylabel='u', \
                     title='some Monte Carlo surrogate samples')

#generate random samples of unobserved parameter values
left_bound = -1.0; right_bound = 1.0
n_mc = 100
xi_mc = np.random.rand(n_mc, 2)*(right_bound - left_bound) + left_bound

#evaluate the surrogate at these values
for i in range(n_mc):
    ax.plot(x, surr.surrogate(xi_mc[i]), 'g')

plt.show()
