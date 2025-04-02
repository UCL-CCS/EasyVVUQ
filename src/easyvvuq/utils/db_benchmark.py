import easyvvuq as uq
import chaospy as cp
import numpy as np
import json
from timeit import Timer


def benchmark(nsamples):
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
    actions = uq.actions.local_execute(encoder, 'sir input.json', decoder)
    campaign = uq.Campaign(name='sir_benchmark', params=params, actions=actions)
    vary = {
        "beta": cp.Uniform(0.15, 0.25),
        "gamma": cp.Normal(0.04, 0.001),
    }
    campaign.set_sampler(uq.sampling.RandomSampler(vary=vary))
    benchmark_results = {}
    t = Timer('campaign.draw_samples(nsamples)', globals=locals())
    benchmark_results['draw_samples'] = t.timeit(1)

    def fake_results():
        counter = 1
        while True:
            yield ('Run_{}'.format(counter), {'values': list(np.random.random(size=100))})
            counter += 1
    fakes = fake_results()
    results_ = []
    for _ in range(nsamples):
        results_.append(next(fakes))
    t = Timer(
        'campaign.campaign_db.store_results(campaign._active_app_name, results_)',
        globals=locals())
    benchmark_results['store_results'] = t.timeit(1)
    t = Timer('campaign.get_collation_result()', globals=locals())
    benchmark_results['get_collation_result'] = t.timeit(1)
    return benchmark_results


if __name__ == '__main__':
    nsamples = [1000, 10000, 100000, 1000000]
    results = {}
    for nsamples_ in nsamples:
        results[nsamples_] = benchmark(nsamples_)
    print(json.dumps(results))
