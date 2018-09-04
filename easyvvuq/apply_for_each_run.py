import os, sys


def apply_for_each_run(campaign, func):
    """For each run in the given Campaign's run list, apply the specified UQP or VVP function"""

    app = campaign.app_info

    if "runs_dir" not in app.keys():
        sys.exit("Missing 'runs_dir' key (Application info must include runs directory path).")
    runs_dir = app["runs_dir"]

    # Loop through all runs in this campaign
    run_ids = campaign.runs.keys()
    for run_id in run_ids:
        dir_name = os.path.join(runs_dir, run_id)
        print("Applying " + func.__name__ + " to " + dir_name + "...")

        # Run user-specified function on this directory, and store the result
        # back into the Campaign object (if there is a result returned)
        result = func(dir_name)
        if result is not None:
            campaign.add_run_result(run_id, result)
