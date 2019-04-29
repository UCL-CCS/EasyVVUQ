from enum import Enum

# TODO: make this auto update with setup.py etc.
version = '0.0.3.dev1'
default_campaign_prefix = 'EasyVVUQ_Campaign_'


class OutputType(Enum):
    """Types of data output by UQPs/VVPs
    """

    SAMPLE = 'sample'
    ARRAY = 'array'
    SAMPLE_ARRAY = 'sample_array'
    TRACK = 'track'
    SUMMARY = 'summary'
