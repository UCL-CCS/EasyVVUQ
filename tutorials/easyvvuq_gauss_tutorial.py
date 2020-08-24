import os
import easyvvuq as uq
import chaospy as cp

# 0. Setup some variables describing app to be run
#
#    gauss.py is in current directory and takes one input file
#    and writes to 'output.csv'.
cwd = os.getcwd()
input_filename = 'gauss_in.json'
cmd = f"{cwd}/gauss.py {input_filename}"
out_file = "output.csv"
# Template input to substitute values into for each run
template = f"{cwd}/gauss.template"

# 1. Create campaign
my_campaign = uq.Campaign(name='gauss', work_dir=".")

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
#    - Define a new application (we'll call it 'gauss'), and the encoding/decoding elements it needs
#    - Also requires a collation element - his will be responsible for aggregating the results
encoder = uq.encoders.GenericEncoder(template_fname=template,
                                     target_filename=input_filename)

decoder = uq.decoders.SimpleCSV(
            target_filename=out_file,
            output_columns=['Step', 'Value'],
            header=0)

collater = uq.collate.AggregateSamples(average=True)

my_campaign.add_app(name="gauss",
                    params=params,
                    encoder=encoder,
                    decoder=decoder,
                    collater=collater
                    )

# 4. Specify Sampler
#    -  vary the `mu` parameter only
vary = {
    "mu": cp.Uniform(1.0, 100.0),
}

my_sampler = uq.sampling.RandomSampler(vary=vary)

my_campaign.set_sampler(my_sampler)

# 5. Get run parameters
my_campaign.draw_samples(num_samples=3,
                         replicas=5)

# 6. Create run input directories
my_campaign.populate_runs_dir()

print(my_campaign)

# 7. Run Application
#    - gauss is executed for each sample
my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(cmd,
                                                           interpret='python3'))

# 8. Collate output
my_campaign.collate()

# 9. Run Analysis
#     - Calculate bootstrap statistics for collated data
stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
my_campaign.apply_analysis(stats)
print("stats:\n", my_campaign.get_last_analysis())
