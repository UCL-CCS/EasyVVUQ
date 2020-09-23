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

import pandas as pd

class AnalysisResults:
    """Contains the analysis results.

    Parameters
    ----------
    raw_data: obj
        an arbitrary object that contains raw analysis data

    samples: pandas DataFrame
        collated samples
    """
    def __init__(self, raw_data=None, samples=None, qois=None, inputs=None):
        self.raw_data = raw_data
        self.samples = samples
        self.qois = qois
        self.inputs = inputs

    def get_sobols_first(self, qoi, input_):
        """Returns first order Sobol indices.

        Parameters
        ----------
        qoi - str or tuple
           Quantity of interest or if a tuple quantity of interest plus 
        coordinate index (for cases where qoi is vector valued.

        input_ - str
           Input variable name.

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

    def get_sobols_first_conf(self, qoi, input_):
        """Returns confidence intervals for first order Sobol indices.

        Attributes
        ----------
        qoi : str
            Name of the qoi for which the first order sensitivity index 
        confidence interval is requested.
        input_ : str
            Name of the input for which the first order sensitivy index
        confidence interval is requested.

        Returns
        -------
        a pandas DataFrame
        """
        raise NotImplementedError

    def get_sobols_total_conf(self, qoi, input_):
        """Returns confidence intervals for total order Sobol indices.

        Attributes
        ----------
        qoi : str
            Name of the qoi for which the first order sensitivity index 
        confidence interval is requested.
        input_ : str
            Name of the input for which the first order sensitivy index
        confidence interval is requested.

        Returns
        -------
        a pandas DataFrame
        """
        raise NotImplementedError

    def sobols_first(self):
        """Creates a pandas DataFrame with the first order sensitivity
        indices.

        The row indices are of the form (qoi, i) where qoi is the name
        of the quantity of interest and i is the coordinate index
        (will be zero for scalar qois).

        The columns indices are of the form (input, i, {low, est,
        high}) where input is the name of the input variable, i is the
        coordinate provided it is a vector quantitty and the last
        element of the 3-tuple is a string which specifies whether it
        is the estimator value for the first order sensitivity index
        or lower or higher 95% confidence interval values.

        Returns
        -------
        a pandas DataFrame

        """
        df = {}
        for qoi in self.qois:
            qoi = AnalysisResults._to_tuple(qoi)
            rows = {}
            for input_ in self.inputs:
                key = AnalysisResults._to_tuple(input_)
                key_1 = key + ('low',)
                key_2 = key + ('est',)
                key_3 = key + ('high',)
                rows[key_1] = self.get_sobols_first_conf(qoi, input_)[0]
                rows[key_2] = self.get_sobols_first(qoi, input_)
                rows[key_3] = self.get_sobols_first_conf(qoi, input_)[1]
            df[qoi] = rows
        return pd.DataFrame(df).T

    def sobols_total(self):
        """Creates a pandas DataFrame with the total order sensitivity indices.

        The row indices are of the form (qoi, i) where qoi is the name
        of the quantity of interest and i is the coordinate index
        (will be zero for scalar qois).

        The columns indices are of the form (input, i, {low, est,
        high}) where input is the name of the input variable, i is the
        coordinate provided it is a vector quantitty and the last
        element of the 3-tuple is a string which specifies whether it
        is the estimator value for the first order sensitivity index
        or lower or higher 95% confidence interval values.

        Returns
        -------
        a pandas DataFrame
        """
        df = {}
        for qoi in self.qois:
            qoi = AnalysisResults._to_tuple(qoi)
            rows = {}
            for input_ in self.inputs:
                key = AnalysisResults._to_tuple(input_)
                key_1 = key + ('low',)
                key_2 = key + ('est',)
                key_3 = key + ('high',)
                rows[key_1] = self.get_sobols_total_conf(qoi, input_)[0]
                rows[key_2] = self.get_sobols_total(qoi, input_)
                rows[key_3] = self.get_sobols_total_conf(qoi, input_)[1]
            df[qoi] = rows
        return pd.DataFrame(df).T        
        
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

    @staticmethod
    def _keys_to_tuples(dictionary):
        """Convert the keys in the dictionary to tuples.

        Parameters
        ----------
        dictionary : dict
            A dictionary with either strings or tuples as keys.

        Examples
        --------
        >>> AnalysisResults._keys_to_tuples({'a': 1, 'b': 2})
        {('a', 0): 1, ('b', 0): 2})

        >>> AnalysisResults._keys_to_tuples({('a', 0): 1, ('b', 0): 2})
        {('a', 0): 1, ('b', 0): 2})

        >>> AnalysisResults._keys_to_tuples({('a', 0): 1, 'b': 2})
        {('a', 0): 1, ('b', 0): 2})
  
        Returns
        -------
        A dictionary with tuples as keys.
        """
        new_dict = {}
        for key in dictionary.keys():
            new_dict[AnalysisResults._to_tuple(key)] = dictionary[key]
        return new_dict

    @staticmethod
    def _to_tuple(key):
        """Convert key to tuple if it is string, otherwise leave as is.

        Parameters
        ----------
        key: str or tuple

        Examples
        --------
        >>> AnalysisResults._to_tuple('a')
        ('a', 0)

        >>> AnalysisResults._to_tuple(('a', 0))
        ('a', 0)

        Returns
        -------
        Tuple if key is string, key if key is tuple.
        """
        if isinstance(key, tuple):
            return key
        elif isinstance(key, str):
            return (key, 0)
        else:
            raise RuntimeError("this method expects either a string or tuple")
