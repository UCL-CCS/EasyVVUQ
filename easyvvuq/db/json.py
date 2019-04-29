import json
import logging
from easyvvuq import constants
from easyvvuq import data_structs
from .base import BaseCampaignDB

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


logger = logging.getLogger(__name__)


def convert_old_state_file(input_state):

    try:

        converted = {}

        app_info = input_state['app']
        converted['campaign'] = {}
        for field in ['campaign_dir', 'campaign_dir_prefix', 'runs_dir']:
            converted['campaign'][field] = app_info.pop(field)

        converted['app'] = app_info

        converted['runs'] = input_state.get('runs', {})

        converted['sample'] = input_state.get('sample', {})

    except KeyError as err:
        message = f'Input state not valid: {err}'
        raise IOError(message)

    return converted


def validate_input_dict(input_info, local):

    info = data_structs.CampaignInfo(**input_info, local=local)

    return info.to_dict()


class CampaignDB(BaseCampaignDB):

    def __init__(self, src=None, new_campaign=False, name=None,
                 info={}, local=False, old_style=True, db_filename=None):

        self.local = local

        self._campaign_info = {}
        self._app = {}
        self._runs = {}
        self._sample = {}

        if old_style and db_filename is None:
            message = ('Loading old_style Campaign requires db_filename to be '
                       'specified (to save database into).')
            logger.critical(message)
            raise RuntimeError(message)
        elif old_style:
            self.db_filename = db_filename
        else:
            self.db_filename = src

        if new_campaign:

            self._campaign_info = validate_input_dict(info, local)
            self._next_run = 0

        else:
            self._load_campaign(src, name)
            self._next_run = len(self._runs)

    def _load_campaign(self, src, name):

        with open(src, "r") as infile:
            input_info = json.load(infile)

        if 'campaign' not in input_info:
            try:
                input_info = convert_old_state_file(input_info)
            except IOError as err:
                message = f"State file {src} could not be read: {err}"
                logger.critical(message)
                raise RuntimeError(message)

        validate_input_dict(input_info, self.local)

        if name is not None and input_info['campaign']['name'] != name:
            message = f'No campaign called {name} found - unable to continue.'
            logger.critical(message)
            raise RuntimeError(message)

        # TODO: Add version check

        self._campaign_info = input_info['campaign']
        self._app = input_info.get('app', {})
        self._runs = input_info.get('runs', {})
        self._sample = input_info.get('sample', {})

        return

    def _save(self):

        out_dict = {
            'campaign': self._campaign_info,
            'app': self._app,
            'runs': self._runs,
            'sample': self._sample,
        }

        with open(self.db_filename, "w") as outfile:
            json.dump(out_dict, outfile, indent=4)

    def app(self, name=None):
        """
        Get app information. Note for this format (JSON/Python dict) only one
        app can be stored in the database.

        Parameters
        ----------
        name: str or None
            Name of selected app, provided for consistency with other formats -
            here will be ignored as only one app.

        Returns
        -------
        dict:
            Application information.

        """

        if name is not None:
            # TODO: Should this raise and Exception?
            message = (f'JSON/Python dictionary database can only support one '
                       f'application - ignoring selected name ({name}).')
            logger.warning(message)

        return self._app

    def campaigns(self):

        return [self._campaign_info['name']]

    def campaign_dir(self, campaign_name=None):

        if campaign_name is not None:
            # TODO: Should this raise and Exception?
            message = (
                f'JSON/Python dictionary database can only support one '
                f'application - ignoring selected name ({campaign_name}).')
            logger.warning(message)

        return self._campaign_info['campaign_dir']

    def runs(self, campaign=None, sampler=None):

        if campaign is not None or sampler is not None:
            message = (f'JSON/Python dictionary database only supports '
                       f'single campaign and sampler workflows - ignoring'
                       f'campaign - {campaign}/ sampler {sampler}')
            logger.warning(message)

        return self._runs

    def run(self, run_name, campaign=None, sampler=None):

        if campaign is not None or sampler is not None:
            message = (f'JSON/Python dictionary database only supports '
                       f'single campaign and sampler workflows - ignoring'
                       f'campaign - {campaign}/ sampler {sampler}')
            logger.warning(message)

        return self._runs[run_name]

    def runs_dir(self, campaign_name=None):

        if campaign_name is not None:
            # TODO: Should this raise and Exception?
            message = (
                f'JSON/Python dictionary database can only support one '
                f'application - ignoring selected name ({campaign_name}).')
            logger.warning(message)

        return self._campaign_info['runs_dir']

    def add_app(self, app):

        if self._app:
            message = ('JSON/Python dict database does not support '
                       'multiple apps')
            logger.critical(message)
            raise RuntimeError(message)

        info = data_structs.AppInfo(**app)

        self._app = info.to_dict()

    def add_run(self, run_config, prefix='Run_'):

        name = f"{prefix}{self._next_run}"

        # TODO: Handle fixtures

        info = data_structs.RunInfo(**run_config, run_name=name)

        self._runs[name] = info.to_dict()

        self._next_run += 1

        self._save()

    def add_sampler(self, sampler):

        if self._sample:
            message = ('JSON/Python dict database does not support '
                       'multiple samplers')
            logger.critical(message)
            raise RuntimeError(message)

        self._sample = sampler
