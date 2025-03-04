"""
Test if a mix of continuous variables (Normal here) and DiscreteUniform
inputs leads to input.json files containing floats for the normal variables,
and integers for the DiscreteUniform inputs
"""

import os
import pytest
import easyvvuq as uq
import chaospy as cp
from easyvvuq.actions import CreateRunDirectory, Encode, ExecuteLocal, Decode, Actions

@pytest.fixture
def get_campaign():
    """
    Create a Campaign for the dummy_type_test/dummy_type model
    """
    WORK_DIR = '/tmp'

    params = {
        "x1": {"type": "integer", "default": 1},
        "x2": {"type": "float", "default": 1.0}
    }

    vary = {
        "x1": cp.DiscreteUniform(0, 5),
        "x2": cp.Normal(1., 1.),
    }

    encoder = uq.encoders.GenericEncoder(
        template_fname="tests/dummy_type_model/config.template",
        delimiter="$", target_filename="input.json"
    )

    decoder = uq.decoders.SimpleCSV(
        target_filename="output.csv", output_columns=["types"]
    )

    execute = ExecuteLocal(os.path.abspath("tests/dummy_type_model/dummy_type.py") + " input.json")

    actions = Actions(CreateRunDirectory(WORK_DIR, flatten=True),
                      Encode(encoder),
                      execute,
                      Decode(decoder))

    campaign = uq.Campaign(name="dummy_type", params=params, actions=actions,
                           work_dir=WORK_DIR, verify_all_runs=True)

    return campaign, vary


def test_sc(get_campaign):
    """
    Perform the test for the SC sampler
    """
    campaign, vary = get_campaign
    sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=1)
    campaign.set_sampler(sampler)
    campaign.execute().collate()
    df = campaign.get_collation_result()
    assert df.values[0][-1] == 'float'
    assert df.values[0][-2] == 'int'

def test_pce(get_campaign):
    """
    Perform the test for the PCE sampler
    """
    campaign, vary = get_campaign
    sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=1)
    campaign.set_sampler(sampler)
    campaign.execute().collate()
    df = campaign.get_collation_result()
    assert df.values[0][-1] == 'float'
    assert df.values[0][-2] == 'int'

def test_mc(get_campaign):
    """
    Perform the test for the MC sampler
    """
    campaign, vary = get_campaign
    sampler = uq.sampling.MCSampler(vary=vary, n_mc_samples=1)
    campaign.set_sampler(sampler)
    campaign.execute().collate()
    df = campaign.get_collation_result()
    assert df.values[0][-1] == 'float'
    assert df.values[0][-2] == 'int'
