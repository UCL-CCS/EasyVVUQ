import pytest
import os
from easyvvuq.actions.execute_kubernetes import ExecuteKubernetes


def test_execute_kubernetes():
    kube_exec = ExecuteKubernetes(
        "orbitfold/easyvvuq:latest",
        "/EasyVVUQ/tutorials/sir /config/input.json && cat output.csv",
        output_file_name='output.csv')

