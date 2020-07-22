import chaospy as cp
import numpy as np
import easyvvuq as uq
import matplotlib.pyplot as plt

plt.close('all')

# author: Wouter Edeling
__license__ = "LGPL"


def run_campaign(d, number_of_adaptations):
    """
    Runs a EasVVUQ campaign with the dimension adaptive SC sampler

    Parameters
    ----------
    d : int (max 10) the number of uncertain variables
    number_of_adaptations : (int) how many adaptation steps are taken

    Returns
    -------
    None.

    """
    # Set up a fresh campaign called "sc"
    my_campaign = uq.Campaign(name='sc', work_dir='/tmp')

    # Define parameter space
    params = {}
    for i in range(10):
        params["x%d" % (i + 1)] = {"type": "float",
                                   "min": 0.0,
                                   "max": 1.0,
                                   "default": 0.5}
    params["out_file"] = {"type": "string", "default": "output.csv"}

    output_filename = params["out_file"]["default"]
    output_columns = ["f"]

    # Create an encoder, decoder and collation element
    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/sc/poly_model_anisotropic.template',
        delimiter='$',
        target_filename='poly_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns,
                                    header=0)
    collater = uq.collate.AggregateSamples(average=False)

    # Add the SC app (automatically set as current app)
    my_campaign.add_app(name="sc",
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        collater=collater)

    # Create the sampler
    vary = {}
    for i in range(d):
        vary["x%d" % (i + 1)] = cp.Uniform(0, 1)

    my_sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=1,
                                       quadrature_rule="C",
                                       sparse=True, growth=True,
                                       midpoint_level1=True,
                                       dimension_adaptive=True)

    # Associate the sampler with the campaign
    my_campaign.set_sampler(my_sampler)

    # Will draw all (of the finite set of samples)
    my_campaign.draw_samples()
    my_campaign.populate_runs_dir()

    # Run the samples using EasyVVUQ on the localhost
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
        "tests/sc/poly_model_anisotropic.py poly_in.json"))

    my_campaign.collate()
    data_frame = my_campaign.get_collation_result()

    # Post-processing analysis
    analysis = uq.analysis.SCAnalysis(sampler=my_sampler, qoi_cols=output_columns)

    my_campaign.apply_analysis(analysis)

    for i in range(number_of_adaptations):
        my_sampler.look_ahead(analysis.l_norm)

        my_campaign.draw_samples()
        my_campaign.populate_runs_dir()
        my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal(
            "tests/sc/poly_model_anisotropic.py poly_in.json"))
        my_campaign.collate()
        data_frame = my_campaign.get_collation_result()
        analysis.adapt_dimension('f', data_frame)

        my_campaign.apply_analysis(analysis)

    results = my_campaign.get_last_analysis()

    analysis.plot_grid()

    # analytic mean and standard deviation
    a = np.ones(d) * 0.01
    effective_d = 1
    a[0:effective_d] = 1.0

    ref_mean = np.prod(a[0:d] + 1) / 2**d
    ref_std = np.sqrt(np.prod(9 * a[0:d]**2 / 5 + 2 * a[0:d] + 1) / 2**(2 * d) - ref_mean**2)

    print("======================================")
    print("Number of samples = %d" % my_sampler._number_of_samples)
    print("--------------------------------------")
    print("Analytic mean = %.4f" % ref_mean)
    print("Computed mean = %.4f" % results['statistical_moments']['f']['mean'])
    print("--------------------------------------")
    print("Analytic standard deiation = %.4f" % ref_std)
    print("Computed standard deiation = %.4f" % results['statistical_moments']['f']['std'])
    print("--------------------------------------")
    print("First order Sobol indices =", results['sobols_first']['f'])
    print("--------------------------------------")


if __name__ == '__main__':
    run_campaign(3, 6)
