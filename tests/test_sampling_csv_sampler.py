import pytest
from easyvvuq.sampling import CSVSampler


def test_csv_sampler():
    with pytest.raises(RuntimeError):
        CSVSampler('tests/simple_csv/test.cs')
    sampler = CSVSampler('tests/simple_csv/test.csv')
    counter = 0
    for sample in sampler:
        if sample['Step'] == 5:
            assert (sample['Value'] == 25.950662)
        counter += 1
    assert (counter == 10)
    assert (sampler.n_samples() == 10)
    assert (sampler.is_finite())
