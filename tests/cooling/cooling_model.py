#!/usr/bin/env python3

import sys
import json
import numpy as np

# author: Jalal Lakhlili

# ... A test model: Cooling Coffee_Cup from Uncertainpy
# it is used by PCE and QMC tests


def model(time, T_0, kappa, T_env):
    # For the ODE integration
    from scipy.integrate import odeint

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
temp0 = float(inputs['T0'])

t = np.linspace(0, 200, 150)

output_filename = inputs['out_file']

te = model(t, temp0, kappa, t_env)

# output csv file
np.savetxt(output_filename, te,
           delimiter=",", comments='',
           header='te')
