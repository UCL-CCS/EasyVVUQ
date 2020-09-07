"""Represents the results obtained during the analysis stage.
All the analysis classes should implement this in a way that makes
most sense. Provides a more unified interface for accessing the results
in a variety of formats (e.g. NumPy arrays or pandas DataFrames).
"""

class AnalysisResults:
    """Contains the analysis results.

    Parameters
    ----------
    raw_data: obj
        an arbitrary object that contains raw analysis data
    """
    def __init__(self, raw_data=None):
        self.raw_data = raw_data

    def to_numpy(self):
        """Returns a NumPy array with the results. Will depend on the analysis
        method. Might not be implemented.

        Returns
        -------
        a NumPy array
        """
        raise NotImplementedError

    def to_pd(self):
        """Returns a pandas DataFrame with the results. Will depend on the
        analysis method. Might not be implemented.

        Returns
        -------
        a pandas DataFrame
        """
        raise NotImplementedError
