from .. import BaseElement
import json
import pandas as pd
import logging

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

        self.check_storage_mode(self.storagemode)

        # Set up storage
        if self.storagemode == 'memory':
           self.memory_dataframe = pd.DataFrame()
        elif self.storagemode == 'csv':
            self.csv_fname = self.campaign._campaign_dir + '/collation.csv'

    def check_storage_mode(self, mode):
        # Check requested storage mode is a recognised mode
        allowed_storage_modes = ['memory', 'csv']
        if mode not in allowed_storage_modes:
            msg = (f'storage mode "{mode}" is not in the allowed modes:'
                   f'\n{str(allowed_storage_modes)}')
            logger.critical(msg)
            raise RuntimeException(msg)

    def get_collated_dataframe(self):
        """
        Returns collated data as a pandas dataframe
        """
        if self.storagemode == 'memory':
            return self.memory_dataframe
        elif self.storagemode == 'csv':
            return df.read_csv(self.csv_fname)

    def append_data(self, new_data):
        if self.storagemode == 'memory':
            self.memory_dataframe = self.memory_dataframe.append(new_data)
        elif self.storagemode == 'csv':
            if os.path.exists(self.csv_fname):
                df.to_csv(self.csv_fname, mode='a', header=False)
            else:
                df.to_csv(self.csv_fname, mode='w', header=True)

    def element_category(self):
        return "collation"

    def element_name(self):
        return self.collater_name

    @staticmethod
    def deserialize(serialized_collater):
        info = json.loads(serialized_collater)
        print(info)
        if not info["restartable"]:
            msg = (f'Collater {info["element_name"]} is not restartable')
            logging.error(msg)
            raise Exception(msg)

        return AVAILABLE_COLLATERS[info["element_name"]](**info["state"])

    def is_restartable(self):
        restartable_modes = ['csv']
        if self.storagemode in restartable_modes:
            return True
        return False
