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
from easyvvuq import ParamsSpecification

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

    def __init__(self, location=None, new_campaign=False, name=None, info=None):

        self._campaign_info = None
        self._app = None
        self._runs = {}
        self._sample = None
        self._collation_csv = None

        if new_campaign:

            self._campaign_info = info.to_dict()
            self._next_run = 1
            self._next_ensemble = 1

            if location is None:
                message = f"No location given for JSON db location"
                logger.critical(message)
                raise RuntimeError(message)

            self._collation_csv = location + ".COLLATION"
        else:
            self._load_campaign(location, name)

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
        self._next_run = input_info['next_run']
        self._next_ensemble = input_info['next_ensemble']

        self._app['params'] = ParamsSpecification.deserialize(self._app['params'])

        # Convert run statuses to enums
        for run_id in self._runs:
            self._runs[run_id]['status'] = constants.Status(self._runs[run_id]['status'])

    def _save(self):
        serialized_app = self._app.copy()
        serialized_app['params'] = serialized_app['params'].serialize()
        out_dict = {
            'campaign': self._campaign_info,
            'app': serialized_app,
            'runs': self._runs,
            'sample': self._sample,
            'collation_csv': self._collation_csv,
            'next_run': self._next_run,
            'next_ensemble': self._next_ensemble
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
        """
        Add new Sampler to the 'sampler' table.

        Parameters
        ----------
        sampler: BaseSamplingElement

        Returns
        -------

        """

        if self._sample:
            message = ('JSON/Python dict database does not support '
                       'multiple samplers')
            logger.critical(message)
            raise RuntimeError(message)

        self._sample = sampler.serialize()

        # For JSON db, sampler ID is always 1
        return 1

    def update_sampler(self, sampler_id, sampler_element):
        """
        Update the state of the Sampler with id 'sampler_id' to
        that in the passed 'sampler_element'

        Parameters
        ----------
        sampler_id: int
            The id of the sampler in the db to update
        sampler_element: BaseSamplingElement
            The sampler whose state should be used as the new state

        Returns
        -------

        """

        if sampler_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'sampler_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        self._sample = sampler_element.serialize()
        self._save()

    def resurrect_sampler(self, sampler_id):
        """
        Return the sampler object corresponding to id sampler_id in the database.
        It is deserialized from the state stored in the database.

        Parameters
        ----------
        sampler_id: int
            The id of the sampler to resurrect

        Returns
        -------
        BaseSamplingElement
            The 'live' sampler object, deserialized from the state in the db

        """

        if sampler_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'sampler_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        sampler = BaseSamplingElement.deserialize(self._sample)
        return sampler

    def resurrect_app(self, app_name):
        """
        Return the 'live' encoder and decoder objects corresponding to the app with
        name 'app_name' in the database. They are deserialized from the states
        previously stored in the database.

        Parameters
        ----------
        app_name: string
            Name of the app to resurrect

        Returns
        -------
        BaseEncoder, BaseDecoder
            The 'live' encoder and decoder objects associated with this app

        """

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
        """
        Store the state of the given collater object in the collation slot
        for the campaign with id 'campaign_id'

        Parameters
        ----------
        collater: BaseCollationElement
            The collater object to serialize
        campaign_id: int
            The id of the campaign this collater should be assigned to

        Returns
        -------

        """

        if campaign_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'campaign_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        self._campaign_info['collater'] = collater.serialize()

    def resurrect_collation(self, campaign_id):
        """
        Return the collater object corresponding to the campaign with id 'campaign_id'
        in the database. It is deserialized from the state stored in the database.

        Parameters
        ----------
        campaign_id: int
            The id of the collater to resurrect

        Returns
        -------
        BaseCollationElement
            The 'live' collater object, deserialized from the state in the db

        """

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

    def add_runs(self, run_info_list=None, run_prefix='Run_', ensemble_prefix='Ensemble_'):
        """
        Add runs to the `runs` table in the database.

        Parameters
        ----------
        run_info_list: List of RunInfo objects
            Each RunInfo contains relevant run fields: params, status (where in the
            EasyVVUQ workflow is this RunTable), campaign (id number),
            sample, app
        run_prefix: str
            Prefix for run id
        ensemble_prefix: str
            Prefix for ensemble id

        Returns
        -------

        """

        for run_info in run_info_list:
            name = f"{run_prefix}{self._next_run}"
            ensemble = f"{ensemble_prefix}{self._next_ensemble}"

            this_run = run_info.to_dict()
            this_run['run_name'] = name
            this_run['ensemble_name'] = ensemble
            this_run['run_dir'] = os.path.join(self._campaign_info['runs_dir'], name)

            self._runs[name] = this_run
            self._next_run += 1
        self._next_ensemble += 1

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
        """
        Set the 'run_dir' path for the specified run in the database.

        Parameters
        ----------
        run_name: str
            Name of run to filter for.
        run_dir: str
            Directory path associated to set for this run.
        campaign:  int or None
            Campaign id to filter for.
        sampler: int or None
            Sample id to filter for.

        Returns
        -------

        """

        if campaign is not None or sampler is not None:
            message = (f'JSON/Python dictionary database only supports '
                       f'single campaign and sampler workflows - ignoring'
                       f'campaign - {campaign}/ sampler {sampler}')
            logger.warning(message)
        self._runs[run_name]['run_dir'] = run_dir

    def campaigns(self):
        """Get list of campaigns for which information is stored in the
        database.

        Returns
        -------
        list:
            Campaign names.
        """

        return [self._campaign_info['name']]

    def campaign_dir(self, campaign_name=None):
        """Get campaign directory for `campaign_name`.

        Returns
        -------
        str:
            Path to campaign directory.
        """

        if campaign_name is not None:
            message = (
                f'JSON/Python dictionary database can only support one '
                f'application - ignoring selected name ({campaign_name}).')
            logger.warning(message)

        return self._campaign_info['campaign_dir']

    def runs(self, campaign=None, sampler=None, status=None, not_status=None):
        """
        A generator to return all run information for selected `campaign` and `sampler`.

        Parameters
        ----------
        campaign: int or None
            Campaign id to filter for.
        sampler: int or None
            Sampler id to filter for.
        status: enum(Status) or None
            Status string to filter for.
        not_status: enum(Status) or None
            Exclude runs with this status string

        Returns
        -------
        dict:
            Information on each selected run (key = run_name, value = dict of
            run information fields.), one at a time.
        """

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
        """
        Returns the number of runs matching the filtering criteria.

        Parameters
        ----------
        campaign: int or None
            Campaign id to filter for.
        sampler: int or None
            Sampler id to filter for.
        status: enum(Status) or None
            Status string to filter for.
        not_status: enum(Status) or None
            Exclude runs with this status string

        Returns
        -------
        int:
            The number of runs in the database matching the filtering criteria

        """

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
        """
        Get the directory used to store run information for `campaign_name`.

        Parameters
        ----------
        campaign_name: str
            Name of the selected campaign.

        Returns
        -------
        str:
            Path containing run outputs.
        """

        if campaign_name is not None:
            message = (
                f'JSON/Python dictionary database can only support one '
                f'application - ignoring selected name ({campaign_name}).')
            logger.warning(message)

        return self._campaign_info['runs_dir']

    def get_campaign_id(self, name):
        """
        Return the (database) id corresponding to the campaign with name 'name'.

        Parameters
        ----------
        name: str
            Name of the campaign.

        Returns
        -------
        int:
            The id of the campaign with the specified name
        """

        logger.warning("JSON database only allows for one campaign. "
                       "Campaign ID is always 1.")

        return 1

    def get_sampler_id(self, campaign_id):
        """
        Return the (database) id corresponding to the sampler currently set
        for the campaign with id 'campaign_id'

        Parameters
        ----------
        campaign_id: int
            ID of the campaign.

        Returns
        -------
        int:
            The id of the sampler set for the specified campaign
        """

        logger.warning("JSON database only allows for one sampler. "
                       "Sampler ID is always 1.")

        return 1

    def set_sampler(self, campaign_id, sampler_id):
        """
        Set specified campaign to be using specified sampler

        Parameters
        ----------
        campaign_id: int
            ID of the campaign.
        sampler_id: int
            ID of the sampler.

        Returns
        -------
        """

        if campaign_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'campaign_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        if sampler_id != 1:
            message = ('JSON/Python dict database does not support a '
                       'sampler_id other than 1')
            logger.critical(message)
            raise RuntimeError(message)

        # Do nothing, as JSON db sampler_id is already always set to 1

    def get_run_status(self, run_name, campaign=None, sampler=None):
        """
        Return the status (enum) for the run with name 'run_name' (and, optionally,
        filtering for campaign and sampler by id)

        Parameters
        ----------
        run_name: str
            Name of the run
        campaign: int
            ID of the desired Campaign
        sampler: int
            ID of the desired Sampler

        Returns
        -------
        status: enum(Status)
            Status of the run.
        """

        if campaign is not None:
            logger.warning("Only 1 campaign is possible in JSON db")
        if sampler is not None:
            logger.warning("Only 1 sampler is possible in JSON db")

        return constants.Status(self._runs[run_name]['status'])

    def set_run_statuses(self, run_name_list, status):
        """
        Set the specified 'status' (enum) for all runs in the list run_ID_list

        Parameters
        ----------
        run_name_list: list of str
            A list of run names run names (format is usually: prefix + int)
        status: enum(Status)
            The new status all listed runs should now have

        Returns
        -------

        """

        for run_name in run_name_list:
            self._runs[run_name]['status'] = status
        self._save()

    def append_collation_dataframe(self, df):
        """
        Append the data in dataframe 'df' to that already collated in the database

        Parameters
        ----------
        df: pandas dataframe
            The dataframe whose contents need to be appended to the collation store

        Returns
        -------
        """

        if os.path.exists(self._collation_csv):
            df.to_csv(self._collation_csv, mode='a', header=False)
        else:
            df.to_csv(self._collation_csv, mode='w', header=True)

    def get_collation_dataframe(self):
        """
        Returns a dataframe containing the full collated results stored in this database
        i.e. the total of what was added with the append_collation_dataframe() method.

        Parameters
        ----------

        Returns
        -------
        df: pandas dataframe
            The dataframe with all contents that were appended to this database
        """

        df = pd.read_csv(self._collation_csv)
        return df
