import pytest
import os.path
import easyvvuq as uq
from easyvvuq.constants import default_campaign_prefix, Status
from easyvvuq.db.sql import CampaignDB
from easyvvuq.data_structs import CampaignInfo, RunInfo, AppInfo
from easyvvuq.constants import Status
from easyvvuq.actions import Actions, ExecutePython
import pandas as pd
import numpy as np


@pytest.fixture
def app_info():
    actions = Actions(ExecutePython(lambda x: {}))
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
        actions)
#        None,
#        uq.encoders.GenericEncoder(
#            template_fname='tests/cooling/cooling.template',
#            delimiter='$',
#            target_filename='cooling_in.json'),
#        uq.decoders.SimpleCSV(
#            target_filename='output.csv',
#            output_columns=["te"]))

    return app_info


@pytest.fixture
def campaign(tmp_path, app_info):
    info = CampaignInfo(
        name='test',
        campaign_dir_prefix=default_campaign_prefix,
        easyvvuq_version=uq.__version__,
        campaign_dir=str(tmp_path))
    campaign = CampaignDB(location='sqlite:///{}/test.sqlite'.format(tmp_path))
    campaign.create_campaign(info)
    campaign.tmp_path = str(tmp_path)
    runs = [RunInfo('run', '.', 1, {'a': 1}, 1, 1) for _ in range(910)]
    campaign.add_runs(runs)
    campaign.add_app(app_info)
    return campaign


def test_db_file_created(campaign):
    assert (os.path.isfile('{}/test.sqlite'.format(campaign.tmp_path)))


def test_get_and_set_status(campaign):
    run_ids = list(range(1, 911))
    assert (all([campaign.get_run_status(id_) == Status.NEW for id_ in run_ids]))
    campaign.set_run_statuses(run_ids, Status.ENCODED)
    assert (all([campaign.get_run_status(id_) == Status.ENCODED for id_ in run_ids]))


def test_get_num_runs(campaign):
    assert (campaign.get_num_runs() == 910)


def test_app(campaign):
    with pytest.raises(RuntimeError):
        campaign.app('test_')
    app_dict = campaign.app('test')
    assert (app_dict['name'] == 'test')
    assert (isinstance(app_dict, dict))


def test_add_app(campaign, app_info):
    with pytest.raises(RuntimeError):
        campaign.add_app(app_info)


def test_campaign(campaign):
    assert ('test' in campaign.campaigns())


def test_get_campaign_id(campaign):
    with pytest.raises(RuntimeError):
        campaign.get_campaign_id('test_')
    assert (campaign.get_campaign_id('test') == 1)


def test_campaign_dir(campaign):
    assert (campaign.campaign_dir('test') == campaign.tmp_path)


def test_version_check(campaign):
    info = CampaignInfo(
        name='test2',
        campaign_dir_prefix=default_campaign_prefix,
        easyvvuq_version="some.other.version",
        campaign_dir=str(campaign.tmp_path))
    with pytest.raises(RuntimeError):
        campaign2 = CampaignDB(location='sqlite:///{}/test.sqlite'.format(campaign.tmp_path))
        campaign2.create_campaign(info)
    info = CampaignInfo(
        name='test3',
        campaign_dir_prefix=default_campaign_prefix,
        easyvvuq_version=uq.__version__,
        campaign_dir=str(campaign.tmp_path))
    campaign3 = CampaignDB(location='sqlite:///{}/test.sqlite'.format(campaign.tmp_path))
    campaign3.create_campaign(info)


def test_collation(campaign):
    results = [(run[0], {'b': i, 'c': [i + 1, i + 2]}) for i, run in enumerate(campaign.runs())]
    campaign.store_results('test', results)
    campaign.set_run_statuses([run[0] for run in campaign.runs()], Status.COLLATED)
    result = campaign.get_results('test', 1)
    assert (isinstance(result, pd.DataFrame))
    assert (list(result.columns) == [('run_id', 0), ('iteration', 0),
                                     ('a', 0), ('b', 0), ('c', 0), ('c', 1)])
    assert (list(result.iloc[100].values) == [101, 0, 1, 100, 101, 102])
    assert (result.count()[0] == 910)


def test_mv_collation(tmp_path, app_info):
    mv_data = {
        'timestep': [
            1.0,
            2.0,
            3.0,
            4.0,
            5.0,
            6.0,
            7.0,
            8.0,
            9.0,
            10.0,
            11.0,
            12.0,
            13.0,
            14.0,
            15.0,
            16.0,
            17.0,
            18.0,
            19.0,
            20.0,
            21.0,
            22.0,
            23.0,
            24.0,
            25.0,
            26.0,
            27.0,
            28.0,
            29.0,
            30.0,
            31.0,
            32.0,
            33.0,
            34.0,
            35.0,
            36.0,
            37.0,
            38.0,
            39.0,
            40.0,
            41.0,
            42.0,
            43.0,
            44.0,
            45.0,
            46.0,
            47.0,
            48.0,
            49.0,
            50.0,
            51.0],
        'time': [
            5e-07,
            1e-06,
            1.5e-06,
            2e-06,
            2.5e-06,
            3e-06,
            3.5e-06,
            4e-06,
            4.5e-06,
            5e-06,
            5.5e-06,
            6e-06,
            6.5e-06,
            7e-06,
            7.5e-06,
            8e-06,
            8.5e-06,
            9e-06,
            9.5e-06,
            1e-05,
            1.05e-05,
            1.1e-05,
            1.15e-05,
            1.2e-05,
            1.25e-05,
            1.3e-05,
            1.35e-05,
            1.4e-05,
            1.45e-05,
            1.5e-05,
            1.55e-05,
            1.6e-05,
            1.65e-05,
            1.7e-05,
            1.75e-05,
            1.8e-05,
            1.85e-05,
            1.9e-05,
            1.95e-05,
            2e-05,
            2.05e-05,
            2.1e-05,
            2.15e-05,
            2.2e-05,
            2.25e-05,
            2.3e-05,
            2.35e-05,
            2.4e-05,
            2.45e-05,
            2.5e-05,
            2.5e-05],
        'resulting_force': [
            154334.0,
            258961.0,
            261115.0,
            341040.0,
            379343.0,
            436974.0,
            494847.0,
            580487.0,
            669071.0,
            760177.0,
            885250.0,
            1003870.0,
            1121100.0,
            1240490.0,
            1351730.0,
            1441980.0,
            1514690.0,
            1562410.0,
            1581580.0,
            1569400.0,
            1527670.0,
            1462240.0,
            1378540.0,
            1284030.0,
            1182790.0,
            1086710.0,
            996340.0,
            920193.0,
            867072.0,
            840048.0,
            838119.0,
            862059.0,
            910291.0,
            975073.0,
            1053810.0,
            1141210.0,
            1226020.0,
            1303890.0,
            1359100.0,
            1387040.0,
            1386630.0,
            1353730.0,
            1296010.0,
            1224370.0,
            1143670.0,
            1061790.0,
            986885.0,
            925497.0,
            879544.0,
            858313.0,
            862543.0]}
    params = {
        'temperature': 274.775390625,
        'strain_rate': 0.004395019531250001,
        'height': 0.0804453125}
    info = CampaignInfo(
        name='test',
        campaign_dir_prefix=default_campaign_prefix,
        easyvvuq_version=uq.__version__,
        campaign_dir=str(tmp_path))
    campaign = CampaignDB(location='sqlite:///{}/test.sqlite'.format(tmp_path))
    campaign.create_campaign(info)
    campaign.tmp_path = str(tmp_path)
    runs = [RunInfo('run', '.', 1, params, 1, 1)]
    run_ids = [0]
    campaign.add_runs(runs)
    campaign.add_app(app_info)
    results = [(0, mv_data), (1, mv_data)]
    campaign.store_results('test', results)
    assert (not campaign.get_results('test', 1).empty)
    
