import os, sys

# For each run in the given Campaign's run list, apply the specified UQP or VVP function
def apply_for_each_run(campaign, func):

    app = campaign.get_application_info()
    if "runs_dir" not in app.keys():
        sys.exit("Missing 'runs_dir' key (Application info must include runs directory path).")
    runs_dir = app["runs_dir"]

    # Loop through all runs in this campaign
    run_IDs = campaign.get_run_IDs()
    for run_ID in run_IDs:
        dirname = os.path.join(runs_dir, run_ID)
        print("Applying " + func.__name__ + " to " + dirname + "...")

        # Run user-specified function on this directory, and store the result back into the Campaign object (if there is a result returned)
        result = func(dirname)
        if result != None:
            campaign.add_run_result(run_ID, result)
