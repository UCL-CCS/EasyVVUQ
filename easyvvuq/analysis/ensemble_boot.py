"""Provides analysis element for ensemble bootstrapping analysis.
"""
import numpy as np
import pandas as pd
from easyvvuq import OutputType
from .base import BaseAnalysisElement

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


def confidence_interval(dist, value, alpha, pivotal=False):
    """
    Get the bootstrap confidence interval for a given distribution.

    Parameters
    ----------
    dist:
        Array containing distribution of bootstrap results.
    value:
        Value of statistic for which we are calculating error bars.
    alpha:
        The alpha value for the confidence intervals.
    pivotal:
        Use the pivotal method? Default to percentile method.

    Returns
    -------

    float:
          Value of the bootstrap statistic
    float:
          Highest value of the confidence interval
    float:
          Lowest value of the confidence interval

    """
    if len(dist) < 1:
        raise ValueError("Dist array should be non-empty")

    if pivotal:

        low = 2 * value - np.percentile(dist, 100 * (1 - alpha / 2.), axis=0)
        stat = value
        high = 2 * value - np.percentile(dist, 100 * (alpha / 2.), axis=0)

    else:

        low = np.percentile(dist, 100 * (alpha / 2.), axis=0)
        stat = np.percentile(dist, 50)
        high = np.percentile(dist, 100 * (1 - alpha / 2.), axis=0)

    # if low > high:
    #     (low, high) = (high, low)

    return stat, low, high


def bootstrap(data, stat_func, alpha=0.05,
              sample_size=None, n_samples=1000,
              pivotal=False):
    """

    Parameters
    ----------
    data : :obj:`pandas.DataFrame`
        Input data to be analysed.
    stat_func : function
        Statistical function to be applied to data for bootstrapping.
    alpha : float
        Produce estimate of 100.0*(1-`alpha`) confidence interval.
    sample_size : int
        Size of the sample to be drawn from the input data.
    n_samples : int
        Number of times samples are to be drawn from the input data.
    pivotal : bool
        Use the pivotal method? Default to percentile method.

    Returns
    -------
    float:
          Value of the bootstrap statistic
    float:
          Highest value of the confidence interval
    float:
          Lowest value of the confidence interval
    """
    if data.empty:
        raise RuntimeError("DataFrame passed to bootstrap has to be non-empty")

    stat = data.apply(stat_func)

    if sample_size is None:
        sample_size = len(data)

    dist = []

    for l in range(n_samples):

        sample = data.sample(sample_size, replace=True)

        dist.append(stat_func(sample))

    return confidence_interval(dist, stat, alpha, pivotal=pivotal)


def ensemble_bootstrap(data, groupby=[], qoi_cols=[],
                       stat_func=np.mean, alpha=0.05,
                       sample_size=None, n_samples=1000,
                       pivotal=False, stat_name='boot'):
    """
    Perform bootstrapping analysis on input data.

    Parameters
    ----------
    data : :obj:`pandas.DataFrame`
        Date to be analysed.
    groupby : list or None
        Columns to use to group the data in `analyse` method before
        calculating stats.
    qoi_cols : list or None
        Columns of quantities of interest (for which stats will be
        calculated).
    stat_func : function
        Statistical function to be applied to data for bootstrapping.
    alpha : float, default=0.05
        Produce estimate of 100.0*(1-`alpha`) confidence interval.
    sample_size : int
        Size of the sample to be drawn from the input data.
    n_samples : int, default=1000
        Number of times samples are to be drawn from the input data.
    pivotal : bool, default=False
        Use the pivotal method? Default to percentile method.
    stat_name : str, default='boot'
        Name to use to describe columns containing output statistic (for example
        'mean').

    Returns
    -------
    :obj:`pandas.DataFrame`
        Description of input data using bootstrap statistic and high/low
        confidence intervals.
    """

    agg_funcs = {}

    if not qoi_cols:
        qoi_cols = [
            x for x in data.columns if x not in groupby + ['run_id', 'status']]

    for col in qoi_cols:
        if col not in data:
            raise RuntimeError(f"No such attribute: {col}\nAttributes found in data: {data}")
        agg_funcs[col] = lambda x: bootstrap(
            x,
            stat_func=stat_func,
            alpha=alpha,
            sample_size=sample_size,
            n_samples=n_samples,
            pivotal=pivotal)

    if not groupby:
        grouped_data = data.groupby(lambda x: True, sort=False)
    else:
        grouped_data = data.groupby(groupby, sort=False)

    # Apply bootstrapping to all value columns selected
    # Note results come a tuple per cell
    results = grouped_data.agg(agg_funcs)

    outputs = [stat_name, 'low', 'high']

    # Split out tuples in each cell and provide sensible naming
    results = pd.concat({col: results[col].apply(
        lambda cell: pd.Series(cell, index=outputs)
    )
        for col in qoi_cols}, axis=1)

    return results


class EnsembleBoot(BaseAnalysisElement):

    def __init__(self, groupby=[], qoi_cols=[],
                 stat_func=np.mean, alpha=0.05,
                 sample_size=None, n_boot_samples=1000,
                 pivotal=False, stat_name='boot'):
        """
        Element to perform bootstrapping on collated simulation output.

        Parameters
        ----------
        groupby : list or None
            Columns to use to group the data in `analyse` method before
            calculating stats.
        qoi_cols : list or None
            Columns of quantities of interest (for which stats will be
            calculated).
        stat_func : function
            Statistical function to be applied to data for bootstrapping.
        alpha : float, default=0.05
            Produce estimate of 100.0*(1-`alpha`) confidence interval.
        sample_size : int
            Size of the sample to be drawn from the input data.
        n_boot_samples : int, default=1000
            Number of times samples are to be drawn from the input data.
        pivotal : bool, default=False
            Use the pivotal method? Default to percentile method.
        stat_name : str, default='boot'
            Name to use to describe columns containing output statistic (for example
            'mean').
        """

        self.groupby = groupby
        self.qoi_cols = qoi_cols

        self.stat_func = stat_func
        self.alpha = alpha
        self.sample_size = sample_size
        self.n_boot_samples = n_boot_samples
        self.pivotal = pivotal
        self.stat_name = stat_name

        self.output_type = OutputType.SUMMARY

        if self.stat_func is None:
            raise ValueError('stat_func cannot be None.')

    def element_name(self):
        """Name for this element for logging purposes"""
        return "ensemble_boot"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.1"

    def analyse(self, data_frame=None):
        """Perform bootstrapping analysis on the input `data_frame`.

        The data_frame is grouped according to `self.groupby` if specified and
        analysis is performed on the columns selected in `self.qoi_cols` if set.

        Parameters
        ----------
        data_frame : :obj:`pandas.DataFrame`
            Summary data produced through collation of simulation output.

        Returns
        -------
        :obj:`pandas.DataFrame`
            Basic statistic for selected columns and groupings of data.
        """

        if data_frame is None:
            raise RuntimeError(
                "This VVUQ element needs a data frame to analyse")
        elif data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        results = ensemble_bootstrap(
            data_frame,
            groupby=self.groupby,
            qoi_cols=self.qoi_cols,
            stat_func=self.stat_func,
            alpha=self.alpha,
            sample_size=self.sample_size,
            n_samples=self.n_boot_samples,
            pivotal=self.pivotal,
            stat_name=self.stat_name)

        return results
