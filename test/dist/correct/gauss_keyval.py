#!/usr/bin/env python3

import sys, os
import numpy as np
import json

if len(sys.argv) != 2:
    sys.exit("Usage: python3 INFILE")

key_val_input = sys.argv[1]

inputs = {}

with open(key_val_input) as f:
    for line in f:
        key, value = line.split()
        inputs[key] = value

mu = float(inputs['mu'])
sigma = float(inputs['sigma'])
num_steps = int(inputs['n_steps'])
output_filename = inputs['output_filename']

if num_steps <= 0:
    sys.exit("num_steps should be > 0")


numbers = np.random.normal(mu, sigma, num_steps)
numbers_out = np.array(list(enumerate(numbers)))

header = 'Step,Value'

fmt = '%i,%f'
np.savetxt(output_filename, numbers_out, fmt=fmt, header=header)

