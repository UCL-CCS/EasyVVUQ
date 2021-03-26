import os
import logging
import csv
from easyvvuq import OutputType
from .base import BaseDecoder

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


class SimpleCSV(BaseDecoder, decoder_name="csv"):

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

    def sim_complete(self, run_info=None):

        out_path = self._get_output_path(run_info, self.target_filename)

        if not os.path.isfile(out_path):
            return False
        else:
            return True

    def parse_sim_output(self, run_info={}):

        out_path = self._get_output_path(run_info, self.target_filename)

        results = {}
        for column in self.output_columns:
            results[column] = []

        with open(out_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for column in self.output_columns:
                    try:
                        results[column].append(float(row[column]))
                    except ValueError:
                        results[column].append(row[column])
                    except KeyError:
                        raise RuntimeError('column not found in the csv file: {}'.format(column))

        return results
