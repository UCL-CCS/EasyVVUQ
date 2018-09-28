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
