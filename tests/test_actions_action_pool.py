import pytest
import time
import chaospy as cp
from unittest.mock import MagicMock
from easyvvuq.actions import ActionPool, ExecutePython, Actions
from easyvvuq import Campaign
from easyvvuq.sampling import RandomSampler


@pytest.fixture
def campaign():
    def model(params):
        return {'y': params['x'] + 1}
    actions = Actions(ExecutePython(model))
    sampler = RandomSampler({'x': cp.Uniform(0, 1)})
    campaign = Campaign('test', {'x': {'default': 0}}, actions)
    campaign.set_sampler(sampler)
    return campaign


def test_action_pool_start(campaign):
    action_pool = campaign.execute(nsamples=3)
    assert (len(action_pool.futures) == 3)
    action_pool.collate()
    assert (len(action_pool.campaign.get_collation_result()) == 3)
    assert (action_pool.progress() == {'ready': 0, 'active': 0, 'finished': 3, 'failed': 0})


def test_action_pool_start_sequential(campaign):
    action_pool = campaign.execute(nsamples=3, sequential=True)
    assert (len(action_pool.results) == 3)
    action_pool.collate()
    assert (len(action_pool.campaign.get_collation_result()) == 3)
