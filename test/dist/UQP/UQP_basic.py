import os,sys
import itertools
import json
import collections
import numpy as np
from pprint import pprint

# Need to specify:
# * application (what wrapper to use?)
# * which parameters are to be varied
# * what kind of variance (range, probabilistic distribution, etc)
#
# Do we pass this info to the UQP in (yet another) JSON file?
# * :(

def validate_input(input_json):
	# Check that it contains an "app" and a "params" block
	if "app" not in input_json.keys():
		sys.exit("Input does not contain an 'app' block")
	if "params" not in input_json.keys():
		sys.exit("Input does not contain an 'params' block")

	# Make sure the app block contains a "wrapper" key
	if "wrapper" not in input_json["app"].keys():
		sys.exit("Input app block should contain a wrapper parameter, designating the wrapper(s) to be used for processing of the given application parameters")

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

if len(sys.argv) != 3:
	sys.exit("Usage: python3 UQP_Basic.py INPUT_JSON OUTPUT_JOBS_JSON")
infname = sys.argv[1]
outfname = sys.argv[2]

# Load and validate input JSON file
with open(infname, "r") as infile:
	input_json = json.load(infile)
validate_input(input_json)

# Split into the application and params blocks
app = input_json["app"]
params = input_json["params"]

#print("Reading input:")
#pprint(params)

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
runs = collections.OrderedDict()
run_num = 0
for dynamic_params in mega_iter:
	run = {}
	for dp in dynamic_params:
		key, value = dp
		run[key] = value
	for sp in static_params:
		key, value = sp
		run[key] = value
	run_num += 1
	run_id = "Run_" + str(run_num)

	# Add run to master dict of runs
	runs[run_id] = run

# Build output (application info block + runs info)
output = {"app": app, "runs": runs}

# Save output as JSON
with open(outfname, 'w') as outfile:
	json.dump(output, outfile, indent=8)
