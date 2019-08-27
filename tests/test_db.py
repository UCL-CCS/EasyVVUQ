import pytest
import os.path
import easyvvuq
from easyvvuq.constants import default_campaign_prefix
from easyvvuq.db.sql import CampaignDB
from easyvvuq.data_structs import CampaignInfo, RunInfo
from easyvvuq.constants import Status


@pytest.fixture
def campaign(tmp_path):
    info = CampaignInfo(
        name='test',
        campaign_dir_prefix=default_campaign_prefix,
        easyvvuq_version=easyvvuq.__version__,
        campaign_dir='.')
    campaign = CampaignDB(location='sqlite:///{}/test.sqlite'.format(tmp_path), new_campaign=True, name='test', info=info)
    campaign.tmp_path = tmp_path
    runs = [RunInfo('run', 'test', '.', 1, {'a' : 1}, 1, 1) for _ in range(1010)]
    run_names = ['Run_{}'.format(i) for i in range(1, 1011)]
    campaign.add_runs(runs)
    return campaign


def test_db_file_created(campaign):
    assert(os.path.isfile('{}/test.sqlite'.format(campaign.tmp_path)))


def test_get_and_set_status(campaign):
    run_names = ['Run_{}'.format(i) for i in range(1, 1011)]
    assert(all([campaign.get_run_status(name) == Status.NEW for name in run_names]))
    campaign.set_run_statuses(run_names, Status.ENCODED)
    assert(all([campaign.get_run_status(name) == Status.ENCODED for name in run_names]))


def test_get_num_runs(campaign):
    assert(campaign.get_num_runs() == 1010)

