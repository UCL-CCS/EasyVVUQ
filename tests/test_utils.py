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


def test_multi_index_parser_corner_cases():
    assert(multi_index_tuple_parser(["a"]) == (["a"], False))
    assert(multi_index_tuple_parser(['a', '("b", 1)']) == (["a", ("b", 1)], False))


def test_multi_index_parser():
    assert(multi_index_tuple_parser(['("a", 1)', '("b", 1)']) == ([("a", 1), ("b", 1)], True))
