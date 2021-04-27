#!/usr/bin/env python3

# scalar analytic test function, defined on [0, 1]**d
import numpy as np
import json
import sys

def poly_model(theta):
    
    sol = 1.0
    for i in range(d):
        sol *= 3 * a[i] * theta[i]**2 + 1.0
    return sol/2**d
    
    # return np.prod(3 * a * theta**2 + 1) / 2**d

# the json input file containing the values of the parameters, and the
# output file
json_input = sys.argv[1]

with open(json_input, "r") as f:
    inputs = json.load(f)
output_filename = inputs['outfile']

# stocastic dimension of the problem
d = inputs['d']
#make only first variables important
a = [1/(2*(i+1)) for i in range(d)]

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