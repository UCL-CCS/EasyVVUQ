import pytest
import os.path
import easyvvuq
from easyvvuq.constants import default_campaign_prefix
from easyvvuq.db.sql import CampaignDB
from easyvvuq.data_structs import CampaignInfo

def test_file_created(tmp_path):
    info = CampaignInfo(
        name='test',
        campaign_dir_prefix=default_campaign_prefix,
        easyvvuq_version=easyvvuq.__version__,
        campaign_dir='.')
    campaign = CampaignDB(location='sqlite:///{}/test.sqlite'.format(tmp_path), new_campaign=True, name='test', info=info)
    assert(os.path.isfile('{}/test.sqlite'.format(tmp_path)))
