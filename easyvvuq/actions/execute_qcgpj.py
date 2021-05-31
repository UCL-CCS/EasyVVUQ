import base64
import json

import time

import dill
from typing import Tuple, Dict, Any

from concurrent.futures import Executor
from qcg.pilotjob.executor_api.qcgpj_executor import QCGPJExecutor
from qcg.pilotjob.executor_api.templates.qcgpj_template import QCGPJTemplate


class EasyVVUQBasicTemplate(QCGPJTemplate):
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
                    'venv': '${venv}'
                }
            }
             """

        defaults = {
            'args': [],
            'stdout': 'stdout',
            'stderr': 'stderr'
        }

        return template, defaults


class QCGPJPool(Executor):

    def __init__(self, qcgpj_executor=None, template=None, template_params=None):
        if qcgpj_executor is None:
            qcgpj_executor = QCGPJExecutor()
        if template is None:
            template = EasyVVUQBasicTemplate()

        self._qcgpj_executor = qcgpj_executor
        self._template = template
        self._template_params = template_params
        self._campaign_dir = None

    def submit(self, fn, *args, **kwargs):
        actions = fn.__self__
        actions.set_wrapper(QCGPJPool._wrapper)
        exec = 'python3 -m easyvvuq.actions.execute_qcgpj_task'

        pickled_actions = base64.b64encode(dill.dumps(actions)).decode('ascii')
        pickled_previous = base64.b64encode(dill.dumps(args[0])).decode('ascii')

        self._campaign_dir = args[0]['campaign_dir']

        return self._qcgpj_executor.submit(
            self._template.template,
            self._template_params,
            exec=exec,
            name=args[0]['run_id'],
            stdout=f"{self._campaign_dir}/stdout_{args[0]['run_id']}",
            stderr=f"{self._campaign_dir}/stderr_{args[0]['run_id']}",
            args=[pickled_actions, pickled_previous])

    def shutdown(self, **kwargs):
        return self._qcgpj_executor.shutdown()

    @staticmethod
    def as_completed(features):

        pending = set(features)
        finished = set()

        for f in features:
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

            time.sleep(1)

    def convert_results(self, result_qcgpj):
        for key, value in result_qcgpj.items():
            if value != 'SUCCEED':
                print(f"Exit status for task {key}: {value}")
            assert value == 'SUCCEED'
            with open(f'{self._campaign_dir}/.qcgpj_result_{key}', 'r') as f:
                previous = json.load(f)
                return previous

    @staticmethod
    def _wrapper(action, previous):
        return action.start(previous)
