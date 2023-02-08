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
    action_pool.start()
    assert (action_pool.progress()['finished'] == 3)
    mock1 = MagicMock()
    mock1.running = MagicMock(return_value=True)
    mock1.done = MagicMock(return_value=False)
    mock1.result = MagicMock(return_value=False)
    mock2 = MagicMock()
    mock2.running = MagicMock(return_value=False)
    mock2.done = MagicMock(return_value=True)
    mock2.result = MagicMock(return_value=False)
    mock3 = MagicMock()
    mock3.running = MagicMock(return_value=False)
    mock3.done = MagicMock(return_value=True)
    mock3.result = MagicMock(return_value=True)
    mock4 = MagicMock()
    mock4.running = MagicMock(return_value=False)
    mock4.done = MagicMock(return_value=False)
    mock4.result = MagicMock(return_value=False)
    action_pool.futures = [mock1, mock2, mock3, mock4]
    progress = action_pool.progress()
    assert (progress['ready'] == 1)
    assert (progress['active'] == 1)
    assert (progress['finished'] == 1)
    assert (progress['failed'] == 1)
