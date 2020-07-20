#!/usr/bin/env python3
"""
Analytic isotropic function to test the SC sampler on
"""

# scalar analytic test function, defined on [0, 1]**d
import json
import sys
import numpy as np


def poly_model(theta):
    """
    A simple analytic test function

    Parameters
    ----------
    theta : array of input parameters in [0, 1]

    Returns
    -------
    (float) function value
    """
    return np.prod(3 * theta**2 + 1) / 2**d


# stocastic dimension of the problem
d = 2

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

print(theta)

# result = sobol_g_func(theta)
result = poly_model(theta)
# print(result)

# output csv file
header = 'f'
np.savetxt(output_filename, np.array([result]),
           delimiter=",", comments='',
           header=header)
