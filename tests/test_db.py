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
    return campaign


def test_db_file_created(campaign):
    assert(os.path.isfile('{}/test.sqlite'.format(campaign.tmp_path)))


def test_get_and_set_status(campaign):
    run1 = RunInfo('run1', 'test', '.', 1, {'a' : 1}, 1, 1)
    run2 = RunInfo('run2', 'test', '.', 1, {'a' : 1}, 1, 1)
    campaign.add_runs([run1, run2])
    assert(campaign.get_run_status('Run_1') == Status.NEW)
    assert(campaign.get_run_status('Run_2') == Status.NEW)
    campaign.set_run_statuses(['Run_1'], Status.ENCODED)
    assert(campaign.get_run_status('Run_1') == Status.ENCODED)


def test_too_many_runs_bug(campaign):
    runs = [RunInfo('run', 'test', '.', 1, {'a' : 1}, 1, 1) for _ in range(2000)]
    run_names = ['Run_{}'.format(i) for i in range(1, 2001)]
    campaign.add_runs(runs)
    

