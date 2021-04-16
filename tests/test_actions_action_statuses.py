import pytest
import time
from unittest.mock import MagicMock
from easyvvuq.actions import ActionPool


@pytest.fixture(scope="module", params=[False])
def action_pool():
    campaign = MagicMock()
    actions = MagicMock()
    inits = [MagicMock(), MagicMock(), MagicMock()]
    return ActionPool(campaign, actions, inits, sequential=False)


def test_action_pool_start(action_pool):
    pass
