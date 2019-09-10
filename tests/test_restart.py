import pytest
import easyvvuq as uq
from gauss.decoder_gauss import GaussDecoder


@pytest.fixture
def test_restart(tmpdir):
    my_campaign = uq.Campaign(name=campaign_name, work_dir=tmpdir, db_type='sql')
    params = {
        "sigma": {
            "type": "float",
            "min": 0.0,
            "max": 100000.0,
            "default": 0.25
        },
        "mu": {
            "type": "float",
            "min": 0.0,
            "max": 100000.0,
            "default": 1
        },
        "num_steps": {
            "type": "integer",
            "min": 0,
            "max": 100000,
            "default": 10
        },
        "out_file": {
            "type": "string",
            "default": "output.csv"
        },
        "bias": {
            "type": "fixture",
            "allowed": ["bias1", "bias2"],
            "default": "bias1"
        }
    }
    encoder = uq.encoders.GenericEncoder(template_fname='tests/gauss/gauss.template',
                                         target_filename='gauss_in.json')
    decoder = GaussDecoder(target_filename=params['out_file']['default'])
    my_campaign.add_app(name='gauss',
                        params=params,
                        encoder=encoder,
                        decoder=decoder,
                        fixtures=None)
    my_campaign.set_app('gauss')
    collater = uq.collate.AggregateSamples(average=False)
    my_campaign.set_collater(collater)
    sampler = uq.sampling.RandomSampler(vary=vary)
    my_campaign.set_sampler(sampler)
    my_campaign.draw_samples(num_samples=2, replicas=2)
    my_campaign.populate_runs_dir()
    my_campaign.collate()
    state_file = tmpdir + "{}_state.json".format('gauss')
    my_campaign.save_state(state_file)
    my_campaign = None
    reloaded_campaign = uq.Campaign(state_file=state_file, work_dir=tmpdir)
    reloaded_campaign.set_app('gauss')
    reloaded_campaign.draw_samples(num_samples=2, replicas=2)
    reloaded_campaign.populate_runs_dir()

