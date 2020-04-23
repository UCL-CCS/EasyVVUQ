import pytest
from easyvvuq.utils.helpers import multi_index_tuple_parser

def test_multi_index_tuple_parser_exceptions():
    with pytest.raises(RuntimeError):
        multi_index_tuple_parser([])
    with pytest.raises(RuntimeError):
        multi_index_tuple_parser([3])
    with pytest.raises(RuntimeError):
        multi_index_tuple_parser(['a', 'b', 3])
    with pytest.raises(RuntimeError):
        multi_index_tuple_parser([3, 'a', 'b'])
