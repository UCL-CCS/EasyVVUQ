#!/usr/bin/env python3

import sys
import os
import json

if __name__ == '__main__':
    json_input = sys.argv[1]
    if not os.path.isfile(json_input):
        sys.exit(json_input + " does not exist.")
    with open(json_input, "r") as fd:
        inputs = json.load(fd)
    x1 = float(inputs['x1'])
    x2 = float(inputs['x2'])
    output_filename = inputs['outfile']
    y = (1.0 - x1) ** 2 + 100.0 * (x2 - x1 ** 2) ** 2
    with open(output_filename, 'w') as fd:
        json.dump({'value': -y}, fd)
