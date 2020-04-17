import sys
from .constants import OutputType
from . import data_structs
from .params_specification import ParamsSpecification
from .campaign import Campaign
from .campaign_dask import CampaignDask
from .worker import Worker
from . import actions
from . import encoders
from . import decoders
from .base_element import BaseElement
from . import sampling
from . import analysis
from . import comparison

# First make sure python version is 3.6+
assert sys.version_info >= (3, 6), (f"Python version must be >= 3.6,"
                                    f"found {sys.version_info}")

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

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
