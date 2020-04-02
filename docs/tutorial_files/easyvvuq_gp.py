import os
import easyvvuq as uq
import chaospy as cp
import matplotlib.pyplot as plt
import numpy as np

# Set up a fresh campaign called "coffee_pce"
my_campaign = uq.Campaign(name='coffee_pce')

# Define parameter space
params = {
    "temp_init": {"type": "float", "min": 0.0, "max": 100.0, "default": 95.0},
    "kappa": {"type": "float", "min": 0.0, "max": 0.1, "default": 0.025},
    "t_env": {"type": "float", "min": 0.0, "max": 40.0, "default": 15.0},
    "out_file": {"type": "string", "default": "output.csv"}
}

# Create an encoder, decoder and collater for PCE test app
encoder = uq.encoders.GenericEncoder(
    template_fname='cooling.template',
    delimiter='$',
    target_filename='cooling_in.json')

decoder = uq.decoders.SimpleCSV(target_filename="output.csv",
                                output_columns=["te"],
                                header=0)

collater = uq.collate.AggregateSamples(average=False)

# Add the app (automatically set as current app)
my_campaign.add_app(name="cooling",
                    params=params,
                    encoder=encoder,
                    decoder=decoder,
                    collater=collater)

# Create the sampler
vary = {
    "kappa": cp.Uniform(0.025, 0.075),
    "t_env": cp.Uniform(15, 25)
}
my_sampler = uq.sampling.quasirandom.LHCSampler(vary)

# Associate the sampler with the campaign
my_campaign.set_sampler(my_sampler)

# Will draw all (of the finite set of samples)
my_campaign.draw_samples(1)

my_campaign.populate_runs_dir()

cwd = os.getcwd()
cmd = f"{cwd}/cooling_model.py cooling_in.json"
my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(cmd, interpret='python3'))
my_campaign.collate()

df = my_campaign.get_collation_result()

analysis = uq.analysis.GaussianProcessSurrogate(['kappa', 't_env', 'temp_init'], ['te'])
my_campaign.apply_analysis(analysis)

gp = my_campaign.get_last_analysis()

x = df[['kappa', 't_env', 'temp_init']].values
y = df[['te']].values
prediction_y = gp.predict(x)

plt.plot(y, '.')
plt.plot(prediction_y, '+')
plt.show()

#print(gp.predict(np.array([[0.059053, 20.34402, 95.0, -74.714927]])))

#matplotlib.plot(

# Post-processing analysis
#my_analysis = uq.analysis.PCEAnalysis(sampler=my_sampler,
                                          #qoi_cols=["te"])
#my_campaign.apply_analysis(my_analysis)

# Get Descriptive Statistics
#results = my_campaign.get_last_analysis()
#stats = results['statistical_moments']['te']
#per = results['percentiles']['te']
#sobols = results['sobols_first']['te']
