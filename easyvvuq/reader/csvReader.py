import os, sys
import csv

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


# Extracts the specified column from the specified csv file. Returns it as a list. Ignores comment lines.
def csvReader(fname, column):
    def csvReaderSpecific(dirname):
        full_path = os.path.join(dirname, fname)
        ret = []
        with open(full_path, "r") as infile:
            csvreader = csv.reader(infile)
            for row in csvreader:
                if '#' in row[0]: # skip comment line
                    continue
                ret.append(float(row[column]))
        return ret

    return csvReaderSpecific
