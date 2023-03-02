import pytest
import numpy as np
import easyvvuq as uq
from easyvvuq.actions import CreateRunDirectory, Encode, Decode, ExecuteLocal, Actions


@pytest.fixture
def sampler():
    vary = {"x1": [0.0, 0.5, 1.0],
            "x2": [True, False]}
    return uq.sampling.Grid_Sampler(vary)


@pytest.fixture
def campaign():

    params = {}
    params["x1"] = {"type": "float", "default": 0.5}
    params["x2"] = {"type": "boolean", "default": True}

    # python file is its own template
    encoder = uq.encoders.GenericEncoder('tests/grid_search/test_grid.template',
                                         target_filename='test_grid.py')

    execute = ExecuteLocal("python3 test_grid.py")

    output_columns = ["f"]
    decoder = uq.decoders.SimpleCSV(
        target_filename='out.csv',
        output_columns=output_columns)

    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))

    campaign = uq.Campaign(name='foo', work_dir='/tmp', params=params, actions=actions)

    vary = {"x1": [0.0, 0.5, 1.0],
            "x2": [True, False]}

    sampler = uq.sampling.Grid_Sampler(vary)

    campaign.set_sampler(sampler)

    campaign.execute().collate()

    return campaign


def test_tensor_product(sampler):
    # test if the tensor product gets constructed properly
    points = sampler.points
    assert (points == np.array([[0.0, True],
                                [0.0, False],
                                [0.5, True],
                                [0.5, False],
                                [1.0, True],
                                [1.0, False]], dtype=object)).all()


def test_grid_search(campaign):
    # test if the sampling works correctly
    df = campaign.get_collation_result()
    assert (df['f'].values == np.array([[0.],
                                        [-0.],
                                        [0.25],
                                        [-0.25],
                                        [1.],
                                        [-1.]])).all()
