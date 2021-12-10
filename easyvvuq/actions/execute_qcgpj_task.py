import base64
import json
import os
import sys

import dill

from . import Actions

if __name__ == "__main__":

    actions: Actions

    print("Invoking execute_qcgpj_task with arguments: " + str(sys.argv))

    if len(sys.argv) != 3 and len(sys.argv) != 5:
        sys.exit(
            "Usage: python3 [-m module] encoded_actions_object encoded_previous_object"
        )

    actions_f = None
    previous_f = None

    if len(sys.argv) == 3:
        actions_f = sys.argv[1]
        previous_f = sys.argv[2]

    if len(sys.argv) == 5:
        actions_f = sys.argv[3]
        previous_f = sys.argv[4]

    if 'QCG_PM_EXEC_API_JOB_ID' not in os.environ:
        sys.exit("The required environment variable QCG_PM_STEP_ID not set")

    jobid = os.environ['QCG_PM_EXEC_API_JOB_ID']

    with open(actions_f) as f:
        pickled_actions = f.read()
        pickled_actions_b64 = pickled_actions.encode('ascii')
        pickled_actions_b = base64.b64decode(pickled_actions_b64)
        actions = dill.loads(pickled_actions_b)
    os.remove(actions_f)

    with open(previous_f) as f:
        pickled_previous = f.read()
        pickled_previous_b64 = pickled_previous.encode('ascii')
        pickled_previous_b = base64.b64decode(pickled_previous_b64)
        previous = dill.loads(pickled_previous_b)
    os.remove(previous_f)

    previous_next = actions.start(previous)

    with open(f'{previous_next["campaign_dir"]}/.qcgpj_result_{jobid}', 'w') as f:
        json.dump(previous_next, f)
