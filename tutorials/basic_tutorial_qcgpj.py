import os
import easyvvuq as uq
import chaospy as cp
import matplotlib.pyplot as plt

# Import necessary actions from EasyVVUQ
from easyvvuq.actions import QCGPJPool
from easyvvuq.actions import CreateRunDirectory, Encode, Decode, ExecuteLocal, Actions

# Define the parameters for the model
params = {
    "F": {"type": "float", "default": 1.0},  # Force parameter
    "L": {"type": "float", "default": 1.5},  # Length parameter
    "a": {"type": "float", "min": 0.7, "max": 1.2, "default": 1.0},  # Variable a with range
    "D": {"type": "float", "min": 0.75, "max": 0.85, "default": 0.8},  # Variable D with range
    "d": {"type": "float", "default": 0.1},  # Variable d
    "E": {"type": "float", "default": 200000},  # Young's modulus (material property)
    "outfile": {"type": "string", "default": "output.json"}  # Output file name
}

# Set up the encoder and decoder to read/write data
encoder = uq.encoders.GenericEncoder(template_fname='beam.template', delimiter='$', target_filename='input.json')  # Template encoder
decoder = uq.decoders.JSONDecoder(target_filename='output.json', output_columns=['g1'])  # Decoder to read the output 'g1'

# Execute the local model using the 'beam' input file
execute = ExecuteLocal('{}/beam input.json'.format(os.getcwd()))  # Path to the model script and input file

# Set up the actions for the campaign
actions = Actions(
    CreateRunDirectory('/tmp'),  # Create a directory to store results
    Encode(encoder),  # Encode the input data
    execute,  # Run the computational model
    Decode(decoder)  # Decode the results from the output
)

# Create the EasyVVUQ campaign using the parameters and actions defined above
campaign = uq.Campaign(name='beam', params=params, actions=actions)

# Define the uncertainty distributions for the input parameters using Chaospy
vary = {
    "F": cp.Normal(1, 0.1),  # Normal distribution for Force with mean 1 and std 0.1
    "L": cp.Normal(1.5, 0.01),  # Normal distribution for Length with mean 1.5 and std 0.01
    "a": cp.Uniform(0.7, 1.2),  # Uniform distribution for parameter a
    "D": cp.Triangle(0.75, 0.8, 0.85)  # Triangular distribution for parameter D
}

# Set the sampling method to use Polynomial Chaos Expansion (PCE) for sensitivity analysis
campaign.set_sampler(uq.sampling.PCESampler(vary=vary, polynomial_order=1))

# Run the campaign with a parallel pool using QCGPJ (a parallel job pool)
with QCGPJPool() as qcgpj:
    # Execute the campaign with the defined pool and then collate the results
    campaign.execute(pool=qcgpj).collate()

# Get the collation results from the campaign
campaign.get_collation_result()

# Dump the campaign database as JSON for debugging purposes
campaign.campaign_db.dump()

# Perform the analysis on the output quantities (in this case, 'g1')
results = campaign.analyse(qoi_cols=['g1'])

# Plot the Sobol indices as a treemap and save it to a file
results.plot_sobols_treemap('g1', figsize=(10, 10))  # Create the Sobol indices treemap plot
plt.axis('off')  # Turn off the axis for a cleaner plot
plt.savefig('sobols_treemap.png', bbox_inches='tight')  # Save the plot to a file
plt.show()  # Display the plot

# Perform additional analysis on the Sobol indices and print the results
results.sobols_first('g1')  # First-order Sobol indices
results.supported_stats()  # Get the supported statistical measures
results._get_sobols_first('g1', 'F')  # First-order Sobol index for parameter 'F'
results.sobols_total('g1', 'F')  # Total Sobol index for parameter 'F'

print("success")  # Print success message after all tasks are complete

