"""EasyVVUQ Campaign

This module contains the Campaign class that is used to coordinate all
EasyVVUQ workflows.
"""
import os
import json
import logging
import tempfile
import easyvvuq
from concurrent.futures import ProcessPoolExecutor
from easyvvuq.constants import default_campaign_prefix, Status
from easyvvuq.data_structs import RunInfo, CampaignInfo, AppInfo
from easyvvuq.sampling import BaseSamplingElement
from easyvvuq.actions import ActionPool
import easyvvuq.db.sql as db

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
    and the VVUQ algorithms being employed. It also collects data from the simulations
    and can be used to store and resume your state.

    Notes
    -----

    Multiple campaigns can be combined in a CampaignDB. Hence the particular
    campaign we are currently working on will be specified using `campaign_id`.

    Parameters
    ----------
    name: str
        Name of the Campaign. Freely chosen, serves as a human-readable way of distinguishing
        between several campaigns in the same database.
    params: dict, optional
        Description of the parameters to associated with the application. Will be used to create
        an app when creating the campaign. It is also possible to add apps manually using `add_app`
        method of the Campaign class. But this can be a useful shorthand when working with single
        app campaigns. To use this functionality both `params` and `actions` has to be specified.
        The name of this app will be the same as the name of the Campaign.
    actions: Actions, optional
        Actions object associated with an application. See description of the `params` parameter
        for more details.
    db_location: str, optional
        Location of the underlying campaign database - either a path or
        acceptable URI for SQLAlchemy.
    work_dir: str, optional, default='./'
        Path to working directory - used to store campaign directory.
    change_to_state: bool, optional, default=False
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
    _log: list
        The log of all elements that have been applied, with information about
        their application
    campaign_id : int
        ID number for the current campaign in the db.CampaignDB.
    campaign_db: easyvvuq.db.Basedb.CampaignDB
        A campaign database object
    last_analysis:
        The result of the most recent analysis carried out on this campaign
    _active_app: dict
        Info about currently set app
    _active_app_name: str
        Name of currently set app
    _active_sampler_id: int
        The database id of the currently set Sampler object

    Examples
    --------
    A typical instantiation might look like this.

    >>> params = {
            "S0": {"type": "float", "default": 997},
            "I0": {"type": "float", "default": 3},
            "beta": {"type": "float", "default": 0.2},
            "gamma": {"type": "float", "default": 0.04, "min": 0.0, "max": 1.0},
            "iterations": {"type": "integer", "default": 100},
            "outfile": {"type": "string", "default": "output.csv"}
        }
    >>> encoder = uq.encoders.GenericEncoder(template_fname='sir.template', delimiter='$', target_filename='input.json')
    >>> decoder = uq.decoders.SimpleCSV(target_filename='output.csv', output_columns=['I'])
    >>> actions = uq.actions.local_execute(encoder, os.path.abspath('sir') + ' input.json', decoder)
    >>> campaign = uq.Campaign(name='sir', params=params, actions=actions)

    A simplified one (without an app) might look simply like this.

    >>> campaign = Campaign('simple')

    An app then can be added.

    >>> campaign.add_app('simple_app', params=params, actions=actions)
    """

    def __init__(
            self,
            name,
            params=None,
            actions=None,
            db_location=None,
            work_dir="./",
            change_to_state=False,
            verify_all_runs=True
    ):

        self.work_dir = os.path.realpath(os.path.expanduser(work_dir))
        self.verify_all_runs = verify_all_runs

        self.campaign_name = name
        self._campaign_dir = None

        if db_location is None:
            self._campaign_dir = tempfile.mkdtemp(prefix=name, dir=self.work_dir)
            self.db_location = "sqlite:///" + self._campaign_dir + "/campaign.db"
        else:
            self.db_location = db_location

        self.campaign_id = None
        self.campaign_db = None

        self.last_analysis = None

        self._active_app = None
        self._active_app_name = None
        self._active_app_actions = None

        self._active_sampler = None
        self._active_sampler_id = None

        self.init_db(name, self.work_dir)
        self._state_dir = None

        # here we assume that the user wants to add an app
        if (params is not None) and (actions is not None):
            self.add_app(name=name, params=params, actions=actions)

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

    def init_db(self, name, work_dir='.'):
        """Initialize the connection with the database and either resume or create the campaign.

        Parameters
        ----------
        name: str
            Name of the campaign.
        work_dir: str
            Work directory, defaults to cwd.
        """
        self.campaign_db = db.CampaignDB(location=self.db_location)
        if self.campaign_db.campaign_exists(name):
            self.campaign_id = self.campaign_db.get_campaign_id(name)
            self._active_app_name = self.campaign_db.get_active_app()[0].name
            self.campaign_name = name
            self._campaign_dir = self.campaign_db.campaign_dir(name)
            if not os.path.exists(self._campaign_dir):
                message = (f"Campaign directory ({self.campaign_dir}) does not exist.")
                raise RuntimeError(message)
            self._active_sampler_id = self.campaign_db.get_sampler_id(self.campaign_id)
            self._active_sampler = self.campaign_db.resurrect_sampler(self._active_sampler_id)
            self.set_app(self._active_app_name)
            self.campaign_db.resume_campaign(name)
        else:
            if self._campaign_dir is None:
                self._campaign_dir = tempfile.mkdtemp(prefix=name, dir=work_dir)
            info = CampaignInfo(
                name=name,
                campaign_dir_prefix=default_campaign_prefix,
                easyvvuq_version=easyvvuq.__version__,
                campaign_dir=self._campaign_dir)
            self.campaign_db.create_campaign(info)
            self.campaign_name = name
            self.campaign_id = self.campaign_db.get_campaign_id(self.campaign_name)

    def add_app(self, name=None, params=None, actions=None, set_active=True):
        """Add an application to the CampaignDB.

        Parameters
        ----------
        name : str
            Name of the application.
        params : dict
            Description of the parameters to associate with the application.
        actions : Actions
            An instance of Actions containing actions to be executed
        set_active: bool
            Should the added app be set to be the currently active app?
        """
        # Verify input parameters dict
        paramsspec = easyvvuq.ParamsSpecification(params, appname=name)
        # validate application input
        app = AppInfo(
            name=name,
            paramsspec=paramsspec,
            actions=actions,
        )
        self.campaign_db.add_app(app)
        if set_active:
            self.set_app(app.name)

    def set_app(self, app_name):
        """Set active app for the campaign.

        Application information is retrieved from `self.campaign_db`.

        Parameters
        ----------
        app_name: str
            Name of selected app, if `None` given then first app will be
            selected.
        """
        self._active_app_name = app_name
        self._active_app = self.campaign_db.app(name=app_name)
        self.campaign_db.set_active_app(app_name)
        # Resurrect the app encoder, decoder and collation elements
        self._active_app_actions = self.campaign_db.resurrect_app(app_name)

    def replace_actions(self, app_name, actions):
        """Replace actions for an app with a given name.

        Parameters
        ----------
        app_name: str
            Name of the app.
        actions: Actions
            `Actions` instance, will replace the current `Actions` of an app.
        """
        self.campaign_db.replace_actions(app_name, actions)
        self._active_app_actions = actions

    def set_sampler(self, sampler, update=False):
        """Set active sampler.

        Parameters
        ----------
        sampler : Sampler
            Sampler that will be used to create runs for the current campaign.
        update : bool
            If set to True it will not add the sampler to the database, just change
            it as the active sampler.
        """
        self._active_sampler = sampler
        if not update:
            self._active_sampler_id = self.campaign_db.add_sampler(sampler)
            sampler.sampler_id = self._active_sampler_id
        self._active_sampler_id = self._active_sampler.sampler_id
        self.campaign_db.set_sampler(self.campaign_id, self._active_sampler.sampler_id)

    def add_external_runs(self, input_files, output_files, input_decoder, output_decoder):
        """Takes a list of files and adds them to the database. This method is to be
        used when adding runs to the EasyVVUQ database that were not executed using
        EasyVVUQ.

        Parameters
        ----------
        output_files: list of str
            A list of output file paths to be loaded to the database.
        decoder: Decoder
            A decoder that will be used to parse these files.
        """
        inputs = []
        for input_file in input_files:
            input_decoder.target_filename = os.path.basename(input_file)
            params = input_decoder.parse_sim_output({'run_dir': os.path.dirname(input_file)})
            inputs.append(params)
        outputs = []
        for output_file in output_files:
            output_decoder.target_filename = os.path.basename(output_file)
            result = output_decoder.parse_sim_output({'run_dir': os.path.dirname(output_file)})
            outputs.append(result)
        i = 0
        for params, result in zip(inputs, outputs):
            i += 1
            table = db.RunTable(run_name='run_{}'.format(i),
                                app=self._active_app['id'],
                                params=json.dumps(params),
                                status=Status.COLLATED,
                                run_dir=self.get_campaign_runs_dir(),
                                result=json.dumps(result),
                                campaign=self.campaign_id,
                                sampler=self._active_sampler_id)
            self.campaign_db.session.add(table)
            self.campaign_db.session.commit()

    def add_runs(self, runs, mark_invalid=False):
        """Add runs to the database.

        Parameters
        ----------
        runs : list of dicts
            Each dict defines the value of each model parameter listed in
            self.params_info for a run to be added to self.runs
        mark_invalid : bool
            Will mark runs that fail verification as invalid (but will not raise an exception)
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
            status = Status.NEW
            try:
                new_run = app_default_params.process_run(new_run, verify=self.verify_all_runs)
            except RuntimeError:
                if mark_invalid:
                    new_run = app_default_params.process_run(new_run, verify=False)
                    status = Status.INVALID
                else:
                    raise
            # Add to run queue
            run_info = RunInfo(app=self._active_app['id'],
                               params=new_run,
                               sample=self._active_sampler_id,
                               campaign=self.campaign_id,
                               status=status)
            run_info_list.append(run_info)
        self.campaign_db.add_runs(run_info_list, iteration=self._active_sampler.iteration)

    def draw_samples(self, num_samples=0, mark_invalid=False):
        """Draws `num_samples` sets of parameters from the currently set
        sampler, resulting in `num_samples` new runs added to the
        runs list. If `num_samples` is 0 (its default value) then
        this method draws ALL samples from the sampler, until exhaustion (this
        will fail if the sampler is not finite).

        Parameters
        ----------
        num_samples : int
            Number of samples to draw from the active sampling element.
            By default is 0 (draw ALL samples)
        mark_invalid : bool
            If True will mark runs that go outside valid parameter range as INVALID.
            This is useful for MCMC style methods where you want those runs to evaluate
            to low probabilities.
        """
        # Make sure `num_samples` is not 0 for an infinite generator
        # (this would add runs forever...)
        if not self._active_sampler.is_finite() and num_samples <= 0:
            msg = (f"Sampling_element '{self._active_sampler.element_name()}' "
                   f"is an infinite generator, therefore a finite number of "
                   f"draws (n > 0) must be specified.")
            raise RuntimeError(msg)
        num_added = 0
        new_runs = []
        for new_run in self._active_sampler:
            new_runs.append(new_run)
            num_added += 1
            if num_samples != 0 and num_added >= num_samples:
                break
        self.add_runs(new_runs, mark_invalid)
        # Write sampler's new state to database
        self.campaign_db.update_sampler(self._active_sampler_id, self._active_sampler)
        return new_runs

    def list_runs(self, sampler=None, campaign=None, app_id=None, status=None):
        """Get list of runs in the CampaignDB.

        Parameters
        ----------
        sampler: int
            Sampler id to filter for.
        campaign: int
            Campaign id to filter for.
        app_id: int
            App id to filter for.
        status: Status
            Status to filter for.

        Returns
        -------
        list of runs
        """
        return list(self.campaign_db.runs(
            sampler=sampler, campaign=campaign, app_id=app_id, status=status))

    def get_campaign_runs_dir(self):
        """Get the runs directory from the CampaignDB.

        Returns
        -------
        str
            Path in which the runs information will be written.
        """
        return self.campaign_db.runs_dir(self.campaign_name)

    def relocate(self, campaign_dir):
        """Relocate the campaign by specifying a new path where campaign is located.

        Parameters
        ----------
        new_path: str
            new runs directory
        """
        if not os.path.exists(campaign_dir):
            raise RuntimeError("specified directory does not exist: {}".format(campaign_dir))
        self.campaign_db.relocate(campaign_dir, self.campaign_name)

    def execute(self, nsamples=0, pool=None, mark_invalid=False, sequential=False):
        """This will draw samples and execute the Actions on those samples.

        Parameters
        ----------
        nsamples: int
            Number of samples to draw. For infinite samplers or when you want to process
            samples in batches.
        pool: Executor
            A pool object to be used when processing runs (e.g. instance of `ThreadPoolExecutor` or
            `ProcessPoolExecutor`).
        mark_invalid: bool
            Mark runs that go outside the specified input parameter range as INVALID.
        sequential: bool
            Whether to process samples sequentially (sometimes more efficient or you might
            want to avoid the concurrent module for some reason).
        """
        self.draw_samples(nsamples, mark_invalid=mark_invalid)
        action_pool = self.apply_for_each_sample(
            self._active_app_actions, sequential=sequential)
        return action_pool.start(pool=pool)

    def apply_for_each_sample(self, actions, status=Status.NEW, sequential=False):
        """For each run in this Campaign's run list, apply the specified action
        (an object of type Action).

        Parameters
        ----------
        actions: Actions
            Actions to be applied to each relevant run in the database.
        status: Status
            Will apply the Actions only to those runs whose status is as specified.
        sequential: bool
            Whether to process samples sequentially (sometimes more efficient or you might
            want to avoid the concurrent module for some reason).

        Returns
        -------
        ActionPool
            An object containing ActionStatus instances to track action execution.
        """
        # Loop through all runs in this campaign with status ENCODED, and
        # run the specified action on each run's dir
        def inits():
            for run_id, run_data in self.campaign_db.runs(
                    status=status, app_id=self._active_app['id']):
                previous = {}
                previous['run_id'] = run_id
                previous['campaign_dir'] = self._campaign_dir
                previous['rundir'] = run_data['run_dir']
                previous['run_info'] = run_data
                previous['result'] = {}
                previous['collated'] = False
                yield previous
        return ActionPool(self, actions, inits=inits(), sequential=sequential)

    def iterate(self, nsamples=0, pool=None, mark_invalid=False, sequential=False):
        """This is the equivalent of `execute` for methods that rely on the output of the
        previous sampling stage (designed for MCMC, should work for others).

        Parameters
        ----------
        nsamples : int
            Number of samples to draw (during a single iteration).
        pool : Executor
            An Executor instance. For example ThreadPoolExecutor or a Dask Client. Defaults
            to the ThreadPoolExecutor.
        mark_invalid : bool
            Mark runs that go outside the specified input parameter range as INVALID.
        sequential: bool
            Will execute the `Actions` associated with runs sequentially. Might be more
            efficient in some situations.

        Yields
        ------
        ActionPool
            An object containing Futures instances to track action execution.
        """
        while True:
            self.draw_samples(nsamples, mark_invalid=mark_invalid)
            action_pool = self.apply_for_each_sample(
                self._active_app_actions, sequential=sequential)
            yield action_pool.start(pool=pool)
            result = self.get_collation_result(last_iteration=True)
            invalid = self.get_invalid_runs(last_iteration=True)
            ignored_runs = self._active_sampler.update(result, invalid)
            for run_id in ignored_runs:
                self.campaign_db.session.query(db.RunTable).\
                    filter(db.RunTable.id == int(run_id)).\
                    update({'status': easyvvuq.constants.Status.IGNORED})
            self.campaign_db.session.commit()

    def recollate(self):
        """Clears the current collation table, changes all COLLATED status runs
           back to ENCODED, then runs collate() again
        """
        collated_run_ids = list(self.campaign_db.run_ids(status=Status.COLLATED))
        self.campaign_db.set_run_statuses(collated_run_ids, Status.ENCODED)
        self.collate()

    def get_collation_result(self, last_iteration=False):
        """Return dataframe containing all collated results

        Parameters
        ----------
        last_iteration : bool
            Will only return the result of the last iteration.

        Returns
        -------
        DataFrame
            A DataFrame with the simulation results along with the inputs
            used to produce them.
        """
        if last_iteration:
            iteration = self._active_sampler.iteration - 1
        else:
            iteration = -1
        return self.campaign_db.get_results(
            self._active_app['name'],
            self._active_sampler_id,
            status=easyvvuq.constants.Status.COLLATED,
            iteration=iteration)

    def get_invalid_runs(self, last_iteration=False):
        """Return dataframe containing all results marked as INVALID.

        Parameters
        ----------
        last_iteration : bool
            Will only return the result of the last iteration.

        Returns
        -------
        DataFrame
            A DataFrame with the results form simulations that were marked as INVALID.
            These will usually be the ones that went outside the specified parameter ranges.
            These still have to be accounted for in some way by some methods (e.g. MCMC).
        """
        if last_iteration:
            iteration = self._active_sampler.iteration - 1
        else:
            iteration = -1
        return self.campaign_db.get_results(
            self._active_app['name'],
            self._active_sampler_id,
            status=easyvvuq.constants.Status.INVALID,
            iteration=iteration)

    def apply_analysis(self, analysis):
        """Run the `analysis` element on the output of the last run collation.

        Parameters
        ----------
        analysis : Analysis
            Element that performs a VVUQ analysis on a dataframe summary of
            run outputs.
        """
        # Apply analysis element to most recent collation result
        self.last_analysis = analysis.analyse(data_frame=self.get_collation_result())

    def analyse(self, **kwargs):
        """If available will call an appropriate analysis class on the collation result.

        Parameters
        ----------
        **kwargs : dict
            Argument to the analysis class constructor (after sampler).

        Returns
        -------
        AnalysisResults
            An object representing analysis results. Can be used to interact with those results
            in some way. Plot, retrieve surrogate models and so on.
            See `easyvvuq.analysis.AnalysisResults` for further information.
        """
        collation_result = self.get_collation_result()
        try:
            analysis = self._active_sampler.analysis_class(sampler=self._active_sampler, **kwargs)
            return analysis.analyse(collation_result)
        except NotImplementedError:
            raise RuntimeError("This sampler does not have a corresponding analysis class")

    def get_last_analysis(self):
        """Return the output of the most recently run analysis element.
        """
        if self.last_analysis is None:
            logging.warning("No last analysis output available.")
        return self.last_analysis

    def __str__(self):
        """Returns formatted summary of the current Campaign state.
        Enables class to work with standard print() method
        """
        return (f"db_location = {self.db_location}\n"
                f"active_sampler_id = {self._active_sampler_id}\n"
                f"campaign_name = {self.campaign_name}\n"
                f"campaign_dir = {self.campaign_dir}\n"
                f"campaign_id = {self.campaign_id}\n")

    def get_active_sampler(self):
        """Return the active sampler element in use by this campaign.

        Returns
        -------
        The sampler currently in use
        """

        return self._active_sampler

    def ignore_runs(self, list_of_run_IDs):
        """Flags the specified runs to be IGNORED in future collation. Note that
        this does NOT remove previously collated results from the collation table.
        For that you must refresh the collation by running recollate().

        Parameters
        ----------
        list
            The list of run IDs for the runs that should be set to status IGNORED
        """
        self.campaign_db.set_run_statuses(list_of_run_IDs, Status.IGNORED)

    def rerun(self, list_of_run_IDs):
        """Sets the status of the specified runs to ENCODED, so that their results
        may be recollated later (presumably after extending, rerunning or otherwise
        modifying the data in the relevant run folder). Note that this method will
        NOT perform any execution - it simply flags the run in EasyVVUQ as being
        uncollated. Actual execution is (as usual) the job of the user or middleware.

        Parameters
        ----------
        list
            The list of run IDs for the runs that should be set to status ENCODED
        """

        for run_ID in list_of_run_IDs:
            status = self.campaign_db.get_run_status(run_ID)
            if status == Status.NEW:
                msg = (f"Cannot rerun {run_ID} as it has status NEW, and must"
                       f"be encoded before execution.")
                raise RuntimeError(msg)
        self.campaign_db.set_run_statuses(list_of_run_IDs, Status.ENCODED)

    def get_active_app(self):
        """Returns a dict of information regarding the application that is currently
        set for this campaign.
        """
        return self._active_app
