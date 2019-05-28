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

    def element_name(self):
        return "basic_stats"

    def element_version(self):
        return "0.1"

    def __init__(self, groupby=None, qoi_cols=[]):

        self.groupby = groupby
        self.qoi_cols = qoi_cols
        self.output_type = OutputType.SUMMARY

    def analyse(self, data_frame=None):

        qoi_cols = self.qoi_cols

        if data_frame is None:
            raise RuntimeError("Analysis element needs a data frame to "
                               "analyse")

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
