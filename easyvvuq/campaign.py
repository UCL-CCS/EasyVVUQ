import os
import sys
import logging
import tempfile
import json
import pprint
import easyvvuq as uq
from easyvvuq.constants import __easyvvuq_version__, default_campaign_prefix
from easyvvuq.data_structs import RunInfo

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


class Campaign:

    def __init__(self, name=None, db_type="sql", db_location=None, workdir="./", state_file=None):

        self._log = []

        self._active_app = None
        self._active_app_encoder = None
        self.campaign_db = None
        self.state_file = state_file
        self.last_collation_dataframe = None
        self.last_analysis = None

        # TODO: These definitely shouldn't be here. Probably should be in DB.
        self._active_app_encoder = None
        self._active_app_decoder = None
        self._active_app_collation = None

        # Load campaign from state_file, if provided. Else make a fresh new
        # campaign with a new campaign database
        if state_file is not None:
            self.init_from_state_file(state_file)
        else:
            self.init_fresh(name, db_type, db_location, workdir)

    def init_fresh(self, name, db_type, db_location, workdir):

        # Create temp dir for campaign
        campaign_dir = tempfile.mkdtemp(prefix=default_campaign_prefix,
                                        dir=workdir)

        if db_type == 'sql':
            from .db.sql import CampaignDB
            if db_location is None:
                db_location = "sqlite:///" + campaign_dir + "test.db"
        elif db_type == 'json':
            from .db.json import CampaignDB
        else:
            message = (f"Invalid 'db_type' {db_type}. Supported types are "
                       f"'sql' or 'json'.")
            logger.critical(message)
            raise RuntimeError(message)

        info = uq.data_structs.CampaignInfo(name=name, campaign_dir_prefix=default_campaign_prefix,
                                            easyvvuq_version=__easyvvuq_version__, campaign_dir=campaign_dir)
        self.campaign_db = CampaignDB(location=db_location, new_campaign=True,
                                      name=name, info=info)

    def init_from_state_file(self, state_file):
        # TODO Implement loading from state file
        print(f"Loading campaign from state file '{state_file}'")
        raise NotImplementedError

    def add_app(self, name=None, params=None, encoder=None, decoder=None, collation=None, set_active=True):
        """
        Add information on a new application to the campaign database.

        Parameters
        ----------
        set_active: bool
            Should the added app be set to be teh currently active app?

        Returns
        -------

        """

        # TODO: Need to look at parameters

        # validate application input
        app = uq.data_structs.AppInfo(
                                        name=name,
                                        params=params,
                                        encoder=encoder,
                                        decoder=decoder,
                                        collation=collation
                                     )

        self.campaign_db.add_app(app)
        if set_active:
            self.set_app(app.name)

        # TODO: Find somewhere sensible to store/resume/set the *live* encoder and decoder for a given app.
        # Currently not possible from the "dead" form stored in the DB
        self._active_app_encoder = encoder
        self._active_app_decoder = decoder
        self._active_app_collation = collation

    def set_app(self, app_name):
        """
        Set the app to be in active use by this campaign. Gets the app info from
        the database.

        Parameters
        ----------
        app_name: str or None
            Name of selected app, if `None` given then first app will be
            selected.
        Returns
        -------

        """

        self._active_app = self.campaign_db.app(name=app_name)

    def set_sampler(self, sampler):
        if not isinstance(sampler, uq.elements.sampling.BaseSamplingElement):
            msg = "set_sampler() must be passed a sampling element"
            logging.error(msg)
            raise Exception(msg)

        self._active_sampler = sampler

    def add_run(self, new_run, prefix='Run_'):
        """Add a new run to the queue

        Parameters
        ----------
        new_run     : dict
            Defines the value of each model parameter listed in
            `self.params_info` for a run to be added to `self.runs`
        prefix      : str
            Prepended to the key used to identify the run in `self.runs`

        Returns
        -------

        """

        app_default_params = self._active_app["params"]

        # Validate:
        # Check if parameter names match those already known for this app
        for param in new_run.keys():
            if param not in app_default_params.keys():

                reasoning = (
                    f"dict passed to add_run() contains extra parameter, "
                    f"{param}, which is not a known parameter name "
                    f"of app {self._active_app['name']}.")

                raise RuntimeError(reasoning)

        # If necessary parameter names are missing, fill them in from the
        # default values in params_info
        for param in app_default_params.keys():
            if param not in new_run.keys():
                default_val = app_default_params[param]["default"]
                new_run[param] = default_val

        # Add to run queue
        # TODO: Get correct sampler and campaign IDs to pass to RunInfo
        run_info = RunInfo(app=self._active_app['id'], params=new_run, sample=0, campaign=0)
        self.campaign_db.add_run(run_info)

    def add_default_run(self):
        """
        Add a single new run to the queue, using only default values for
        all parameters.
        """

        new_run = {}
        self.add_run(new_run)

    def draw_samples(self, N=0):

        # Make sure N is not 0 for an infinite generator (this would add runs
        # forever...)
        if self._active_sampler.is_finite() is False and N <= 0:
            raise RuntimeError(
                "sampling_element '" +
                self._active_sampler.element_name() +
                "' is an infinite generator, therefore a finite number of draws (N > 0) must be specified.'")

        num_added = 0
        for new_run in self._active_sampler.generate_runs():

            self.add_run(new_run)

            num_added += 1
            if num_added == N:
                break

    def list_runs(self):
        return self.campaign_db.runs()

    def populate_runs_dir(self):
        """Populate run directories based on runs in the DB

        This calls the App encoder object to create input files for the
        specified application in each run directory, usually with varying input
        (scientific) parameters.

        Parameters
        ----------

        Returns
        -------

        """

        runs = self.campaign_db.runs()
        runs_dir = self.campaign_db.runs_dir()

        # TODO: Check if encoder exists / is set correctly
        if self._active_app_encoder is None:
            raise RuntimeError('Cannot populate runs without valid '
                               'encoder in campaign')

        for run_id, run_data in runs.items():

            # Make run directory
            target_dir = os.path.join(runs_dir, run_id)
            os.makedirs(target_dir)

            # TODO: Should we check if the run has been created?

            # TODO: Check that this isn't insanely inefficient (almost certainly will be hammering the database for large run lists)
            self.campaign_db.set_dir_for_run(run_id, target_dir)

            # TODO: Apply encoder
            self._active_app_encoder.encode(params=run_data['params'], target_dir=target_dir)

    def get_campaign_runs_dir(self):
        return self.campaign_db.runs_dir()

    def apply_for_each_run_dir(self, action):
        """
        For each run in this Campaign's run list, apply the specified action
        (an object of type Action)

        Parameters
        ----------
        action : the action to be applied to each run directory
            The function to be applied to each run directory. func() will
            be called with the run directory path as its only argument.
        Returns
        -------
        """

        runs = self.campaign_db.runs()
        runs_dir = self.campaign_db.runs_dir()

        # Loop through all runs in this campaign
        for run_id in runs.keys():
            dir_name = os.path.join(runs_dir, run_id)
            print("Applying " + action.__module__ + " to " + dir_name + "...")

            # Run user-specified action on this directory
            action.act_on_dir(dir_name)


    def collate(self, store=True):

        # Apply collation element, and obtain the resulting dataframe
        self.last_collation_dataframe = self._active_app_collation.collate(self)

        if store == True:
            # Set up dirs and files to store collation results in
            data_dir = os.path.join(campaign.get_campaign_dir(), 'data')
            out_dir = tempfile.mkdtemp(dir=data_dir)
            out_file = os.path.join(out_dir, 'aggregate_sample.tsv')

            # Convert dataframe to file
            df.to_csv(out_file, sep='\t', index=False)

        # TODO: Log this collation appropriately

    def get_last_collation(self):
        # TODO: Make check work with pandas dataframe
#        if self.last_collation_dataframe == None:
#            logging.warning("No dataframe available as no collation has been done. Was this campaign's collate() function run?")
#            return None
        return self.last_collation_dataframe

    def apply_analysis(self, analysis_element):
        # TODO: Check that collation was done before applying this
        self.last_analysis = analysis_element.analyse(self.last_collation_dataframe)
        # TODO: Log this analysis appropriately

    def get_last_analysis(self):
        # TODO: Check that analysis was done
#        if self.last_analysis == None:
#            logging.warning("No last analysis available as no analysis has been done. Was this campaign's collate() function run?")
#            return None
        return self.last_analysis

    def scan_completed(self, *args, **kwargs):
        """
        Check campaign database for completed runs.

        Returns
        -------

        """

        # TODO: Recreate functionality

        pass

    def all_complete(self):
        """
        Check if all runs have reported having output generated by
        a completed simulation.

        Returns
        -------

        """

        # TODO: Recreate functionality

        pass

    def __str__(self):
        """Returns formatted summary of the current Campaign state.
        Enables class to work with standard print() method"""

        # TODO: Recreate functionality

        pass















class CampaignOld:
    def log_element_application(self, element, further_info):
        """
        Adds an entry to the campaign log for the given element, with the
        provided further_info dictionary. The further_info dict should give
        specific information about this element's application, where
        suitable.
        """

        log_entry = {
            "element": {
                "name": element.element_name(),
                "version": element.element_version(),
                "category": element.element_category()
            },
            "info": further_info
        }
        self._log.append(log_entry)

    def record_analysis(self, primitive, output_file, output_type,
                        log_file, state_file):
        """
        Add information about analysis primitives applied to this campaign to
        `self._analysis_uqps`.

        Parameters
        ----------
        primitive:      str
            Name of analysis primitive applied.
        output_file:    str
            Path to file containing output from the analysis.
        output_type:    str or `uq.constants.OutputType`
            Class of data output by analysis.
        log_file:       str
            Path to JSON logfile produced by primitive.
        state_file:     str
            Path to Campaign state file logged by primitive.
            Provides information on the state of runs when executed.

        Returns
        -------

        """

        if isinstance(output_type, uq.constants.OutputType):
            output_type = output_type.value

        info = {'primitive': primitive,
                'output': output_file,
                'type': output_type,
                'log': log_file,
                'state': state_file,
                }

        self._analysis_uqps.append(info)

    def unique_runs(self):
        """
        Check the `runs` list to find which are executed for unique parameters
        lists. Each entry in the list contains a list of the `run_ids` which
        correspond to the parameter set.

        Returns
        -------
        list
            List in which each items is parameter dict from run with a list of
            run_ids which contain those parameters.
        """

        runs = self.runs
        unique = []

        for run_id, run_info in runs.items():

            if run_info not in unique:

                tmp = dict(run_info)
                tmp['run_ids'] = [run_id]
                unique.append(tmp)

            else:

                match_ndx = unique.index(run_info)

                unique[match_ndx]['run_ids'].append(run_id)

        return unique
