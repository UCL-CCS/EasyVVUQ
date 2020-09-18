from easyvvuq.analysis.results import AnalysisResults

def test_keys_to_tuples():
    assert(AnalysisResults._keys_to_tuples({}) == {})
    assert(AnalysisResults._keys_to_tuples(
        {'a': 1, 'b': 2}) == {('a', 0): 1, ('b', 0): 2})
    assert(AnalysisResults._keys_to_tuples(
        {('a', 0): 1, ('b', 0): 2}) == {('a', 0): 1, ('b', 0): 2})
    assert(AnalysisResults._keys_to_tuples(
        {('a', 0): 1, 'b': 2}) == {('a', 0): 1, ('b', 0): 2})
