# for the Sobol g function, the exact (1st-order)
# Sobol indices are known analytically
import matplotlib.pyplot as plt
import os
import easyvvuq as uq
import numpy as np
import chaospy as cp


def print_exact_sobols():
    V_i = np.zeros(d)

    for i in range(d):
        V_i[i] = 1.0 / (3.0 * (1 + a[i])**2)

    V = np.prod(1 + V_i) - 1

    print('----------------------')
    print('Exact 1st-order Sobol indices: ', V_i / V)


plt.close('all')

# number of unknown variables
d = 5

# parameters required by test function
a = [0.0, 0.5, 3.0, 9.0, 99.0]

# author: Wouter Edeling
__license__ = "LGPL"

# home directory of user
home = os.path.expanduser('~')
HOME = os.path.abspath(os.path.dirname(__file__))

# Set up a fresh campaign called "sc"
my_campaign = uq.Campaign(name='sc', work_dir='/tmp')

# Define parameter space
params = {
    "x1": {
        "type": "float",
        "min": 0.0,
        "max": 1.0,
        "default": 0.5},
    "x2": {
        "type": "float",
        "min": 0.0,
        "max": 1.0,
        "default": 0.5},
    "x3": {
        "type": "float",
        "min": 0.0,
        "max": 1.0,
        "default": 0.5},
    "x4": {
        "type": "float",
        "min": 0.0,
        "max": 1.0,
        "default": 0.5},
    "x5": {
        "type": "float",
        "min": 0.0,
        "max": 1.0,
        "default": 0.5},
    "out_file": {
        "type": "string",
        "default": "output.csv"}}

output_filename = params["out_file"]["default"]
output_columns = ["f"]

# Create an encoder, decoder and collation element
encoder = uq.encoders.GenericEncoder(
    template_fname=HOME + '/sobol.template',
    delimiter='$',
    target_filename='sobol_in.json')
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
    "x1": cp.Uniform(0.0, 1.0),
    "x2": cp.Uniform(0.0, 1.0),
    "x3": cp.Uniform(0.0, 1.0),
    "x4": cp.Uniform(0.0, 1.0),
    "x5": cp.Uniform(0.0, 1.0)}

"""
SPARSE GRID PARAMETERS
----------------------
- sparse = True: use a Smolyak sparse grid
- growth = True: use an exponential rule for the growth of the number
  of 1D collocation points per level. Used to make e.g. clenshaw-curtis
  quadrature nested.
"""
my_sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=2,
                                   quadrature_rule="G", sparse=False,
                                   growth=False)

# Associate the sampler with the campaign
my_campaign.set_sampler(my_sampler)

# Will draw all (of the finite set of samples)
my_campaign.draw_samples()
my_campaign.populate_runs_dir()

# Use this instead to run the samples using EasyVVUQ on the localhost
my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
    "tests/sc/sobol_model.py sobol_in.json"))

my_campaign.collate()

# Post-processing analysis
analysis = uq.analysis.SCAnalysis(sampler=my_sampler, qoi_cols=output_columns)

my_campaign.apply_analysis(analysis)

results = my_campaign.get_last_analysis()

print(results.sobols_first())

print_exact_sobols()

plt.show()
