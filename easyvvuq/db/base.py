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

    def __init__(self, location=None, new_campaign=False, name=None,
                 info=None):
        pass

    def app(self, name):
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
        raise NotImplementedError

    def add_app(self, app_info):
        """
        Add application to the database.

        Parameters
        ----------
        app_info: `easyvvuq.data_structs.AppInfo`
            Application definition.

        Returns
        -------

        """
        raise NotImplementedError

    def add_sampler(self, sampler):
        """
        Add passed sampler information to the the database.

        Parameters
        ----------
        sampler  :  dict
            Information on the sampler that was used

        Returns
        -------

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
        Get a dictionary of all run information for selected `campaign` and
        `sampler`.

        Parameters
        ----------
        campaign: int
            Campaign id to filter for.
        sampler: int
            Sampler id to filter for.

        Returns
        -------
        dict:
            Information on all selected runs (key = run_name, value = dict of
            run information fields.).

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
