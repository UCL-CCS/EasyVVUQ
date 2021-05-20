import base64
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

    def submit(self, fn, *args, **kwargs):
        actions = fn.__self__
        actions.set_wrapper(QCGPJPool._wrapper)
        exec = 'python3 -m easyvvuq.actions.execute_qcgpj_task'

        pickled_actions = base64.b64encode(dill.dumps(actions)).decode('ascii')
        pickled_previous = base64.b64encode(dill.dumps(args[0])).decode('ascii')

        return self._qcgpj_executor.submit(
            self._template.template,
            self._template_params,
            exec=exec,
            name=args[0]['run_id'],
            stdout=f"stdout_{args[0]['run_id']}",
            stderr=f"stderr_{args[0]['run_id']}",
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

        while pending != 0:
            for f in pending:
                if f.done():
                    finished.add(f)
            pending = pending - finished

            while finished:
                yield finished.pop()

            time.sleep(1)

    @staticmethod
    def _wrapper(action, previous):
        print("TESTING WRAPPER")
        return action.start(previous)

