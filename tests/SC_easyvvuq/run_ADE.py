#!/usr/bin/env python3

import json
import ADE as ade
import sys
import numpy as np

ade_obj = ade.ADE([100, 200], [0.9, 1.1], 100)

json_input = sys.argv[1]

with open(json_input, "r") as f:
    inputs = json.load(f)
    
Pe = float(inputs['Pe'])
f = float(inputs['f'])
output_filename = inputs['outfile']

u = ade_obj.solve([Pe, f])

header = 'u'

np.savetxt(output_filename, u, 
           delimiter=",", comments='',
           header=header)