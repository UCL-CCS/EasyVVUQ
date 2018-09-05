import os
import tempfile


def populate_runs_dir(campaign, prefix='Runs_EASYVVUQ_', default_dir='.'):
    """Populate run directories as specified in the input Campaign object

    This calls the Campaigns encoder object to create input files for the
    specified application in each run directory, usually with varying input
    (scientific) parameters.

    Parameters
    ----------
    campaign    : Campaign
        Object that contains information about a set of related runs.
    prefix      : str
        Text that will appear at the start of each run directories name.
    default_dir : str
        Top level directory where all the run directories will be created.
    Returns
    -------

    """

    # Get application info block and runs block
    runs = campaign.runs

    # Get application encoder to use

    if campaign.encoder is None:
        raise RuntimeError('Cannot populate runs without valid encoder in campaign')

    encoder = campaign.encoder

    # Build a temp directory to store run files (unless it already exists)
    if not campaign.run_dir:

        base_dir = tempfile.mkdtemp(prefix=prefix, dir=default_dir)
        print("Creating temp runs directory: " + base_dir)

        campaign.run_dir = base_dir

    else:

        base_dir = campaign.run_dir

    for run_id, run_data in runs.items():

        # Make run directory
        target_dir = os.path.join(base_dir, run_id)
        os.makedirs(target_dir)

        encoder.encode(params=run_data, target_dir=target_dir)

