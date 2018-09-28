import numpy as np
import pandas as pd
from easyvvuq import OutputType

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

    if pivotal:

        low = 2 * value - np.percentile(dist, 100 * (1 - alpha / 2.))
        stat = value
        high = 2 * value - np.percentile(dist, 100 * (alpha / 2.))

    else:

        low = np.percentile(dist, 100 * (alpha / 2.))
        stat = np.percentile(dist, 50)
        high = np.percentile(dist, 100 * (1 - alpha / 2.))

    if low > high:
        (low, high) = (high, low)

    return stat, low, high

def bootstrap(data, stat_func=None, alpha=0.05,
              sample_size=None, n_samples=1000,
              pivotal= False):

    stat = data.apply(stat_func)

    if sample_size is None:
        sample_size = len(data)

    dist = []

    for l in range(n_samples):

        sample = data.sample(sample_size)

        dist.append(sample.apply(stat_func))

    return confidence_interval(dist, stat, alpha, pivotal=False)


def ensemble_bootstrap(data, params_cols=[], value_cols=[],
                       stat_func=None, alpha=0.05,
                       sample_size=None, n_samples=1000,
                       pivotal=False):

    agg_funcs = {}

    for col in value_cols:
        agg_funcs[col] = lambda x: bootstrap(x, stat_func=stat_func, alpha=alpha,
                                             sample_size=sample_size, n_samples=n_samples,
                                             pivotal=pivotal)

    if stat_func is None:
        stat_func = np.mean

    grouped_data = data.groupby(params_cols)

    grouped_data.agg(agg_funcs)

    outputs = ['_boot', '_high', '_low']

    results = pd.concat([grouped_data[col].apply(
                         lambda cell: pd.Series(cell, index=[col+x for x in outputs]))
                         for col in value_cols
                         ], axis=1)

    return results
