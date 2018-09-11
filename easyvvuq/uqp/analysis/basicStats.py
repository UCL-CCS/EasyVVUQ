import os, sys
import numpy as np
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


def basicStats(reader=None):
    if reader is None:
        sys.exit("A reader (e.g. csvReader) must be specified for the appropriate file type")

    def basicStats_specific(dirname):
        l = reader(dirname)
        mean = np.mean(l)
        std = np.std(l)

        result = {"UQP": "statsUQP", "mean": mean, "std": std}
        return result

    return statsUQP_specific
