import os, sys
import json
import glob

# For each run in the given Campaign's run list, apply the specified UQP or VVP function
def apply_for_each_run(campaign, func):

    app = campaign.get_application_info()
    if "runs_dir" not in app.keys():
        sys.exit("Missing 'runs_dir' key (Application info must include runs directory path).")
    runs_dir = app["runs_dir"]

    for dirname in glob.glob(runs_dir+"/Run_*"):
        print("Applying " + func.__name__ + " to " + dirname + "...")
        func(dirname)
