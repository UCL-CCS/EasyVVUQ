from easyvvuq.decoders.simple_csv import SimpleCSV
import os
import numpy as np
import pytest

TEST_MV_DATA = {
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


@pytest.fixture
def decoder():
    return SimpleCSV('test.csv', output_columns=['Step', 'Value'])


@pytest.fixture
def mv_data():
    return SimpleCSV(
        os.path.join('mv_data.csv'),
        output_columns=[
            'timestep',
            'time',
            'resulting_force'])


@pytest.fixture
def mv_data_fail():
    return SimpleCSV(
        os.path.join('mv_data.csv'),
        output_columns=[
            'timesteps'])


def test_wrong_column_exception(mv_data_fail):
    with pytest.raises(RuntimeError):
        mv_data_fail.parse_sim_output({'run_dir': 'tests/files'})


def test_simple_csv(decoder):
    df = decoder.parse_sim_output({'run_dir': os.path.join('tests', 'simple_csv')})
    assert (df['Step'][1] == 1)
    assert (df['Value'][5] == 25.950662)


def test_init_exceptions():
    with pytest.raises(RuntimeError):
        SimpleCSV('test.csv', [])


def test_get_output_path(decoder):
    assert (decoder._get_output_path(
        {'run_dir': os.path.join('tests', 'simple_csv')}, 'test.csv') ==
        os.path.join('tests', 'simple_csv', 'test.csv'))
    with pytest.raises(RuntimeError):
        decoder._get_output_path({'run_dir': os.path.join('simple_csv')}, 'test.csv')


def test_mv_data(mv_data):
    data = mv_data.parse_sim_output({'run_dir': 'tests/files'})
    assert (data == TEST_MV_DATA)
    for key in data.keys():
        assert (len(data[key]) == 51)
