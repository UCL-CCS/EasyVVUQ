"""
SCRIPT TO TEST THE SPARSE GRID INTERPOLATION, QUADRATURE AND SOBOL INDICES
FOR THE STOCHASTIC COLLOCATION METHOD
"""

import chaospy as cp
import numpy as np
import easyvvuq as uq
import os


import matplotlib.pyplot as plt
plt.close('all')

# author: Wouter Edeling
__license__ = "LGPL"

# home directory of user
home = os.path.expanduser('~')
HOME = os.path.abspath(os.path.dirname(__file__))

# Set up a fresh campaign called "sc"
my_campaign = uq.Campaign(name='sc', work_dir='/tmp')

# Define parameter space
params = {
    "Pe": {
        "type": "float",
        "min": 1.0,
        "max": 2000.0,
        "default": 100.0},
    "f": {
        "type": "float",
        "min": 0.0,
        "max": 10.0,
        "default": 1.0},
    "out_file": {
        "type": "string",
        "default": "output.csv"}}

output_filename = params["out_file"]["default"]
output_columns = ["u"]

# Create an encoder, decoder and collation element
encoder = uq.encoders.GenericEncoder(
    template_fname=HOME + '/sc.template',
    delimiter='$',
    target_filename='ade_in.json')
decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                output_columns=output_columns,
                                header=0)
collater = uq.collate.AggregateSamples(average=False)

# Add the SC app (automatically set as current app)
my_campaign.add_app(name="sc",
                    params=params,
                    encoder=encoder,
                    decoder=decoder,
                    collater=collater)

# Create the sampler
vary = {
    "Pe": cp.Uniform(100.0, 200.0),
    "f": cp.Uniform(0.9, 1.0)
}

"""
SPARSE GRID PARAMETERS
----------------------
- sparse = True: use a Smolyak sparse grid
- growth = True: use an exponential rule for the growth of the number
  of 1D collocation points per level. Used to make e.g. clenshaw-curtis
  quadrature nested.
"""
my_sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=3,
                                   quadrature_rule="C", sparse=True,
                                   growth=True)

# Associate the sampler with the campaign
my_campaign.set_sampler(my_sampler)

# Will draw all (of the finite set of samples)
my_campaign.draw_samples(num_samples=my_sampler.n_samples)
my_campaign.populate_runs_dir()

# Use this instead to run the samples using EasyVVUQ on the localhost
my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
    "tests/sc/sc_model.py ade_in.json"))

my_campaign.collate()

# Post-processing analysis
analysis = uq.analysis.SCAnalysis(sampler=my_sampler, qoi_cols=output_columns)

my_campaign.apply_analysis(analysis)

results = my_campaign.get_last_analysis()

###################################
# Plot the moments and SC samples #
###################################

mu = results.describe()['u']['mean']
std = results.describe()['u']['std']

print("mu", mu, ", std", std)

if __name__ == '__main__':

    x = np.linspace(0, 1, 301)

    fig = plt.figure(figsize=[10, 5])
    ax = fig.add_subplot(121, xlabel='x', ylabel='u',
                         title=r'code mean +/- standard deviation')
    ax.plot(x, mu, 'b', label='mean')
    ax.plot(x, mu + 3 * std, '--r', label='std-dev')
    ax.plot(x, mu - 3 * std, '--r')

    #####################################
    # Plot the random surrogate samples #
    #####################################

    if analysis.element_name() == 'SC_Analysis':

        ax = fig.add_subplot(122, xlabel='x', ylabel='u',
                             title='Surrogate and code samples')

        xi_mc = analysis.xi_d
        n_mc = xi_mc.shape[0]
        code_samples = analysis.get_sample_array('u')

        # evaluate the surrogate at these values
        print('Evaluating surrogate model', n_mc, 'times')
        for i in range(n_mc):
            ax.plot(x, analysis.surrogate('u', xi_mc[i]), 'g')
            ax.plot(x, code_samples[i], 'r+')
        print('done')

        plt.tight_layout()

        analysis.plot_grid()

        #######################
        # Plot Sobol indices #
        #######################

        fig = plt.figure()
        ax = fig.add_subplot(
            111,
            xlabel='x',
            ylabel='Sobol indices',
            title='spatial dist. Sobol indices, Pe only important in viscous regions')

        lbl = ['Pe', 'f', 'Pe-f interaction']
        idx = 0

        if analysis.element_name() == 'SC_Analysis':

            for S_i in results['sobols']['u']:
                ax.plot(x, results['sobols']['u'][S_i], label=lbl[idx])
                idx += 1
        else:
            for S_i in results['sobols']['u'][1]:
                ax.plot(x, results['sobols']['u'][1][S_i], label=lbl[idx])
                idx += 1

        leg = plt.legend(loc=0)
        leg.set_draggable(True)

        plt.tight_layout()

    plt.show()
