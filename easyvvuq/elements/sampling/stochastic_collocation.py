from .base import BaseSamplingElement
import numpy as np
import chaospy as cp
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

    def __init__(self, campaign, polynomial_order=4, quadrature_rule="G"):

        self.campaign = campaign
        self.all_vars = self.campaign.vars

        # The probality distributions of uncertain parameters
        params_distribution = list(self.all_vars.values())

        # Multivariate distribution
        joint = cp.J(*params_distribution)

        xi_d, _ = cp.generate_quadrature(
            polynomial_order, joint, rule=quadrature_rule)

        self.xi_d = xi_d.T

        self.number_of_samples = self.xi_d.shape[0]

#        # required counter in generate_runs()
        self.counter = 0

    def element_name(self):
        return "sc_sampler"

    def element_version(self):
        return "0.2"

    def is_finite(self):
        return False

    # SC collocations points are not random, generate_runs simply returns
    # one collocation point from the tensor product after the other
    def generate_runs(self):
        #all_vars = self.campaign.vars

        while True:
            idx = 0

            run_dict = {}
            for key in self.all_vars.keys():
                run_dict[key] = self.xi_d[self.counter][idx]
                idx += 1
            self.counter += 1
            yield run_dict
