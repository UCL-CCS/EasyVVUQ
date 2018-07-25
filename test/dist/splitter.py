import os, sys
import json
import tempfile
from pprint import pprint

if len(sys.argv) != 2:
	sys.exit("Usage: python3 splitter.py UQP_JSON")

infname = sys.argv[1]
with open(infname, "r") as infile:
	all_runs = json.load(infile)

# Build a temp directory to store run files
basedir = tempfile.mkdtemp(prefix='Runs_EasyVVUQ_', dir='.')
print("Creating temp runs directory: " + basedir)

for run_ID, run_data in all_runs.items():

	# Make run directory
	target_dir = os.path.join(basedir, run_ID)
	os.makedirs(target_dir)

	# Get application wrapper to use (and remove __wrapper key from run_data)
	wrapper_name = run_data.pop('__wrapper', None)
	if wrapper_name == None:
		sys.exit("__wrapper param missing from run '" + run_ID + "' block in " + infname)

	# Write json input for wrapper
	wrap_infname = os.path.join(target_dir, 'run_data.json')
	with open(wrap_infname, "w") as outfile:
		json.dump(run_data, outfile, indent=8)

	# Run wrapper to populate directory
	wrapcmd = " ".join(["python3", wrapper_name, wrap_infname, target_dir])
	os.system(wrapcmd)

