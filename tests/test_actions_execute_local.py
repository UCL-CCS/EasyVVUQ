import pytest
import os
from easyvvuq.actions.execute_local import CreateRunDirectory


def test_create_run_directory(tmpdir):
    action = CreateRunDirectory(tmpdir)
    action.start({'campaign_dir': 'test', 'run_id': 123456789, 'run_info': {'id': 123456789}})
    assert (os.path.exists(
        os.path.join(
            tmpdir, 'test', 'runs', 'runs_100000000-200000000', 'runs_123000000-124000000',
            'runs_123450000-123460000', 'runs_123456700-123456800', 'run_123456789')))
    
    action.start({'campaign_dir': 'test', 'run_id': 0, 'run_info': {'id': 0}})
    assert (os.path.exists(
        os.path.join(
            tmpdir, 'test', 'runs', 'runs_0-100000000', 'runs_0-1000000', 'runs_0-10000',
            'runs_0-100')))

    action = CreateRunDirectory(tmpdir, flatten=True)
    action.start({'campaign_dir': 'test', 'run_id': 100, 'run_info': {'id': 100}})
    assert (os.path.exists(os.path.join(tmpdir, 'test', 'runs', 'run_100')))
