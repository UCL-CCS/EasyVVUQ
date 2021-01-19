#!/usr/bin/env python3

import sys
import json
import numpy as np
import fusion

# author: David Coster (based on work from Jalal Lakhlili)

# ... A test model: 
# it is used by PCE and QMC tests

json_input = sys.argv[1]
with open(json_input, "r") as f:
    inputs = json.load(f)

Te, ne, rho, rho_norm = fusion.solve_Te(
                                        Qe_tot =   float(inputs['Qe_tot']),
                                        H0 =       float(inputs['H0']),
                                        Hw =       float(inputs['Hw']),
                                        Te_bc =    float(inputs['Te_bc']),
                                        chi =      float(inputs['chi']),
                                        a0 =       float(inputs['a0']),
                                        R0 =       float(inputs['R0']),
                                        E0 =       float(inputs['E0']),
                                        b_pos =    float(inputs['b_pos']),
                                        b_height = float(inputs['b_height']),
                                        b_sol =    float(inputs['b_sol']),
                                        b_width =  float(inputs['b_width']),
                                        b_slope =  float(inputs['b_slope']),
                                        nr =       int(inputs['nr']),
                                        dt =       float(inputs['dt']),
                                        plots =    False)

output_filename = inputs['out_file']

# output csv file
header = 'te,ne,rho,rho_norm'
np.savetxt(output_filename, np.c_[Te, ne, rho, rho_norm],
           delimiter=",", comments='',
           header=header)
