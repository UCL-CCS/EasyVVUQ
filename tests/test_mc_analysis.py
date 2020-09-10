import matplotlib.pyplot as plt
import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import pytest


def exact_sobols_g_func():
    # for the Sobol g function, the exact (1st-order)
    # Sobol indices are known analytically
    V_i = np.zeros(d)

    for i in range(d):
        V_i[i] = 1.0 / (3.0 * (1 + a[i])**2)

    V = np.prod(1 + V_i) - 1

    print('----------------------')
    print('Exact 1st-order Sobol indices: ', V_i / V)

    return V_i / V


plt.close('all')

# number of unknown variables
d = 2

# parameters required by test function
a = [0.0, 0.5, 3.0, 9.0, 99.0]

# author: Wouter Edeling
__license__ = "LGPL"

HOME = os.path.abspath(os.path.dirname(__file__))


def run_campaign():
    # fix random seed to make this test deterministic
    np.random.seed(10000000)

    # Set up a fresh campaign called "mc"
    my_campaign = uq.Campaign(name='mc', work_dir='/tmp')

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
        template_fname=HOME + '/sc/sobol.template',
        delimiter='$',
        target_filename='model_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns,
                                    header=0)
    collater = uq.collate.AggregateSamples(average=False)

    # Add the SC app (automatically set as current app)
    my_campaign.add_app(name="mc",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)

    # Create the sampler
    vary = {
        "x1": cp.Uniform(0.0, 1.0),
        "x2": cp.Uniform(0.0, 1.0)}
    # "x3": cp.Uniform(0.0, 1.0),
    # "x4": cp.Uniform(0.0, 1.0),
    # "x5": cp.Uniform(0.0, 1.0)}

    # Select the MC sampler
    my_sampler = uq.sampling.MCSampler(vary, n_mc_samples=100)

    # Associate the sampler with the campaign
    my_campaign.set_sampler(my_sampler)

    # Will draw all (of the finite set of samples)
    my_campaign.draw_samples()
    my_campaign.populate_runs_dir()

    # Use this instead to run the samples using EasyVVUQ on the localhost
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
        "tests/sc/sobol_model.py model_in.json"))
    my_campaign.collate()

    # Post-processing analysis
    analysis = uq.analysis.QMCAnalysis(sampler=my_sampler, qoi_cols=output_columns)
    my_campaign.apply_analysis(analysis)
    results = my_campaign.get_last_analysis()

    return results

    # sobol_exact = exact_sobols_g_func()
    # fig = plt.figure()
    # ax = fig.add_subplot(111, ylim=[0,1])
    # ax.plot(sobol_exact, 'ro')
    # for i, param_name in enumerate(results['sobols_total']['f']):
    #     sobol_idx = results['sobols_first']['f'][param_name]
    #     low = results['conf_sobols_first']['f'][param_name]['low']
    #     high = results['conf_sobols_first']['f'][param_name]['high']
    #     yerr = np.array([sobol_idx - low, high - sobol_idx])
    #     ax.errorbar(i, sobol_idx,
    #                 yerr=yerr,
    #                 fmt='*', color='b')
    # plt.tight_layout()


if __name__ == '__main__':

    # analytic Sobol indices
    results = run_campaign()

    ref_sobols = exact_sobols_g_func()
    sobol_x1 = results['sobols_first']['f']['x1']
    sobol_x2 = results['sobols_first']['f']['x2']

    assert sobol_x1 == pytest.approx(ref_sobols[0], abs=0.1)
    assert sobol_x2 == pytest.approx(ref_sobols[1], abs=0.1)

plt.show()
