from easyvvuq.decoders.json import JSONDecoder
import os


def test_jsondecoder_basic():
    decoder = JSONDecoder(os.path.join('jsondecoder', 'fredrik.json'), ['cfrac'])
    run_info = {'run_dir' : 'tests'}
    data = decoder.parse_sim_output(run_info)
    assert(data['cfrac'] ==  0.24000000131541285)
