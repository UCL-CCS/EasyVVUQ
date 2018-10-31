import easyvvuq.utils.json as json_utils

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

# Dict to store all registered encoders (any class which extends BaseEncoder is automatically registered as an encoder)
available_encoders = {}

class BaseEncoder(object):
    """Baseclass for all EasyVVUQ encoders.

    Skeleton encoder which establishes the format and provides the basis of our
    contract - take in ``app_info`` and provide an ``encode``
    method to parse these and write relevant run file to a target directory.

    TODO: If we end up converting Attributes to Properties with ``@property``
    of Kristof style ``@advanced_property`` decorators then they should be
    documented in the property's getter method.

    Parameters
    ----------
    app_info    : dict, optional
        Application information. Will try interpreting as a dict or JSON
        file/stream or filename.

    Attributes
    ----------
    app_info    : dict
        Contains application information.

    """

    def __init__(self, app_info, *args, **kwargs):
        if not hasattr(app_info, 'items'):
            self.app_info = json_utils.process_json(app_info)
        else:
            self.app_info = app_info

    def __init_subclass__(cls, encoder_name, **kwargs):
        """
        Catch any new encoders (all encoders must inherit from BaseEncoder) and add them
        to the dict of available encoders.
        """
        super().__init_subclass__(**kwargs)
        print(f"Called __init_subclass({cls}, {encoder_name})")

        # Register new encoder
        available_encoders[encoder_name] = cls

    def encode(self, params={}, target_dir=''):
        raise NotImplementedError


