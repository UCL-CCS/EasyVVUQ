import os, time
import numpy    as np
import chaospy  as cp
import easyvvuq as uq

# author: Jalal Lakhlili

# ...
def test_pce(tmpdir):
    input_json = "tests/pce/pce_in.json"
    output_json = os.path.join(tmpdir, "out_pce.json")

    assert(os.path.exists(input_json))

    # Initialize Campaign object
    my_campaign = uq.Campaign(state_filename=input_json, workdir=tmpdir)

    # Define the parameters dictionary
    my_campaign.vary_param("kappa", dist=cp.Uniform(0.025, 0.075))
    my_campaign.vary_param("t_env", dist=cp.Uniform(15, 25))

    # Create the sampler
    my_sampler = uq.elements.sampling.PCESampler(my_campaign)

    # Use the sampler
    my_campaign.add_runs(my_sampler)
    my_campaign.populate_runs_dir()

    # Execute runs
    my_campaign.apply_for_each_run_dir(
        uq.actions.ExecuteLocal("tests/pce/pce_model.py pce_in.json"))

    # Aggregate the results from all runs.
    output_filename = my_campaign.params_info['out_file']['default']
    output_columns = ['te']

    aggregate = uq.elements.collate.AggregateSamples(
        my_campaign,
        output_filename = output_filename,
        output_columns  = output_columns,
        header = 0,
    )

    aggregate.apply()

    # Post-processing analysis
    analysis = uq.elements.analysis.PCEAnalysis(
        my_campaign, value_cols=output_columns)

    stats, sobols, corr_matrix = analysis.apply()

    return stats, sobols
# ...


if __name__ == "__main__":

    start_time = time.time()

    stats, sobols  = test_pce("/tmp/")

    end_time = time.time()
    print('>>>>> elapsed time = ', end_time - start_time)

    # Plot statistical results
    __plot = False

    if __plot:
        import matplotlib.pyplot as plt
        mean = stats["mean"].to_numpy()
        std  = stats["std"].to_numpy()
        var  = stats["var"].to_numpy()

        s_kappa = sobols["kappa"].to_numpy()
        s_t_env = sobols["t_env"].to_numpy()

        t = np.linspace(0, 200, 150)

        fig1 = plt.figure()

        ax11 = fig1.add_subplot(111)
        ax11.plot(t, mean, 'g-', alpha=0.75, label='Mean')
        ax11.plot(t, mean - std, 'b-', alpha=0.25)
        ax11.plot(t, mean + std, 'b-', alpha=0.25)
        ax11.fill_between(
            t,
            mean - std,
            mean + std,
            alpha=0.25,
            label=r'Mean $\pm$ deviation')
        ax11.set_xlabel('Time')
        ax11.set_ylabel('Temperature', color='b')
        ax11.tick_params('y', colors='b')
        ax11.legend()

        ax12 = ax11.twinx()
        ax12.plot(t, var, 'r-', alpha=0.5)
        ax12.set_ylabel('Variance', color='r')
        ax12.tick_params('y', colors='r')

        ax11.grid()
        plt.title('Statistical moments')

        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111)
        ax2.plot(t, s_kappa, 'b-', label=r'$\kappa$')
        ax2.plot(t, s_t_env, 'g-', label=r'$t_{env}$')
        ax2.legend()
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Sobol indices')
        ax2.set_title('First order Sobol indices')

        ax2.grid()
        ax2.legend()

        plt.show()
