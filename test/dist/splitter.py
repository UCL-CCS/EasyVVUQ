import os, sys
import json
import tempfile
from pprint import pprint

if len(sys.argv) != 3:
    sys.exit("Usage: python3 splitter.py UQP_JSON OUTPUT_RUNS_DIR_JSON")

infname = sys.argv[1]
outfname = sys.argv[2]
with open(infname, "r") as infile:
    input_json = json.load(infile)

# Split into application info block and runs block
app = input_json["app"]
runs = input_json["runs"]

# Get application wrapper to use
if 'wrapper' not in app.keys():
    sys.exit("__wrapper param missing from run '" + run_ID + "' block in " + infname)
wrapper_name = app['wrapper']

# Build a temp directory to store run files
basedir = tempfile.mkdtemp(prefix='Runs_EasyVVUQ_', dir='.')
print("Creating temp runs directory: " + basedir)

for run_ID, run_data in runs.items():

    # Make run directory
    target_dir = os.path.join(basedir, run_ID)
    os.makedirs(target_dir)

    # Build json input for wrapper
    wrapper_input = {"app": app, "params": run_data}

    # Write json input for wrapper
    wrap_infname = os.path.join(target_dir, 'run_data.json')

    with open(wrap_infname, "w") as outfile:
        json.dump(wrapper_input, outfile, indent=8)

    # Run wrapper to populate directory
    wrapcmd = " ".join(["python3", wrapper_name, wrap_infname, target_dir])
    r = os.system(wrapcmd)
    if r != 0:
        sys.exit("Wrapper returned non-zero exit code (command was '" + wrapcmd + "')")

output = {"runs_dir": basedir}
with open(outfname, "w") as outfile:
    json.dump(output, outfile, indent=8)
