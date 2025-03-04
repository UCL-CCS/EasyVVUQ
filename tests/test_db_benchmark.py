import pytest
import easyvvuq as uq
import chaospy as cp
import numpy as np
from easyvvuq.actions import Actions, Encode, Decode, CreateRunDirectory


def pytest_namespace():
    return {'shared': None}


@pytest.mark.dependency()
def test_draw(benchmark):
    params = {
        "S0": {"type": "float", "default": 997},
        "I0": {"type": "float", "default": 3},
        "beta": {"type": "float", "default": 0.2},
        "gamma": {"type": "float", "default": 0.04, "min": 0.0, "max": 1.0},
        "iterations": {"type": "integer", "default": 100},
        "outfile": {"type": "string", "default": "output.csv"}
    }
    encoder = uq.encoders.GenericEncoder(
        template_fname='tutorials/sir.template',
        delimiter='$',
        target_filename='input.json')
    decoder = uq.decoders.SimpleCSV(target_filename='output.csv', output_columns=['I'])
    execute = uq.actions.ExecuteLocal('test')
    actions = Actions(execute)
    campaign = uq.Campaign(name='sir_benchmark', params=params, actions=actions)
    pytest.shared = campaign
    vary = {
        "beta": cp.Uniform(0.15, 0.25),
        "gamma": cp.Normal(0.04, 0.001),
    }
    campaign.set_sampler(uq.sampling.RandomSampler(vary=vary))
    benchmark(campaign.draw_samples, 10000)


def fake_results():
    counter = 1
    while True:
        yield ('Run_{}'.format(counter), {'values': list(np.random.random(size=100))})
        counter += 1


@pytest.mark.dependency(depends=['test_draw'])
def test_store_results(benchmark):
    iterator = fake_results()
    results = []
    for _ in range(10000):
        results.append(next(iterator))
    benchmark(pytest.shared.campaign_db.store_results, pytest.shared._active_app_name, results)


@pytest.mark.dependency(depends=['test_store_results'])
def test_get_collation_result(benchmark):
    benchmark(pytest.shared.get_collation_result)


@pytest.mark.dependency(depends=['test_get_collation_result'])
def test_draw_add(benchmark):
    benchmark(pytest.shared.draw_samples, 10000)


@pytest.mark.dependency(depends=['test_draw_add'])
def test_store_results_add(benchmark):
    iterator = fake_results()
    results = []
    for _ in range(10000):
        results.append(next(iterator))
    benchmark(pytest.shared.campaign_db.store_results, pytest.shared._active_app_name, results)


@pytest.mark.dependency(depends=['test_store_results_add'])
def test_get_collation_result_add(benchmark):
    benchmark(pytest.shared.get_collation_result)
