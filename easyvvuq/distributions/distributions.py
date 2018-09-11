import os,sys
import easyvvuq as uq
import itertools
import json
import collections
import numpy as np
from pprint import pprint

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


# Generator returning samples picked from the specified normal distribution
def normal(mean, sigma):
    while True:
        yield np.random.normal(mean, sigma)

# Generator returning values picked from the specified uniform distribution
def uniform(min_val, max_val):
    while True:
        yield np.random.uniform(min_val, max_val)
