#!/usr/bin/env python3

import sys
import json
import numpy as np

json_input = sys.argv[1]
with open(json_input, "r") as f:
    inputs = json.load(f)
    
x1 = inputs['x1']
x2 = inputs['x2']

# output csv file, write the type of the inputs
np.savetxt("output.csv", 
           np.array([type(x1).__name__, type(x2).__name__]),
           fmt='%s',  delimiter=",", comments='', header='types')