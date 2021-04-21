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
import numpy as np
import itertools


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

    def supported_stats(self):
        raise NotImplementedError('descriptive statistics not available in this method')

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

    def _get_sobols_second(self, qoi, input_):
        """Returns second order Sobol indices.

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

    def describe(self, qoi=None, statistic=None):
        """Returns descriptive statistics.

        Examples
        --------
        >>> results.describe()
                     g                             h
                     0         1         2         0         1
        mean  0.500000  0.500000  1.000000  0.250000  0.693787
        var   0.083333  0.083333  0.166667  0.048611  0.068236
        std   0.288675  0.288675  0.408248  0.220479  0.261220
        10%   0.100897  0.099462  0.441589  0.019049  0.276504
        90%   0.896960  0.899417  1.544624  0.584600  0.974707
        min   0.000041  0.000005  0.016687  0.000016 -0.008642
        max   0.999998  0.999873  1.993517  0.985350  1.024599

        >>> result.describe('h')
                     h
                     0         1
        mean  0.250000  0.693787
        var   0.048611  0.068236
        std   0.220479  0.261220
        10%   0.019049  0.276504
        90%   0.584600  0.974707
        min   0.000016 -0.008642
        max   0.985350  1.024599

        >>> results.describe('h', 'var')
        array([0.04861111, 0.06823568])

        Parameters
        ----------
        qoi: str or None
            if not None it is the name of the quantity of interest
        statistic: str or None
            if not None it is the name of the statistic, currently supported ones
            are: ['mean', 'var', 'std', '10%', '90%', 'min', 'max', 'median']

        Returns
        -------
        pandas DataFrame or a numpy array
        """
        assert(not ((qoi is None) and (statistic is not None)))
        statistics = ['mean', 'var', 'std', '1%', '10%', '90%', '99%', 'min', 'max', 'median']
        qois = self.qois
        if qoi is not None:
            qois = [qoi]
        if statistic is not None:
            statistics = [statistic]
        result = {}
        for qoi in qois:
            for statistic_ in statistics:
                try:
                    value = self._describe(qoi, statistic_)
                    assert(isinstance(value, np.ndarray))
                    for i, x in enumerate(value):
                        try:
                            result[(qoi, i)][statistic_] = x
                        except KeyError:
                            result[(qoi, i)] = {statistic_: x}
                except NotImplementedError:
                    if statistic is not None:
                        raise RuntimeError(
                            "this statistic ({}) is not reported by this analysis class".format(statistic))
        if qois is not None and statistic is not None:
            return pd.DataFrame(result)[qoi].loc[statistic].values
        else:
            return pd.DataFrame(result)

    def plot_sobols_treemap(self, qoi, figsize=(10, 10), ax=None, filename=None, dpi=None):
        """Plot sobols first and second order indices in a hierarchical treemap format.

        Parameters
        ----------
        qoi: str
           Name of the quantity of interest.
        figsize: tuple
           A tuple with two integers representing figure size in inches.
        ax: matplotlib
           Matplotlib axis to plot on.
        filename: str
           Filename to write the plot to. If left None will display to screen.
        dpi: int
           Dots per inches. Only used when writing to file.
        """
        if qoi not in self.qois:
            raise RuntimeError("no such qoi - {}".format(qoi))
        import matplotlib.pyplot as plt
        import matplotlib._color_data as mcd
        import squarify
        sobols_first = self.sobols_first(qoi)
        keys = list(sobols_first.keys())
        values = [value[0] for value in list(sobols_first.values())]
        keys = ["{}\n{:.5f}".format(key, value) for key, value in zip(keys, values)]
        if sum(values) < 1.0:
            keys.append("higher orders\n{:.5f}".format(1.0 - sum(values)))
            values.append(1.0 - sum(values))
        colors = mcd.XKCD_COLORS
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.get_figure()
        fig.set_size_inches(figsize)
        ax.set_title("Decomposition of {} variance".format(qoi))
        squarify.plot(sizes=values, label=keys, color=colors, ax=ax, pad=True)
        ax.axis('off')
        if filename is None:
            fig.show()
        else:
            fig.savefig(filename, dpi=dpi)

    def plot_sobols_first(self, qoi, inputs=None, withdots=False,
                          ylabel=None, xlabel=None, xvalues=None,
                          filename=None, dpi=None, ax=None):
        """Plot first order sobol indices.

        Parameters
        ----------
        qoi: str
            a vector quantity of interest for which sobol indices will be plotted
        inputs: list of str or None
            list of inputs to plot if None will use all input variables
        withdots: bool
            if True will add shapes on top of the lines in the plot for visual clarity
        ylabel: str or None
            if None will use "First Order Sobol Index"
        xlabel: str or None
            if None will use the name of the qoi
        xvalues: array or None
           x-axis coordiante if None will use range(len(qoi_values))
        filename: str or None
            if None will try to open a plotting window on-screen, otherwise will write the plot to this file, with the type determined by the extension specified
        dpi: int
            dots per inch, quality of the image if a raster format was chosen
        ax: matplotlib axes object, default None
            if None, plots to a new axes, otherwise plot to existing axes ax

        Returns
        -------
        matplotlib axes object
            the actual axes plotted to
        """
        if qoi not in self.qois:
            raise RuntimeError("no such qoi - {}".format(qoi))
        if inputs is None:
            inputs = self.inputs
        for input_ in inputs:
            if input_ not in self.inputs:
                raise RuntimeError("no such input variable - {}".format(input_))
        import matplotlib.pyplot as plt
        if withdots:
            styles = itertools.cycle(['-o', '-v', '-^', '-<', '->', '-8', '-s',
                                      '-p', '-*', '-h', '-H', '-D', '-d', '-P', '-X'])
        else:
            styles = itertools.cycle(['-'])
        points = None
        for input_ in inputs:
            if points is None:
                indices = self.sobols_first(qoi, input_)
                if len(indices) < 2:
                    raise RuntimeError('this method is only implemented for vector qois')
                points = [indices]
            else:
                points.append(self.sobols_first(qoi, input_))
        if xvalues is None:
            xvalues = np.arange(len(points[0]))
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.get_figure()
        higher = np.array([1.0] * len(points[0]))
        for p, label in zip(points, inputs):
            higher -= p
            ax.plot(xvalues, p, next(styles), label=label)
        ax.plot(xvalues, higher, next(styles), label='higher orders')
        ax.grid(True)
        if ylabel is None:
            ax.set_ylabel('First Order Sobol Index')
        else:
            ax.set_ylabel(ylabel)
        if xlabel is None:
            ax.set_xlabel('x-axis')
        else:
            ax.set_xlabel(xlabel)
        ax.legend()
        if filename is not None:
            fig.savefig(filename, dpi=dpi)
        return ax

    def plot_moments(
            self,
            qoi,
            ylabel=None,
            xlabel=None,
            xvalues=None,
            alpha=0.2,
            filename=None,
            dpi=None,
            ax=None):
        """Plot statistical moments for this analysis.

        Parameters
        ----------
        qoi: str
            a vector quantity of interest for which sobol indices will be plotted
        ylabel: str or None
            if None will use "Values"
        xlabel: str or None
            if None will use the name of the qoi
        xvalues: array or None
            x-axis coordiante if None will use range(len(qoi_values)))
        alpha: float
            transparency amount
        filename: str or None
            if None will try to open a plotting window on-screen, otherwise will
            write the plot to this file, with the type determined by the extension specified
        dpi: int
            dots per inch, quality of the image if a raster format was chosen
        ax: matplotlib axes object, default None
            if None, plots to a new axes, otherwise plot to existing axes ax

        Returns
        -------
        matplotlib axes object
            the actual axes plotted to
        """
        if qoi not in self.qois:
            raise RuntimeError("no such qoi - {}".format(qoi))
        import matplotlib.pyplot as plt
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.get_figure()
        if xvalues is None:
            xvalues = np.arange(len(self.describe(qoi, 'mean')))
#        ax.fill_between(
#            xvalues, self.describe(
#                qoi, 'min'), self.describe(
#                qoi, 'max'), label='min-max', alpha=alpha)
        ax.fill_between(xvalues, self.describe(qoi, 'mean') -
                        self.describe(qoi, 'std'), self.describe(qoi, 'mean') +
                        self.describe(qoi, 'std'), label='std', alpha=alpha)
        ax.plot(xvalues, self.describe(qoi, 'mean'), label='mean')
        ax.plot(xvalues, self.describe(qoi, '1%'), '--', label='1%', color='black')
        ax.plot(xvalues, self.describe(qoi, '99%'), '--', label='99%', color='black')
        ax.grid(True)
        if ylabel is None:
            ax.set_ylabel(qoi)
        else:
            ax.set_ylabel(ylabel)
        if xlabel is None:
            ax.set_xlabel('x-axis')
        else:
            ax.set_xlabel(xlabel)
        ax.legend()
        if filename is not None:
            fig.savefig(filename, dpi=dpi)
        return ax

    def get_distribution(self, qoi):
        """Returns a distribution for the given qoi.

        Parameters
        ----------
        qoi: str
            QoI name
        
        Returns
        -------
        A ChaosPy distribution
        """
        raise NotImplementedError

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

