"""Constants and Enums to set defaults and constrain selections


Attributes
----------

default_campaign_prefix : str
    Text used to ensure campaign names are identifiable and somewhat human
    readable.
"""
from enum import Enum, IntEnum

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

default_campaign_prefix = 'EasyVVUQ_Campaign_'


class OutputType(Enum):
    """
    Types of data output by UQPs/VVPs
    """

    SAMPLE = 'sample'
    ARRAY = 'array'
    SAMPLE_ARRAY = 'sample_array'
    TRACK = 'track'
    SUMMARY = 'summary'


class Status(IntEnum):
    """
    Status of runs in the Run Table
    """

    NEW = 1
    ENCODED = 2
    COLLATED = 3
    IGNORED = 4
