from collections import OrderedDict
"""
Perform stochastic collocation using EasyVVUQ.
Test problem: advection-diffusion equation: u_x - 1/Pe*u_xx = f,
with uncertain Peclet number (Pe) and scalar forcing term (f).
"""

import numpy as np
import matplotlib.pyplot as plt
import easyvvuq as uq
import chaospy as cp

# Input file containing information about parameters of interest
input_json = "ade_input.json"
output_json = "ade_output.json"

# 1. Initialize `Campaign` object which information on parameters to be sampled
#    and the values used for all sampling runs
my_campaign = uq.Campaign(state_filename=input_json)

# 2. Set which parameters we wish to include in the analysis and the
#    distribution from which to draw samples
m = 4
my_campaign.vary_param("Pe", dist=cp.distributions.Uniform(-1, 1))
my_campaign.vary_param("f", dist=cp.distributions.Uniform(-1, 1))

# 3. Select the SC sampler to create a tensor grid
sc_sampler = uq.elements.sampling.SCSampler(my_campaign, m)
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


# 7.  Post-processing analysis: computes the 1st two statistical moments and
#     gives the ability to use the SCAnalysis object as a surrogate, which
#     interpolated the code samples to unobserved parameter variables.
sc_analysis = uq.elements.analysis.SCAnalysis(
    my_campaign, value_cols=output_columns)
results, output_file = sc_analysis.get_moments(m)  # moment calculation
# results, output_file = sc_analysis.apply()

# 8. Use the SC samples and integration weights to estimate the
#    (1-st order or all) Sobol indices. In this example, at x=1 the Sobol indices
#    are NaN, since the variance is zero here.

# get Sobol indices for free
#typ = 'first_order'
typ = 'all'
sobol_idx = sc_analysis.get_Sobol_indices(typ)

my_campaign.save_state(output_json)
###############################################################################

plt.close('all')

# spatial grid of advection diffusion problem
x = np.linspace(0, 1, sc_analysis.N_qoi)

###################################
# Plot the moments and SC samples #
###################################

fig = plt.figure(figsize=[10, 5])
ax = fig.add_subplot(121, xlabel='x', ylabel='u',
                     title=r'code samples and stats')
ax.plot(x, results['mean_f'], 'b', label='mean')
ax.plot(x, results['mean_f'] + results['var_f']**0.5, '--r', label='std-dev')
ax.plot(x, results['mean_f'] - results['var_f']**0.5, '--r')

# plot individual SC samples
for i in range(number_of_samples):
    plt.plot(x, sc_analysis.samples[i], 'g', alpha=0.1, label='samples')

# display legend, remove duplicate entries
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
leg = plt.legend(by_label.values(), by_label.keys())
leg.set_draggable(True)

#####################################
# Plot the random surrogate samples #
#####################################

ax = fig.add_subplot(122, xlabel='x', ylabel='u',
                     title='some Monte Carlo surrogate samples')

# generate random samples of unobserved parameter values
left_bound = -1.0
right_bound = 1.0
n_mc = 100
xi_mc = np.random.rand(n_mc, 2) * (right_bound - left_bound) + left_bound

# evaluate the surrogate at these values
for i in range(n_mc):
    ax.plot(x, sc_analysis.surrogate(xi_mc[i]), 'g')

plt.tight_layout()

######################
# Plot Sobol indices #
######################

fig = plt.figure()
ax = fig.add_subplot(
    111,
    xlabel='x',
    ylabel='Sobol indices',
    title='spatial dist. Sobol indices, Pe only important in viscous regions')

lbl = ['Pe', 'f', 'Pe-f interaction']
idx = 0

for S_i in sobol_idx:
    ax.plot(x, S_i, label=lbl[idx])
    idx += 1

leg = plt.legend(loc=0)
leg.draggable(True)

plt.tight_layout()

plt.show()
