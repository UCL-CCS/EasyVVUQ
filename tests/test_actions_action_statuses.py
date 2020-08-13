import pytest
import time
from unittest.mock import MagicMock
from easyvvuq.actions import ActionStatuses


def test_action_status_kubernetes():
    status1, status2, status3 = (MagicMock(), MagicMock(), MagicMock())
    status1.finished.return_value = False
    status2.finished.return_value = True
    status3.finished.return_value = True
    status1.succeeded.return_value = False
    status2.succeeded.return_value = False
    status3.succeeded.return_value = True
    statuses = ActionStatuses([status1, status2, status3], 3)
    time.sleep(1)
    stats = statuses.progress()
    assert(stats['active'] == 1)
    assert(stats['finished'] == 1)
    assert(stats['failed'] == 1)
    assert(not status1.finalise.called)
    assert(not status2.finalise.called)
    assert(status3.finalise.called)
    status1.finished.return_value = True
    status2.finished.return_value = True
    status3.finished.return_value = True
    status1.succeeded.return_value = True
    status2.succeeded.return_value = True
    status3.succeeded.return_value = True
