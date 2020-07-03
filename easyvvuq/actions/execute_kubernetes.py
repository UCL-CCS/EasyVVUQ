"""Provides element to execute a simulation on a Kubernetes cluster
and retrieve the output.

Examples
--------
"""

import os
import sys
import logging
import yaml
import time
import uuid
from kubernetes.client.api import core_v1_api
from kubernetes import config
from kubernetes.client import Configuration, V1ConfigMap, V1ObjectMeta
from . import BaseAction

__copyright__ = """

    Copyright 2020 Vytautas Jancauskas

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"

logger = logging.getLogger(__name__)


class ExecuteKubernetes(BaseAction):
    """ Provides an action element to run a shell command in a specified
    directory.

    Parameters
    ----------

    pod_config : str
        Command to execute.
    input_file_names : list of str
        A list of input file names for your simulation.
    output_file_name : str
        An output file name for the output of the simulation.
    """
    def __init__(self, pod_config, input_file_names, output_file_name):
        if os.name == 'nt':
            msg = ('Local execution is provided for testing on Posix systems'
                   'only. We detect you are using Windows.')
            logger.error(msg)
            raise NotImplementedError(msg)
        with open(pod_config, 'r') as fd:
            self.dep = yaml.load(fd)
        self.dep['metadata']['name'] = str(uuid.uuid4())
        self.input_file_names = [(input_file_name, str(uuid.uuid4()))
                                 for input_file_name in input_file_names]
        self.output_file_name = output_file_name
        config.load_kube_config()
        c = Configuration()
        c.assert_hostname = False
        Configuration.set_default(c)
        self.core_v1 = core_v1_api.CoreV1Api()
        self.create_config_maps()
        self.create_volumes()


    def create_volumes(self):
        """Create descriptions of Volumes that will hold the input files.
        """
        volumes = [{'name': id_ + '-volume', 'configMap': {'name': id_}}
                   for _, id_ in self.input_file_names]
        volume_mounts = [{'name': id_ + '-volume',
                          'mountPath': os.path.join('/config/', os.path.basename(file_name)),
                          'subPath': os.path.basename(file_name),
                          'readOnly': True}
                         for file_name, id_ in self.input_file_names]
        self.dep['spec']['volumes'] = volumes
        self.dep['spec']['containers'][0]['volumeMounts'] = volume_mounts


    def create_config_maps(self):
        """Create Kubernetes ConfigMaps for the input files to the simulation.
        """
        for file_name, id_ in self.input_file_names:
            with open(file_name, 'r') as fd:
                data = fd.read()
            metadata = V1ObjectMeta(
                name=id_,
                namespace='default'
            )
            configmap = V1ConfigMap(
                api_version='v1',
                kind='ConfigMap',
                data={os.path.basename(file_name): data},
                metadata=metadata
            )
            self.core_v1.create_namespaced_config_map(namespace='default', body=configmap)


    def act_on_dir(self, target_dir):
        """Executes a dockerized simulation on input files found in `target_dir`.

        target_dir : str
            Directory in which to execute simulation.
        """
        resp = self.core_v1.create_namespaced_pod(
            body=self.dep, namespace="default")
        while True:
            resp = self.core_v1.read_namespaced_pod(
                name=self.dep['metadata']['name'],
                namespace='default')
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)
        log_ = self.core_v1.read_namespaced_pod_log(
            self.dep['metadata']['name'], 'default')
        with open(self.output_file_name, 'w') as fd:
            fd.write(log_)
        for filename, id_ in self.input_file_names:
            self.core_v1.delete_namespaced_config_map(id_, 'default')
        self.core_v1.delete_namespaced_pod(
            name=self.dep['metadata']['name'],
            namespace='default')
