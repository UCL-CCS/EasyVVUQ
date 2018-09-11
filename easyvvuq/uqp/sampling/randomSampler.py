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


def randomSampler(campaign, num_samples=1):

    all_vars = campaign.get_vars()

    print(all_vars)

    run_dict = {}
    for i in range(num_samples):
        for param_name, dist in all_vars.items():
            run_dict[param_name] = next(dist)
        campaign.add_run(run_dict)

# Build runs
#    for dynamic_params in mega_iter:
#        run_dict = {}
#        for dp in dynamic_params:
#            key, value = dp
#            run_dict[key] = value
#        for sp in static_params:
#            key, value = sp
#            run_dict[key] = value
#
#        # Add run to Application's run list
#        campaign.add_run(run_dict)
