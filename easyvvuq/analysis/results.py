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

    all_analysis_methods = []
    implemented = []

    def __init__(self, raw_data=None, samples=None, qois=None, inputs=None):
        self.raw_data = raw_data
        self.samples = samples
        self.qois = qois
        self.inputs = inputs

    def __getattr__(self, attr):
        if attr in self.all_analysis_methods:
            raise RuntimeError(
                "analysis results method '{}' is not implement in '{}',\
                 implemented methods are {}".format(
                    attr, self.__class__.__name__, self.implemented))
        else:
            raise AttributeError(
                "type object '{}' has no attribute '{}'".format(self.__class__.__name__, attr))

    def implemented(self):
        """Returns a list of implemented functionality.

        Returns
        -------
        a list of str
           names of types of analysis results that are implemented
           for this method
        """
        return []

    def _get_sobols_first(self, qoi, input_):
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

    def _get_sobols_total(self, qoi, input_):
        """Returns total order Sobol indices.

        Returns
        -------
        a pandas DataFrame
        """
        raise NotImplementedError

    def _get_sobols_first_conf(self, qoi, input_):
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

    def _get_sobols_total_conf(self, qoi, input_):
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

    def _get_sobols_general(self, getter, qoi=None, input_=None):
        """A generic method for getting sobol indices.

        Parameters
        ----------
        getter: function
             Method that takes a AnalysisResults instance and returns
             a Sobol index of some kind. For example _get_bonols_first.

        qoi: str or tuple
            The name of the quantity of interest or None.
            Use a tuple of the form (qoi, index) where index is integer
            that means the coordinate index of a vector qoi.

        input_: str
            The name of the input parameter or None.

        Returns
        -------
        a dictionary or an array
        """
        assert(not ((qoi is None) and (input_ is not None)))
        if (qoi is not None) and (qoi not in self.qois):
            raise RuntimeError('no such qoi in this analysis')
        if (input_ is not None) and (input_ not in self.inputs):
            raise RuntimeError('no such input variable in this analysis')
        try:
            if input_ is None:
                if qoi is None:
                    return dict([(qoi_, dict([(in_, getter(qoi_, in_))
                                              for in_ in self.inputs]))
                                 for qoi_ in self.qois])
                else:
                    return dict([(in_, getter(qoi, in_))
                                 for in_ in self.inputs])
            else:
                return getter(qoi, input_)
        except NotImplementedError:
            raise RuntimeError(
                'this kind of sobol index reporting not implemented in this analysis method')

    def sobols_first(self, qoi=None, input_=None):
        """Return first order sensitivity indices.

        Parameters
        ----------
        qoi: str or tuple
            The name of the quantity of interest or None.
            Use a tuple of the form (qoi, index) where index is integer
            that means the coordinate index of a vector qoi.

        input_: str
            The name of the input parameter or None.

        Examples
        --------
        >>> results.sobols_first()
        {'f': {'x1': array([0.610242]), 'x2': array([0.26096511])}}
        >>> results.sobols_first('f')
        {'x1': array([0.610242]), 'x2': array([0.26096511])}
        >>> results.sobols_first('f', 'x1')
        array([0.610242])
        >>> results_vectors.sobols_first(('g', 2))
        {'x1': array([0.5]), 'x2': array([0.5])}

        Returns
        -------
        a dictionary or an array
        """
        return self._get_sobols_general(self._get_sobols_first, qoi, input_)

    def sobols_second(self, qoi=None, input_=None):
        """Return second order sensitivity indices.

        Parameters
        ----------
        qoi: str or tuple
            The name of the quantity of interest or None.
            Use a tuple of the form (qoi, index) where index is integer
            that means the coordinate index of a vector qoi.

        input_: str
            The name of the input parameter or None.

        Examples
        --------

        Returns
        -------
        a dictionary or an array
        """
        return self._get_sobols_general(self._get_sobols_second, qoi, input_)

    def sobols_total(self, qoi=None, input_=None):
        """Returns total order sensitivity indices.

        Parameters
        ----------
        qoi: str or tuple
            The name of the quantity of interest or None.
            Use a tuple of the form (qoi, index) where index is integer
            that means the coordinate index of a vector qoi.

        input_: str
            The name of the input parameter or None.


        Examples
        --------

        Returns
        -------
        a dictionary or an array
        """
        return self._get_sobols_general(self._get_sobols_total, qoi, input_)

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

    def describe(self, groupby=None, qoi_cols=[], percentiles=[0.1, 0.5, 0.9]):
        """Returns descriptive statistics.

        Examples
        --------
        >>> results.moments()
                   run_id          x1          x2           f
        count  400.000000  400.000000  400.000000  400.000000
        mean   199.500000    0.466909    0.469184    1.018103
        std    115.614301    0.290085    0.292512    0.775780
        min      0.000000    0.005779    0.003853    0.017025
        25%     99.750000    0.208518    0.201850    0.351034
        50%    199.500000    0.471223    0.449555    0.882288
        75%    299.250000    0.724372    0.686953    1.548116
        max    399.000000    0.984971    0.998398    3.152954

        Returns
        -------
        a pandas DataFrame with descriptive statistics
        """
        assert(not self.samples.empty)
        if groupby:
            grouped_data = self.samples.groupby(groupby)
            results = grouped_data.describe(percentiles=percentiles)
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
