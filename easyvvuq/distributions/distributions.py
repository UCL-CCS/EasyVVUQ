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


## TODO: Change to use numpy linspace
#def range_dist(param, start, end, incr):
#    i = 0
#    r = start
#    while r < end:
#        r = start + i * incr
#        i += 1
#        yield (param, r)

# Generator returning samples picked from the specified normal distribution forever
def normal(mean, sigma):
    while True:
        for pick in np.random.normal(mean, sigma, 1):
            yield pick
