"""Provides baseclass for all decoders and dictionary to register all imported
decoders.

Decoders are objects which provide functions to check simulation runs have
completed and parse the output when they have.

Attributes
----------
AVAILABLE_DECODERS : dict
    Registers all imported decoders.
"""
from easyvvuq import OutputType

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


# Dict to store all registered decoders (any class which extends
# BaseDecoder is automatically registered as an decoder)
AVAILABLE_DECODERS = {}


class BaseDecoder:
    """Baseclass for all EasyVVUQ decoders.

    Skeleton decoder which establishes the format and provides the basis of our
    contract - <need to define contract>.


    Parameters
    ----------

    Attributes
    ----------

    """

    def __init_subclass__(cls, decoder_name, **kwargs):
        """
        Catch any new decoders (all decoders must inherit from BaseDecoder) and add them
        to the dict of available decoders.
        """
        super().__init_subclass__(**kwargs)

        # Register new decoder
        AVAILABLE_DECODERS[decoder_name] = cls

    def sim_complete(self, *args, run_info=None, **kwargs):
        """
        Check whether the simulation specified by `run_info` has completed and
        produced results.

        Parameters
        ----------
        run_info: dict or None
            Information defining the run to check.
        *args
            Variable length argument list.
        **kwargs
            Arbitrary keyword arguments.

        Returns
        -------

        """
        raise NotImplementedError

    def parse_sim_output(self, *args, run_info=None, **kwargs):
        """

        Parameters
        ----------
        run_info: dict or None
            Information defining the run for which we want to parse the output.
        *args
            Variable length argument list.
        **kwargs
            Arbitrary keyword arguments.

        Returns
        -------

        """
        raise NotImplementedError

    def serialize(self):
        raise NotImplementedError

    def deserialize(self):
        raise NotImplementedError
