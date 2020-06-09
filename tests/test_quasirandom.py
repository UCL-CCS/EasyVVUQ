import easyvvuq as uq
import chaospy as cp


def test_lhc():
    vary = {'a': cp.Uniform(-5, 3), 'b': cp.Uniform(2, 10)}
    sampler = uq.sampling.quasirandom.LHCSampler(vary, max_num=10)
    for sample in sampler:
        assert(sample['a'] >= -5.0)
        assert(sample['a'] <= 3.0)
        assert(sample['b'] >= 2.0)
        assert(sample['b'] <= 10.0)
    assert(sampler.n_samples() == 10)


def test_halton():
    vary = {'a': cp.Uniform(-5, 3), 'b': cp.Uniform(2, 10)}
    sampler = uq.sampling.quasirandom.HaltonSampler(vary, max_num=10)
    for sample in sampler:
        assert(sample['a'] >= -5.0)
        assert(sample['a'] <= 3.0)
        assert(sample['b'] >= 2.0)
        assert(sample['b'] <= 10.0)
    assert(sampler.n_samples() == 10)
