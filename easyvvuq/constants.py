from enum import Enum

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

# TODO: make this auto update with setup.py etc.
__easyvvuq_version__ = '0.3.dev3'

default_campaign_prefix = 'EasyVVUQ_Campaign_'


class OutputType(Enum):
    """Types of data output by UQPs/VVPs
    """

    SAMPLE = 'sample'
    ARRAY = 'array'
    SAMPLE_ARRAY = 'sample_array'
    TRACK = 'track'
    SUMMARY = 'summary'
