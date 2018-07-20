#!/usr/bin/env python3

import sys, os
import numpy as np


if len(sys.argv) != 5:
	sys.exit("Usage: python3 MU SIGMA NUM_STEPS OUTPUTFILE")

mu = float(sys.argv[1])
sigma = float(sys.argv[2])
num_steps = int(sys.argv[3])
output_filename = sys.argv[4]

if num_steps <= 0:
	sys.exit("num_steps should be > 0")


numbers = np.random.normal(mu, sigma, num_steps)
numbers_out = np.array(list(enumerate(numbers)))

header = 'Step,Value'

fmt = '%i,%f'
np.savetxt(output_filename, numbers_out, fmt=fmt, header=header)

