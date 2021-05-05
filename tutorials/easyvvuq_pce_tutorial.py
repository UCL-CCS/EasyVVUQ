import os
import easyvvuq as uq
import chaospy as cp
import numpy as np
from shutil import rmtree


work_dir = os.path.dirname(os.path.abspath(__file__))
campaign_work_dir = os.path.join(work_dir, "easyvvuq_pce_tutorial")
# clear the target campaign dir
if os.path.exists(campaign_work_dir):
    rmtree(campaign_work_dir)
os.makedirs(campaign_work_dir)

# Set up a fresh campaign called "coffee_pce"
db_location = "sqlite:///" + campaign_work_dir + "/campaign.db"
my_campaign = uq.Campaign(
    name="coffee_pce",
    db_location=db_location,
    work_dir=campaign_work_dir
)

# Define parameter space
params = {
    "temp_init": {"type": "float", "min": 0.0, "max": 100.0, "default": 95.0},
    "kappa": {"type": "float", "min": 0.0, "max": 0.1, "default": 0.025},
    "t_env": {"type": "float", "min": 0.0, "max": 40.0, "default": 15.0},
    "out_file": {"type": "string", "default": "output.csv"}
}

# Create encoder and decoder
encoder = uq.encoders.GenericEncoder(
    template_fname="cooling.template",
    delimiter="$",
    target_filename="cooling_in.json"
)

decoder = uq.decoders.SimpleCSV(
    target_filename="output.csv",
    output_columns=["te"]
)

execute = uq.actions.ExecuteLocal(
    "python3 {}/cooling_model.py cooling_in.json".format(work_dir)
)

actions = uq.actions.Actions(
    uq.actions.CreateRunDirectory(root=campaign_work_dir, flatten=True),
    uq.actions.Encode(encoder),
    execute,
    uq.actions.Decode(decoder)
)

# Add the app (automatically set as current app)
my_campaign.add_app(
    name="cooling",
    params=params,
    actions=actions
)

# Create the sampler
vary = {
    "kappa": cp.Uniform(0.025, 0.075),
    "t_env": cp.Uniform(15, 25)
}
my_sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=3)

# Associate the sampler with the campaign
my_campaign.set_sampler(my_sampler)

# Will draw all (of the finite set of samples)
my_campaign.draw_samples()

my_campaign.execute().collate()

# Post-processing analysis
my_analysis = uq.analysis.PCEAnalysis(sampler=my_sampler, qoi_cols=["te"])
my_campaign.apply_analysis(my_analysis)

# Get some descriptive statistics
results = my_campaign.get_last_analysis()
mean = results.describe("te", "mean")
var = results.describe("te", "var")

# Plots
t = np.linspace(0, 200, 150)
results.plot_moments(qoi="te", ylabel="Temperature", xlabel="Time", alpha=0.2)
results.plot_sobols_first(
    qoi="te", xlabel="Time",
    filename=os.path.join(campaign_work_dir, 'Te.png')
)
