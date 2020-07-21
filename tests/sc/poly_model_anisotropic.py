#!/usr/bin/env python3
"""
Analytic anisotropic function to test the SC sampler on
"""

# scalar analytic test function, defined on [0, 1]**d
import json
import sys
import numpy as np


def poly_model(theta):
    """
    Analytic test function where some parameters are more important than others.

    Parameters
    ----------
    theta :  array of input parameters in [0, 1]

    Returns
    -------
    (float) function value
    """
    sol = 1.0
    for i in range(d):
        sol *= 3 * a[i] * theta[i]**2 + 1.0
    return sol / 2**d


# stocastic dimension of the problem
d = 3
a = np.ones(d) * 0.01
# effective dimension of the problem
effective_d = 1
a[0:effective_d] = 1.0

# the json input file containing the values of the parameters, and the
# output file
json_input = sys.argv[1]

with open(json_input, "r") as f:
    inputs = json.load(f)
output_filename = inputs['outfile']

theta = []
for i in range(d):
    theta.append(float(inputs['x' + str(i + 1)]))
theta = np.array(theta)

result = poly_model(theta)

# output csv file
header = 'f'
np.savetxt(output_filename, np.array([result]),
           delimiter=",", comments='',
           header=header)
