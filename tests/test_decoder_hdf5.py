from easyvvuq.decoders.hdf5 import HDF5
import os
import numpy as np
import pytest


@pytest.fixture
def decoder():
    return HDF5('test.hdf5', output_columns=['array10', 'array2'])


def test_hdf5(decoder):
    df = decoder.parse_sim_output({'run_dir': os.path.join('tests', 'hdf5')})
    # test decoding arrays of different length from the same file
    assert df['array10'] == np.arange(10).tolist()
    assert df['array2'] == np.arange(2).tolist()


def test_get_output_path(decoder):
    assert (decoder._get_output_path(
        {'run_dir': os.path.join('tests', 'hdf5')}, 'test.hdf5') ==
        os.path.join('tests', 'hdf5', 'test.hdf5'))
    with pytest.raises(RuntimeError):
        decoder._get_output_path({'run_dir': os.path.join('hdf5')}, 'test.hdf5')
