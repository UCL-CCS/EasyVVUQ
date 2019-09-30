from easyvvuq import Campaign
from dask import delayed
import dask.bag
from fabric import Connection

class CampaignDask(Campaign):
    def apply_for_each_run_dir(self, client):
        run_dirs = []
        for run_id, run_data in self.campaign_db.runs(status=status, app_id=self._active_app['id']):
           run_dirs.append(run_data['run_dir'])
        bag = dask.bag.from_sequence(run_dirs)
        bag.map(action.act_on_dir).compute(client)

    def populate_runs_dir(self):
        """Populate run directories based on runs in the CampaignDB.

        This calls the encoder element defined for the current application to
        create input files for it in each run directory, usually with varying
        input (scientific) parameters.

        Returns
        -------

        """

        # Get the encoder for this app. If none is set, only the directory structure
        # will be created.
        active_encoder = self._active_app_encoder
        if active_encoder is None:
            logger.warning('No encoder set for this app. Creating directory structure only.')
        else:
            use_fixtures = active_encoder.fixture_support
            fixtures = self._active_app['fixtures']

        run_ids = []

        for run_id, run_data in self.campaign_db.runs(
                status=Status.NEW, app_id=self._active_app['id']):

            # Make directory for this run's output
            os.makedirs(run_data['run_dir'])

            # Encode run
            if active_encoder is not None:
                if use_fixtures:
                    active_encoder.encode(params=run_data['params'],
                                          fixtures=fixtures,
                                          target_dir=run_data['run_dir'])
                else:
                    active_encoder.encode(params=run_data['params'],
                                          target_dir=run_data['run_dir'])

            run_ids.append(run_id)
        self.campaign_db.set_run_statuses(run_ids, Status.ENCODED)
