from .base import BaseSamplingElement
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


class RandomSampler(BaseSamplingElement):

    def __init__(self, vary=None):
        """
            Expects dict of var names, and their corresponding distributions
        """

        if vary is None:
            msg = ("'vary' cannot be None. RandomSampler must be passed a "
                   "dict of the names of the parameters you want to vary, "
                   "and their corresponding distributions.")
            logging.error(msg)
            raise Exception(msg)
        if not isinstance(vary, dict):
            msg = ("'vary' must be a dictionary of the names of the "
                   "parameters you want to vary, and their corresponding "
                   "distributions.")
            logging.error(msg)
            raise Exception(msg)
        if len(vary) == 0:
            msg = "'vary' cannot be empty."
            logging.error(msg)
            raise Exception(msg)

        self.vary = vary

        # Keep track of how many samples we have drawn
        self.count = 0

    def element_name(self):
        return "random_sampler"

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return False

    def generate_runs(self) -> dict:
        while True:
            run_dict = {}
            for param_name, dist in self.vary.items():
                run_dict[param_name] = dist.sample(1)[0]
            self.count += 1
            yield(run_dict)

    def serialized_state(self):
        return json.dumps({"vary": self.vary, "count": self.count})
