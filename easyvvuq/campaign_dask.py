from easyvvuq import Campaign
import dask.bag
from easyvvuq.constants import Status


class CampaignDask(Campaign):
    def apply_for_each_run_dir(self, action, client, status=Status.ENCODED):
        run_dirs = []
        for run_id, run_data in self.campaign_db.runs(status=status, app_id=self._active_app['id']):
            run_dirs.append(run_data['run_dir'])
        bag = dask.bag.from_sequence(run_dirs)
        future = client.compute(bag.map(action.act_on_dir))
        future.result()
