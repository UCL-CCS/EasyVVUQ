"""A basic JSON format decoder.

Will read a JSON file and will output select values. Values have to be either
numeric or lists. In case of lists it will treat those as vector-valued quantities
of interest.
"""

import os
import logging
from easyvvuq import OutputType
import json

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


logger = logging.Logger(__name__)


class JSONDecoder:
    def __init__(self, target_filename, output_columns):
        if len(output_columns) == 0:
            msg = "output_columns cannot be empty."
            logger.error(msg)
            raise RuntimeError(msg)
        self.target_filename = target_filename
        self.output_columns = output_columns
        self.output_type = OutputType('sample')

    @staticmethod
    def _get_output_path(run_info=None, outfile=None):
        run_path = run_info['run_dir']
        if not os.path.isdir(run_path):
            raise RuntimeError(f"Run directory does not exist: {run_path}")
        return os.path.join(run_path, outfile)

    def parse_sim_output(self, run_info={}):
        def get_value(data, path):
            for node in path:
                data = data[node]
            return data
        out_path = self._get_output_path(run_info, self.target_filename)
        raw_data = self._get_raw_data(out_path)
        data = []
        for col in self.output_columns:
            try:
                if isinstance(col, str):
                    data.append((col, raw_data[col]))
                elif isinstance(col, list):
                    data.append(('.'.join(col), get_value(raw_data, col)))
            except KeyError:
                raise RuntimeError("no such field: {} in this json file".format(col))
        return dict(data)

    def _get_raw_data(self, out_path):
        with open(out_path) as fd:
            return json.load(fd)
