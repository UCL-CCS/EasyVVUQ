from .. import BaseElement
import json
import pandas as pd

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

    Attributes
    ----------
    collater_name : str
        Name of particular collation element.

    """

    def collate(self, campaign):
        """
        Collates the campaign's decoded run output.
        Must be implemented by all collation subclasses.
        """
        raise NotImplementedError

    def __init_subclass__(cls, collater_name, **kwargs):
        """
        Catch any new collaters (all collaters must inherit from
        BaseCollationElement) and add them to the dict of available collaters.

        Parameters
        ----------
        collater_name : str
            Name of the collater element represented by the class.

        """
        super().__init_subclass__(**kwargs)

        cls.collater_name = collater_name

        # Register new collater
        AVAILABLE_COLLATERS[collater_name] = cls

    def __init__(self, storagemode=None):
        self.storagemode = storagemode

        # Check requested storage mode is a recognised mode
        allowed_storage_modes = ['memory', 'campaigndb']
        if self.storagemode not in allowed_storage_modes:
            msg = (f'storage mode "{self.storagemode}" is not in the allowed modes:'
                   f'\n{str(allowed_storage_modes)}')
            logger.critical(msg)
            raise RuntimeException(msg)

        # Set up storage
        if self.storagemode == 'memory':
           self.memory_dataframe = pd.DataFrame()

    def get_collated_dataframe(self):
        """
        Returns collated data as a pandas dataframe
        """
        if self.storagemode == 'memory':
            return self.memory_dataframe

    def append_data(self, new_data):
        if self.storagemode == 'memory':
            self.memory_dataframe = self.memory_dataframe.append(new_data)

    def element_category(self):
        return "collation"

    def element_name(self):
        return self.collater_name

    @staticmethod
    def deserialize(serialized_collater):
        info = json.loads(serialized_collater)

        return AVAILABLE_COLLATERS[info["element_name"]](**info["state"])

    def is_restartable(self):
        restartable_modes = ['csv']
        if self.storagemode in restartable_modes:
            return True
        return False
