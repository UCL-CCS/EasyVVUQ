import os
import tempfile
from easyvvuq import Campaign
from easyvvuq import OutputType
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


# Dict to store all registered collaters (any class which extends
# BaseCollationElement is automatically registered as a collater)
AVAILABLE_COLLATERS = {}

class BaseCollationElement(BaseElement):
    """Baseclass for all EasyVVUQ collation elements.

    Parameters
    ----------
    data_src    : dict or Campaign or stream
        Information on the infomration Application information.
        Will try interpreting as a dict or JSON file/stream or filename.


    Attributes
    ----------

    """

    def __init_subclass__(cls, collater_name, **kwargs):
        """
        Catch any new collaters (all collaters must inherit from BaseCollationElement) and add them
        to the dict of available collaters.
        """
        super().__init_subclass__(**kwargs)

        cls.collater_name = collater_name

        # Register new collater
        AVAILABLE_COLLATERS[collater_name] = cls

    def collate(self):
        """
        Collates the campaign run output into a pandas dataframe.
        Must be implemented by all collation subclasses.
        """
        raise NotImplementedError

    def element_category(self):
        return "collation"

    def element_name(self):
        return self.collater_name

    @staticmethod
    def deserialize(collaterstr):
        print("Deserializing:", collaterstr)
        collaterdict = json.loads(collaterstr)
        print(collaterdict.keys())
        collater = AVAILABLE_COLLATERS[collaterdict["element_name"]](**collaterdict["state"])
        return decoder

