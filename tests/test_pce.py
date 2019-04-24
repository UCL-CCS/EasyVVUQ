import os
import time
import numpy as np
import chaospy as cp
import easyvvuq as uq

# author: Jalal Lakhlili
__license__ = "LGPL"


def test_pce(tmpdir):

    # Params for testing
    input_json = "tests/pce/pce_in.json"
    output_json = os.path.join(tmpdir, "out_pce.json")

    assert(os.path.exists(input_json))

    # Initialize Campaign object
    my_campaign = uq.Campaign(
        name='test_campaign',
        state_filename=input_json,
        workdir=tmpdir
    )

    # Define the parameters dictionary
    my_campaign.vary_param("kappa", dist=cp.Uniform(0.025, 0.075))
    my_campaign.vary_param("t_env", dist=cp.Uniform(15, 25))

    # Create the sampler
    my_sampler = uq.elements.sampling.PCESampler(
        my_campaign, polynomial_order=3)

    # Use the sampler
    my_campaign.add_runs(my_sampler)
    my_campaign.populate_runs_dir()

    # Execute runs
    my_campaign.apply_for_each_run_dir(
        uq.actions.ExecuteLocal("tests/pce/pce_model.py pce_in.json"))

    # Aggregate the results from all runs.
    output_filename = my_campaign.params_info["out_file"]["default"]
    output_columns = ["te", "ti"]

    aggregate = uq.elements.collate.AggregateSamples(
        my_campaign,
        output_filename=output_filename,
        output_columns=output_columns,
        header=0,
    )

    aggregate.apply()

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
