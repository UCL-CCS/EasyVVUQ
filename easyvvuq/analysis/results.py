"""Represents the results obtained during the analysis stage.
"""

class AnalysisResults:
    """Contains the analysis results.

    Parameters
    ----------
    raw_data: obj
        an arbitrary object that contains raw analysis data
    """
    def __init__(self, raw_data=None):
        self.raw_data = None

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
