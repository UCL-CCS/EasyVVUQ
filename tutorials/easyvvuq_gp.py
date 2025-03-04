import os
import easyvvuq as uq
import chaospy as cp
import matplotlib.pyplot as plt
from shutil import rmtree


work_dir = os.path.dirname(os.path.abspath(__file__))
campaign_work_dir = os.path.join(work_dir, "easyvvuq_gp")
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

# Create an encoder, decoder and collater for PCE test app
encoder = uq.encoders.GenericEncoder(
    template_fname="cooling.template",
    delimiter="$",
    target_filename="cooling_in.json"
)

decoder = uq.decoders.SimpleCSV(
    target_filename="output.csv",
    output_columns=["te"]
)

cmd = f"{work_dir}/cooling_model.py cooling_in.json"
execute = uq.actions.ExecuteLocal(
    "python3 {}".format(cmd)
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
my_sampler = uq.sampling.quasirandom.LHCSampler(vary)

# Associate the sampler with the campaign
my_campaign.set_sampler(my_sampler)


my_campaign.execute(nsamples=1).collate()

df = my_campaign.get_collation_result()

analysis = uq.analysis.GaussianProcessSurrogate(
    ["kappa", "t_env", "temp_init"], ["te"]
)
my_campaign.apply_analysis(analysis)

gp = my_campaign.get_last_analysis()

x = df[["kappa", "t_env", "temp_init"]].values
y = df[["te"]].values
prediction_y = gp.predict(x)

plt.plot(y, ".")
plt.plot(prediction_y, "+")
plt.savefig(os.path.join(campaign_work_dir, "te.png"))
# plt.show()


# print(gp.predict(np.array([[0.059053, 20.34402, 95.0, -74.714927]])))

# matplotlib.plot(

# Post-processing analysis
# my_analysis = uq.analysis.PCEAnalysis(sampler=my_sampler,
# qoi_cols=["te"])
# my_campaign.apply_analysis(my_analysis)

# Get Descriptive Statistics
# results = my_campaign.get_last_analysis()
# stats = results["statistical_moments"]["te"]
# per = results["percentiles"]["te"]
# sobols = results["sobols_first"]["te"]
