import os
from .base import BaseEncoder
import logging
import easyvvuq.utils as utils

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


class ApplyFixtures(BaseEncoder, encoder_name="apply_fixtures"):
    """ An encoder to copy/transfer files (as specified by 'fixtures' params)

    Parameters
    ----------

    Attributes
    ----------

    """

    def __init__(self, fixtures=None):
        self.fixtures = fixtures

    def encode(self, params={}, target_dir=''):

        if self.fixtures is not None:
            local_params = self.substitute_fixtures_params(params, self.fixtures, target_dir)
        else:
            local_params = params

    def substitute_fixtures_params(params, fixtures, target_dir, path_depth=0):

        fixed_params = dict(params)

        for key, current_fixture in fixtures.items():

            if current_fixture['type'] == 'dir':
                is_dir = True
            else:
                is_dir = False

            fix = utils.fixture.Fixture(
                current_fixture['path'],
                is_dir=is_dir,
                common=current_fixture['common'],
                exists_local=current_fixture['exists_local'],
                target_name=current_fixture['target'],
                group=current_fixture['group'])

            fixed_params[key] = fix.fixture_path(depth_in_run=path_depth)
            fix.copy_to_target(target_dir=target_dir)

        return fixed_params

    def get_restart_dict(self):
        return {"fixtures": self.fixtures}

    def element_version(self):
        return "0.1"
