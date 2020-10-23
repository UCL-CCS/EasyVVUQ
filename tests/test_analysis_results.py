from easyvvuq.analysis.results import AnalysisResults
import pytest


def test_keys_to_tuples():
    assert(AnalysisResults._keys_to_tuples({}) == {})
    assert(AnalysisResults._keys_to_tuples(
        {'a': 1, 'b': 2}) == {('a', 0): 1, ('b', 0): 2})
    assert(AnalysisResults._keys_to_tuples(
        {('a', 0): 1, ('b', 0): 2}) == {('a', 0): 1, ('b', 0): 2})
    assert(AnalysisResults._keys_to_tuples(
        {('a', 0): 1, 'b': 2}) == {('a', 0): 1, ('b', 0): 2})


def test_to_tuple():
    assert(AnalysisResults._to_tuple('a') == ('a', 0))
    assert(AnalysisResults._to_tuple(('a', 0)) == ('a', 0))
    with pytest.raises(RuntimeError):
        AnalysisResults._to_tuple(3)


# def test_not_implemented():
#     results = AnalysisResults()
#     with pytest.raises(AttributeError):
#         results.testing()
#     with pytest.raises(RuntimeError, match=r".* {} .*".format(
#         AnalysisResults.all_analysis_methods)):
#         results.sobols_first()
