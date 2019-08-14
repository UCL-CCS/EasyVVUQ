import pytest
import os.path
import easyvvuq
from easyvvuq.constants import default_campaign_prefix
from easyvvuq.db.sql import CampaignDB
from easyvvuq.data_structs import CampaignInfo

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

def test_add_runs(tmp_path):
    pass
