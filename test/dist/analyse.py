import os, sys
import json
import glob

if len(sys.argv) != 2:
    sys.exit("python3 analyse.py RUNS_DIR_JSON")

infname = sys.argv[1]
with open(infname, "r") as infile:
    in_data = json.load(infile)

if "runs_dir" not in in_data.keys():
    sys.exit("Missing 'runs_dir' key (input json must contain the runs directory path).")

runs_dir = in_data["runs_dir"]

for dirname in glob.glob(runs_dir+"/Run_*"):
    print("Analysing " + dirname + "...")
    outfname = os.path.join(dirname, "output.csv")
    cmd = "python3 UQP/UQP_analyse.py " + outfname
    r = os.system(cmd)
    if r != 0:
        sys.exit("Non-zero exit code from command '" + cmd + "'")
