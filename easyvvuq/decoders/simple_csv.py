import os
import pandas as pd
from .base import BaseDecoder
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


class SimpleCSV(BaseDecoder, decoder_name = "csv"):

    def __init__(self, *args, **kwargs):

        # Handles creation of `self.app_info` attribute (dicts)
        super().__init__(*args, **kwargs)

        self.output_type = OutputType('sample')


    @staticmethod
    def _get_output_path(run_info={}, *args, **kwargs):

        run_path = run_info['run_dir']

        if 'output_filename' in kwargs:
            out_file = kwargs['output_filename']
        else:
            raise RuntimeError('A value for "output_columns" must be '
                               'specified for the simple encoder')

        if not os.path.isdir(run_path):
            raise RuntimeError(f"Run directory does not exist: {run_path}")

        return os.path.join(run_path, out_file)

    def sim_complete(self, run_info={}, *args, **kwargs):

        out_path = self._get_output_path(run_info, *args, **kwargs)

        if not os.path.isfile(out_path):
            return False
        else:
            return True

    def parse_sim_output(self, run_info={}, *args, **kwargs):

        out_path = self._get_output_path(run_info, *args, **kwargs)

        if 'output_columns' in kwargs:
            self.output_columns = kwargs['output_columns']
        else:
            raise RuntimeError('A value for "names" must be '
                               'specified for the simple encoder')

        # Remove 'output_filename' and 'output_columns' from the kwargs before passing to pandas read_csv
        # (as these are clearly going to be rejected by pandas)
        del kwargs['output_filename']
        del kwargs['output_columns']

        data = pd.read_csv(out_path, names=self.output_columns, **kwargs)

        return data
