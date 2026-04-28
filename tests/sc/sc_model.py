#!/usr/bin/env python3

import json
import sys
import numpy as np
import math

# Author: Wouter Edeling

# solves the steady advection diffusion equation at Peclet number Pe and
# constant forcing term f, using Finite Elements with linear shape functions.


def solve(Pe, f, nel):

    print('Solving advection diffusion equation at Pe = ', Pe, ' and f = ', f)

    h = 1.0 / nel

    K = np.zeros([nel + 1, nel + 1])
    F = np.zeros(nel + 1)

    # GQ RULES
    Q = 2
    eps_i = np.array([-1 / math.sqrt(3.0), 1 / math.sqrt(3.0)])
    wi = np.ones(2)

    # assumble K matrix and F vector
    for e in range(nel):

        XA1 = e * h
        XA2 = (e + 1) * h

        x = (h * eps_i + XA1 + XA2) / 2

        [N1x, N2x] = der_shape(h, Q)
        [N1, N2] = shape(x, XA1, XA2)

        # diffusive term
        k11 = 1.0 / Pe * N1x * N1x * wi - N1x * N1 * wi
        k11 = k11.sum()
        k12 = 1.0 / Pe * N1x * N2x * wi - N1x * N2 * wi
        k12 = k12.sum()
        k21 = 1.0 / Pe * N2x * N1x * wi - N2x * N1 * wi
        k21 = k21.sum()
        k22 = 1.0 / Pe * N2x * N2x * wi - N2x * N2 * wi
        k22 = k22.sum()

        # forcing term
        f1 = N1 * f
        f1 = f1.sum()
        f2 = N2 * f
        f2 = f2.sum()

        # local element matrices
        if e > 0 and e < int(nel - 1):
            K[e, e] = K[e, e] + k11
            K[e, e + 1] = K[e, e + 1] + k12
            K[e + 1, e] = K[e + 1, e] + k21
            K[e + 1, e + 1] = K[e + 1, e + 1] + k22

            F[e] = F[e] + f1
            F[e + 1] = F[e + 1] + f2
        elif e == 0:
            K[e + 1, e] = K[e + 1, e] + k21
            K[e + 1, e + 1] = K[e + 1, e + 1] + k22

            F[e + 1] = F[e + 1] + f2
        else:
            K[e, e] = K[e, e] + k11
            K[e, e + 1] = K[e, e + 1] + k12

            F[e] = F[e] + f1

    K[0, 0] = 1.0
    K[nel, nel] = 1.0

    return np.linalg.solve(K, F)

# Finite element linear shape functions and their derivatives


def der_shape(h, Q):
    N1x = -1 / h * np.ones(Q)
    N2x = 1 / h * np.ones(Q)

    return [N1x, N2x]


def shape(x, XA1, XA2):

    if np.max(x) < 1.0:
        eps = (2.0 * x - XA1 - XA2) / (XA2 - XA1)
    else:
        eps = (2.0 * x - XA1 - XA2) / (XA2 - XA1)
        eps[-1] = -1

    # value shape function
    N1 = 0.5 * (1 - eps)
    N2 = 0.5 * (1 + eps)
    return [N1, N2]


# the json input file containing the values of the parameters, and the
# output file
json_input = sys.argv[1]

with open(json_input, "r") as f:
    inputs = json.load(f)

Pe = float(inputs['Pe'])
f = float(inputs['f'])
output_filename = inputs['outfile']

# run FEM solver at current value of Pe and f
u = solve(Pe, f, nel=300)
u[0] = 0.0

# output csv file
header = 'u'
np.savetxt(output_filename, u,
           delimiter=",", comments='',
           header=header)
