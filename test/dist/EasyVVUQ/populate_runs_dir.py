import os, sys
import json
import tempfile
from pprint import pprint

def populate_runs_dir(campaign):

    # Get application info block and runs block
    app = campaign.get_application_info()
    runs = campaign.get_runs_info()

    # Get application wrapper to use
    if 'wrapper' not in app.keys():
        sys.exit("wrapper param missing from campaign application info ('app' block currently contains: " + str(app) + ")")
    wrapper_name = app['wrapper']

    # Build a temp directory to store run files (unless it already exists)
    if campaign.has_run_dir() == False:
        basedir = tempfile.mkdtemp(prefix='Runs_EasyVVUQ_', dir='.')
        print("Creating temp runs directory: " + basedir)
        campaign.set_run_dir(basedir)
    else:
        basedir = campaign.get_run_dir()

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

# If module is run as standalone script, read in application/params info from json file, and write the (unique) runs dir name to the specified file
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 populate_runs_dir.py INPUT_JSON OUTPUT_JOBS_JSON")
        infname = sys.argv[1]
        outfname = sys.argv[2]

        app = easy.Application()
        app.load_state(infname)

        easy.build_runs_dir(app)
        app.save_state(outfname)                                   
