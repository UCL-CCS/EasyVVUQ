from easyvvuq.decoders.json import JSONDecoder
import os
import numpy as np
import pytest


def test_jsondecoder_basic():
    decoder = JSONDecoder(os.path.join('jsondecoder', 'fredrik.json'), ['cfrac', 'we', 'v'])
    run_info = {'run_dir': 'tests'}
    data = decoder.parse_sim_output(run_info)
    assert (data['cfrac'] == 0.24000000131541285)
    assert (data['we'] == -0.4910355508327484)
    assert (len(data['v']) == 126)
    assert (data['v'][:3] == [0.014841768890619278, 0.014779693447053432, 0.014733896590769291])
    assert (data['v'][-3:] == [0.0010381652973592281, 0.0010054642334580421, 0.0009733123588375747])


def test_jsondecoder_scalars_only():
    # like test_jsondecoder_basics, but with only scalar quantities
    decoder = JSONDecoder(os.path.join('jsondecoder', 'fredrik.json'), ['cfrac', 'we'])
    run_info = {'run_dir': 'tests'}
    data = decoder.parse_sim_output(run_info)
    assert (data['cfrac'] == 0.24000000131541285)
    assert (data['we'] == -0.4910355508327484)


def test_json_nested():
    decoder = JSONDecoder(os.path.join('jsondecoder', 'nested.json'),
                          [['root1', 'node1', 'leaf1'], ['root1', 'leaf2'], 'leaf3'])
    run_info = {'run_dir': 'tests'}
    data = decoder.parse_sim_output(run_info)
    assert (data['root1.node1.leaf1'] == 0.33)
    assert (data['root1.leaf2'] == 0.32)
    assert (data['leaf3'] == [0.2, 0.3])


def test_missing_column():
    # Check if a RuntimeError is raised if a wrong column is specified
    decoder = JSONDecoder(os.path.join('jsondecoder', 'nested.json'),
                          [['root1', 'node1', 'abcd'], ['root1', 'leaf2'], 'leaf3'])
    run_info = {'run_dir': 'tests'}
    with pytest.raises(RuntimeError) as excinfo:
        data = decoder.parse_sim_output(run_info)
    # Check if the missing column is reported in the exception message
    assert ("['root1', 'node1', 'abcd']" in str(excinfo.value))


def test_init_exceptions():
    with pytest.raises(RuntimeError):
        JSONDecoder('nested.json', [])
