#!/usr/bin/env python3

import sys
import json
import numpy as np

# author: Jalal Lakhlili

# ... A test model: Coffee_Cup from Uncertainpy


def model(time, kappa, T_env):
    # For the ODE integration
    from scipy.integrate import odeint

    # Initial temperature
    T_0 = 95

    # The equation describing the model
    def f(T, time, kappa, T_env):
        return -kappa * (T - T_env)

    # Solving the equation by intergration
    temp = odeint(f, T_0, time, args=(kappa, T_env))[:, 0]

    # The output temperature
    return temp
# ...


json_input = sys.argv[1]
with open(json_input, "r") as f:
    inputs = json.load(f)

kappa = float(inputs['kappa'])
t_env = float(inputs['t_env'])
t = np.linspace(0, 200, 150)

output_filename = inputs['out_file']

te = model(t, kappa, t_env)
ti = -te
# output csv file
header = 'te, ti'
np.savetxt(output_filename, np.c_[te, ti],
           delimiter=",", comments='',
           header=header)
