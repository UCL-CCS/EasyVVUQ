import base64
import sys

import dill

from actions import Actions

if __name__ == "__main__":

    actions: Actions

    if len(sys.argv) != 3:
        sys.exit(
            "Usage: python3 encoded_actions_object encoded_previous_object"
        )

    pickled_actions = sys.argv[1]
    pickled_actions_b64 = pickled_actions.encode('ascii')
    pickled_actions_b = base64.b64decode(pickled_actions_b64)
    actions = dill.loads(pickled_actions_b)

    pickled_previous = sys.argv[2]
    pickled_previous_b64 = pickled_previous.encode('ascii')
    pickled_previous_b = base64.b64decode(pickled_previous_b64)
    previous = dill.loads(pickled_previous_b)

    previous_next = actions.start(previous)
    print(previous_next)
