import os,sys
import EasyVVUQ as uq
import itertools
import json
import collections
import numpy as np
from pprint import pprint

def Basic(application):

    # TODO: Change to use numpy linspace
    def range_float(param, start, end, incr):
        i = 0
        r = start
        while r < end:
            r = start + i * incr
            i += 1
            yield (param, r)

    def normal_dist(param, mean, sigma, num_samples):
        for pick in np.random.normal(mean, sigma, num_samples):
            yield (param, pick)

    params = application.get_params_info()

    # Extract static and dynamic variables from input
    static_params = []
    gens = []
    for key in params.keys():
        value = params[key]
        function, args = value[0], value[1]
        if function == "static":
            static_params.append((key, args))
        else:
            if function == "range":
                gens.append(range_float(key, args[0], args[1], args[2]))
            elif function == "normal":
                gens.append(normal_dist(key, args[0], args[1], args[2]))
            else:
                sys.exit("Unrecognised function " + function + " for parameter " + key)

    # Combine all the iterables/generators into one
    mega_iter = itertools.product(*gens)

    # Build runs
    for dynamic_params in mega_iter:
        run_dict = {}
        for dp in dynamic_params:
            key, value = dp
            run_dict[key] = value
        for sp in static_params:
            key, value = sp
            run_dict[key] = value

        # Add run to Application's run list
        application.add_run(run_dict)

# If module is run as standalone script, read in application/params info from json file, then write resultant runs to specified json file
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 Basic.py INPUT_JSON OUTPUT_JOBS_JSON")
        infname = sys.argv[1]
        outfname = sys.argv[2]

        app = uq.Application()
        app.load_state(infname)

        UQP_basic(app)
        app.save_state(outfname)
