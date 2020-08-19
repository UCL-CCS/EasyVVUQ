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
    

# def test_execute_kubernetes():
#     action = execute_kubernetes.ExecuteKubernetes(
#         'tests/kubernetes/epidemic.yaml', ['epidemic.json'], 'out.csv')
#     action.act_on_dir('tests/kubernetes')


# def test_action_status_kubernetes():
#     api = MagicMock()
#     pod_name = 'test'
#     config_names = [('a', 'b'), ('c', 'd')]
#     namespace = 'test_namespace'
#     outfile = 'test.csv'
#     status = ActionStatusKubernetes(
#         api, {'metadata': {'name': 'test'}},
#         config_names, namespace, outfile)
#     resp = MagicMock()
#     resp.status.phase = 'Pending'
#     api.read_namespaced_pod.return_value = resp
#     assert(not status.finished())
#     with pytest.raises(RuntimeError):
#         status.finalise()
#     assert(not status.succeeded())
#     resp.status.phase = 'Succeeded'
#     assert(status.finished())
#     api.read_namespaced_pod_log.return_value = 'testing'
#     status.finalise()
#     assert(os.path.isfile('test.csv'))
#     with open('test.csv', 'r') as fd:
#         assert(fd.read() == 'testing')
#     os.remove('test.csv')
#     assert(api.delete_namespaced_config_map.called_with('b', 'test_namespace'))
#     assert(api.delete_namespaced_config_map.called_with('d', 'test_namespace'))
#     assert(api.delete_namespaced_pod.called_with('test', 'test_namespace'))
