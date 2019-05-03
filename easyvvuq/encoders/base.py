"""Base class for all encoders and dictionary to register all imported encoders

Encoders provide functions to convert generic problem space parameters lists
into inputs for particular simulation codes.

Attributes
----------
AVAILABLE_ENCODERS : dict
    Registers all imported encoders.
"""
import easyvvuq.utils.json as json_utils
from easyvvuq.utils import fixtures

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

# Dict to store all registered encoders (any class which extends
# BaseEncoder is automatically registered as an encoder)
AVAILABLE_ENCODERS = {}


class BaseEncoder:
    """Baseclass for all EasyVVUQ encoders.

    Skeleton encoder which establishes the format and provides the basis of our
    contract - provide an ``encode``
    method to parse these and write relevant run file to a target directory.

    TODO: If we end up converting Attributes to Properties with ``@property``
    of Kristof style ``@advanced_property`` decorators then they should be
    documented in the property's getter method.

    Parameters
    ----------

    Attributes
    ----------

    """

    def __init_subclass__(cls, encoder_name, **kwargs):
        """
        Catch any new encoders (all encoders must inherit from BaseEncoder) and add them
        to the dict of available encoders.
        """
        super().__init_subclass__(**kwargs)

        # Register new encoder
        AVAILABLE_ENCODERS[encoder_name] = cls

    def encode(self, params=None, target_dir=''):
        """
        Takes list of generic parameter values from `params` and
        converts them into simulation input files (in `target_dir`).

        Parameters
        ----------
        params: dict or None
            Dictionary containing parameter names and values.
        target_dir: str
            Path into which output will be written.

        Returns
        -------

        """
        raise NotImplementedError

    def serialize(self):
        raise NotImplementedError

    def deserialize(self):
        raise NotImplementedError

    @staticmethod
    def parse_fixtures_params(info, target_dir, path_depth=0):
        """
        Interpret a dictionary of run information to covert the 'fixtures' sub-
        dictionary to paths of files relative to `target_dir` or a directory
        `path_depth` beneath this.

        Notes
        -----
            Use case `path_depth` is e.g. NAMD where the file paths in the input
            must be relative to where the configuration input file is stored
            rather than where the executable is run from.

        Parameters
        ----------
        info: dict
            Run information dictionary.
        target_dir: str
            Path into which input files will be written for the run.
        path_depth: int
            Depth beneath `target_dir` to which fixture paths must be relative.

        Returns
        -------
        dict
            Updated version of input dictionary with parameters replaced with
            fixture paths where relevant.

        """

        fixture_list = info.get('fixtures', {})

        if fixture_list:
            for key, current_fixture in fixture_list.items():

                path = current_fixture['path']

                is_dir = bool(current_fixture['type'] == 'dir')

                common = current_fixture['common']
                exists_local = current_fixture['exists_local']
                target_name = current_fixture['target']
                group = current_fixture['group']

                tmp_fixture = fixtures.Fixture(
                    path,
                    is_dir=is_dir,
                    common=common,
                    exists_local=exists_local,
                    target_name=target_name,
                    group=group)

                info[key] = tmp_fixture.fixture_path(depth_in_run=path_depth)
                tmp_fixture.copy_to_target(target_dir=target_dir)

        return info
