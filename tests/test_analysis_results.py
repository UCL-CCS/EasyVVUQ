from easyvvuq.analysis.results import AnalysisResults

def test_keys_to_tuples():
    assert(AnalysisResults._keys_to_tuples({}) == {})
