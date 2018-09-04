import os, sys
import json
import tempfile


def populate_runs_dir(campaign, prefix='Runs_EASYVVUQ_', default_dir='.'):

    # Get application info block and runs block
    runs = campaign.runs

    # Get application encoder to use

    if campaign.encoder is None:
        raise RuntimeError('Cannot populate runs without valid encoder in campaign')

    encoder = campaign.encoder

    # Build a temp directory to store run files (unless it already exists)
    if not campaign.run_dir:

        basedir = tempfile.mkdtemp(prefix=prefix, dir=default_dir)
        print("Creating temp runs directory: " + basedir)

        campaign.run_dir = basedir

    else:

        basedir = campaign.run_dir

    for run_ID, run_data in runs.items():

        # Make run directory
        target_dir = os.path.join(basedir, run_ID)
        os.makedirs(target_dir)

        encoder.encode(params=run_data, target_dir=target_dir)


# If module is run as standalone script, read in application/params info from json file,
# and write the (unique) runs dir name to the specified file
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 populate_runs_dir.py INPUT_JSON OUTPUT_JOBS_JSON")
        in_filename = sys.argv[1]
        out_filename = sys.argv[2]

        my_app = easy.Application()
        my_app.load_state(in_filename)

        easy.build_runs_dir(my_app)
        app.save_state(out_filename)
