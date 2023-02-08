from easyvvuq.sampling.sweep import BasicSweep, wrap_iterable
import pytest


@pytest.fixture
def basic_sweep_sampler():
    return BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]})


def test_wrap_iterable():
    res = []
    for var_name, val in wrap_iterable('a', [1, 2, 3]):
        res.append((var_name, val))
    assert (res == [('a', 1), ('a', 2), ('a', 3)])


def test_sweep(basic_sweep_sampler):
    res = []
    for run_dict in basic_sweep_sampler:
        res.append(run_dict)
    assert (res == [{'a': 1, 'b': 4}, {'a': 1, 'b': 5}, {'a': 1, 'b': 6},
                    {'a': 2, 'b': 4}, {'a': 2, 'b': 5}, {'a': 2, 'b': 6},
                    {'a': 3, 'b': 4}, {'a': 3, 'b': 5}, {'a': 3, 'b': 6}])


def test_init():
    sweep = BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]}, 10)
    with pytest.raises(StopIteration):
        sweep.__next__()


def test_is_finite(basic_sweep_sampler):
    assert (basic_sweep_sampler.is_finite())


def test_n_samples(basic_sweep_sampler):
    assert (basic_sweep_sampler.n_samples() == 9)


def test_basic_sweep_single_list():
    assert (len(list(BasicSweep({'a': [1, 2, 3]}))) == 3)
