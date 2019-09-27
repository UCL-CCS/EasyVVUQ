"""Provides a base class for CampaignDBs

"""

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


class BaseCampaignDB:
    """Baseclass for all EasyVVUQ CampaignDBs

    Skeleton for class that provides database access for the campaign.

    Parameters
    ----------
    location: str or None
        Location to look for database.
    new_campaign: bool
        Does the database need to be initialised as a new campaign.
    name: str or None
        Name of the campaign.
    info: `easyvvuq.data_structs.CampaignInfo`
        Information defining the campaign.
    """

    def __init__(self, location=None, new_campaign=False, name=None, info=None):
        pass

    def app(self, name):
        """
        Get app information. Specific applications selected by `name`,
        otherwise first entry in database 'app' selected.

        Parameters
        ----------
        name : str or None
            Name of selected app, if `None` given then first app will be
            selected.

        Returns
        -------
        dict:
            Application information.
        """

        raise NotImplementedError

    def add_app(self, app_info):
        """
        Add application to the 'app' table.

        Parameters
        ----------
        app_info: AppInfo
            Application definition.

        Returns
        -------

        """

        raise NotImplementedError

    def add_sampler(self, sampler):
        """
        Add new Sampler to the 'sampler' table.

        Parameters
        ----------
        sampler: BaseSamplingElement

        Returns
        -------

        """

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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
        BaseEncoder, BaseDecoder, BaseCollationElement
            The 'live' encoder and decoder objects associated with this app

        """

        raise NotImplementedError

    def add_run(self, run_info=None, prefix='Run_'):
        """
        Add run to the `runs` table in the database.

        Parameters
        ----------
        run_info: `easyvvuq.data_structs.RunInfo`
            Contains relevant run fields: params, status (where in the
            EasyVVUQ workflow is this RunTable), campaign (id number),
            sample, app
        prefix: str
            Prefix for run id

        Returns
        -------

        """

        raise NotImplementedError

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

        raise NotImplementedError

    def run(self, run_name, campaign=None, sampler=None):
        """
        Get the information for a specified run.

        Parameters
        ----------
        run_name: str
            Name of run to filter for.
        campaign:  int or None
            Campaign id to filter for.
        sampler: int or None
            Sample id to filter for.

        Returns
        -------
        dict
            Containing run information (run_name, params, status, sample,
            campaign, app)
        """
        raise NotImplementedError

    def campaigns(self):
        """Get list of campaigns for which information is stored in the
        database.

        Returns
        -------
        list:
            Campaign names.
        """

        raise NotImplementedError

    def campaign_dir(self, campaign_name=None):
        """Get campaign directory for `campaign_name`.

        Returns
        -------
        str:
            Path to campaign directory.
        """

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

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

        raise NotImplementedError

    def append_collation_dataframe(self, df, app_id):
        """
        Append the data in dataframe 'df' to that already collated in the database

        Parameters
        ----------
        df: pandas dataframe
            The dataframe whose contents need to be appended to the collation store
        app_id: int
            The id of this app in the sql database. Used to determine which collation
            table is appended to.

        Returns
        -------
        """

        raise NotImplementedError

    def get_collation_dataframe(self, app_id):
        """
        Returns a dataframe containing the full collated results stored in this database
        i.e. the total of what was added with the append_collation_dataframe() method.

        Parameters
        ----------
        app_id: int
            The id of this app in the sql database. Used to determine which collation
            table is returned.

        Returns
        -------
        df: pandas dataframe
            The dataframe with all contents that were appended to the table corresponding
            to this app_id.
        """

        raise NotImplementedError
