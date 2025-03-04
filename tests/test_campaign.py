import easyvvuq as uq
from easyvvuq.actions import CreateRunDirectory, Encode, ExecuteLocal, Decode, Actions
import chaospy as cp
import os
import logging
import pytest

TEST_PATH = os.path.dirname(os.path.realpath(__file__))
LOGGER = logging.getLogger(__name__)


@pytest.fixture
def campaign(tmpdir):
    params = {
        "angle": {
            "type": "float",
            "min": 0.0,
            "max": 6.28,
            "default": 0.79},
        "air_resistance": {
            "type": "float",
            "min": 0.0,
            "max": 1.0,
            "default": 0.2},
        "height": {
            "type": "float",
            "min": 0.0,
            "max": 1000.0,
            "default": 1.0},
        "time_step": {
            "type": "float",
            "min": 0.0001,
            "max": 1.0,
            "default": 0.01},
        "gravity": {
            "type": "float",
            "min": 0.0,
            "max": 1000.0,
            "default": 9.8},
        "mass": {
            "type": "float",
            "min": 0.0001,
            "max": 1000.0,
            "default": 1.0},
        "velocity": {
            "type": "float",
            "min": 0.0,
            "max": 1000.0,
            "default": 10.0}
    }
    encoder = uq.encoders.GenericEncoder(
        template_fname=f'{TEST_PATH}/cannonsim/test_input/cannonsim.template',
        target_filename='in.cannon')
    decoder = uq.decoders.SimpleCSV(
        target_filename='output.csv', output_columns=[
            'Dist', 'lastvx', 'lastvy'])
    execute = ExecuteLocal(f"{TEST_PATH}/cannonsim/bin/cannonsim in.cannon output.csv")
    campaign = uq.Campaign(name='test', work_dir=tmpdir)
    actions = Actions(CreateRunDirectory('/tmp'), Encode(encoder), execute, Decode(decoder))
    campaign.add_app(name='test', params=params, actions=actions)
    campaign.set_app('test')
    stats = uq.analysis.BasicStats(qoi_cols=['Dist', 'lastvx', 'lastvy'])
    # Make a random sampler
    vary = {
        "angle": cp.Uniform(0.0, 1.0),
        "height": cp.Uniform(2.0, 10.0),
        "velocity": cp.Normal(10.0, 1.0),
        "mass": cp.Uniform(1.0, 5.0)
    }
    sampler = uq.sampling.RandomSampler(vary=vary)
    campaign.set_sampler(sampler)
    campaign.execute(nsamples=100, sequential=True).collate()
    return campaign


def test_campaign_exists(tmp_path):
    campaign = uq.Campaign(name='test', work_dir=tmp_path)
    assert (campaign.campaign_db.campaign_exists('test'))
    assert (not campaign.campaign_db.campaign_exists('test2'))


def test_invalid_sampler(tmp_path):
    with pytest.raises(Exception):
        our_campaign = uq.Campaign(name='test', work_dir=tmp_path)
        our_campaign.set_sampler('not_a_sampler')


def test_premature_run_addition(tmp_path):
    with pytest.raises(Exception):
        our_campaign = uq.Campaign(name='test', work_dir=tmp_path)
        # Requires an active app to be set
        our_campaign.add_runs([])


def test_none_run_addition(tmp_path):
    with pytest.raises(Exception):
        our_campaign = uq.Campaign(name='test', work_dir=tmp_path)
        # Requires an active app to be set
        our_campaign.add_runs([None])


def test_premature_get_last_analysis(caplog, tmp_path):
    with caplog.at_level(logging.WARNING):
        our_campaign = uq.Campaign(name='test', work_dir=tmp_path)
        result = our_campaign.get_last_analysis()

    assert 'No last analysis output available.' in caplog.text
    assert result is None


def test_string(campaign):
    target_str = (
        f"db_location = {campaign.db_location}\n"
        f"active_sampler_id = 1\n"
        f"campaign_name = test\n"
        f"campaign_dir = {campaign.campaign_dir}\n"
        f"campaign_id = 1\n")
    assert str(campaign) == target_str


def test_get_active_sampler(tmp_path):
    camp = uq.Campaign(name='test', work_dir=tmp_path)
    vary = {
        "angle": cp.Uniform(0.0, 1.0),
        "height": cp.Uniform(2.0, 10.0),
        "velocity": cp.Normal(10.0, 1.0),
        "mass": cp.Uniform(1.0, 5.0)
    }
    sampler = uq.sampling.RandomSampler(vary=vary)
    camp.set_sampler(sampler)

    assert camp.get_active_sampler() == sampler


def test_get_active_app(campaign):
    assert campaign.get_active_app() == campaign._active_app


def test_add_external_runs(campaign):
    input_decoder = uq.decoders.JSONDecoder(
        '', ['outfile', 'S0', 'I0', 'beta', 'gamma', 'iterations'])
    output_decoder = uq.decoders.SimpleCSV('', ['S', 'I', 'R', 'r0', 't'])
    campaign.add_external_runs(['tests/add_files/input_1.json',
                                'tests/add_files/input_2.json',
                                'tests/add_files/input_3.json'],
                               ['tests/add_files/output_1.csv',
                                'tests/add_files/output_2.csv',
                                'tests/add_files/output_3.csv'],
                               input_decoder, output_decoder)
