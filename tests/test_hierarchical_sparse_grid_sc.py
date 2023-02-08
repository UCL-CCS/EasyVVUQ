import os
import easyvvuq as uq
import numpy as np
import chaospy as cp
import pytest
import logging
from easyvvuq.actions import CreateRunDirectory, Encode, ExecuteLocal, Decode, Actions


def exact_sobols_g_func(d=2, a=[0.0, 0.5, 3.0, 9.0, 99.0]):
    # for the Sobol g function, the exact (1st-order)
    # Sobol indices are known analytically
    V_i = np.zeros(d)
    for i in range(d):
        V_i[i] = 1.0 / (3.0 * (1 + a[i])**2)
    V = np.prod(1 + V_i) - 1
    logging.debug('Exact 1st-order Sobol indices: ', V_i / V)
    return V_i / V


# number of unknown variables
d = 2

# author: Wouter Edeling
__license__ = "LGPL"

HOME = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def sparse_campaign():
    # Set up a fresh campaign called "sc"
    campaign = uq.Campaign(name='sc', work_dir='/tmp')

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
        "out_file": {
            "type": "string",
            "default": "output.csv"}}

    output_filename = params["out_file"]["default"]
    output_columns = ["f"]

    # Create an encoder, decoder and collation element
    encoder = uq.encoders.GenericEncoder(
        template_fname=HOME + '/sc/sobol.template',
        delimiter='$',
        target_filename='poly_in.json')
    decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
                                    output_columns=output_columns)
    execute = ExecuteLocal(os.path.abspath("tests/sc/sobol_model.py") + " poly_in.json")
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))

    # Add the SC app (automatically set as current app)
    campaign.add_app(name="sc",
                     params=params,
                     actions=actions)

    # Create the sampler
    vary = {
        "x1": cp.Uniform(0.0, 1.0),
        "x2": cp.Uniform(0.0, 1.0)}

    # To use 'next_level_sparse_grid' below, we must select a nested
    # sparse grid here
    sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=5,
                                    quadrature_rule="C", sparse=True,
                                    growth=True)

    # Associate the sampler with the campaign
    campaign.set_sampler(sampler)

    logging.debug('Number of samples:', sampler.n_samples)

    campaign.execute().collate()

    # Post-processing analysis
    analysis = uq.analysis.SCAnalysis(sampler=sampler, qoi_cols=output_columns)
    campaign.apply_analysis(analysis)
    results = campaign.get_last_analysis()

    n_adaptations = 1

    for i in range(n_adaptations):
        # update the sparse grid to the next level
        sampler.next_level_sparse_grid()
        campaign.execute().collate()

    campaign.apply_analysis(analysis)
    results = campaign.get_last_analysis()

    return sampler, analysis, results


def test_next_level_sparse_grid(sparse_campaign):
    """
    Check if the isotropic refinement worked properly (sampler.next_level_sparse_grid)
    """
    sampler, analysis, _ = sparse_campaign
    # we started with a level 5 grid, check if the grid is now level 6
    validation_array = np.array([[1, 1], [1, 2], [2, 1], [1, 3], [3, 1],
                                 [2, 2], [3, 2], [2, 3], [4, 1], [1, 4],
                                 [5, 1], [3, 3], [1, 5], [4, 2], [2, 4],
                                 [6, 1], [5, 2], [1, 6], [4, 3], [2, 5],
                                 [3, 4]])
    all_in = True
    for l in validation_array:
        if l not in analysis.l_norm:
            all_in = False
            break
    assert (all_in)

    # check if the grid has the right size
    assert (sampler.xi_d.shape[0] == 145)


def test_results(sparse_campaign):
    """
    Check if the results were computed correctly
    """
    _, _, results = sparse_campaign
    ref_sobols = exact_sobols_g_func()

    # check the computed Sobol indices against the analytical result
    for i in range(ref_sobols.size):
        computed_sobol = results._get_sobols_first('f', 'x%d' % (i + 1))
        logging.debug('Exact Sobol indices x%d = %.4f' % (i + 1, ref_sobols[i]))
        logging.debug('Computed Sobol indices x%d = %.4f' % (i + 1, computed_sobol))
        assert (ref_sobols[i] == pytest.approx(computed_sobol, abs=0.01))
