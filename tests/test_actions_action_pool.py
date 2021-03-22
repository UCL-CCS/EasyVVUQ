import pytest
import time
from unittest.mock import MagicMock
from easyvvuq.actions import ActionPool


def action_pool(sequential):
    campaign = MagicMock()
    actions = MagicMock()
    inits = [MagicMock(), MagicMock(), MagicMock()]
    return ActionPool(campaign, actions, inits, sequential=sequential)
