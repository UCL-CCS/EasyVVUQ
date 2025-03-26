"""A Decoder that can be used to get information from a YAML file.
Works identically to the JSON decoder. Look at the documentation of that
class for more information
"""

from easyvvuq.decoders.json import JSONDecoder
import logging
import yaml

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


logger = logging.Logger(__name__)


class YAMLDecoder(JSONDecoder):
    def _get_raw_data(self, out_path):
        """Reads in data from a YAML file.

        Parameters
        ----------
        out_path: str
            File name of a YAML file produced by the simulation code.
        """
        with open(out_path) as fd:
            return yaml.load(fd, yaml.SafeLoader)
