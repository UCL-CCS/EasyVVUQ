#!/usr/bin/env python3

import sys
import os
import numpy as np
import json

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

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


if len(sys.argv) != 2:
    sys.exit("Usage: python3 gauss_json.py JSONIN")

json_input = sys.argv[1]

if not os.path.isfile(json_input):
    sys.exit(json_input + " does not exist.")

with open(json_input, "r") as f:
    inputs = json.load(f)

mu = float(inputs['mu'])
sigma = float(inputs['sigma'])
num_steps = int(inputs['num_steps'])
output_filename = inputs['outfile']

if 'biasfile' in inputs:
    with open(inputs['biasfile']) as fin:
        line = fin.readline()

    bias = float(line.split()[0])
else:
    bias = 0


if num_steps <= 0:
    sys.exit("num_steps should be > 0")

numbers = np.random.normal(mu, sigma, num_steps)
numbers += bias
numbers_out = np.array(list(enumerate(numbers)))

#header = 'Step,Value'

#fmt = '%i,%f'
#np.savetxt(output_filename, numbers_out, fmt=fmt, header=header)

#json_output = {'numbers': list(numbers)}
# with open(output_filename + '.json', 'wt') as json_fp:
#    json.dump(json_output, json_fp)

# output csv file
np.savetxt(output_filename, numbers,
           delimiter=",", comments='',
           header='numbers')
