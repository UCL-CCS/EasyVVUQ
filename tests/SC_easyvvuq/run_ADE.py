#!/usr/bin/env python3

import json
import ADE as ade
import sys
import numpy as np

# create an object from the finite-element Advection Diffusion Equation solver
Pe_range = [100, 200]  # range uncertain Peclet number
f_range = [0.9, 1.1]  # range uncertain forcing term
nel = 300  # number of elements in FEM solver
ade_obj = ade.ADE(Pe_range, f_range, nel)

# the json input file containing the values of the parameters, and the
# output file
json_input = sys.argv[1]

with open(json_input, "r") as f:
    inputs = json.load(f)

Pe = float(inputs['Pe'])
f = float(inputs['f'])
output_filename = inputs['outfile']

# run FEM solver at current value of Pe and f
u = ade_obj.solve([Pe, f])

# output csv file
header = 'u'
np.savetxt(output_filename, u,
           delimiter=",", comments='',
           header=header)
