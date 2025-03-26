"""A Decoder for CSV format files.
"""

import os
import logging
import csv
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


logger = logging.Logger(__name__)


class SimpleCSV:
    """CSV Decoder.

    Parameters
    ----------
    target_filename: str
        Filename of a CSV file to decode.
    ouput_columns: list
        A list of column names that will be selected to appear in the output.
    """

    def __init__(self, target_filename, output_columns, dialect='excel'):
        if len(output_columns) == 0:
            msg = "output_columns cannot be empty."
            logger.error(msg)
            raise RuntimeError(msg)
        self.target_filename = target_filename
        self.output_columns = output_columns
        self.output_type = OutputType('sample')
        self.dialect = dialect

    @staticmethod
    def _get_output_path(run_info=None, outfile=None):
        """Constructs absolute path from the `target_filename` and the `run_dir` parameter
        in the `run_info` retrieved from the database.

        Parameters
        ----------
        run_info: dict
            Run info as retrieved from the database.
        outfile: str
            Filename of the file to be parsed.

        Returns
        -------
        str
            An absolute path to the output file in the run directory.
        """
        run_path = run_info['run_dir']
        if not os.path.isdir(run_path):
            raise RuntimeError(f"Run directory does not exist: {run_path}")
        return os.path.join(run_path, outfile)

    def parse_sim_output(self, run_info={}):
        """Parses the CSV file and converts it to the EasyVVUQ internal dictionary based
        format. The file is parsed in such a way that each column will appear as a vector
        QoI in the output dictionary.

        For example if the file contains the following data
        a,b
        1,2
        3,4

        And both `a` and `b` are specified as `output_columns` the output will look as follows
        {'a': [1, 3], 'b': [2, 4]}.

        Parameters
        ----------
        run_info: dict
            Information about the run (used to retrieve construct the absolute path
            to the CSV file that needs decoding.
        """
        out_path = self._get_output_path(run_info, self.target_filename)
        results = {}
        for column in self.output_columns:
            results[column] = []
        with open(out_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, dialect=self.dialect)
            for row in reader:
                for column in self.output_columns:
                    try:
                        results[column].append(float(row[column]))
                    except ValueError:
                        results[column].append(row[column])
                    except KeyError:
                        raise RuntimeError('column not found in the csv file: {}'.format(column))
        return results
