from easyvvuq.decoders.json import JSONDecoder


def test_jsondecoder_basic():
    decoder = JSONDecoder(os.path.join('jsondecoder', 'fredrik.json'))
