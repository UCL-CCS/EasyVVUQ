import easyvvuq as uq
from easyvvuq.actions import CreateRunDirectory, Encode, ExecuteLocal, Decode, Actions
import chaospy as cp
import os
import logging
import pytest
import shutil
from easyvvuq.db.sql import CampaignTable

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

def test_invalid_db_type(tmp_path):
    with pytest.raises(RuntimeError):
        uq.Campaign(name='test', work_dir=tmp_path, db_type='pen&paper')


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


# def test_relocate_campaign(campaign, tmpdir):
#     runs = campaign.campaign_db.runs()
#     runs_dir = campaign.campaign_db.runs_dir()
#     for run in runs:
#         assert(run[1]['run_dir'].startswith(runs_dir))
#     with pytest.raises(RuntimeError):
#         campaign.relocate('/test/test')
#     campaign.relocate(tmpdir)
#     for run in campaign.campaign_db.runs():
#         assert(run[1]['run_dir'] == os.path.join(tmpdir, 'runs', run[0]))


# def test_relocate_full(tmp_path):
#     campaign = uq.Campaign(name='test', work_dir=tmp_path)
#     params = {
#         "temp_init": {
#             "type": "float",
#             "min": 0.0,
#             "max": 100.0,
#             "default": 95.0},
#         "kappa": {
#             "type": "float",
#             "min": 0.0,
#             "max": 0.1,
#             "default": 0.025},
#         "t_env": {
#             "type": "float",
#             "min": 0.0,
#             "max": 40.0,
#             "default": 15.0},
#         "out_file": {
#             "type": "string",
#             "default": "output.csv"}}
#     output_filename = params["out_file"]["default"]
#     output_columns = ["te"]
#     # Create an encoder and decoder for PCE test app
#     encoder = uq.encoders.GenericEncoder(
#         template_fname='tests/cooling/cooling.template',
#         delimiter='$',
#         target_filename='cooling_in.json')
#     decoder = uq.decoders.SimpleCSV(target_filename=output_filename,
#                                     output_columns=output_columns)
#     vary = {
#         "kappa": cp.Uniform(0.025, 0.075),
#         "t_env": cp.Uniform(15, 25)
#     }
#     sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=3)
#     actions = uq.actions.ExecuteLocal("tests/cooling/cooling_model.py cooling_in.json")
#     campaign.add_app(name='test_app', params=params, encoder=encoder, decoder=decoder)
#     campaign.set_app('test_app')
#     campaign.set_sampler(sampler)
#     campaign.draw_samples()
#     campaign.populate_runs_dir()
#     campaign.apply_for_each_run_dir(actions)
#     campaign.collate()
#     campaign.save_state(os.path.join(tmp_path, "state.json"))
#     shutil.copytree(
#         campaign.campaign_dir,
#         os.path.join(
#             tmp_path,
#             'relocation/'))
#     relocated = uq.Campaign(
#         state_file=os.path.join(
#             tmp_path,
#             "state.json"),
#         relocate={
#             'work_dir': tmp_path,
#             'campaign_dir': 'relocation'})
#     assert(relocated.campaign_dir == os.path.join(tmp_path, 'relocation'))
#     assert(relocated.work_dir == str(tmp_path))
#     for run in relocated.campaign_db.runs():
#         assert(run[1]['run_dir'] == os.path.join(tmp_path, 'relocation', 'runs', run[0]))
#     campaign_table = campaign.campaign_db.session.query(CampaignTable).first()
#     assert(campaign_table.campaign_dir == os.path.join(tmp_path, 'relocation'))
#     assert(campaign_table.runs_dir == os.path.join(tmp_path, 'relocation', 'runs'))
#     relocated.recollate()
