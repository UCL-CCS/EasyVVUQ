from enum import Enum


class OutputType(Enum):
    """Types of data output by UQPs/VVPs
    """

    SAMPLE = 'sample'
    ARRAY = 'array'
    SAMPLE_ARRAY = 'sample_array'
    TRACK = 'track'
    SUMMARY = 'summary'
