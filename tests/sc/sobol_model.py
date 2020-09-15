#!/usr/bin/env python3

# scalar analytic test function, defined on [0, 1]**d
import numpy as np
import json
import sys
import logging


def sobol_g_func(theta, d=5, a=[0.0, 0.5, 3.0, 9.0, 99.0]):
    Y = 1.0
    for i in range(d):
        Y *= (np.abs(4.0 * theta[i] - 2.0) + a[i]) / (1.0 + a[i])
    return Y


if __name__ == '__main__':
    # parameters required by test function
    a = [0.0, 0.5, 3.0, 9.0, 99.0]
    # stocastic dimension of the problem
    d = 5
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
    result = sobol_g_func(theta)
    logging.debug(result)
    # output csv file
    header = 'f'
    np.savetxt(output_filename, np.array([result]),
               delimiter=",", comments='',
               header=header)
