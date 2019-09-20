"""Provides base class for all collation elements.
"""
from easyvvuq.base_element import BaseElement
import json
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

    def collate(self, campaign, app_id):
        """
        Collates the campaign's decoded run output for the specified app.
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

    def get_collated_dataframe(self, campaign, app_id):
        """
        Returns collated data as a pandas dataframe
        """
        raise NotImplementedError

    def element_category(self):
        return "collation"

    def element_name(self):
        return self.collater_name

    @staticmethod
    def deserialize(serialized_collater):
        info = json.loads(serialized_collater)
        if not info["restartable"]:
            msg = (f'Collater {info["element_name"]} is not restartable')
            logging.error(msg)
            raise Exception(msg)

        return AVAILABLE_COLLATERS[info["element_name"]](**info["state"])

    def is_restartable(self):
        raise NotImplementedError
