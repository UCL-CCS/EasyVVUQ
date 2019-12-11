"""Provided base class for all encoders and dictionary to register all imported
encoders.

Encoders provide functions to convert generic problem space parameters lists
into inputs for particular simulation codes.

Attributes
----------
AVAILABLE_ENCODERS : dict
    Registers all imported encoders.
"""

from easyvvuq.base_element import BaseElement
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

# Dict to store all registered encoders (any class which extends
# BaseEncoder is automatically registered as an encoder)
AVAILABLE_ENCODERS = {}


class BaseEncoder(BaseElement):
    """Baseclass for all EasyVVUQ encoders.

    Skeleton encoder which establishes the format and provides the basis of our
    contract - provide an ``encode``
    method to parse these and write relevant run file to a target directory.

    Parameters
    ----------

    Attributes
    ----------

    """

    def __init_subclass__(cls, encoder_name, **kwargs):
        """
        Catch any new encoders (all encoders must inherit from BaseEncoder) and add them
        to the dict of available encoders.
        """
        super().__init_subclass__(**kwargs)

        cls.encoder_name = encoder_name

        # Register new encoder
        AVAILABLE_ENCODERS[encoder_name] = cls

    def encode(self, params=None, target_dir=''):
        """
        Takes list of generic parameter values from `params` and
        converts them into simulation input files (in `target_dir`).

        Parameters
        ----------
        params: dict or None
            Dictionary containing parameter names and values.
        target_dir: str
            Path into which output will be written.

        Returns
        -------

        """
        raise NotImplementedError

    def element_category(self):
        return "encoding"

    def element_name(self):
        return self.encoder_name

    def is_restartable(self):
        return True

    @staticmethod
    def deserialize(encoderstr):
        encoderdict = json.loads(encoderstr)
        encoder = AVAILABLE_ENCODERS[encoderdict["element_name"]](**encoderdict["state"])
        return encoder
