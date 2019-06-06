"""Provides base class for all analysis elements.
"""
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
    """Base class for all EasyVVUQ analysis elements.

    Attributes
    ----------

    """

    def analyse(self, data_frame=None):
        """Perform analysis on input `data_frame`.

        Parameters
        ----------
        data_frame : :obj:`pandas.DataFrame`
            Input data for analysis.

        Returns
        -------

        """
        raise NotImplementedError

    def element_category(self):
        """Element type for logging and verification"""
        return "analysis"

    def element_name(self):
        """Name for this element for logging purposes"""
        raise NotImplementedError

    def element_version(self):
        """Version of this element for logging purposes"""
        raise NotImplementedError
