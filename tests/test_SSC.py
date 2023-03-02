import os
import chaospy as cp
import numpy as np
import easyvvuq as uq
# import matplotlib.pyplot as plt
from easyvvuq.actions import CreateRunDirectory, Encode, Decode, ExecuteLocal, Actions
# from matplotlib import cm
import pytest


def f(x1, x2):
    """
    Discontinuous 2D test function

    Parameters
    ----------
    x1 : float
        1st input in [0, 1].
    x2 : float
        2nd input in [0, 1].

    Returns
    -------
    float
        Function value at (x1, x2)

    """

    if x2 <= -0.6 * x1 + 0.8:
        return x1 + x2 - 1
    else:
        return x1 ** 3 + x2 ** 2 + 1


@pytest.fixture
def SSC_campaign():
    ##################################
    # Define (total) parameter space #
    ##################################

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
            "default": 0.5}}

    ###########################
    # Set up a fresh campaign #
    ###########################

    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/discont_model/discont_model.template',
        delimiter='$',
        target_filename='input.csv')

    execute = ExecuteLocal(os.path.abspath("tests/discont_model/discont_model.py"))

    output_columns = ["f"]
    decoder = uq.decoders.SimpleCSV(
        target_filename='output.csv',
        output_columns=output_columns)

    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))

    # actions = Actions(CreateRunDirectory(root='/tmp', flatten=True), Encode(encoder), execute,
    #                   Decode(decoder))

    campaign = uq.Campaign(name='foo', work_dir='/tmp', params=params, actions=actions)

    #######################
    # Specify input space #
    #######################

    vary = {
        "x1": cp.Uniform(0.0, 1.0),
        "x2": cp.Uniform(0.0, 1.0)
    }

    ##################
    # Select sampler #
    ##################

    sampler = uq.sampling.SSCSampler(vary=vary)

    # Associate the sampler with the campaign
    campaign.set_sampler(sampler)

    # ###############################
    # # execute the defined actions #
    # ###############################

    campaign.execute().collate()

    analysis = uq.analysis.SSCAnalysis(sampler=sampler, qoi_cols=['f'])

    return campaign, sampler, analysis


@pytest.fixture
def SSC_campaign_1D():
    ##################################
    # Define (total) parameter space #
    ##################################

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
            "default": 0.5}}

    ###########################
    # Set up a fresh campaign #
    ###########################

    encoder = uq.encoders.GenericEncoder(
        template_fname='tests/discont_model/discont_model.template',
        delimiter='$',
        target_filename='input.csv')

    execute = ExecuteLocal(os.path.abspath("tests/discont_model/discont_model.py"))

    output_columns = ["f"]
    decoder = uq.decoders.SimpleCSV(
        target_filename='output.csv',
        output_columns=output_columns)

    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))

    # actions = Actions(CreateRunDirectory(root='/tmp', flatten=True), Encode(encoder), execute,
    #                   Decode(decoder))

    campaign = uq.Campaign(name='foo', work_dir='/tmp', params=params, actions=actions)

    #######################
    # Specify input space #
    #######################

    vary = {
        "x1": cp.Uniform(0.0, 1.0),
    }

    ##################
    # Select sampler #
    ##################

    sampler = uq.sampling.SSCSampler(vary=vary)

    # Associate the sampler with the campaign
    campaign.set_sampler(sampler)

    # ###############################
    # # execute the defined actions #
    # ###############################

    campaign.execute().collate()

    analysis = uq.analysis.SSCAnalysis(sampler=sampler, qoi_cols=['f'])

    return campaign, sampler, analysis


def test_init(SSC_campaign):
    # test the grid initialization
    _, sampler, _ = SSC_campaign
    points = sampler.tri.points
    assert ((points == np.array([[0., 0.],
                                 [0., 1.],
                                 [1., 0.],
                                 [1., 1.],
                                 [0.5, 0.5]])).all())
    assert (sampler.pmax_cutoff == 4)


def test_find_pmax(SSC_campaign):
    # test finding the max polynomials order, given the number of samples
    _, sampler, _ = SSC_campaign
    assert (sampler.find_pmax(5) == 1)
    assert (sampler.find_pmax(6) == 2)
    assert (sampler.find_pmax(10) == 3)


def test_compute_vol(SSC_campaign):
    # test simplex volume computation
    _, sampler, _ = SSC_campaign
    assert ((sampler.compute_vol() == np.array([0.25, 0.25, 0.25, 0.25])).all())


def test_compute_xi_center(SSC_campaign):
    # test computing the center of the simplex elements
    _, sampler, _ = SSC_campaign
    assert sampler.compute_xi_center_j() == pytest.approx(np.array([[0.16666667, 0.5],
                                                                    [0.5, 0.16666667],
                                                                    [0.5, 0.83333333],
                                                                    [0.83333333, 0.5]]), 1e-5)


def test_sub_simplex(SSC_campaign):
    # test computing the subvertices of a simplex
    _, sampler, _ = SSC_campaign
    assert (sampler.compute_sub_simplex_vertices(0) == np.array([[0., 0.5],
                                                                 [0.25, 0.25],
                                                                 [0.25, 0.75]])).all()


def test_sampling(SSC_campaign):
    _, sampler, _ = SSC_campaign
    np.random.seed(42)
    assert sampler.sample_inputs(1) == pytest.approx(np.array([[0.37454012, 0.95071431]]), 1e-5)


def test_probability(SSC_campaign):
    # check if the simplex probabilities are computed correctly
    _, sampler, _ = SSC_campaign
    assert sampler.compute_probability() == pytest.approx(np.array([0.25, 0.25, 0.25, 0.25]), 0.01)


def test_compute_i_norm_le_pj(SSC_campaign):
    # test the multi index sets |i| = i_1 + i_1 <= p
    _, sampler, _ = SSC_campaign
    i_norm_le_p_j = sampler.compute_i_norm_le_pj(3)
    assert (i_norm_le_p_j[1] == np.array([[0, 0], [0, 1], [1, 0]])).all()
    assert (i_norm_le_p_j[2] == np.array([[0, 0],
                                          [0, 1],
                                          [0, 2],
                                          [1, 0],
                                          [1, 1],
                                          [2, 0]])).all()
    assert (i_norm_le_p_j[3] == np.array([[0, 0],
                                          [0, 1],
                                          [0, 2],
                                          [0, 3],
                                          [1, 0],
                                          [1, 1],
                                          [1, 2],
                                          [2, 0],
                                          [2, 1],
                                          [3, 0]])).all()


def test_compute_stencil_j(SSC_campaign):
    # test nearest neighbour stencil computation
    _, sampler, _ = SSC_campaign
    assert (sampler.compute_stencil_j() == np.array([[4, 1, 0, 2, 3],
                                                    [2, 4, 0, 1, 3],
                                                    [4, 3, 1, 0, 2],
                                                    [3, 4, 2, 0, 1]])).all()


def test_find_simplices(SSC_campaign):
    _, sampler, _ = SSC_campaign
    assert sampler.find_simplices(sampler.tri.simplices[0]) == np.array([0])
    assert sampler.find_simplices(sampler.tri.simplices[1]) == np.array([1])
    assert sampler.find_simplices(sampler.tri.simplices[2]) == np.array([2])
    assert sampler.find_simplices(sampler.tri.simplices[3]) == np.array([3])


def check_LEC_ENO(SSC_campaign):
    # test LEC + ENO subroutines, more comprehensive LEC test done in test_adapt_locally
    campaign, sampler, analysis = SSC_campaign

    data_frame = campaign.get_collation_result()

    # the number of code evaluations
    n_s = sampler.n_samples
    # the number of simplex elements
    n_e = sampler.n_elements

    # load the EasyVVUQ data frame
    analysis.load_samples(data_frame)
    # code outputs
    v = analysis.samples['f']

    # find the max polynomial order and set the p_j = pmax
    pmax = sampler.find_pmax(n_s)

    # polynomial order per simplex elememt
    p_j = (np.ones(n_e) * pmax).astype('int')

    # compute nearest neighbour stencils
    S_j = sampler.compute_stencil_j()

    # check the LEC condition of all stencil
    np.random.seed(42)

    res_LEC = sampler.check_LEC(p_j, v, S_j, n_mc=5)

    assert (res_LEC['p_j'] == np.array([1, 1, 1, 1])).all()
    assert res_LEC['el_idx'][0] == np.array([0])
    assert res_LEC['el_idx'][1] == np.array([1])
    assert res_LEC['el_idx'][2] == np.array([2])
    assert res_LEC['el_idx'][3] == np.array([3])

    p_j = res_LEC['p_j']
    S_j = res_LEC['S_j']
    el_idx = res_LEC['el_idx']

    # convert the nearest-neighbour stencils to ENO stencils
    _, p_j, el_idx = sampler.compute_ENO_stencil(p_j, S_j, el_idx)

    # nothing should have changed yet
    assert (p_j == np.array([1, 1, 1, 1])).all()
    assert el_idx[0] == np.array([0])
    assert el_idx[1] == np.array([1])
    assert el_idx[2] == np.array([2])
    assert el_idx[3] == np.array([3])


def test_adapt_locally(SSC_campaign):
    # test of full adaptation workflow
    campaign, sampler, analysis = SSC_campaign
    np.random.seed(42)

    # number of samples used in the LEC check
    n_mc = 50

    # max number of functions evaluations that can be run in parallel
    max_fjobs = 4

    analysis = uq.analysis.SSCAnalysis(sampler=sampler, qoi_cols=['f'])

    for i in range(2):
        data_frame = campaign.get_collation_result()
        analysis.update_surrogate('f', data_frame, n_mc_LEC=n_mc)
        analysis.adapt_locally(max_fjobs)
        campaign.execute().collate()

    data_frame = campaign.get_collation_result()
    analysis.update_surrogate('f', data_frame)

    # check if sampler.check_LEC worked
    assert (analysis.p_j == np.array([2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2])).all()


def test_adapt_locally_1D(SSC_campaign_1D):
    # test of full adaptation workflow with 1 variable (tests Tri1D class
    # in SSCSampler)
    campaign, sampler, analysis = SSC_campaign_1D
    np.random.seed(42)

    # number of samples used in the LEC check
    n_mc = 50

    # max number of functions evaluations that can be run in parallel
    max_fjobs = 4

    analysis = uq.analysis.SSCAnalysis(sampler=sampler, qoi_cols=['f'])

    for i in range(2):
        data_frame = campaign.get_collation_result()
        analysis.update_surrogate('f', data_frame, n_mc_LEC=n_mc)
        analysis.adapt_locally(max_fjobs)
        campaign.execute().collate()

    data_frame = campaign.get_collation_result()
    analysis.update_surrogate('f', data_frame)

    assert (analysis.p_j == np.array([4, 4, 4, 4, 1, 3, 3, 3])).all()


def test_sample_simplex(SSC_campaign):
    # test the random simplex sampling
    _, sampler, _ = SSC_campaign

    n_mc = 10
    n_xi = 2
    xi_k_jl = sampler.tri.points[sampler.tri.simplices[0]]
    np.random.seed(42)
    x = sampler.sample_simplex(n_mc, xi_k_jl)

    avg = np.sum(xi_k_jl, 0) / (n_xi + 1.)
    el = sampler.tri.find_simplex(avg)

    outside_simplex = 0
    for i in range(n_mc):
        if sampler.tri.find_simplex(x[i, :]) != el:
            outside_simplex += 1

    # none of the simplex samples in x should lie outside the target simplex
    # with points xi_k_jl
    assert outside_simplex == 0


def test_sample_simplex_edge(SSC_campaign):
    # test edge refinement
    _, sampler, _ = SSC_campaign

    np.random.seed(42)
    xi, _, _ = sampler.sample_simplex_edge(0, [])
    assert xi == pytest.approx(np.array([0., 0.52509198]), 1e-5)


def test_surplus(SSC_campaign):
    # test hierarchical surplus computation
    campaign, sampler, analysis = SSC_campaign
    n_xi = 2
    xi_k_jl = sampler.tri.points[sampler.tri.simplices[0]]
    xi_k_jref = np.sum(xi_k_jl, 0) / (n_xi + 1.)
    S_j = sampler.compute_stencil_j()
    p_j = np.ones(4).astype('int')

    data_frame = campaign.get_collation_result()

    # load the EasyVVUQ data frame
    analysis.load_samples(data_frame)
    # code outputs
    v = analysis.samples['f']

    v_k_jref = f(xi_k_jref[0], xi_k_jref[1])

    surplus = sampler.compute_surplus_k(xi_k_jref, S_j, p_j, v, v_k_jref)

    assert surplus == pytest.approx(2 / 3, 1e-5)


def test_surrogate(SSC_campaign):
    campaign, _, analysis = SSC_campaign
    data_frame = campaign.get_collation_result()
    analysis.update_surrogate('f', data_frame)

    assert analysis.surrogate('f', np.array([0, 0])) == pytest.approx(np.array([-1]), 1e-5)
    assert analysis.surrogate('f', np.array([0.5, 0.5])) == pytest.approx(np.array([0]), 1e-5)


def test_compute_eps_bar_j(SSC_campaign):
    # test geometric refinement measure
    campaign, sampler, analysis = SSC_campaign
    data_frame = campaign.get_collation_result()
    analysis.update_surrogate('f', data_frame)

    eps_bar_j, _ = sampler.compute_eps_bar_j(analysis.p_j, analysis.prob_j)

    assert eps_bar_j == pytest.approx(
        np.array([0.01559687, 0.01564313, 0.01560813, 0.01565187]), 0.01)
