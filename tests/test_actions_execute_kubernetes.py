import pytest
from easyvvuq.actions import ExecuteKubernetes

def test_init():
    kube_action = ExecuteKubernetes(
        'docs/tutorial_files/kubernetes/epidemic.yaml',
        ['docs/epidemic/example.json'])
    with open('docs/epidemic/example.json', 'r') as fd:
        input_file = fd.read()
    assert(kube_action.dep['metadata']['annotations']['example.json'] == input_file)
