import os
import easyvvuq as uq
import chaospy as cp

# 0. Setup some variables describing app to be run
#
#    gauss.py is in current directory and takes one input file
#    and writes to 'output.csv'.
cwd = os.cwd()
input_filename = gauss_in.json
cmd = f"{cwd}/gauss.py {input_filename}"
out_file = "output.csv"
# Template input to substitute values into for each run
template = f"{cwd}/gauss_in.template"

# 1. Create campaign
my_campaign = uq.Campaign(name='gauss', work_dir=".")

# 2. Parameter space definition
params = {
    "sigma": {"type": "real", "min": "0.0", "max": "100000.0",
              "default": "0.25"},
    "mu": {"type": "real", "min": "0.0", "max": "100000.0",
           "default": "1"},
    "num_steps": {"type": "int", "min": "0", "max": "100000",
                  "default": "10"},
    "out_file": {"type": "str", "default": out_file}
}

# 3. Wrap Application
#    - Create and add elements to the campaign
encoder = uq.encoders.GenericEncoder(template_fname=template,
                                     target_filename=input_filename)

decoder = uq.decoders.SimpleCSV(
            target_filename=out_file, 
            output_columns=['Step', 'Value'], 
            header=0)

collation = uq.collate.AggregateSamples(average=True)

my_campaign.add_app(name="gauss",
                    params=params,
                    encoder=encoder,
                    decoder=decoder,
                    collation=collation
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

# 6. Create input directories
my_campaign.populate_runs_dir()

# 7. Run Application
#    - gauss is executed for each sample
my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(cmd)

# 8. Collate output
my_campaign.collate()

# 9. Run Analysis
#     - Calculate bootstrap statistics for collated data
stats = uq.analysis.EnsembleBoot(groupby=["mu"], qoi_cols=["Value"])
my_campaign.apply_analysis(stats)
print("stats:\n", my_campaign.get_last_analysis())
