from easyvvuq.db.json import CampaignDB
from easyvvuq.constants import default_campaign_prefix
from easyvvuq.data_structs import CampaignInfo, RunInfo, AppInfo
from easyvvuq.sampling.sweep import BasicSweep
import json
from easyvvuq.constants import Status
import easyvvuq as uq
import pytest
import os


@pytest.fixture
def app_info():
    app_info = AppInfo('test', uq.ParamsSpecification({
        "temp_init": {
            "type": "float",
            "min": 0.0,
            "max": 100.0,
            "default": 95.0},
        "kappa": {
            "type": "float",
            "min": 0.0,
            "max": 0.1,
            "default": 0.025},
        "t_env": {
            "type": "float",
            "min": 0.0,
            "max": 40.0,
            "default": 15.0},
        "out_file": {
            "type": "string",
            "default": "output.csv"}}),
        uq.encoders.GenericEncoder(
            template_fname='tests/cooling/cooling.template',
            delimiter='$',
            target_filename='cooling_in.json'),
        uq.decoders.SimpleCSV(
            target_filename='output.csv',
            output_columns=["te"],
            header=0),
        uq.collate.AggregateSamples(average=False))
    return app_info


@pytest.fixture
def campaign_db(tmpdir, app_info):
    res = CampaignDB(str(tmpdir) + "/test.json", True, 'test',
                     CampaignInfo('test', 'v0.5.1', default_campaign_prefix, str(tmpdir)))
    res.add_app(app_info)
    return res


@pytest.fixture
def runs():
    return [RunInfo('run', 'test', '.', 1, {'a': i}, 1, 1) for i in range(1010)]


def test_campaign(campaign_db):
    assert(campaign_db.get_sampler_id(0) == 1)


def test_set_sampler(campaign_db):
    with pytest.raises(RuntimeError):
        campaign_db.set_sampler(1, 2)
    with pytest.raises(RuntimeError):
        campaign_db.set_sampler(2, 1)


def test_load_save(campaign_db):
    campaign_db._save()
    with open(campaign_db.location) as fd:
        dict1 = json.load(fd)
    campaign_db._load_campaign(campaign_db.location, 'test')
    campaign_db._save()
    with open(campaign_db.location) as fd:
        dict2 = json.load(fd)
    assert(dict1 == dict2)


def test_campaign_dir(campaign_db):
    assert(campaign_db.campaign_dir() == campaign_db._campaign_info['campaign_dir'])


def test_new_campaign(campaign_db, tmpdir):
    with pytest.raises(RuntimeError):
        CampaignDB(new_campaign=True,
                   info=CampaignInfo('test', 'v0.5.1', default_campaign_prefix, str(tmpdir)))
    reloaded_campaign = CampaignDB(campaign_db.location)
    assert(reloaded_campaign.location == campaign_db.location)


def test_load_campaign(campaign_db, tmpdir):
    with open(os.path.join(tmpdir, 'test1.json'), 'w') as fd:
        json.dump('{}', fd)
    with pytest.raises(RuntimeError):
        campaign_db._load_campaign(os.path.join(tmpdir, 'test1.json'), None)
    with open(os.path.join(tmpdir, 'test2.json'), 'w') as fd:
        json.dump({"campaign": {"name": "test_"}}, fd)
    with pytest.raises(RuntimeError):
        campaign_db._load_campaign(os.path.join(tmpdir, 'test2.json'), 'test')


def test_app(campaign_db, app_info):
    d1 = campaign_db.app('test')
    d2 = app_info.to_dict()
    del d1['id']
    assert(d1 == d2)


def test_add_app(campaign_db, app_info):
    with pytest.raises(RuntimeError):
        campaign_db.add_app(app_info)
    campaign_db._app = None
    campaign_db.add_app(app_info)


def test_add_sampler(campaign_db):
    campaign_db.add_sampler(BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]}))
    with pytest.raises(RuntimeError):
        campaign_db.add_sampler(BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]}))
    assert(campaign_db._sample == BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]}).serialize())


def test_update_sampler(campaign_db):
    sampler = BasicSweep({'a': [1, 11, 3], 'b': [4, 5, 6]})
    with pytest.raises(RuntimeError):
        campaign_db.update_sampler(2, sampler)
    campaign_db.update_sampler(1, sampler)
    assert(campaign_db._sample == sampler.serialize())


def test_resurrect_sampler(campaign_db):
    sampler = BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]})
    campaign_db.add_sampler(sampler)
    with pytest.raises(RuntimeError):
        campaign_db.resurrect_sampler(2)
    assert(campaign_db.resurrect_sampler(1).serialize() == sampler.serialize())


def test_resurrect_app_1(campaign_db, app_info):
    campaign_db._app = None
    with pytest.raises(RuntimeError):
        encoder, decoder, collater = campaign_db.resurrect_app('test')


def test_resurrect_app_2(campaign_db, app_info):
    with pytest.raises(RuntimeError):
        encoder, decoder, collater = campaign_db.resurrect_app('test_')
    encoder, decoder, collater = campaign_db.resurrect_app('test')
    assert(app_info.input_encoder.serialize() == encoder.serialize())
    assert(app_info.output_decoder.serialize() == decoder.serialize())
    assert(app_info.collater.serialize() == collater.serialize())


def test_add_runs(campaign_db, runs):
    campaign_db.add_runs(runs)
    for i in range(1010):
        assert(campaign_db.run('Run_{}'.format(i + 1))['params'] ==
               runs[i].to_dict()['params'])
