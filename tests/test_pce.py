import os
import time
import numpy as np
import chaospy as cp
import easyvvuq as uq

# author: Jalal Lakhlili
__license__ = "LGPL"


def test_pce(tmpdir):

    # Set up a fresh campaign called "pce"
    my_campaign = uq.Campaign(name='pce', workdir=tmpdir)

    # Define parameter space
    params = {
      "kappa":    {"type": "real", "min": "0.0", "max": "0.1",  "default": "0.025"},
      "t_env":    {"type": "real", "min": "0.0", "max": "40.0", "default": "15.0"},
      "out_file": {"type": "str", "default": "output.csv"}
    }

    output_filename = params["out_file"]["default"]
    output_columns = ["te", "ti"]

    # Create an encoder, decoder and collation element for PCE test app
    encoder = uq.encoders.GenericEncoder(template_fname='tests/pce/pce.template',
                                         delimiter='#',
                                         target_filename='pce_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns,
                                    header=0)
    collation = uq.elements.collate.AggregateSamples(average=False)

    # Add the PCE app (automatically set as current app)
    my_campaign.add_app(name="pce",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collation=collation
                        )

    # Create the sampler
    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }

    my_sampler = uq.elements.sampling.PCESampler(vary=vary, polynomial_order=3)

    # Associate the sampler with the campaign
    my_campaign.set_sampler(my_sampler)

    # Will draw all (of the finite set of samples)
    my_campaign.draw_samples()

    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
        "tests/pce/pce_model.py pce_in.json"))

    my_campaign.collate(store=False)

    # Update after here

    # Post-processing analysis
    analysis = uq.elements.analysis.PCEAnalysis(
        my_campaign, value_cols=output_columns)

    analysis.apply()

    # Get Descriptive Statistics
    stats = analysis.statistical_moments('te')
    per = analysis.percentiles('te')
    sobols = analysis.sobol_indices('te', 'first_order')
    #dist_out = analysis.output_distributions('te')

    return stats, per, sobols


if __name__ == "__main__":

    start_time = time.time()
    stats, per, sobols = test_pce("/ptmp/ljala/")
    end_time = time.time()
    print('>>>>> elapsed time = ', end_time - start_time)

    # Plot statistical results
    __plot = False

    if __plot:
        import matplotlib.pyplot as plt
        mean = stats["mean"]
        var = stats["var"]
        p10 = per['p10']
        p90 = per['p90']

        s_kappa = sobols["kappa"]
        s_t_env = sobols["t_env"]

        t = np.linspace(0, 200, 150)

        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax1.plot(t, mean, 'g-', alpha=0.75, label='Mean')
        ax1.plot(t, p10, 'b-', alpha=0.25)
        ax1.plot(t, p90, 'b-', alpha=0.25)
        ax1.fill_between(
            t,
            p10,
            p90,
            alpha=0.25,
            label='90% prediction interval')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Temperature', color='b')
        ax1.tick_params('y', colors='b')
        ax2 = ax1.twinx()
        ax2.plot(t, var, 'r-', alpha=0.5)
        ax2.set_ylabel('Variance', color='r')
        ax2.tick_params('y', colors='r')
        ax1.grid()
        ax1.legend()
        ax1.set_title('Statistical moments')

        fig2 = plt.figure()
        ax = fig2.add_subplot(111)
        ax.plot(t, s_kappa, 'b-', label=r'$\kappa$')
        ax.plot(t, s_t_env, 'g-', label=r'$t_{env}$')
        ax.set_xlabel('Time')
        ax.set_ylabel('Sobol indices')
        ax.grid()
        ax.legend()
        ax.set_title('First order Sobol indices')
        plt.show()
