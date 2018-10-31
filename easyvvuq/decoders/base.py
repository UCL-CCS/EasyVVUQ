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


# Dict to store all registered decoders (any class which extends BaseDecoder is automatically registered as an decoder)
available_decoders = {}

class BaseDecoder(object):
    """Baseclass for all EasyVVUQ decoders.

    Skeleton decoder which establishes the format and provides the basis of our
    contract - <need to define contract>.


    Parameters
    ----------

    Attributes
    ----------

    """

    def __init__(self, *args, **kwargs):

        self.output_type = OutputType('sample')
        self.output_columns = []

    def __init_subclass__(cls, decoder_name, **kwargs):
        """
        Catch any new decoders (all decoders must inherit from BaseDecoder) and add them
        to the dict of available decoders.
        """
        super().__init_subclass__(**kwargs)

        # Register new decoder
        available_decoders[decoder_name] = cls

    def sim_complete(self, run_info={}, *args, **kwargs):
        raise NotImplementedError

    def parse_sim_output(self, run_info={}, *args, **kwargs):
        raise NotImplementedError
