"""Provides analysis element for basic statistical analysis.

The analysis is based on `pandas.DataFrame.describe()` function.
"""
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


class BasicStats(BaseAnalysisElement):

    def __init__(self, groupby=None, qoi_cols=None):
        """Element to calculate basic stats for `qoi_cols` values.

        This results in values for: count, mean, std, min, max and 25%, 50% &
        75% percentiles for each value in the analysis.

        Parameters
        ----------
        groupby : list or None
            Columns to use to group the data in `analyse` method before
            calculating stats.
        qoi_cols : list or None
            Columns of quantities of interest (for which stats will be
            calculated).
        """
        self.groupby = groupby
        if qoi_cols is not None:
            self.qoi_cols = qoi_cols
        else:
            self.qoi_cols = []
        self.output_type = OutputType.SUMMARY

    def element_name(self):
        """Name for this element for logging purposes"""
        return "basic_stats"

    def element_version(self):
        """Version of this element for logging purposes"""
        return "0.1"

    def analyse(self, data_frame=None):
        """Perform the basis stats analysis on the input `data_frame`.

        Analysis is based on `pandas.Dataframe.describe` and results in
        values for: count, mean, std, min, max and 25%, 50% & 75% percentiles
        for each value in the analysis.

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

        qoi_cols = self.qoi_cols

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")
        elif data_frame.empty:
            raise RuntimeError(
                "No data in data frame passed to analyse element")

        # Get summary statistics
        if self.groupby:
            grouped_data = data_frame.groupby(self.groupby)
            results = grouped_data.describe()
            if qoi_cols:
                results = results[qoi_cols]

        else:
            if qoi_cols:
                results = data_frame[qoi_cols].describe()
            else:
                results = data_frame.describe()

        return results
