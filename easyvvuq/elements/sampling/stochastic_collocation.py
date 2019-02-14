from .base import BaseSamplingElement
import numpy as np
from itertools import product

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


class SCSampler(BaseSamplingElement):

    def __init__(self, campaign):
        self.campaign = campaign
        all_vars = self.campaign.vars
        
        #get the 1D collocation points and quad weights
        xi = []
        wi = []
        for key in all_vars.keys():
            xi.append(all_vars[key]['xi_1d'])
            wi.append(all_vars[key]['wi_1d'])
        
        #turn 1d rules in a d-dimensional tensor product of collocation points
        self.xi_d, self.wi_d = self.compute_tensor_prod(xi, wi)
        self.number_of_samples = self.xi_d.shape[0]
        
        #required counter in generate_runs()
        self.counter = 0
        
        #IS THIS OKAY, OR A PROGRAMMING NO NO?
        campaign.xi_d = self.xi_d
        campaign.wi_d = self.wi_d

    def element_name(self):
        return "sc_sampler"

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return False
    
    def compute_tensor_prod(self, xi, wi):

        """
        tensor products for colloc point and weights 
        """
        
        #full d-dimensional tensor product
        xi_d = np.array(list(product(*xi)))
        wi_d = np.array(list(product(*wi)))
    
        return xi_d , wi_d

    #SC collocations points are not random, generate_runs simply returns
    #one collocation point from the tensor product after the other
    def generate_runs(self):
        all_vars = self.campaign.vars

        while True:        
            idx = 0

            run_dict = {}
            for key in all_vars.keys():
                run_dict[key] = self.xi_d[self.counter][idx]
                idx += 1
            self.counter += 1
            yield run_dict