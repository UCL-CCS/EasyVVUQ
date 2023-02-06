"""A grid sampler

Useful for e.g. hyperparameter search. The "vary" dict contains the values
that must be considered per (hyper)parameter, for instance:
    
    vary = {"x1": [0.0, 0.5, 0.1],
            "x2 = [1, 3],
            "x3" = [True, False]}

The sampler will create a tensor grid using all specified 1D parameter 
values.
"""

__author__ = "Wouter Edeling"
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

from itertools import product
import numpy as np
from .base import BaseSamplingElement, Vary

class Grid_Sampler(BaseSamplingElement, sampler_name="grid_sampler"):
    
    def __init__(self, vary, count=0):
        """
        Initialize the grid sampler.

        Parameters
        ----------
        vary : dict, or list of dicts
            A dictionary containing all 1D values for each parameter. For instance
            vary = {"x1": [0.0, 0.5. 1.0], "x2": [True, False]}. This will
            create a 2D tensor product of all (x1, x2) parameter combinations.
            The tensor product points are stored in the 'points' attribute.
        count : int, optional
            Internal counter used to count the number of samples that have
            been executed. The default is 0.

        Returns
        -------
        None.

        """

        self.vary = Vary(vary)
        self.count = count

        # make sure all parameters are stored in a list or array, even
        # if they have only a single value        
        for param in vary.keys():
            if type(vary[param]) != list and type(vary[param]) != np.ndarray:
                vary[param] = [vary[param]]

        # use dtype=object to allow for multiple different type (float, boolean etc)
        self.points = np.array(list(product(*list(vary.values()))), dtype=object)

    def is_finite(self):
        return True

    def n_samples(self):
        """Returns the number of samples in this sampler.
        """
        return self.points.shape[0]

    def __next__(self):
        if self.count < self.n_samples():
            run_dict = {}
            i_par = 0
            for param_name in self.vary.get_keys():
                run_dict[param_name] = self.points[self.count][i_par]
                i_par += 1
            self.count += 1
            return run_dict
        else:
            raise StopIteration    