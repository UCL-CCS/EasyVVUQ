import easyvvuq as uq


def test_lhc():
    vary = {'a': (-5, 3), 'b': (2, 10)}
    sampler = uq.sampling.quasirandom.LHCSampler(vary, 5)
    for sample in sampler:
        assert(sample['a'] >= -5.0)
        assert(sample['a'] <= 3.0)
        assert(sample['b'] >= 2.0)
        assert(sample['b'] <= 10.0)


def test_halton():
    vary = {'a': (-5, 3), 'b': (2, 10)}
    sampler = uq.sampling.quasirandom.HaltonSampler(vary, 5)
    for sample in sampler:
        assert(sample['a'] >= -5.0)
        assert(sample['a'] <= 3.0)
        assert(sample['b'] >= 2.0)
        assert(sample['b'] <= 10.0)
