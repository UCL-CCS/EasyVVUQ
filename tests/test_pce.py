import chaospy as cp
import easyvvuq as uq

__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"


def test_pce(tmpdir):

    # Set up a fresh campaign called "pce"
    my_campaign = uq.Campaign(name='pce', work_dir=tmpdir)

    # Define parameter space
    params = {
        "kappa": {
            "type": "real",
            "min": "0.0",
            "max": "0.1",
            "default": "0.025"},
        "t_env": {
            "type": "real",
            "min": "0.0",
            "max": "40.0",
            "default": "15.0"},
        "out_file": {
            "type": "str",
            "default": "output.csv"}}

    output_filename = params["out_file"]["default"]
    output_columns = ["te", "ti"]

    # Create an encoder and decoder for PCE test app
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/pce/pce.template',
        delimiter='$',
        target_filename='pce_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns,
                                    header=0)

    # Add the PCE app (automatically set as current app)
    my_campaign.add_app(name="pce",
                        params=params,
                        encoder=encoder,
                        decoder=decoder
                        )

    # Create a collation element for this campaign
    collater = uq.collate.AggregateSamples(average=False)
    my_campaign.set_collater(collater)

    # Create the sampler
    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }

    my_sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=3)

    # Associate the sampler with the campaign
    my_campaign.set_sampler(my_sampler)

    # Will draw all (of the finite set of samples)
    my_campaign.draw_samples()

    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
        "tests/pce/pce_model.py pce_in.json"))

    my_campaign.collate()

    # Update after here

    # Post-processing analysis
    pce_analysis = uq.analysis.PCEAnalysis(sampler=my_sampler,
                                           qoi_cols=output_columns)

    my_campaign.apply_analysis(pce_analysis)

    results = my_campaign.get_last_analysis()

    # Get Descriptive Statistics
    stats = results['statistical_moments']['te']
    per = results['percentiles']['te']
    S1 = results['sobol_indices']['te']['first']
    St = results['sobol_indices']['te']['total']
    sobols = [S1, St]
    dist_out = results['output_distributions']['te']

    # Test saving and reloading campaign
    state_file = tmpdir + "pce_state.json"
    my_campaign.save_state(state_file)
    new = uq.Campaign(state_file=state_file, work_dir=tmpdir)
    print(new)

    return stats, per, sobols, dist_out


if __name__ == "__main__":

    stats, per, sobols, dist_out = test_pce("/tmp/")
