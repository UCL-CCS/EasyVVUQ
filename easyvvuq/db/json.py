"""Provides class that allows access to an JSON/Python dictionary format
CampaignDB.
"""
import json
import logging
import tempfile
from easyvvuq.constants import __easyvvuq_version__
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


class CampaignDB(BaseCampaignDB):

    def __init__(self, location=None, new_campaign=False, name=None,
                 info=None):

        self._campaign_info = {}
        self._app = {}
        self._runs = {}
        self._sample = {}

        if new_campaign:

            self._campaign_info = info.to_dict()
            self._campaign_info['easyvvuq_version'] = __easyvvuq_version__
            self._next_run = 0

            if location is None:

                location = tempfile.mkstemp(suffix='json', prefix='easyvvuq')[1]
                logging.info('No database location provided - db will be saved '
                             'in {location}.')

        else:
            self._load_campaign(location, name)
            self._next_run = len(self._runs)

        self.location = location

    def _load_campaign(self, src, name):

        with open(src, "r") as infile:
            input_info = json.load(infile)

        if 'campaign' not in input_info:
            message = f"Campaign information missing from state file {src}."
            logger.critical(message)
            raise RuntimeError(message)

        if name is not None and input_info['campaign']['name'] != name:
            message = f'No campaign called {name} found - unable to continue.'
            logger.critical(message)
            raise RuntimeError(message)

        # TODO: Add version check

        self._campaign_info = input_info['campaign']
        self._app = input_info.get('app', {})
        self._runs = input_info.get('runs', {})
        self._sample = input_info.get('sample', {})

    def _save(self):

        out_dict = {
            'campaign': self._campaign_info,
            'app': self._app,
            'runs': self._runs,
            'sample': self._sample,
        }

        with open(self.location, "w") as outfile:
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

    def add_app(self, app_info):
        """
        Add application to the 'app' table.

        Parameters
        ----------
        app_info: `easyvvuq.data_structs.AppInfo`
            Application definition.

        Returns
        -------

        """

        if self._app:
            message = ('JSON/Python dict database does not support '
                       'multiple apps')
            logger.critical(message)
            raise RuntimeError(message)

        self._app = app_info.to_dict()
        self._app['id'] = 0
        self._save()

    def add_sampler(self, sampler):

        if self._sample:
            message = ('JSON/Python dict database does not support '
                       'multiple samplers')
            logger.critical(message)
            raise RuntimeError(message)

        self._sample = sampler

    def add_run(self, run_info=None, prefix='Run_'):
        """
        Add run to the `runs` table in the database.

        Parameters
        ----------
        run_info: RunInfo
            Contains relevant run fields: params, status (where in the
            EasyVVUQ workflow is this RunTable), campaign (id number),
            sample, app
        prefix: str
            Prefix for run id

        Returns
        -------

        """

        name = f"{prefix}{self._next_run}"

        this_run = run_info.to_dict()
        this_run['run_name'] = name

        self._runs[name] = this_run

        self._next_run += 1

        self._save()

    def run(self, run_name, campaign=None, sampler=None):
        """
        Get the information for a specified run.

        Parameters
        ----------
        run_name: str
            Name of run to filter for.
        campaign:  int
            Campaign id to filter for.
        sampler:
            Sample id to filter for.

        Returns
        -------
        dict
            Containing run information (run_name, params, status, sample,
            campaign, app)
        """

        if campaign is not None or sampler is not None:
            message = (f'JSON/Python dictionary database only supports '
                       f'single campaign and sampler workflows - ignoring'
                       f'campaign - {campaign}/ sampler {sampler}')
            logger.warning(message)

        return self._runs[run_name]

    def set_dir_for_run(self, run_name, run_dir, campaign=None, sampler=None):
        if campaign is not None or sampler is not None:
            message = (f'JSON/Python dictionary database only supports '
                       f'single campaign and sampler workflows - ignoring'
                       f'campaign - {campaign}/ sampler {sampler}')
            logger.warning(message)
        self._runs[run_name]['run_dir'] = run_dir

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

    def runs_dir(self, campaign_name=None):

        if campaign_name is not None:
            # TODO: Should this raise and Exception?
            message = (
                f'JSON/Python dictionary database can only support one '
                f'application - ignoring selected name ({campaign_name}).')
            logger.warning(message)

        return self._campaign_info['runs_dir']
