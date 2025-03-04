import pytest
import os
from unittest.mock import MagicMock
from easyvvuq.actions.execute_kubernetes import ExecuteKubernetes
import easyvvuq.actions.execute_kubernetes as execute_kubernetes

execute_kubernetes.config = MagicMock()
execute_kubernetes.V1ConfigMap = MagicMock()
execute_kubernetes.V1ObjectMeta = MagicMock()


def test_execute_kubernetes():
    kube_exec = ExecuteKubernetes(
        "orbitfold/easyvvuq:latest",
        "/EasyVVUQ/tutorials/sir /config/input.json && cat output.csv",
        output_file_name='output.csv')
