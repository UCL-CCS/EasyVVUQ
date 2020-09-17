"""Represents the results obtained during the analysis stage.
All the analysis classes should implement this in a way that makes
most sense. Provides a more unified interface for accessing the results
in a variety of formats (e.g. NumPy arrays or pandas DataFrames).

Examples
--------

>>> results = PCEAnalysis(sampler, ['a', 'b'])
>>> results.to_pd()
>>> results.describe()
"""

class AnalysisResults:
    """Contains the analysis results.

    Parameters
    ----------
    raw_data: obj
        an arbitrary object that contains raw analysis data

    samples: pandas DataFrame
        collated samples
    """
    def __init__(self, raw_data=None, samples=None):
        self.raw_data = raw_data
        self.samples = samples

    def get_sobols_first(self, qoi, input_):
        """Returns first order Sobol indices.

        Attribute
        ---------

        Returns
        -------
        a pandas DataFrame
        """
        raise NotImplementedError


    def get_sobols_total(self, qoi, input_):
        """Returns total order Sobol indices.
        
        Returns
        -------
        a pandas DataFrame
        """
        raise NotImplementedError

    def surrogate(self):
        """Returns the surrogate model as a function from parameter dictionary 
        to pandas DataFrame. This only needs to be implemented if the analysis
        method in question provides surrogate models.


        Returns
        -------
        a function that takes a dictionary of parameter - value pairs and returns
        a pandas DataFrame with the results (same output as decoder)
        """
        raise NotImplementedError


    def moments(self, groupby=None, qoi_cols=[]):
        """Returns descriprive statistics.

        Returns
        -------
        a pandas DataFrame with descriptive statistics (moments)
        """
        assert(not self.samples.empty)
        if groupby:
            grouped_data = self.samples.groupby(groupby)
            results = grouped_data.describe()
            if qoi_cols:
                results = results[qoi_cols]
        else:
            if qoi_cols:
                results = self.samples[qoi_cols].describe()
            else:
                results = self.samples.describe()
        return results
