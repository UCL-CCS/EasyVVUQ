import numpy as np
import chaospy as cp
import easyvvuq as uq
import matplotlib.pyplot as plt
from math import exp


# Input params
vary = {
    "kappa": cp.Uniform(0.025, 0.075),
    "t_env": cp.Uniform(15, 25)
}

# The exact solution
def cooling_exact(t, k, Te):
    T0 = 95.
    return Te + (T0 - Te)*exp(-k*t)

# UQ
def cooling_uq(tmpdir):

    # Set up a fresh campaign called "pce"
    my_campaign = uq.Campaign(name='vvtest', work_dir=tmpdir)

    # Define parameter space
    params = {
        "temp_init": {
            "type": "float",
            "min": 0.0,
            "max": 100.0,
            "default": 95.0},
        "kappa": {
            "type": "float",
            "min": 0.0,
            "max": 0.1,
            "default": 0.025},
        "t_env": {
            "type": "float",
            "min": 0.0,
            "max": 40.0,
            "default": 15.0},
        "out_file": {
            "type": "string",
            "default": "output.csv"}
    }

    output_filename = params["out_file"]["default"]
    output_columns = ["te"]

    # Create an encoder, decoder and collater for PCE test app
    encoder = uq.encoders.GenericEncoder(
        template_fname='cooling/cooling.template',
        delimiter='$',
        target_filename='cooling_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns,
                                    header=0)
    collater = uq.collate.AggregateSamples(average=False)

    # Add the PCE app (automatically set as current app)
    my_campaign.add_app(name="vvtest",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater
                        )


    my_sampler = uq.sampling.PCESampler(vary=vary,
                                        polynomial_order=3)

    print("N samples: ", my_sampler._number_of_samples)
    # Associate the sampler with the campaign
    my_campaign.set_sampler(my_sampler)

    # Will draw all (of the finite set of samples)
    my_campaign.draw_samples()
    #my_campaign.draw_samples(num_samples=6)

    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
        "cooling/cooling_model.py cooling_in.json"))

    my_campaign.collate()

    # Post-processing analysis
    my_analysis = uq.analysis.PCEAnalysis(sampler=my_sampler,
                                          qoi_cols=output_columns)

    my_campaign.apply_analysis(my_analysis)

    results = my_campaign.get_last_analysis()

    # Get Descriptive Statistics
    stat = results['statistical_moments']['te']
    dist = results['output_distributions']['te']

    return stat, dist


if __name__ == "__main__":
    # Perform UQ
    stat, dist = cooling_uq("/tmp/")

    # get 10 'measurements' in t=100
    ti = 100
    Texp = []
    for j in range(10):
        k_j = vary["kappa"].sample()
        tenv_j = vary["kappa"].sample()
        Texp.append(cooling_exact(ti, k_j, tenv_j))

    # PLOTS
    t= np.linspace(0, 200, 150)
    mean = np.array(stat["mean"])
    std = np.array(stat['std'])
    plt.plot(t, mean, 'g-', alpha=0.75, label='Mean')
    plt.plot(t, mean-std, 'b-', alpha=0.25)
    plt.plot(t, mean+std, 'b-', alpha=0.25)
    plt.fill_between(
        t,
        mean-std,
        mean+std,
        alpha=0.25,
        label=r'Mean $\pm$ deviation')
    plt.xlabel('Time (min)')
    plt.ylabel('Temperature (°C)', color='b')
    plt.tick_params('y', colors='b')
    plt.legend()
    plt.grid()


    plt.show()
