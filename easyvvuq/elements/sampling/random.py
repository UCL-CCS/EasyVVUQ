from .base import BaseSamplingElement

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


class RandomSampler(BaseSamplingElement):

    def __init__(self, campaign):
        self.campaign = campaign

    def element_name(self):
        return "random_sampler"

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return False

    def generate_runs(self):
        all_vars = self.campaign.vars
        while True:
            run_dict = {}
            for param_name, dist in all_vars.items():
                run_dict[param_name] = next(dist)
            yield(run_dict)
