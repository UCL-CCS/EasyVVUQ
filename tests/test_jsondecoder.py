from easyvvuq.decoders.json import JSONDecoder
import os


def test_jsondecoder_basic():
    decoder = JSONDecoder(os.path.join('jsondecoder', 'fredrik.json'), ['cfarc'])
