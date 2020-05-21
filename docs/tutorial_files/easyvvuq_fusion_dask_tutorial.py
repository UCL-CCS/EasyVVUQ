#! /usr/bin/env python
"""
Run an EasyVVUQ campaign to analyze the sensitivity of the temperature
profile predicted by a simplified model of heat conduction in a
tokamak plasma.

This is done with PCE.
"""
import os
import easyvvuq as uq
import chaospy as cp
import pickle
import time
import numpy as np 
import matplotlib
if not os.getenv("DISPLAY"): matplotlib.use('Agg')
import matplotlib.pylab as plt

import argparse
parser = argparse.ArgumentParser(description="EasyVVUQ applied (using DASK) to a cylindrical tokamak", epilog="",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--local", "-l", action='store_true', default=False)
args=parser.parse_args()

if args.local:
    print('Running locally')
    from dask.distributed import Client, LocalCluster
else:
    print('Running using SLURM')
    from dask.distributed import Client
    from dask_jobqueue import SLURMCluster

if __name__ == '__main__':      ### This is needed if you are using a local cluster; see https://github.com/dask/dask/issues/3877#issuecomment-425692984
    
    time_start = time.time()
    # Set up a fresh campaign called "fusion_pce."
    my_campaign = uq.CampaignDask(name='fusion_pce.')

    # Define parameter space
    params = {
        "Qe_tot":   {"type": "float",   "min": 1.0e6, "max": 50.0e6, "default": 2e6}, 
        "H0":       {"type": "float",   "min": 0.00,  "max": 1.0,    "default": 0}, 
        "Hw":       {"type": "float",   "min": 0.01,  "max": 100.0,  "default": 0.1}, 
        "Te_bc":    {"type": "float",   "min": 10.0,  "max": 1000.0, "default": 100}, 
        "chi":      {"type": "float",   "min": 0.01,  "max": 100.0,  "default": 1}, 
        "a0":       {"type": "float",   "min": 0.2,   "max": 10.0,   "default": 1}, 
        "R0":       {"type": "float",   "min": 0.5,   "max": 20.0,   "default": 3}, 
        "E0":       {"type": "float",   "min": 1.0,   "max": 10.0,   "default": 1.5}, 
        "b_pos":    {"type": "float",   "min": 0.95,  "max": 0.99,   "default": 0.98}, 
        "b_height": {"type": "float",   "min": 3e19,  "max": 10e19,  "default": 6e19}, 
        "b_sol":    {"type": "float",   "min": 2e18,  "max": 3e19,   "default": 2e19}, 
        "b_width":  {"type": "float",   "min": 0.005, "max": 0.025,  "default": 0.01}, 
        "b_slope":  {"type": "float",   "min": 0.0,   "max": 0.05,   "default": 0.01}, 
        "nr":       {"type": "integer", "min": 10,    "max": 1000,   "default": 100}, 
        "dt":       {"type": "float",   "min": 1e-3,  "max": 1e3,    "default": 100},
        "out_file": {"type": "string",  "default": "output.csv"}
    }
    """ code snippet for writing the template file
    str = ""
    first = True
    for k in params.keys():
        if first:
            str += '{"%s": "$%s"' % (k,k) ; first = False
        else:
            str += ', "%s": "$%s"' % (k,k)
    str += '}'
    print(str, file=open('fusion.template','w'))
    """

    # Create an encoder, decoder and collater for PCE test app
    encoder = uq.encoders.GenericEncoder(template_fname='fusion.template',
                                         delimiter='$',
                                         target_filename='fusion_in.json')


    decoder = uq.decoders.SimpleCSV(target_filename="output.csv",
                                    output_columns=["te", "ne", "rho", "rho_norm"],
                                    header=0)

    collater = uq.collate.AggregateSamples(average=False)

    # Add the app (automatically set as current app)
    my_campaign.add_app(name="fusion",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)

    time_end = time.time()
    print('Time for phase 1 = %.3f' % (time_end-time_start))
    time_start = time.time()

    # Create the sampler
    vary = {
        "Qe_tot":   cp.Uniform(1.8e6, 2.2e6),
        "H0":       cp.Uniform(0.0,   0.2),
        "Hw":       cp.Uniform(0.1,   0.5),
        "chi":      cp.Uniform(0.8,   1.2), 
        "Te_bc":    cp.Uniform(80.0,  120.0)
    }
    """ other possible quantities to vary
        "a0":       cp.Uniform(0.9,   1.1), 
        "R0":       cp.Uniform(2.7,   3.3), 
        "E0":       cp.Uniform(1.4,   1.6), 
        "b_pos":    cp.Uniform(0.95,  0.99), 
        "b_height": cp.Uniform(5e19,  7e19), 
        "b_sol":    cp.Uniform(1e19,  3e19), 
        "b_width":  cp.Uniform(0.015, 0.025), 
        "b_slope":  cp.Uniform(0.005, 0.020)
    """

    # Associate a sampler with the campaign
    my_campaign.set_sampler(uq.sampling.PCESampler(vary=vary, polynomial_order=3))

    # Will draw all (of the finite set of samples)
    my_campaign.draw_samples()
    print('Number of samples = %s' % my_campaign.get_active_sampler().count)

    time_end = time.time()
    print('Time for phase 2 = %.3f' % (time_end-time_start))
    time_start = time.time()

    my_campaign.populate_runs_dir()

    time_end = time.time()
    print('Time for phase 3 = %.3f' % (time_end-time_start))
    time_start = time.time()

    if args.local:
        from dask.distributed import Client
        client = Client(processes=True, threads_per_worker=1)
    else:
        cluster = SLURMCluster(job_extra=['--qos=p.tok.openmp.2h', '--mail-type=end', '--mail-user=dpc@rzg.mpg.de'], queue='p.tok.openmp', cores=8, memory='8 GB', processes=8)
        cluster.scale(32)
        print(cluster)
        print(cluster.job_script())
        client = Client(cluster)
    print(client)

    cwd = os.getcwd().replace(' ', '\ ')      # deal with ' ' in the path
    cmd = f"{cwd}/fusion_model.py fusion_in.json"
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(cmd, interpret='python3'), client)

    client.close()
    client.shutdown()
    
    time_end = time.time()
    print('Time for phase 4 = %.3f' % (time_end-time_start))
    time_start = time.time()

    my_campaign.collate()

    time_end = time.time()
    print('Time for phase 5 = %.3f' % (time_end-time_start))
    time_start = time.time()

    # Post-processing analysis
    my_campaign.apply_analysis(uq.analysis.PCEAnalysis(sampler=my_campaign.get_active_sampler(), qoi_cols=["te", "ne", "rho", "rho_norm"]))

    time_end = time.time()
    print('Time for phase 6 = %.3f' % (time_end-time_start))
    time_start = time.time()

    # Get Descriptive Statistics
    results = my_campaign.get_last_analysis()
    stats = results['statistical_moments']['te']
    per = results['percentiles']['te']
    sobols = results['sobols_first']['te']
    rho = results['statistical_moments']['rho']['mean']
    rho_norm = results['statistical_moments']['rho_norm']['mean']

    time_end = time.time()
    print('Time for phase 7 = %.3f' % (time_end-time_start))
    time_start = time.time()

    my_campaign.save_state("campaign_state.json")

    ###old_campaign = uq.Campaign(state_file="campaign_state.json", work_dir=".")

    pickle.dump(results, open('fusion_results.pickle','bw'))
    ###saved_results = pickle.load(open('fusion_results.pickle','br'))

    time_end = time.time()
    print('Time for phase 8 = %.3f' % (time_end-time_start))

    plt.ion()

    plt.figure() 
    plt.plot(rho, stats['mean'], 'b-', label='Mean')
    plt.plot(rho, stats['mean']-stats['std'], 'b--', label='+1 std deviation')
    plt.plot(rho, stats['mean']+stats['std'], 'b--')
    plt.fill_between(rho, stats['mean']-stats['std'], stats['mean']+stats['std'], color='b', alpha=0.2)
    plt.plot(rho, per['p10'].ravel(), 'b:', label='10 and 90 percentiles')
    plt.plot(rho, per['p90'].ravel(), 'b:')
    plt.fill_between(rho, per['p10'].ravel(), per['p90'].ravel(), color='b', alpha=0.1)
    plt.fill_between(rho, [r.lower[0] for r in results['output_distributions']['te']], [r.upper[0] for r in results['output_distributions']['te']], color='b', alpha=0.05)
    plt.legend(loc=0)
    plt.xlabel('rho [m]')
    plt.ylabel('Te [eV]')
    plt.title(my_campaign.campaign_dir)
    plt.savefig('Te.png')

    plt.figure() 
    for k in sobols.keys(): plt.plot(rho, sobols[k][0], label=k)
    plt.legend(loc=0)
    plt.xlabel('rho [m]')
    plt.ylabel('sobols_first')
    plt.title(my_campaign.campaign_dir)
    plt.savefig('sobols_first.png')

    plt.figure() 
    for k in results['sobols_total']['te'].keys(): plt.plot(rho, results['sobols_total']['te'][k][0], label=k)
    plt.legend(loc=0)    
    plt.xlabel('rho [m]')
    plt.ylabel('sobols_total')
    plt.title(my_campaign.campaign_dir)
    plt.savefig('sobols_total.png')

    plt.figure()
    for i, D in enumerate(results['output_distributions']['te']):
        _Te = np.linspace(D.lower[0], D.upper[0], 101)
        _DF = D.pdf(_Te)
        plt.loglog(_Te, _DF, 'b-')
        plt.loglog(stats['mean'][i], np.interp(stats['mean'][i], _Te, _DF), 'bo')
        plt.loglog(stats['mean'][i]-stats['std'][i], np.interp(stats['mean'][i]-stats['std'][i], _Te, _DF), 'b*')
        plt.loglog(stats['mean'][i]+stats['std'][i], np.interp(stats['mean'][i]+stats['std'][i], _Te, _DF), 'b*')
        plt.loglog(per['p10'].ravel()[i],  np.interp(per['p10'].ravel()[i], _Te, _DF), 'b+')
        plt.loglog(per['p90'].ravel()[i],  np.interp(per['p90'].ravel()[i], _Te, _DF), 'b+')
    plt.xlabel('Te')
    plt.ylabel('distribution function')
    plt.savefig('distribution_functions.png')

