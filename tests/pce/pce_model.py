#!/usr/bin/env python3

import json
import numpy as np
import sys

# ... A test model
def model(x, c1, c2):
    def c(x):
        if x < 0.5:
            return c1
        else:
            return c2

    N = len(x)
    u = np.zeros(N)

    u[0] = c1
    for n in range(N-1):
        dx = x[n+1] -x[n]
        K1 = -dx*u[n]*c(x[n])
        K2 = -dx*u[n] + K1/2*c(x[n]+dx/2)
        u[n+1] = u[n] + K1 + K2

    return u
# ...


json_input = sys.argv[1]
with open(json_input, "r") as f:
    inputs = json.load(f)

c1 = float(inputs['d1'])
c2 = float(inputs['d2'])
x  = np.linspace(0, 1, 101)

output_filename = inputs['out_file']

u = model(x, c1, c2)

#output csv file
header = 'u'
np.savetxt(output_filename, u,
           delimiter=",", comments='',
           header=header)
