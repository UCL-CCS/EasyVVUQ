import chaospy as cp
import easyvvuq as uq

__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"


def test_qmc(tmpdir):

    # Set up a fresh campaign called "qmc"
    my_campaign = uq.Campaign(name='qmc', work_dir=tmpdir)

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
            "default": "output.csv"}}

    output_filename = params["out_file"]["default"]
    output_columns = ["te", "ti"]

    # Create an encoder and decoder for QMC test app
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/cooling/cooling.template',
        delimiter='$',
        target_filename='cooling_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns,
                                    header=0)

    # Add the PC app (automatically set as current app)
    my_campaign.add_app(name="qmc",
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

    my_sampler = uq.sampling.QMCSampler(vary=vary,
                                        number_of_samples=100)

    # Associate the sampler with the campaign
    my_campaign.set_sampler(my_sampler)

    # Will draw all (of the finite set of samples)
    my_campaign.draw_samples()

    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
        "tests/cooling/cooling_model.py cooling_in.json"))

    my_campaign.collate()

    # Post-processing analysis
    my_analysis = uq.analysis.QMCAnalysis(sampler=my_sampler,
                                          qoi_cols=output_columns)

    my_campaign.apply_analysis(my_analysis)

    results = my_campaign.get_last_analysis()

    # Get Descriptive Statistics
    stats = results['statistical_moments']['te']
    per = results['percentiles']['te']

    return stats, per


if __name__ == "__main__":

    stats, per = test_qmc("/tmp/")
