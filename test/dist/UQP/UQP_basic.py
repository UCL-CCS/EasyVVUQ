import os,sys
import itertools
import json
import collections

# Need to specify:
# * application (what wrapper to use?)
# * which parameters are to be varied
# * what kind of variance (range, probabilistic distribution, etc)
#
# Do we pass this info to the UQP in (yet another) JSON file?
# * :(

# TODO: Change to use numpy linspace
def range_float(key, start, end, incr):
	i = 0
	r = start
	while r < end:
		r = start + i * incr
		i += 1
		yield (key, r)

if len(sys.argv) != 1:
	sys.exit("Usage: python3 UQP_Basic.py ")

# Input to this UQP
params = {
		"mu":		("range", [0, 1, 0.1]),
		"sigma":	("range", [0, 1, 0.1]),
		"num_steps":    ("static", 10),
		"outfile":	("static", "output.csv")
	 }

# Extract static and dynamic variables
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
			print("No.")
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

# Save runs as JSON

with open('runs.json', 'w') as outfile:
	json.dump(runs, outfile, indent=8)
