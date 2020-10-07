"""EasyVVUQ Campaign

This module contains the Campaign class that is used to coordinate all
EasyVVUQ workflows.
"""
import os
import logging
import tempfile
import json
import easyvvuq
from easyvvuq import ParamsSpecification
from easyvvuq.constants import default_campaign_prefix, Status
from easyvvuq.data_structs import RunInfo, CampaignInfo, AppInfo
from easyvvuq.sampling import BaseSamplingElement
from easyvvuq.actions import ActionStatuses

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

    Parameters
    ----------
    name : :obj:`str`, optional
        Description of `param1`.
    db_type : str, default="sql"
        Type of database to use for CampaignDB.
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
    verify_all_runs: bool, optional, default=True
        Check all new runs being added for unrecognised params (not defined for the currently set
        app), values lying within defined physical range, type checking etc. This should normally
        always be set to True, but in cases where the performance is too degraded, the checks can
        be disabled by setting to False.

    Attributes
    ----------
    campaign_name : str or None
        Name for the campaign/workflow.
    _campaign_dir: str or None
        Path to the directory campaign uses for local storage (runs inputs etc)
    db_location : str or None
        Location of the underlying campaign database - either a path or
        acceptable URI for SQLAlchemy.
    db_type : str or None
        Type of CampaignDB ("sql").
    _log: list
        The log of all elements that have been applied, with information about
        their application
    campaign_id : int
        ID number for the current campaign in the CampaignDB.
    campaign_db: easyvvuq.db.BaseCampaignDB
        A campaign database object
    last_analysis:
        The result of the most recent analysis carried out on this campaign
    _active_app: dict
        Info about currently set app
    _active_app_name: str
        Name of currently set app
    _active_app_encoder: easyvvuq.encoders.BaseEncoder
        The current Encoder object being used, from the currently set app
    _active_app_decoder: easyvvuq.decoders.BaseDecoder
        The current Decoder object being used, from the currently set app
    _active_app_collater: easyvvuq.collate.BaseCollationElement
        The current Collater object assigned to this campaign
    _active_sampler: easyvvuq.sampling.BaseSamplingElement
        The currently set Sampler object
    _active_sampler_id: int
        The database id of the currently set Sampler object

    """

    def __init__(
            self,
            name=None,
            db_type="sql",
            db_location=None,
            work_dir="./",
            state_file=None,
            change_to_state=False,
            verify_all_runs=True
    ):

        self.work_dir = os.path.realpath(os.path.expanduser(work_dir))
        self.verify_all_runs = verify_all_runs

        self.campaign_name = name
        self._campaign_dir = None
        self.db_location = db_location
        self.db_type = db_type
        self._log = []

        self.campaign_id = None
        self.campaign_db = None

        self.last_analysis = None

        self._active_app = None
        self._active_app_name = None
        self._active_app_encoder = None
        self._active_app_decoder = None
        self._active_app_collater = None

        self._active_sampler = None
        self._active_sampler_id = None

        # Load campaign from state_file, if provided. Else make a fresh new
        # campaign with a new campaign database
        if state_file is not None:
            self._state_dir = self.init_from_state_file(state_file)
            if change_to_state:
                os.chdir(self._state_dir)
        else:
            self.init_fresh(name, db_type, db_location, self.work_dir)
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
            Database type - current options are 'sql'.
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
        campaign_prefix = default_campaign_prefix
        if name is not None:
            campaign_prefix = name

        campaign_dir = tempfile.mkdtemp(prefix=campaign_prefix, dir=work_dir)

        self._campaign_dir = os.path.relpath(campaign_dir, start=work_dir)

        self.db_location = db_location
        self.db_type = db_type

        if self.db_type == 'sql':
            from .db.sql import CampaignDB
            if self.db_location is None:
                self.db_location = "sqlite:///" + self.campaign_dir + "/campaign.db"
        else:
            message = (f"Invalid 'db_type' {db_type}. Supported types are "
                       f"'sql'.")
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
        else:
            message = (f"Invalid 'db_type' {self.db_type}. Supported types "
                       f"are 'sql'.")
            logger.critical(message)
            raise RuntimeError(message)

        logger.info(f"Opening session with CampaignDB at {self.db_location}")
        self.campaign_db = CampaignDB(location=self.db_location,
                                      new_campaign=False,
                                      name=self.campaign_name)
        campaign_db = self.campaign_db
        self.campaign_id = campaign_db.get_campaign_id(self.campaign_name)

        # Resurrect the sampler
        self._active_sampler_id = campaign_db.get_sampler_id(self.campaign_id)
        self._active_sampler = campaign_db.resurrect_sampler(self._active_sampler_id)

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
        self._active_app_name = input_json["active_app"]
        self.campaign_name = input_json["campaign_name"]
        self._campaign_dir = input_json["campaign_dir"]
        self._log = input_json["log"]

        if not os.path.exists(self.campaign_dir):
            message = (f"Campaign directory in state_file {state_filename}"
                       f" ({self.campaign_dir}) does not exist.")
            logger.critical(message)
            raise RuntimeError(message)

    def add_app(self, name=None, params=None,
                encoder=None, decoder=None, collater=None,
                set_active=True):
        """Add an application to the CampaignDB.

        Parameters
        ----------
        name : str
            Name of the application.
        params : dict
            Description of the parameters to associate with the application.
        encoder : :obj:`easyvvuq.encoders.base.BaseEncoder`
            Encoder element to convert parameters into application run inputs.
        decoder : :obj:`easyvvuq.decoders.base.BaseDecoder`
            Decoder element to convert application run output into data for
            VVUQ analysis.
        collater : obj:`easyvvuq.collate.base.BaseCollationElement`
            Collation element for this app.
        set_active: bool
            Should the added app be set to be the currently active app?

        Returns
        -------

        """

        # Verify input parameters dict
        paramsspec = ParamsSpecification(params, appname=name)

        # validate application input
        app = AppInfo(
            name=name,
            paramsspec=paramsspec,
            encoder=encoder,
            decoder=decoder,
            collater=collater
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

        # Resurrect the app encoder, decoder and collation elements
        (self._active_app_encoder,
         self._active_app_decoder,
         self._active_app_collater) = self.campaign_db.resurrect_app(app_name)

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
        self.campaign_db.set_sampler(self.campaign_id, self._active_sampler_id)

    def add_runs(self, runs):
        """Add a new run to the queue.

        Parameters
        ----------
        runs : list of dicts
            Each dict defines the value of each model parameter listed in
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

        run_info_list = []
        for new_run in runs:

            if new_run is None:
                msg = ("add_run() was passed new_run of type None. Bad sampler?")
                logging.error(msg)
                raise Exception(msg)

            # Verify and complete run with missing/default param values
            new_run = app_default_params.process_run(new_run, verify=self.verify_all_runs)

            # Add to run queue
            run_info = RunInfo(app=self._active_app['id'],
                               params=new_run,
                               sample=self._active_sampler_id,
                               campaign=self.campaign_id)

            run_info_list.append(run_info)

        self.campaign_db.add_runs(run_info_list)

    def add_default_run(self):
        """
        Add a single new run to the queue, using only default values for
        all parameters.
        """

        new_run = {}
        self.add_runs([new_run])

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

            list_of_runs = [new_run for i in range(replicas)]
            self.add_runs(list_of_runs)

            num_added += 1

            if num_samples != 0 and num_added >= num_samples:
                break

        # Write sampler's new state to database
        self.campaign_db.update_sampler(self._active_sampler_id, self._active_sampler)

        # Log application of this sampling element
        self.log_element_application(self._active_sampler,
                                     {"num_added": num_added, "replicas": replicas})

    def list_runs(self, sampler=None, campaign=None, status=None):
        """Get list of runs in the CampaignDB.

        Returns
        -------
            list of runs

        """
        return list(self.campaign_db.runs(sampler=sampler, campaign=campaign, status=status))

    def scan_completed(self, *args, **kwargs):
        """
        Check campaign database for completed runs (defined as runs with COLLATED status)

        Returns
        -------
            list of runs

        """
        return self.list_runs(status=Status.COLLATED)

    def all_complete(self):
        """
        Check if all runs have reported having output generated by
        a completed simulation.

        Returns
        -------
            list of runs

        """

        num = self.campaign_db.get_num_runs(not_status=Status.COLLATED)
        if num == 0:
            return True
        return False

    def populate_runs_dir(self):
        """Populate run directories based on runs in the CampaignDB.

        This calls the encoder element defined for the current application to
        create input files for it in each run directory, usually with varying
        input (scientific) parameters. Note that this method will also create
        the directories in the file system. The directory names will be formed
        in relation to the work_dir argument you have specified when creating
        the Campaign object.

        Returns
        -------

        """

        # Get the encoder for this app. If none is set, only the directory structure
        # will be created.
        active_encoder = self._active_app_encoder
        if active_encoder is None:
            logger.warning('No encoder set for this app. Creating directory structure only.')

        run_ids = []

        for run_id, run_data in self.campaign_db.runs(
                status=Status.NEW, app_id=self._active_app['id']):

            # Make directory for this run's output
            os.makedirs(run_data['run_dir'])

            # Encode run
            if active_encoder is not None:
                active_encoder.encode(params=run_data['params'],
                                      target_dir=run_data['run_dir'])

            run_ids.append(run_id)
        self.campaign_db.set_run_statuses(run_ids, Status.ENCODED)

    def get_campaign_runs_dir(self):
        """Get the runs directory from the CampaignDB.

        Returns
        -------
        str
            Path in which the runs information will be written.

        """
        return self.campaign_db.runs_dir()

    def call_for_each_run(self, fn, status=Status.ENCODED):

        # Loop through all runs in this campaign with the specified status,
        # and call the specified user function for each.
        for run_id, run_data in self.campaign_db.runs(status=status, app_id=self._active_app['id']):
            fn(run_id, run_data)

    def apply_for_each_run_dir(self, action, status=Status.ENCODED, batch_size=1):
        """
        For each run in this Campaign's run list, apply the specified action
        (an object of type Action)

        Parameters
        ----------
        action : the action to be applied to each run directory
            The function to be applied to each run directory. func() will
            be called with the run directory path as its only argument.
        status : Status
            Will apply the action only to those runs whose status is as specified

        Returns
        -------
        action_statuses: ActionStatuses
            An object containing ActionStatus instances to track action execution
        """

        # Loop through all runs in this campaign with status ENCODED, and
        # run the specified action on each run's dir
        assert(isinstance(status, Status))
        action_statuses = []
        for run_id, run_data in self.campaign_db.runs(status=status, app_id=self._active_app['id']):
            action_statuses.append(action.act_on_dir(run_data['run_dir']))
        return ActionStatuses(action_statuses, batch_size=batch_size)

    def sample_and_apply(self, nsamples, action, batch_size):
        """This will draw samples, populated the runs directories and run the specified action.
        This is a convenience method.

        Parameters
        ----------
        nsamples : int
            number of samples to draw
        action : BaseAction
            an action to be executed
        batch_size : int
            number of actions to be executed at the same time

        Returns
        -------
        action_statuses: ActionStatuses
            An object containing ActionStatus instances to track action execution
        """
        self.draw_samples(nsamples)
        self.populate_runs_dir()
        action_statuses = self.apply_for_each_run_dir(action, batch_size=batch_size)
        return action_statuses

    def collate(self):
        """Combine the output from all runs associated with the current app.

        Uses the collation element held in `self._active_app_collater`.

        Returns
        -------

        """

        # Apply collation element
        num_collated = self._active_app_collater.collate(self, self._active_app['id'])

        if num_collated < 1:
            logger.warning("No data collected during collation.")

        # Log application of this collation element
        info = {'num_collated': num_collated}
        self.log_element_application(self._active_app_collater, info)

    def clear_collation(self):
        self.campaign_db.clear_collation(self._active_app['id'])

    def recollate(self):
        """Clears the current collation table, changes all COLLATED status runs
           back to ENCODED, then runs collate() again

        Returns
        -------

        """

        self.clear_collation()
        collated_run_ids = list(self.campaign_db.run_ids(status=Status.COLLATED))
        self.campaign_db.set_run_statuses(collated_run_ids, Status.ENCODED)
        self.collate()

    def get_collation_result(self):
        """
        Return dataframe containing all collated results

        Parameters
        ----------

        Returns
        -------
            pandas dataframe

        """
        return self._active_app_collater.get_collated_dataframe(self, self._active_app['id'])

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
        """
        Return the output of the most recently run analysis element.

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

    def get_active_sampler(self):
        """ Return the active sampler element in use by this campaign.

        Parameters
        ----------

        Returns
        -------
        The sampler currently in use
            easyvvuq.sampling.base.BaseSamplingElement

        """

        return self._active_sampler

    def ignore_runs(self, list_of_run_IDs):
        """ Flags the specified runs to be IGNORED in future collation. Note that
        this does NOT remove previously collated results from the collation table.
        For that you must refresh the collation by running recollate().

        Parameters
        ----------
        list_of_run_IDs: list
            The list of run IDs for the runs that should be set to status IGNORED


        Returns
        -------

        """
        self.campaign_db.set_run_statuses(list_of_run_IDs, Status.IGNORED)

    def rerun(self, list_of_run_IDs):
        """ Sets the status of the specified runs to ENCODED, so that their results
        may be recollated later (presumably after extending, rerunning or otherwise
        modifying the data in the relevant run folder). Note that this method will
        NOT perform any execution - it simply flags the run in EasyVVUQ as being
        uncollated. Actual execution is (as usual) the job of the user or middleware.

        Parameters
        ----------
        list_of_run_IDs: list
            The list of run IDs for the runs that should be set to status ENCODED


        Returns
        -------

        """

        for run_ID in list_of_run_IDs:
            status = self.campaign_db.get_run_status(run_ID)
            if status == Status.NEW:
                msg = (f"Cannot rerun {run_ID} as it has status NEW, and must"
                       f"be encoded before execution.")
                raise RuntimeError(msg)

        self.campaign_db.set_run_statuses(list_of_run_IDs, Status.ENCODED)

    def get_active_app(self):
        """
        Returns a dict of information regarding the application that is currently
        set for this campaign.
        """
        return self._active_app
