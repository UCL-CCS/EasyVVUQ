from .. import BaseElement
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


class BaseSamplingElement(BaseElement):
    """Baseclass for all EasyVVUQ sampling elements.

    Attributes
    ----------

    """

    def element_category(self):
        return "sampling"

    def element_name(self):
        raise NotImplementedError

    def element_version(self):
        raise NotImplementedError

    def is_finite(self):
        raise NotImplementedError

    def generate_runs(self):
        raise NotImplementedError

    @staticmethod
    def deserialize(samplerdict):
        print("Deserializing:", samplerdict)
        if samplerdict["element_name"] == "random_sampler":
            return RandomSampler()
        return None


class Vary:
    def __init__(self, vary):
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

    def get_items(self):
        return self.vary.items()

    def serialize(self):
        serialized_vary = {}
        for var, dist in self.vary.items():
            serialized_vary[var] = dist.__class__.__module__
        return json.dumps(serialized_vary)

    @staticmethod
    def deserialize():
        pass
