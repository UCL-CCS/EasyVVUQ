import pytest
import easyvvuq as uq
import chaospy as cp
import numpy as np

def pytest_namespace():
    return {'shared': None}

@pytest.mark.dependency()
def test_db_benchmark_draw(benchmark):
    params = {
        "S0": {"type": "float", "default": 997}, 
        "I0": {"type": "float", "default": 3}, 
        "beta": {"type": "float", "default": 0.2}, 
        "gamma": {"type": "float", "default": 0.04, "min": 0.0, "max": 1.0},
        "iterations": {"type": "integer", "default": 100},
        "outfile": {"type": "string", "default": "output.csv"}
    }
    encoder = uq.encoders.GenericEncoder(template_fname='tutorials/sir.template', delimiter='$', target_filename='input.json')
    decoder = uq.decoders.SimpleCSV(target_filename='output.csv', output_columns=['I'])
    campaign = uq.Campaign(name='sir_benchmark', params=params, encoder=encoder, decoder=decoder)
    pytest.shared = campaign
    vary = {
        "beta": cp.Uniform(0.15, 0.25),
        "gamma": cp.Normal(0.04, 0.001),
    }
    campaign.set_sampler(uq.sampling.MCSampler(vary=vary, n_mc_samples=2000))
    benchmark.pedantic(campaign.draw_samples, iterations=1, rounds=1)

def fake_results():
    counter = 1
    while True:
        yield ('Run_{}'.format(counter), {'values': list(np.random.random(size=100))})
        counter += 1

@pytest.mark.dependency(depends=['test_db_benchmark_draw'])
def test_db_benchmark_store_results(benchmark):
    iterator = fake_results()
    results = []
    pass
    for _ in range(6000):
        results.append(next(iterator))
    benchmark.pedantic(pytest.shared.campaign_db.store_results,
                       args=(pytest.shared._active_app_name, results), iterations=1, rounds=1)

@pytest.mark.dependency(depends=['test_db_benchmark_store_results'])
def test_db_benchmark_get_collation_result(benchmark):
    benchmark.pedantic(pytest.shared.get_collation_result, iterations=1, rounds=1)
