from easyvvuq import Campaign
from dask import delayed
import dask.bag

class CampaignDask(Campaign):
    def apply_for_each_run_dir(self, client):
        run_dirs = []
        for run_id, run_data in self.campaign_db.runs(status=status, app_id=self._active_app['id']):
           run_dirs.append(run_data['run_dir'])
        bag = dask.bag.from_sequence(run_dirs)
        bag.map(action.act_on_dir).compute(client)

