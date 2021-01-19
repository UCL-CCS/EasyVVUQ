import pytest
from unittest.mock import MagicMock
import easyvvuq.actions.execute_kubernetes as execute_kubernetes
from easyvvuq.actions.execute_kubernetes import ActionStatusKubernetes
import os


# Monkey patch some stuff

execute_kubernetes.config = MagicMock()
execute_kubernetes.core_v1_api = MagicMock()
execute_kubernetes.Configuration = MagicMock()
execute_kubernetes.V1ConfigMap = MagicMock()
execute_kubernetes.V1ObjectMeta = MagicMock()


def test_execute_kubernetes():
    action = execute_kubernetes.ExecuteKubernetes(
        'tests/kubernetes/epidemic.yaml', ['epidemic.json'], 'out.csv')
    action.act_on_dir('tests/kubernetes')


def test_action_status_kubernetes():
    api = MagicMock()
    pod_name = 'test'
    config_names = [('a', 'b'), ('c', 'd')]
    namespace = 'test_namespace'
    outfile = 'test.csv'
    status = ActionStatusKubernetes(
        api, {'metadata': {'name': 'test'}},
        config_names, namespace, outfile)
    resp = MagicMock()
    resp.status.phase = 'Pending'
    api.read_namespaced_pod.return_value = resp
    assert(not status.finished())
    with pytest.raises(RuntimeError):
        status.finalise()
    assert(not status.succeeded())
    resp.status.phase = 'Succeeded'
    assert(status.finished())
    api.read_namespaced_pod_log.return_value = 'testing'
    status.finalise()
    assert(os.path.isfile('test.csv'))
    with open('test.csv', 'r') as fd:
        assert(fd.read() == 'testing')
    os.remove('test.csv')
    assert(api.delete_namespaced_config_map.called_with('b', 'test_namespace'))
    assert(api.delete_namespaced_config_map.called_with('d', 'test_namespace'))
    assert(api.delete_namespaced_pod.called_with('test', 'test_namespace'))
