from easyvvuq.base_element import BaseElement
import logging
import json
import jsonpickle

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

    def n_samples(self):
        raise NotImplementedError

    def __iter__(self):
        """
        This method allows the sampler to be used as an iterator.
        The campaign object's draw_samples() method uses samplers
        in that manner.
        """
        return self

    def __next__(self):
        """
        This must be implemented by any sampler class.
        It should return the next run in the sequence.
        In the case of a finite sampler, when there are
        no more runs remaining, __next__() should
        raise a StopIteration exception
        """
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

        if 'vary' in inputs["state"]:
            inputs["state"]["vary"] = Vary.deserialize(inputs["state"]["vary"]).vary_dict

        sampler = AVAILABLE_SAMPLERS[inputs["element_name"]](**inputs["state"])
        return sampler


class Vary:
    def __init__(self, vary_dict):
        if vary_dict is None:
            msg = ("'vary_dict' cannot be None. RandomSampler must be passed a "
                   "dict of the names of the parameters you want to vary, "
                   "and their corresponding distributions.")
            logging.error(msg)
            raise Exception(msg)
        if not isinstance(vary_dict, dict):
            msg = ("'vary_dict' must be a dictionary of the names of the "
                   "parameters you want to vary, and their corresponding "
                   "distributions.")
            logging.error(msg)
            raise Exception(msg)
        if len(vary_dict) == 0:
            msg = "'vary_dict' cannot be empty."
            logging.error(msg)
            raise Exception(msg)

        self.vary_dict = vary_dict

    def get_items(self):
        return self.vary_dict.items()

    def get_values(self):
        return self.vary_dict.values()

    def get_keys(self):
        return self.vary_dict.keys()

    def __str__(self):
        return self.vary_dict.__str__()

    def serialize_distribution(self, dist):
        return jsonpickle.encode(dist)

    @staticmethod
    def deserialize_distribution(sdist):
        return jsonpickle.decode(sdist)

    def serialize(self):
        serialized_vary = {}
        for var, dist in self.vary_dict.items():
            serialized_vary[var] = self.serialize_distribution(dist)

        return json.dumps(serialized_vary)

    @staticmethod
    def deserialize(serialized_vary):
        vary = json.loads(serialized_vary)
        for var, sdist in vary.items():
            vary[var] = Vary.deserialize_distribution(sdist)

        return Vary(vary)
