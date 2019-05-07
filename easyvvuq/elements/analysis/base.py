import os
import tempfile
import json
import easyvvuq.utils.json as json_utils
from pandas import DataFrame
from easyvvuq import Campaign
from easyvvuq import constants
from .. import BaseElement


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


class BaseAnalysisElement(BaseElement):
    """Baseclass for all EasyVVUQ analysis elements.

    Parameters
    ----------
    data_src    : dict or Campaign or stream
        Information on the infomration Application information.
        Will try interpreting as a dict or JSON file/stream or filename.


    Attributes
    ----------

    """

    def _apply_analysis(self):
        raise NotImplementedError

    def element_category(self):
        return "analysis"

    def apply(self, data_frame):
        # Run the element specific analysis, then log the application
        return_vals = self._apply_analysis(data_frame)

        return return_vals
