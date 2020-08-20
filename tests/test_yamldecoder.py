from easyvvuq.decoders.yaml import YAMLDecoder
import os
import numpy as np
import pytest


@pytest.mark.parametrize("keys, vals", [
    (['a'], [0.0]),  # single scalar
    (['a', 'b', 'c'], [0.0, 1.0, 2.0]),  # multiple scalar
    (['d'], [[1.0, 2.0, 3.0]]),  # single vector
    (['d', 'e'], [[1.0, 2.0, 3.0], [0.0, 1.0, 2.0]]),  # multiple vector
    (['a', 'b', 'd', 'e'], [0.0, 1.0, [1.0, 2.0, 3.0], [0.0, 1.0, 2.0]]),
])
def test_yamldecoder_data(keys, vals):
    decoder = YAMLDecoder(os.path.join('yamldecoder', 'test.yml'), keys)
    run_info = {'run_dir': 'tests'}
    data = decoder.parse_sim_output(run_info)

    for k, v in zip(keys, vals):
        assert((data[k] == np.array([v])).all().all())


def test_yaml_nested():
    decoder = YAMLDecoder(os.path.join('yamldecoder', 'nested.yml'),
                          [['root1', 'node1', 'leaf1'], ['root1', 'leaf2'], 'leaf3'])
    run_info = {'run_dir': 'tests'}
    data = decoder.parse_sim_output(run_info)
    assert((data['root1.node1.leaf1'] == np.array([0.33])).all().all())
    assert((data['root1.leaf2'] == np.array([0.32])).all().all())
    assert((data['leaf3'] == np.array([0.2, 0.3])).all().all())


def test_get_restart_dict():
    decoder = YAMLDecoder('nested.yml',
                          [['root1', 'node1', 'leaf1'], ['root1', 'leaf2'], 'leaf3'])
    restart_dict = decoder.get_restart_dict()
    assert(restart_dict['target_filename'] == 'nested.yml')
    assert(restart_dict['output_columns'] ==
           [['root1', 'node1', 'leaf1'], ['root1', 'leaf2'], 'leaf3'])


def test_sim_complete():
    decoder = YAMLDecoder('nested.yml',
                          [['root1', 'node1', 'leaf1'], ['root1', 'leaf2'], 'leaf3'])
    assert(decoder.sim_complete({'run_dir': os.path.join('tests', 'yamldecoder')}))


def test_init_exception():
    with pytest.raises(RuntimeError):
        YAMLDecoder(None, output_columns=[['root1', 'node1', 'leaf1'],
                                          ['root1', 'leaf2'], 'leaf3'])

    with pytest.raises(RuntimeError):
        YAMLDecoder('yamldecoder/nested.yaml', None)

    with pytest.raises(RuntimeError):
        YAMLDecoder('yamldecoder/nested.yaml', None)
