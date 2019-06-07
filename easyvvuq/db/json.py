"""Provides class that allows access to an JSON/Python dictionary format
CampaignDB.
"""
import json
import logging
import os
import pandas as pd
from .base import BaseCampaignDB
from easyvvuq.sampling.base import BaseSamplingElement
from easyvvuq.encoders.base import BaseEncoder
from easyvvuq.decoders.base import BaseDecoder
from easyvvuq.collate.base import BaseCollationElement
from easyvvuq import constants

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

        self._campaign_info = None
        self._app = None
        self._runs = {}
        self._sample = None
        self._collation_csv = None

        if new_campaign:

            self._campaign_info = info.to_dict()
            self._next_run = 0

            if location is None:
                message = f"No location given for JSON db location"
                logger.critical(message)
                raise RuntimeError(message)

            self._collation_csv = location + ".COLLATION"
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
        self._collation_csv = input_info.get('collation_csv', {})

        # Convert run statuses to enums
        for run_id in self._runs:
            self._runs[run_id]['status'] = constants.Status(self._runs[run_id]['status'])

    def _save(self):
        out_dict = {
            'campaign': self._campaign_info,
            'app': self._app,
            'runs': self._runs,
            'sample': self._sample,
            'collation_csv': self._collation_csv
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

        self._sample = sampler.serialize()

        # For JSON db, sampler ID is always 1
        return 1

    def update_sampler(self, sampler_id, sampler_element):
        if sampler_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'sampler_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        self._sample = sampler_element.serialize()
        self._save()

    def resurrect_sampler(self, sampler_id):
        if sampler_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'sampler_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        sampler = BaseSamplingElement.deserialize(self._sample)
        return sampler

    def resurrect_app(self, app_name):
        if not self._app:
            message = 'No app in JSON database'
            logger.critical(message)
            raise RuntimeError(message)

        if self._app['name'] != app_name:
            message = (f"JSON database does not contain app {app_name}"
                       f"App found was {self._app['name']}")
            logger.critical(message)
            raise RuntimeError(message)

        encoder = BaseEncoder.deserialize(self._app['input_encoder'])
        decoder = BaseDecoder.deserialize(self._app['output_decoder'])
        return encoder, decoder

    def set_campaign_collater(self, collater, campaign_id):
        if campaign_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'campaign_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        self._campaign_info['collater'] = collater.serialize()

    def resurrect_collation(self, campaign_id):
        if campaign_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'campaign_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        if self._campaign_info['collater'] is None:
            print("Loaded campaign does not have a collation element currently set")
            return None

        collater = BaseCollationElement.deserialize(self._campaign_info['collater'])
        return collater

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
            message = (
                f'JSON/Python dictionary database can only support one '
                f'application - ignoring selected name ({campaign_name}).')
            logger.warning(message)

        return self._campaign_info['campaign_dir']

    def runs(self, campaign=None, sampler=None, status=None, not_status=None):

        if campaign is not None or sampler is not None:
            message = (f'JSON/Python dictionary database only supports '
                       f'single campaign and sampler workflows - ignoring'
                       f'campaign - {campaign}/ sampler {sampler}')
            logger.warning(message)

        for run_id, run_info in self._runs.items():
            if (status is None or run_info['status'] ==
                    status) and run_info['status'] != not_status:
                yield run_id, run_info

    def get_num_runs(self, campaign=None, sampler=None, status=None, not_status=None):

        if campaign is not None or sampler is not None:
            message = (f'JSON/Python dictionary database only supports '
                       f'single campaign and sampler workflows - ignoring'
                       f'campaign - {campaign}/ sampler {sampler}')
            logger.warning(message)

        num = 0
        for run_id, run_info in self._runs.items():
            if (status is None or run_info['status'] ==
                    status) and run_info['status'] != not_status:
                num += 1
        return num

    def runs_dir(self, campaign_name=None):

        if campaign_name is not None:
            message = (
                f'JSON/Python dictionary database can only support one '
                f'application - ignoring selected name ({campaign_name}).')
            logger.warning(message)

        return self._campaign_info['runs_dir']

    def get_campaign_id(self, name):
        logger.warning("JSON database only allows for one campaign. "
                       "Campaign ID is always 1.")
        return 1

    def get_run_status(self, run_name, campaign=None, sampler=None):
        if campaign is not None:
            logger.warning("Only 1 campaign is possible in JSON db")
        if sampler is not None:
            logger.warning("Only 1 sampler is possible in JSON db")

        return constants.Status(self._runs[run_name]['status'])

    def set_run_statuses(self, run_name_list, status, campaign=None, sampler=None):
        if campaign is not None:
            logger.warning("Only 1 campaign is possible in JSON db")
        if sampler is not None:
            logger.warning("Only 1 sampler is possible in JSON db")

        for run_name in run_name_list:
            self._runs[run_name]['status'] = status
        self._save()

    def append_collation_dataframe(self, df):
        if os.path.exists(self._collation_csv):
            df.to_csv(self._collation_csv, mode='a', header=False)
        else:
            df.to_csv(self._collation_csv, mode='w', header=True)

    def get_collation_dataframe(self):
        df = pd.read_csv(self._collation_csv)
        return df
