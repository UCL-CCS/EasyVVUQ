from .. import BaseElement
import importlib
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


# Dict to store all registered samplers (any class which extends
# BaseSamplingElement is automatically registered as a sampler)
AVAILABLE_SAMPLERS = {}


class BaseSamplingElement(BaseElement):
    """Baseclass for all EasyVVUQ sampling elements.

    Attributes
    ----------
    sampler_name : str
        Name of the particular sampler.

    """

    def __init_subclass__(cls, sampler_name, **kwargs):
        """
        Catch any new samplers (all samplers must inherit from
        BaseSamplingElement) and add them to the dict of available samplers.

        Parameters
        ----------
        sampler_name : str
            Name of the particular sampler.
        """

        super().__init_subclass__(**kwargs)

        cls.sampler_name = sampler_name

        # Register new sampler
        AVAILABLE_SAMPLERS[sampler_name] = cls

    def element_category(self):
        return "sampling"

    def element_name(self):
        return self.sampler_name

    def element_version(self):
        raise NotImplementedError

    def is_finite(self):
        raise NotImplementedError

    def generate_runs(self):
        raise NotImplementedError

    @staticmethod
    def deserialize(serialized_sampler):
        """Deserialize a sampler element.

        Parameters
        ----------
        serialized_sampler : str
            Sampler serialized in JSON format.

        Returns
        -------

        """

        inputs = json.loads(serialized_sampler)

        if not inputs["restartable"]:
            msg = f'Sampler {inputs["element_name"]} is not restartable'
            logging.error(msg)
            raise Exception(msg)

        inputs["state"]["vary"] = Vary.deserialize(inputs["state"]["vary"]).vary
        sampler = AVAILABLE_SAMPLERS[inputs["element_name"]](**inputs["state"])
        return sampler


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

    def __str__(self):
        return self.vary.__str__()

    def serialize(self):
        serialized_vary = {}
        for var, dist in self.vary.items():
            serialized_vary[var] = dist.__class__.__module__
        return json.dumps(serialized_vary)

    @staticmethod
    def deserialize(serialized_vary):
        vary = json.loads(serialized_vary)
        for var, dist in vary.items():
            vary[var] = importlib.import_module(dist)
        return Vary(vary)
