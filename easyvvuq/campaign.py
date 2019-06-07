"""EasyVVUQ Campaign

This module contains the Campaign class that is used to coordinate all
EasyVVUQ workflows.
"""
import os
import logging
import tempfile
import json
import easyvvuq
from easyvvuq.constants import default_campaign_prefix, Status
from easyvvuq.data_structs import RunInfo, CampaignInfo, AppInfo
from easyvvuq.sampling import BaseSamplingElement
from easyvvuq.collate import BaseCollationElement

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
    """Campaigns organise the dataflow in EasyVVUQ workflows.

    The Campaign functions as as state machine for the VVUQ workflows. It uses a
    database (CampaignDB) to store information on both the target application
    and the VVUQ algorithms being employed.

    Notes
    -----

    Multiple campaigns can be combined in a CampaignDB. Hence the particular
    campaign we are currently working on will be specified using `campaign_id`.

    The JSON CampaignDB only supports a single campaign.

    Parameters
    ----------
    name : :obj:`str`, optional
        Description of `param1`.
    db_type : str, default="sql"
        Type of database to use for CampaignDB. Options at present are "sql"
        and "json".
    db_location : :obj:`str`, optional
        Location of the underlying campaign database - either a path or
        acceptable URI for SQLAlchemy.
    work_dir : :obj:`str`, optional, default='./'
        Path to working directory - used to store campaign directory.
    state_file : :obj:`str`, optional
        Path to serialised state - used to initialise the Campaign.
    change_to_state : bool, optional, default=False
        Should we change to the directory containing any specified `state_file`
        in order to make relative paths work.

    Attributes
    ----------
    campaign_name : str or None
        Name for the campaign/workflow.
    db_location : str or None
        Location of the underlying campaign database - either a path or
        acceptable URI for SQLAlchemy.
    db_type : str or None
        Type of CampaignDB ("sql" or "json").
    campaign_id : int
        ID number for the current campaign in the CampaignDB.
    last_analysis : :obj:`pandas.DataFrame`
        Output from the last applied analysis element
    """

    def __init__(
            self,
            name=None,
            db_type="sql",
            db_location=None,
            work_dir="./",
            state_file=None,
            change_to_state=False
    ):

        self.work_dir = os.path.realpath(os.path.expanduser(work_dir))

        self.campaign_name = None
        self._campaign_dir = None
        self.db_location = None
        self.db_type = None
        self._log = []

        self.campaign_id = None
        self._active_app = None
        self._active_app_name = None
        self.campaign_db = None

        self.last_analysis = None

        self._active_app_id = None
        self._active_app_encoder = None
        self._active_app_decoder = None

        self._active_collater = None
        self._active_sampler = None
        self._active_sampler_id = None

        # Load campaign from state_file, if provided. Else make a fresh new
        # campaign with a new campaign database
        if state_file is not None:
            self._state_dir = self.init_from_state_file(state_file)
            if change_to_state:
                os.chdir(self._state_dir)
        else:
            self.init_fresh(name, db_type, db_location, work_dir)
            self._state_dir = None

    @property
    def campaign_dir(self):
        """Get the path in which to load/save files related to the campaign.

        Returns
        -------
        str
            Path to the campaign directory - given as a subdirectory of the
            working directory.
        """

        return os.path.join(self.work_dir, self._campaign_dir)

    def init_fresh(self, name, db_type='sql',
                   db_location=None, work_dir='.'):
        """
        Initialise a new campaign - create database and output directory
        (`campaign_dir`, a uniquely named directory in `work_dir`).

        Parameters
        ----------
        name : str
            Campaign name.
        db_type : str
            Database type - current options are 'sql' and 'json'.
        db_location : str or None
            Path in which to create campaign database - defaults to None which
            results in the database being placed in `campaign_dir` with a
            default name.
        work_dir : str
            Path in which to create the `campaign_dir`.

        Returns
        -------

        """

        # Create temp dir for campaign
        campaign_dir = tempfile.mkdtemp(prefix=default_campaign_prefix, dir=work_dir)

        self._campaign_dir = os.path.relpath(campaign_dir, start=work_dir)

        self.db_location = db_location
        self.db_type = db_type

        if self.db_type == 'sql':
            from .db.sql import CampaignDB
            if self.db_location is None:
                self.db_location = "sqlite:///" + self.campaign_dir + "test.db"
        elif self.db_type == 'json':
            from .db.json import CampaignDB
            if self.db_location is None:
                self.db_location = tempfile.mkstemp(suffix='.json', prefix='easyvvuq')[1]
        else:
            message = (f"Invalid 'db_type' {db_type}. Supported types are "
                       f"'sql' or 'json'.")
            logger.critical(message)
            raise RuntimeError(message)

        info = CampaignInfo(
            name=name,
            campaign_dir_prefix=default_campaign_prefix,
            easyvvuq_version=easyvvuq.__version__,
            campaign_dir=self.campaign_dir)
        self.campaign_db = CampaignDB(location=self.db_location,
                                      new_campaign=True,
                                      name=name, info=info)

        # Record the campaign's name and its associated ID in the database
        self.campaign_name = name
        self.campaign_id = self.campaign_db.get_campaign_id(self.campaign_name)

    def init_from_state_file(self, state_file):
        """Load campaign state from file.

        Parameters
        ----------
        state_file : str
            Path to the file containing the campaign state.

        Returns
        -------

        """

        full_state_path = os.path.realpath(os.path.expanduser(state_file))

        if not os.path.isfile(full_state_path):
            if not os.path.exists(full_state_path):
                msg = (f"Unable to open state file (no file exists): "
                       f"{state_file}")
            else:
                msg = (f"Unable to open state file (path is not a file): "
                       f"{state_file}")

            logger.error(msg)
            raise RuntimeError(msg)

        state_dir = os.path.dirname(full_state_path)

        logger.info(f"Loading campaign from state file '{full_state_path}'")
        self.load_state(full_state_path)

        if self.db_type == 'sql':
            from .db.sql import CampaignDB
        elif self.db_type == 'json':
            from .db.json import CampaignDB
        else:
            message = (f"Invalid 'db_type' {self.db_type}. Supported types "
                       f"are 'sql' or 'json'.")
            logger.critical(message)
            raise RuntimeError(message)

        logger.info(f"Opening session with CampaignDB at {self.db_location}")
        self.campaign_db = CampaignDB(location=self.db_location,
                                      new_campaign=False,
                                      name=self.campaign_name)
        campaign_db = self.campaign_db
        self.campaign_id = campaign_db.get_campaign_id(self.campaign_name)

        # Resurrect the sampler and collation elements
        self._active_sampler = campaign_db.resurrect_sampler(self._active_sampler_id)
        self._active_collater = campaign_db.resurrect_collation(self.campaign_id)

        self.set_app(self._active_app_name)

        return state_dir

    def save_state(self, state_filename):
        """Save the current Campaign state to file in JSON format
        Parameters
        ----------
        state_filename : str
            Name of file in which to save the state
        Returns
        -------
        """

        output_json = {
            "db_location": self.db_location,
            "db_type": self.db_type,
            "active_sampler_id": self._active_sampler_id,
            "active_app": self._active_app_name,
            "campaign_name": self.campaign_name,
            "campaign_dir": self._campaign_dir,
            "log": self._log
        }
        with open(state_filename, "w") as outfile:
            json.dump(output_json, outfile, indent=4)

    def load_state(self, state_filename):
        """Load up a Campaign state from the specified JSON file

        Parameters
        ----------
        state_filename : str
            Name of file from which to load the state

        Returns
        -------

        """

        with open(state_filename, "r") as infile:
            input_json = json.load(infile)

        self.db_location = input_json["db_location"]
        self.db_type = input_json["db_type"]
        self._active_sampler_id = input_json["active_sampler_id"]
        self._active_app_name = input_json["active_app"]
        self.campaign_name = input_json["campaign_name"]
        self._campaign_dir = input_json["campaign_dir"]
        self._log = input_json["log"]

        if not os.path.exists(self.campaign_dir):
            message = (f"Campaign directory in state_file {state_filename}"
                       f" ({self.campaign_dir}) does not exist.")
            logger.critical(message)
            raise RuntimeError(message)

    def add_app(self, name=None, params=None, fixtures=None,
                encoder=None, decoder=None,
                set_active=True):
        """Add an application to the CampaignDB.

        Parameters
        ----------
        name : str
            Name of the application.
        params : dict
            Description of the parameters to associate with the application.
        fixtures : dict
            Description of files/assets.
        encoder : :obj:`easyvvuq.encoders.base.BaseEncoder`
            Encoder element to convert parameters into application run inputs.
        decoder : :obj:`easyvvuq.decoders.base.BaseDecoder`
            Decoder element to convert application run output into data for
            VVUQ analysis.
        set_active: bool
            Should the added app be set to be the currently active app?

        Returns
        -------

        """

        # Verify input parameters dict

        if not isinstance(params, dict):
            msg = "params must be of type 'dict'"
            logger.error(msg)
            raise Exception(msg)

        if not params:
            msg = ("params must not be empty. At least one parameter "
                   "should be specified.")
            logger.error(msg)
            raise Exception(msg)

        # Check each param has a dict as a value, and that dict has a "default"
        # defined
        for param_key, param_def in params.items():
            if not isinstance(param_def, dict):
                msg = f"Entry for param '{param_key}' must be a dictionary"
                logger.error(msg)
                raise Exception(msg)
            if "default" not in param_def:
                msg = (
                    f"Entry for param '{param_key}' must be a dictionary"
                    f"defining a 'default' value for this parameter."
                )
                logger.error(msg)
                raise Exception(msg)

        # validate application input
        app = AppInfo(
            name=name,
            params=params,
            fixtures=fixtures,
            encoder=encoder,
            decoder=decoder
        )

        self.campaign_db.add_app(app)
        if set_active:
            self.set_app(app.name)

    def set_app(self, app_name):
        """Set active app for the campaign.

        Application information is retrieved from `self.campaign_db`.

        Parameters
        ----------
        app_name: str or None
            Name of selected app, if `None` given then first app will be
            selected.

        Returns
        -------

        """

        self._active_app_name = app_name
        self._active_app = self.campaign_db.app(name=app_name)

        # Resurrect the app encoder and decoder elements
        (self._active_app_encoder,
         self._active_app_decoder) = self.campaign_db.resurrect_app(app_name)

    def set_sampler(self, sampler):
        """Set active sampler.

        Parameters
        ----------
        sampler : `easyvvuq.sampling.base.BaseSamplingElement`
            Sampler that will be used to create runs for the current campaign.

        Returns
        -------

        """
        if not isinstance(sampler, BaseSamplingElement):
            msg = "set_sampler() must be passed a sampling element"
            logging.error(msg)
            raise Exception(msg)

        self._active_sampler = sampler
        self._active_sampler_id = self.campaign_db.add_sampler(sampler)

    def set_collater(self, collater):
        """Set a collater for this campaign.

        Parameters
        ----------
        collater : `easyvvuq.collate.base.BaseCollationElement`
            Collation that will be used to create runs for the current campaign.

        Returns
        -------

        """
        if not isinstance(collater, BaseCollationElement):
            msg = "set_collater() must be passed a collation element"
            logging.error(msg)
            raise Exception(msg)

        self.campaign_db.set_campaign_collater(collater, self.campaign_id)
        self._active_collater = collater

    def add_run(self, new_run):
        """Add a new run to the queue.

        Parameters
        ----------
        new_run : dict
            Defines the value of each model parameter listed in
            `self.params_info` for a run to be added to `self.runs`

        Returns
        -------

        """

        if self._active_app is None:
            msg = ("No app is currently set for this campaign. "
                   "Use set_app('name_of_app').")
            logging.error(msg)
            raise Exception(msg)

        app_default_params = self._active_app["params"]

        # Check if parameter names match those already known for this app
        for param in new_run.keys():
            if param not in app_default_params.keys():
                allowed_params_str = ','.join(list(app_default_params.keys()))
                reasoning = (
                    f"dict passed to add_run() contains extra parameter, "
                    f"{param}, which is not a known parameter name "
                    f"of app {self._active_app['name']}.\n"
                    f"The allowed param names for this app appear to be:\n"
                    f"{allowed_params_str}")

                raise RuntimeError(reasoning)

        # If necessary parameter names are missing, fill them in from the
        # default values in params_info
        for param in app_default_params.keys():
            if param not in new_run.keys():
                default_val = app_default_params[param]["default"]
                new_run[param] = default_val

        # Add to run queue
        run_info = RunInfo(app=self._active_app['id'],
                           params=new_run,
                           sample=self._active_sampler_id,
                           campaign=self.campaign_id)
        self.campaign_db.add_run(run_info)

    def add_default_run(self):
        """
        Add a single new run to the queue, using only default values for
        all parameters.
        """

        new_run = {}
        self.add_run(new_run)

    def draw_samples(self, num_samples=0, replicas=1):
        """Draws `num_samples` sets of parameters from the currently set
        sampler, resulting in `num_samples` * `replicas` new runs added to the
        runs list. If `num_samples` is 0 (its default value) then
        this method draws ALL samples from the sampler, until exhaustion (this
        will fail if the sampler is not finite).

        Notes
        -----
        Do NOT use this in cases where you need 'replicas' with a different
        random seed. In those cases need to sample from a uniform_integer
        distribution and filter at analysis step.

        Parameters
        ----------
        num_samples : int
                Number of samples to draw from the active sampling element.
                By default is 0 (draw ALL samples)
        replicas : int
                Number of replica runs to create with each set of parameters.
                Default is 1 - so only a single run added for each set of
                parameters.

        Returns
        -------

        """

        # Make sure `num_samples` is not 0 for an infinite generator
        # (this would add runs forever...)
        if not self._active_sampler.is_finite() and num_samples <= 0:
            msg = (f"Sampling_element '{self._active_sampler.element_name()}' "
                   f"is an infinite generator, therefore a finite number of "
                   f"draws (n > 0) must be specified.")
            raise RuntimeError(msg)

        if replicas < 1:
            msg = "Number of replicas ({replicas}) must be at least 1"
            raise RuntimeError(msg)

        num_added = 0
        for new_run in self._active_sampler:

            for __ in range(replicas):
                self.add_run(new_run)

            num_added += 1
            if num_added == num_samples:
                break

        # Write sampler's new state to database
        self.campaign_db.update_sampler(self._active_sampler_id, self._active_sampler)

        # Log application of this sampling element
        self.log_element_application(
            self._active_sampler, {
                "num_added": num_added})

    def list_runs(self, sampler=None, campaign=None, status=None):
        """Get list of runs in the CampaignDB.

        Returns
        -------

        """
        return list(self.campaign_db.runs(sampler=sampler, campaign=campaign, status=status))

    def scan_completed(self, *args, **kwargs):
        """
        Check campaign database for completed runs (defined as runs with COLLATED status)

        Returns
        -------

        """
        return self.list_runs(status=Status.COLLATED)

    def all_complete(self):
        """
        Check if all runs have reported having output generated by
        a completed simulation.

        Returns
        -------

        """

        num = self.campaign_db.get_num_runs(not_status=Status.COLLATED)
        if num == 0:
            return True
        return False

    def populate_runs_dir(self):
        """Populate run directories based on runs in the CampaignDB.

        This calls the encoder element defined for the current application to
        create input files for it in each run directory, usually with varying
        input (scientific) parameters.

        Returns
        -------

        """

        active_encoder = self._active_app_encoder

        if active_encoder is None:
            raise RuntimeError('Cannot populate runs without valid '
                               'encoder in campaign')

        use_fixtures = active_encoder.fixture_support

        fixtures = self._active_app['fixtures']

        runs_dir = self.campaign_db.runs_dir()

        # Loop through all runs with status NEW
        for run_id, run_data in self.campaign_db.runs(status=Status.NEW):

            # Make run directory
            target_dir = os.path.join(runs_dir, run_id)
            os.makedirs(target_dir)

            # TODO: Check that this isn't insanely inefficient (almost
            #  certainly will be hammering the database for large run lists)
            self.campaign_db.set_dir_for_run(run_id, target_dir)

            if use_fixtures:
                active_encoder.encode(params=run_data['params'],
                                      fixtures=fixtures,
                                      target_dir=target_dir)
            else:
                active_encoder.encode(params=run_data['params'],
                                      target_dir=target_dir)

            self.campaign_db.set_run_statuses([run_id], Status.ENCODED)

    def get_campaign_runs_dir(self):
        """Get the runs directory from the CampaignDB.

        Returns
        -------
        str
            Path in which the runs information will be written.

        """
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

        runs_dir = self.campaign_db.runs_dir()

        # Loop through all runs in this campaign with status ENCODED
        for run_id, run_data in self.campaign_db.runs(status=Status.ENCODED):

            dir_name = os.path.join(runs_dir, run_id)
            print("Applying " + action.__module__ + " to " + dir_name + "...")

            # Run user-specified action on this directory
            action.act_on_dir(dir_name)

    def collate(self):
        """Combine the output from all runs associated with the current app.

        Uses the collation element held in `self._active_collater`.

        Returns
        -------

        """

        # Apply collation element
        num_collated = self._active_collater.collate(self)

        if num_collated < 1:
            logger.warning("No data collected during collation.")

        # Log application of this collation element
        info = {'num_collated': num_collated}
        self.log_element_application(self._active_collater, info)

    def get_collation_result(self):
        return self._active_collater.get_collated_dataframe()

    def apply_analysis(self, analysis):
        """Run the `analysis` element on the output of the last run collation.

        Parameters
        ----------
        analysis : `easyvvuq.analysis.base.BaseAnalysisElement`
            Element that performs a VVUQ analysis on a dataframe summary of
            run outputs.

        Returns
        -------

        """

        # Apply analysis element to most recent collation result
        self.last_analysis = analysis.analyse(data_frame=self.get_collation_result())

        # Log application of this analysis element
        self.log_element_application(analysis, None)

    def get_last_analysis(self):
        """Return the output of the most recently run analysis element.

        Returns
        -------

        """
        if self.last_analysis is None:
            logging.warning("No last analysis output available.")

        return self.last_analysis

    def __str__(self):
        """Returns formatted summary of the current Campaign state.
        Enables class to work with standard print() method"""

        return (f"db_location = {self.db_location}\n"
                f"active_sampler_id = {self._active_sampler_id}\n"
                f"campaign_name = {self.campaign_name}\n"
                f"campaign_dir = {self.campaign_dir}\n"
                f"campaign_id = {self.campaign_id}\n"
                f"log = {self._log}\n")

    def log_element_application(self, element, further_info):
        """Add an entry to the campaign log for the given element.

        The `further_info` dictionary adds detail to the log. The `further_info`
        dict should give specific information about this element's application,
        where suitable.

        Parameters
        ----------
        element
        further_info

        Returns
        -------

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
