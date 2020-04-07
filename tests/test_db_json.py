from easyvvuq.db.json import CampaignDB
from easyvvuq.data_structs import CampaignInfo
import pytest


@pytest.fixture
def campaign_db(tmp_path):
    return CampaignDB(str(tmp_path), True, 'test',
                      CampaignInfo('test', 'v0.5.1', 'test',
                      str(tmp_path), str(tmp_path)))


def test_campaign(campaign_db):
    assert(campaign_db.get_sampler_id(0) == 1)


def test_set_sampler(campaign_db):
    with pytest.raises(RuntimeError):
        campaign_db.set_sampler(1, 2)
    with pytest.raises(RuntimeError):
        campaign_db.set_sampler(2, 1)

