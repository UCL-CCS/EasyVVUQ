import os
import numpy as np
import pandas as pd
from easyvvuq import OutputType
from .base import BaseAnalysisUQP

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
              pivotal=False):

    stat = data.apply(stat_func)

    if sample_size is None:
        sample_size = len(data)

    dist = []

    for l in range(n_samples):

        sample = data.sample(sample_size)

        dist.append(sample.apply(stat_func))

    return confidence_interval(dist, stat, alpha, pivotal=pivotal)


def ensemble_bootstrap(data, params_cols=[], value_cols=[],
                       stat_func=None, alpha=0.05,
                       sample_size=None, n_samples=1000,
                       pivotal=False, stat_name='boot'):

    agg_funcs = {}

    if not value_cols:
        value_cols = [x for x in data.columns if x not in params_cols + ['run_id', 'completed']]

    if stat_func is None:
        stat_func = np.mean

    for col in value_cols:
        agg_funcs[col] = lambda x: bootstrap(x, stat_func=stat_func, alpha=alpha,
                                             sample_size=sample_size, n_samples=n_samples,
                                             pivotal=pivotal)

    grouped_data = data.groupby(params_cols)

    # Apply bootstrapping to all value columns selected
    # Note results come a tuple per cell
    results = grouped_data.agg(agg_funcs)

    outputs = [stat_name, 'high', 'low']

    # Split out tuples in each cell and provide sensible naming
    results = pd.concat({col: results[col].apply(
                                 lambda cell: pd.Series(cell, index=outputs)
                              )
                         for col in value_cols}, axis=1)

    return results


class EnsembleBoot(BaseAnalysisUQP):

    def __init__(self, data_src, params_cols=[], value_cols=[],
                 stat_func=None, alpha=0.05,
                 sample_size=None, n_boot_samples=1000,
                 pivotal=False, stat_name='boot',
                 *args, **kwargs):

        # Handles creation of `self.data_src` attribute (dict)
        super().__init__(data_src, uqp_name='ensemble_boot', *args, **kwargs)

        data_src = self.data_src

        if data_src:

            if 'files' in data_src:

                if len(data_src['files']) != 1:

                    raise RuntimeError("Data source must contain a SINGLE file path for this UQP")

                else:

                    self.data_frame = pd.read_csv(data_src['files'][0], sep='\t')

        self.value_cols = value_cols

        if self.campaign is not None:

            if not params_cols:
                self.params_cols = list(self.campaign.params_info.keys())

            self.value_cols = self.campaign.decoder.output_columns

        else:

            self.params_cols = params_cols

        self.stat_func = stat_func
        self.alpha = alpha
        self.sample_size = sample_size
        self.n_boot_samples = n_boot_samples
        self.pivotal = pivotal
        self.stat_name = stat_name

        self.output_type = OutputType.SUMMARY

    def run_analysis(self):

        if self.data_frame is None:
            raise RuntimeError("UQP needs a data frame to analyse")

        data_frame = self.data_frame
        params_cols = self.params_cols
        value_cols = self.value_cols
        stat_func = self.stat_func
        alpha = self.alpha
        sample_size = self.sample_size
        n_boot_samples = self.n_boot_samples
        pivotal = self.pivotal
        stat_name = self.stat_name
        output_dir = self.output_dir

        output_file = os.path.join(output_dir, 'ensemble_boot.tsv')

        results = ensemble_bootstrap(data_frame, params_cols=params_cols,
                                     value_cols=value_cols, stat_func=stat_func,
                                     alpha=alpha, sample_size=sample_size,
                                     n_samples=n_boot_samples, pivotal=pivotal,
                                     stat_name=stat_name)

        results.to_csv(output_file, sep='\t')
        self.output_file = output_file

        self.log_run()

        return results, output_file
