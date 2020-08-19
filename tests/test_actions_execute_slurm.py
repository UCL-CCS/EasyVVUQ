import pytest
from unittest.mock import MagicMock
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

def test_action_status_slurm():
    execute_slurm.subprocess.run = MagicMock()
    slurm_result = MagicMock()
    slurm_result.stdout.decode.return_value = "sbatch: Submitted batch job 65541"
    execute_slurm.subprocess.run.return_value = slurm_result
    action = ExecuteSLURM('docs/epidemic/example.slurm', '$target_dir')
    status = action.act_on_dir('docs/epidemic')
    assert(isinstance(status, ActionStatusSLURM))
    status.start()
    assert(status.job_id == '65541')
    assert(status.started())
