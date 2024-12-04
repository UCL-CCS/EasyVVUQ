import chaospy as cp
import numpy as np
import easyvvuq as uq
import matplotlib.pyplot as plt
import os
import logging
import pytest
from easyvvuq.actions import CreateRunDirectory, Encode, ExecuteLocal, Decode, Actions

plt.close('all')

# author: Wouter Edeling
__license__ = "LGPL"


def poly_model(theta):
    """
    Analytic test function where some parameters are more important than others.

    Parameters
    ----------
    theta :  array of input parameters in [0, 1]

    Returns
    -------
    (float) function value
    """
    # stocastic dimension of the problem
    d = 3
    a = np.ones(d) * 0.01
    # effective dimension of the problem
    effective_d = 1
    a[0:effective_d] = 1.0

    sol = 1.0
    for i in range(d):
        sol *= 3 * a[i] * theta[i]**2 + 1.0
    return sol / 2**d


@pytest.fixture
def adaptive_campaign():

    d = 3
    number_of_adaptations = 3
    campaign = uq.Campaign(name='sc', work_dir='/tmp')
    params = {}
    for i in range(d):
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
        # template_fname='./sc/poly_model_anisotropic.template',
        delimiter='$',
        target_filename='poly_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns)
    execute = ExecuteLocal(os.path.abspath("tests/sc/poly_model_anisotropic.py") + " poly_in.json")
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))

    # Add the SC app (automatically set as current app)
    campaign.add_app(name="sc",
                     params=params,
                     actions=actions)

    # Create the sampler
    vary = {}
    for i in range(d):
        vary["x%d" % (i + 1)] = cp.Uniform(0, 1)

    sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=1,
                                    quadrature_rule="C",
                                    sparse=True, growth=True,
                                    midpoint_level1=True,
                                    dimension_adaptive=True)
    campaign.set_sampler(sampler)
    campaign.execute().collate()
    data_frame = campaign.get_collation_result()
    analysis = uq.analysis.SCAnalysis(sampler=sampler, qoi_cols=output_columns)

    campaign.apply_analysis(analysis)

    for i in range(number_of_adaptations):
        sampler.look_ahead(analysis.l_norm)

        campaign.execute().collate()
        data_frame = campaign.get_collation_result()
        analysis.adapt_dimension('f', data_frame)

        campaign.apply_analysis(analysis)
    logging.debug(analysis.l_norm)
    logging.debug(sampler.admissible_idx)

    results = campaign.get_last_analysis()

    return sampler, analysis, results


def test_look_ahead(adaptive_campaign):
    """
    Test the sampler.look_ahead function
    """
    sampler, _, _ = adaptive_campaign
    # check if the correct candidate dimensions for the next iteration are selected
    admissible_idx = np.array([[3, 1, 1], [2, 2, 1], [1, 3, 1], [1, 1, 2]])
    # Note: the order is not important and may change between different Python versions.
    # This is because the order is not preserved in the setdiff2d subroutine of the
    # analysis class.
    for idx in admissible_idx:
        assert (idx in sampler.admissible_idx)

    # check if the right number of new samples were computed during the 1st 3 iterations
    assert (sampler.n_new_points == [6, 2, 6])


def test_adapt_dimension(adaptive_campaign):
    """
    Test analysis.adapt_dimension
    """
    _, analysis, _ = adaptive_campaign
    # check if the dimensions were refined in the right order
    assert (np.array_equal(analysis.l_norm, np.array([[1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2]])))


def test_SC2PCE(adaptive_campaign):
    """
    Test the conversion from the SC basis to the PCE basis (analysis.SC2PCE)
    """
    _, analysis, _ = adaptive_campaign
    assert (analysis.pce_coefs['f'][(1, 1, 1)][(1, 1, 1)] ==
            pytest.approx(np.array([0.22204355]), abs=0.0001))
    assert (analysis.pce_coefs['f'][(2, 1, 1)][(1, 1, 1)] ==
            pytest.approx(np.array([0.25376406]), abs=0.0001))
    assert (analysis.pce_coefs['f'][(2, 1, 1)][(2, 1, 1)] ==
            pytest.approx(np.array([0.10988306]), abs=0.0001))


def test_comb_coef(adaptive_campaign):
    """
    Test the computation of combination coefficients (analysis.compute_comb_coef)
    """
    _, analysis, _ = adaptive_campaign
    coefs = analysis.compute_comb_coef(l_norm=np.array([[1, 1, 1], [1, 2, 1], [1, 3, 1],
                                                        [2, 1, 1], [2, 2, 1]]))
    assert (coefs == {(1, 1, 1): 0.0, (1, 2, 1): -1.0,
                      (1, 3, 1): 1.0, (2, 1, 1): 0.0, (2, 2, 1): 1.0})


def test_error(adaptive_campaign):
    """

    """
    _, analysis, _ = adaptive_campaign
    assert (np.array_equal(analysis.adaptation_errors, np.array(
        [0.19032304687500004, 0.0033058593749999976, 0.0033058593749999976])))


def test_results(adaptive_campaign):
    """
    Test if the moments and Sobol indices are correctly computed, using analytical reference.
    """
    _, analysis, results = adaptive_campaign

    # analytic mean and standard deviation
    d = 3
    a = np.ones(d) * 0.01
    effective_d = 1
    a[0:effective_d] = 1.0
    ref_mean = np.prod(a[0:d] + 1) / 2**d
    ref_std = np.sqrt(np.prod(9 * a[0:d]**2 / 5 + 2 * a[0:d] + 1) / 2**(2 * d) - ref_mean**2)

    # check moments
    computed_mean = results.describe('f', 'mean')
    computed_std = results.describe('f', 'std')
    assert (computed_mean == pytest.approx(ref_mean, 0.01))
    assert (computed_std == pytest.approx(ref_std, 0.1))

    # check sobols, x_1 should be close to 1, others to 0
    assert (results._get_sobols_first('f', 'x1') == pytest.approx(1.0, abs=0.01))
    assert (results._get_sobols_first('f', 'x2') == pytest.approx(0.0, abs=0.01))
    assert (results._get_sobols_first('f', 'x3') == pytest.approx(0.0, abs=0.01))

    # check the quality of the polynomial surrogate
    x = np.array([0.2, 0.1, 0.6])
    f_at_x = poly_model(x)
    surrogate_at_x = analysis.surrogate('f', x)
    assert (f_at_x == pytest.approx(surrogate_at_x, abs=0.01))

    # check uncertainty magnification factor
    assert (analysis.get_uncertainty_amplification('f') == pytest.approx(0.8048, abs=1e-4))
