#!/usr/bin/env python3

import sys, os
import numpy as np
import json

if len(sys.argv) != 2:
    sys.exit("Usage: python3 JSONIN")

json_input = sys.argv[1]

if os.path.isfile(json_input) == False:
    sys.exit(json_input + " does not exist.")

with open(json_input, "r") as f:
    inputs = json.load(f)

mu = float(inputs['mu'])
sigma = float(inputs['sigma'])
num_steps = int(inputs['num_steps'])
output_filename = inputs['outfile']

if num_steps <= 0:
    sys.exit("num_steps should be > 0")

numbers = np.random.normal(mu, sigma, num_steps)
numbers_out = np.array(list(enumerate(numbers)))

header = 'Step,Value'

fmt = '%i,%f'
np.savetxt(output_filename, numbers_out, fmt=fmt, header=header)

