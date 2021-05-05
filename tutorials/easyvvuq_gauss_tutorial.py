import os
from shutil import rmtree
import easyvvuq as uq
import chaospy as cp

# 0. Setup some variables describing app to be run
#
#    gauss.py is in current directory and takes one input file
#    and writes to 'output.csv'.
work_dir = os.path.dirname(os.path.abspath(__file__))
input_filename = "gauss_in.json"
out_file = "output.csv"
# Template input to substitute values into for each run
template = f"{work_dir}/gauss.template"

campaign_work_dir = os.path.join(work_dir, "easyvvuq_gauss_tutorial")
# clear the target campaign dir
if os.path.exists(campaign_work_dir):
    rmtree(campaign_work_dir)
os.makedirs(campaign_work_dir)


# 1. Create campaign
db_location = "sqlite:///" + campaign_work_dir + "/campaign.db"
my_campaign = uq.Campaign(
    name="gauss",
    db_location=db_location,
    work_dir=campaign_work_dir
)

# 2. Parameter space definition
params = {
    "sigma": {
        "type": "float",
        "min": 0.0,
        "max": 100000.0,
        "default": 0.25
    },
    "mu": {
        "type": "float",
        "min": 0.0,
        "max": 100000.0,
        "default": 1
    },
    "num_steps": {
        "type": "integer",
        "min": 0,
        "max": 100000,
        "default": 10
    },
    "out_file": {
        "type": "string",
        "default": "output.csv"
    }
}

# 3. Wrap Application
#    - Define a new application (we'll call it 'gauss'),
#      and the encoding/decoding elements it needs
#    - Also requires a collation element - his will be responsible for
#      aggregating the results
encoder = uq.encoders.GenericEncoder(
    template_fname=template,
    target_filename=input_filename
)

decoder = uq.decoders.SimpleCSV(
    target_filename=out_file,
    output_columns=['Step', 'Value']
)

cmd = f"{work_dir}/gauss.py {input_filename}"
execute = uq.actions.ExecuteLocal(
    "python3 {}".format(cmd)
)

actions = uq.actions.Actions(
    uq.actions.CreateRunDirectory(root=campaign_work_dir, flatten=True),
    uq.actions.Encode(encoder),
    execute,
    uq.actions.Decode(decoder)
)

my_campaign.add_app(
    name="gauss",
    params=params,
    actions=actions
)


# 4. Specify Sampler
#    -  vary the `mu` parameter only
vary = {
    "mu": cp.Uniform(1.0, 100.0),
}

my_sampler = uq.sampling.RandomSampler(vary=vary)

my_campaign.set_sampler(my_sampler)

print(my_campaign)

# 5. Run Application and Collate output
#    - gauss is executed for each sample
my_campaign.execute(nsamples=3).collate()

# 6. Run Analysis
#     - Calculate bootstrap statistics for collated data
stats = uq.analysis.EnsembleBoot(groupby=[("mu", 0)], qoi_cols=[("Value", 0)])
my_campaign.apply_analysis(stats)
print("stats:\n", my_campaign.get_last_analysis())
