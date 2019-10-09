from easyvvuq import Campaign
import dask.bag
from easyvvuq.constants import Status


class CampaignDask(Campaign):
    """ This extends the standard Campaign to enable execution on clusters using
    the Dask JobQueue functionality.
    """

    def apply_for_each_run_dir(self, action, client, status=Status.ENCODED):
        """
        For each run in this Campaign's run list, apply the specified action
        (an object of type Action)

        Parameters
        ----------
        action : the action to be applied to each run directory
            The function to be applied to each run directory. func() will
            be called with the run directory path as its only argument.
        client : a Dask client associated with a cluster you want to
            run your jobs on.

        Returns
        -------
        """
        run_dirs = []
        for run_id, run_data in self.campaign_db.runs(status=status, app_id=self._active_app['id']):
            run_dirs.append(run_data['run_dir'])
        bag = dask.bag.from_sequence(run_dirs)
        future = client.compute(bag.map(action.act_on_dir))
        future.result()
