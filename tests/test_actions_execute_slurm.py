import pytest
from unittest.mock import MagicMock, patch
import easyvvuq.actions.execute_slurm as execute_slurm
from easyvvuq.actions.execute_slurm import ExecuteSLURM, ActionStatusSLURM
import os


BATCH_FILE = """#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --output=res.txt
#
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=100

srun python3 /EasyVVUQ/docs/epidemic/epidemic.py docs/epidemic/epidemic_in.json out.csv"""

SQUEUE_OUTPUT_1 = """CLUSTER: mpp3
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
"""

SQUEUE_OUTPUT_2 = """JOBID PARTITION     NAME     USER  ST       TIME  NODES NODELIST(REASON)
  65541 general-c hello_te      cdc  PD       0:00      2 (Priority)
"""


@patch.object(execute_slurm.subprocess, 'run')
def test_action_status_slurm(mock_subprocess_run):
    slurm_result = MagicMock()
    slurm_result.stdout.decode.return_value = "sbatch: Submitted batch job 65541"
    mock_subprocess_run.return_value = slurm_result

    action = ExecuteSLURM('tutorials/epidemic/example.slurm', '$target_dir')
    status = action.act_on_dir('.')
    assert(isinstance(status, ActionStatusSLURM))
    assert(not status.finished())
    status.start()
    assert(status.job_id == '65541')
    assert(status.started())
    slurm_result.stdout.decode.return_value = SQUEUE_OUTPUT_2
    assert(not status.finished())
    slurm_result.stdout.decode.return_value = SQUEUE_OUTPUT_1
    assert(status.finished())
