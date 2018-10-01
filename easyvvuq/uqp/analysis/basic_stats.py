import os
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


class BasicStats(BaseAnalysisUQP):

    def __init__(self, data_src, params_cols=[], value_cols=[],
                 *args, **kwargs):

        # TODO: Fix this to allow more flexibility - basically pass through
        # available options to `pd.DataFrame.describe()`

        self.uqp_name = 'basic_stats'

        # Handles creation of `self.data_src` attribute (dict)
        super().__init__(data_src, uqp_name=self.uqp_name, *args, **kwargs)

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

        self.output_type = OutputType.SUMMARY

    def run_analysis(self):

        if self.data_frame is None:
            raise RuntimeError("UQP needs a data frame to analyse")

        df = self.data_frame

        output_dir = self.output_dir
        output_file = os.path.join(output_dir, 'basic_stats.tsv')

        grouped_data = df.groupby(self.params_cols)

        # Apply bootstrapping to all value columns selected
        # Note results come a tuple per cell
        results = grouped_data.describe()
        results.to_csv(output_file, sep='\t')

        self.output_file = output_file

        self.log_run()

        return results, output_file
