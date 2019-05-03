import os
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
        self.campaign_db = None
        self.state_file = state_file

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

    def add_app(self, app_info, set_active=True):
        """
        Add information on a new application to the campaign database.

        Parameters
        ----------
        app_info: dict
            Contains the information needed to describe and wrap an
            application: name, input_encoder, output_decoder,
            encoder_options, decoder_options, execution, params (all
            parameters that can be passed via encoder to the application),
            fixtures, collation and variable (which parameters can be varied
            in this workflow).
        set_active: bool
            Should the added app be set to be teh currently active app?

        Returns
        -------

        """

        # TODO: Need to look at parameters

        # validate application input
        app = uq.data_structs.AppInfo(**app_info)

        self.campaign_db.add_app(app)
        if set_active:
            self.set_app(app.name)

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

    def draw_samples(self, N=0):

        # Make sure N is not 0 for an infinite generator (this would add runs
        # forever...)
        if self._active_sampler.is_finite() is False and N <= 0:
            raise RuntimeError(
                "sampling_element '" +
                self._active_sampler.element_name() +
                "' is an infinite generator, therefore a finite number of draws (N > 0) must be specified.'")


        num_added = 0
        for param_vals in self._active_sampler.generate_runs():
            # TODO: Get correct sampler and campaign IDs to pass to RunInfo
            run_info = RunInfo(app=self._active_app['id'], params=param_vals, sample=0, campaign=0)
            self.campaign_db.add_run(run_info)
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
        #if self._active_app.encoder is None:
        #    raise RuntimeError('Cannot populate runs without valid '
        #                       'encoder in campaign')


        print(runs)
        for run_id, run_data in runs.items():
            print("RUNID", run_id)
            print("RUNSDIR", runs_dir)
            print("RUNDATA", run_data)
            print("RUNPARAMS", run_data['params'])

            # Make run directory
            target_dir = os.path.join(runs_dir, run_id)
            os.makedirs(target_dir)

            # TODO: Should we check if the run has been created?

            # TODO: record target_dir along with the run info? (Would need a new entry in RunTable)
            # runs[run_id]['run_dir'] = target_dir

            # TODO: Apply encoder
            #self._active_app_encoder.encode(params=run_data, target_dir=target_dir)

class CampaignOld:
    def campaign_id(self, without_prefix=False):

        # The "ID" of the campaign is just the name of the campaign
        # directory (without the trailing slash)
        campaign_id = os.path.basename(
            os.path.normpath(self.app_info['campaign_dir']))

        if without_prefix:
            # Ignore the prefix at the start of the string.
            prefix = self.app_info['campaign_dir_prefix']

            if campaign_id.startswith(prefix):
                return campaign_id[len(prefix):]

            print(f"Warning: campaign_ID() called with option "
                  f"'without_prefix' set, but prefix {prefix} was "
                  f"not found at the start of campaign_ID {campaign_id}.")

        return campaign_id



    def save_state(self, state_filename):
        """Save the current Campaign state to file in JSON format

        Parameters
        ----------
        state_filename  :   str
            Name of file in which to save the state

        Returns
        -------

        """

        # TODO: Make this make sense

        # with open(state_filename, "w") as outfile:
        #    json.dump(output_json, outfile, indent=4)

        pass

    def add_default_run(self):
        """
        Add a single new run to the queue, using only default values for
        all parameters.
        """

        new_run = {}
        self.add_run(new_run)

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

        if "runs_dir" not in self.app_info.keys():

            print(self.app_info)

            raise RuntimeError("Missing 'runs_dir' key (Application info must "
                               "include runs directory path).")
        runs_dir = self.app_info["runs_dir"]

        # Loop through all runs in this campaign
        run_ids = self.runs.keys()
        for run_id in run_ids:
            dir_name = os.path.join(runs_dir, run_id)
            print("Applying " + action.__module__ + " to " + dir_name + "...")

            # Run user-specified action on this directory
            action.act_on_dir(dir_name)
