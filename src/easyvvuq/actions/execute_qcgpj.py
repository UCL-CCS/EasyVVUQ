import base64
import json
import logging
from os import environ
from os import remove

import time

import dill
from typing import Tuple, Dict, Any

from concurrent.futures import Executor

from qcg.pilotjob.executor_api.qcgpj_executor import QCGPJExecutor
from qcg.pilotjob.executor_api.templates.qcgpj_template import QCGPJTemplate


logger = logging.getLogger(__name__)


class EasyVVUQBasicTemplate(QCGPJTemplate):
    """A basic template class for submission of QCG-PilotJob tasks that run on a single core

    The class can be used only for the most simple use-cases. For example it doesn't allow
    to specify resource requirements. Thus, for more advanced use-cases, it is recommended to provide custom
    implementation of QCGPJTemplate. For complete reference of QCG-PilotJob task's description parameters
    please look at https://qcg-pilotjob.readthedocs.io/en/latest/fileinterface.html#submit
    """
    @staticmethod
    def template() -> Tuple[str, Dict[str, Any]]:
        template = """
            {
                'name': '${name}',
                'execution': {
                    'exec': '${exec}',
                    'args': ${args},
                    'stdout': '${stdout}',
                    'stderr': '${stderr}',
                    'venv': '${venv}',
                    'modules': ${modules},
                    'model': '${model}',
                    'model_opts': ${model_opts}
                }
            }
             """

        defaults = {
            'args': [],
            'stdout': 'stdout',
            'stderr': 'stderr',
            'venv': '',
            'modules': [],
            'model': 'default',
            'model_opts': {}
        }

        return template, defaults


class EasyVVUQParallelTemplate(QCGPJTemplate):
    """A template class for submission of QCG-PilotJob tasks that run on exact number cores / nodes

    With this class it is possible to define basic resource requirements for tasks.
    For advanced use-cases, it is recommended to provide custom implementation of QCGPJTemplate.
    For complete reference of QCG-PilotJob task's description parameters
    please look at https://qcg-pilotjob.readthedocs.io/en/latest/fileinterface.html#submit
    """
    @staticmethod
    def template() -> Tuple[str, Dict[str, Any]]:
        template = """
            {
                'name': '${name}',
                'execution': {
                    'exec': '${exec}',
                    'args': ${args},
                    'stdout': '${stdout}',
                    'stderr': '${stderr}',
                    'venv': '${venv}',
                    'modules': ${modules},
                    'model': '${model}',
                    'model_opts': ${model_opts}
                },
                'resources': {
                    'numCores': {
                        'exact': ${numCores}
                    },
                    'numNodes': {
                        'exact': ${numNodes}
                    }
                }
            }
             """

        defaults = {
            'args': [],
            'stdout': 'stdout',
            'stderr': 'stderr',
            'venv': '',
            'modules': [],
            'model': 'default',
            'model_opts': {},
            'numCores': 1,
            'numNodes': 1
        }

        return template, defaults


class QCGPJPool(Executor):
    """A Pool that manages execution of actions with QCG-PilotJob.

    Parameters
    ----------
    qcgpj_executor: str
        An instance of QCGPJExecutor. If not provided, an instance of QCGPJExecutor
        with default settings will be created
    template: QCGPJTemplate
        An object which contains only a single method `template` that returns a tuple.
        The first element of a tuple should be a string representing a QCG-PilotJob task's description
        with placeholders (identifiers preceded by $ symbol)
        and the second a dictionary that assigns default values for selected placeholders.
        If not provided, a default EasyVVUQBasicTemplate will be used
    template_params: dict
        A dictionary that contains parameters that will be used to substitute placeholders
        defined in the template
    polling_interval: int
        An interval between queries to the QCG-PilotJob Manager service about state of the tasks, in seconds.
    """

    def __init__(
            self,
            qcgpj_executor=None,
            template=None,
            template_params=None,
            polling_interval=1):
        if qcgpj_executor is None:
            qcgpj_executor = QCGPJExecutor()
        if template is None:
            template = EasyVVUQBasicTemplate()

        self._qcgpj_executor = qcgpj_executor
        self._template = template
        self._template_params = template_params
        self._polling_interval = polling_interval
        self._campaign_dir = None

    def submit(self, fn, *args, **kwargs):
        """Submits a callable to be executed by QCG-PilotJob.

        Schedules the callable to be executed inside a QCG-PilotJob's task and returns
        a Future representing the execution of the callable.

        Returns
        -------
        QCGPJFuture
            QCGPJFuture representing the given call.
        """
        actions = fn.__self__
        actions.set_wrapper(QCGPJPool._wrapper)
        exec = 'python3'
        arg1 = "-m"
        arg2 = "easyvvuq.actions.execute_qcgpj_task"

        self._campaign_dir = args[0]['campaign_dir']

        pickled_actions = base64.b64encode(dill.dumps(actions)).decode('ascii')
        pickled_previous = base64.b64encode(dill.dumps(args[0])).decode('ascii')

        actions_file = f'{self._campaign_dir}/.qcgpj_in_act_{args[0]["run_id"]}'
        previous_file = f'{self._campaign_dir}/.qcgpj_in_prev_{args[0]["run_id"]}'

        with open(actions_file, 'w') as f:
            f.write(pickled_actions)

        with open(previous_file, 'w') as f:
            f.write(pickled_previous)

        return self._qcgpj_executor.submit(
            self._template.template,
            self._template_params,
            exec=exec,
            name=args[0]['run_id'],
            stdout=f"{self._campaign_dir}/stdout_{args[0]['run_id']}",
            stderr=f"{self._campaign_dir}/stderr_{args[0]['run_id']}",
            args=[arg1, arg2, actions_file, previous_file])

    @property
    def executor(self):
        """Returns current QCGPJExecutor instance.

        It gives you an access to QCG-PilotJob Manager instance, which in turn can be used to
        get information about the QCG-PilotJob execution environment.
        """
        return self._qcgpj_executor

    def convert_results(self, result_qcgpj):
        """Converts results generated by QCG-PilotJob task to EasyVVUQ-compatible form

        The method loads results data from a file where it was stored by QCG-PilotJob's task
        and then converts it to a dictionary which can be further processed by EasyVVUQ.

        Parameters
        ----------
        result_qcgpj: list or None
            A list of results returned by a QCG-PilotJob task (only the first element will be used),
            or None if the task hasn't finished with the status SUCCEED

        Returns
        -------
        dict
            A dictionary containing results
        """

        for key, value in result_qcgpj.items():
            if value != 'SUCCEED':
                logging.error(f"Task {key} finished with the status: {value}")
                raise RuntimeError(f"QCG-PilotJob task {key} finished with the status: {value}")

            result_file = f'{self._campaign_dir}/.qcgpj_result_{key}'
            with open(result_file, 'r') as f:
                previous = json.load(f)
            remove(result_file)

            return previous

    def shutdown(self, **kwargs):
        """Clean-up the resources associated with the QCGPJPool.
        """
        return self._qcgpj_executor.shutdown()

    def as_completed(self, futures):
        """Checks for the status of features and yields those that are finished
        """

        pending = set(futures)
        finished = set()

        for f in futures:
            if f.done():
                finished.add(f)
        pending = pending - finished

        while finished:
            yield finished.pop()

        while pending:
            for f in pending:
                if f.done():
                    finished.add(f)
            pending = pending - finished

            while finished:
                yield finished.pop()

            time.sleep(self._polling_interval)

    @staticmethod
    def _wrapper(action, previous):
        # TODO: Implement support for specialised execution models of QCG-PilotJob
        # """For the actions other than ExecuteQCGPJ ensures that the code is invoked only once
        # """
        # if not isinstance(action, ExecuteQCGPJ):
        #     rank = 0
        #     if 'OMPI_COMM_WORLD_RANK' in environ:
        #         rank = environ.get('OMPI_COMM_WORLD_RANK')
        #     elif 'PMI_RANK' in environ:
        #         rank = environ.get('PMI_RANK')
        #
        #     if rank != 0:
        #         return
        return action.start(previous)


class ExecuteQCGPJ:
    """A utility decorator over action that marks the action as configured for parallel execution by QCG-PilotJob
    Currently it has no influence on the processing.

    Parameters
    ----------
    action: Action
        an action that will be decorated in order to enable parallel execution inside a QCG-PilotJob task.
    """

    def __init__(self, action):
        self._action = action

    def start(self, previous=None):
        return self._action.start(previous)

    def finished(self):
        return self._action.finished()

    def finalise(self):
        return self._action.finalise()

    def succeeded(self):
        return self._action.succeeded()
