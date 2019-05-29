from .base import BaseSamplingElement, Vary
from easyvvuq import distributions
import logging
import json

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


class RandomSampler(BaseSamplingElement, sampler_name="random_sampler"):

    def __init__(self, vary=None, count=0):
        """
            Expects dict of var names, and their corresponding distributions
        """
        self.vary = Vary(vary)
        self.count = count

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return False

    def generate_runs(self) -> dict:
        while True:
            run_dict = {}
            for param_name, dist in self.vary.get_items():
                run_dict[param_name] = dist.sample(1)[0]
            self.count += 1
            yield(run_dict)

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {"vary": self.vary.serialize(), "count": self.count}
