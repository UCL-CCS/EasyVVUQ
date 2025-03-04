import os
from shutil import rmtree
import easyvvuq as uq
import chaospy as cp
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="EasyVVUQ applied (using DASK) to a cylindrical tokamak",
        epilog="",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("--local", "-l", action="store_true", default=True)
    args = parser.parse_args()

    if args.local:
        print("Running locally")
        from dask.distributed import Client
    else:
        print("Running using SLURM")
        from dask.distributed import Client
        from dask_jobqueue import SLURMCluster

    work_dir = os.path.dirname(os.path.abspath(__file__))
    campaign_work_dir = os.path.join(work_dir, "easyvvuq_dask_tutorial")
    # clear the target campaign dir
    if os.path.exists(campaign_work_dir):
        rmtree(campaign_work_dir)
    os.makedirs(campaign_work_dir)

    # Set up a fresh campaign called "coffee_pce"
    db_location = "sqlite:///" + campaign_work_dir + "/campaign.db"
    campaign = uq.Campaign(
        name='coffee_pce',
        db_location=db_location,
        work_dir=campaign_work_dir
    )
    # Define parameter space
    params = {
        "temp_init": {
            "type": "float", "min": 0.0, "max": 100.0, "default": 95.0
        },
        "kappa": {
            "type": "float", "min": 0.0, "max": 0.1, "default": 0.025
        },
        "t_env": {
            "type": "float", "min": 0.0, "max": 40.0, "default": 15.0
        },
        "out_file": {
            "type": "string", "default": "output.csv"
        }
    }
    # Create an encoder, decoder and collater for PCE test app
    encoder = uq.encoders.GenericEncoder(
        template_fname='cooling.template',
        delimiter='$',
        target_filename='cooling_in.json'
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

    if args.local:
        from dask.distributed import Client
        client = Client(processes=True, threads_per_worker=1)
    else:
        cluster = SLURMCluster(
            job_extra=['--cluster=mpp2'],
            queue='mpp2_batch',
            cores=28,
            memory='1 GB'
        )
        cluster.scale(1)
        print(cluster)
        print(cluster.job_script())
        client = Client(cluster)
    print(client)

    # Add the app (automatically set as current app)
    campaign.add_app(
        name="cooling",
        params=params,
        actions=actions
    )

    # Create the sampler
    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }
    sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=3)

    # Associate the sampler with the campaign
    campaign.set_sampler(sampler)

    # Run the cases
    campaign.execute(pool=client).collate()

    client.close()
    if not args.local:
        client.shutdown()

    # Get Descriptive Statistics
    results = campaign.analyse(qoi_cols=["te"])

    print("descriptive statistics :")
    print(results.describe("te"))
    print("the first order sobol index :")
    print(results.sobols_first()['te'])
