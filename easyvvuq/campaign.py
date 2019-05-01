import os
import logging
import tempfile
import json
import pprint
import easyvvuq as uq

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
    """Campaign coordinates information for a series of related runs

    Sampling Primitives need to be applied to the object to specify the runs to
    be included in the simulation 'campaign'. Information on each run is stored
    in the `runs` dictionary.

    # TODO: need to make dbtype an Enum

    Parameters
    ----------
    name: str
        Campaign name. Either new name or the name of a campaign to be resumed.
    state_filename  : str
        Path to file containing serialized state of a Campaign in JSON format.
    new_campaign: bool
        If True will start a new campaign. If false will query the database for
        a campaign with the given name. Will raise an exception if it does not
        exist.
    local: bool
        Is this campaign being processed locally - in which case we can check
        files and directories.

    Attributes
    ----------
    run_number    : int
        Counter keeping track of what order runs were added
    encoder
        Encoder for the application input files. Initialized to None and
        with an encoder class from `uq.app_encoders` and initialized
        dynamically.

    """

    def __init__(self, name, state_filename=None, new_campaign=False,
                 local=False, work_dir='.', **kwargs):

        self._log = []

        self.campaign_db = None
        self.db_location = None
        self.db_type = None
        self.campaign_name = name
        self.local = local
        self.state_filename = None
        self.work_dir = '.'

        self._current_app = None

        self._reserved_keys = ['completed', 'fixtures']

        if state_filename is not None:

            self.setup_state(state_filename, new_campaign=new_campaign,
                             name=name)

    def setup_state(self, state_filename, new_campaign=False, name=''):
        """Load Campaign state from file (JSON format)

        Parameters
        ----------
        state_filename : str
            JSON file from which to load the Campaign state
        new_campaign : bool
            Do we need to create a new database or load an old one.
        name :  str
            Name of the campaign of interest or that to be created.

        Returns
        -------

        """

        self.state_filename = state_filename

        # Load info from input JSON file
        with open(state_filename, "r") as infile:
            input_json = json.load(infile)

        if 'db_type' not in input_json:
            logging.warning(f'No db_type specified in {infile} - '
                            f'assuming this is an old style (EasyVVUQ version '
                            f'< 0.0.3) state file.')
            try:
                input_json = self._convert_old_state_file(input_json)
                os.rename(os.path.realpath(state_filename),
                          os.path.realpath(state_filename) + ".bak")
            except IOError as err:
                message = f"State file {state_filename} could not be read: {err}"
                logger.critical(message)
                raise RuntimeError(message)

            db_type = 'json'

        else:
            db_type = input_json['db_type']

        if db_type == 'sql':
            from .db.sql import CampaignDB
        elif db_type == 'json':
            from .db.json import CampaignDB
        else:
            message = f"Invalid 'db_type' {db_type} specified in {state_filename}. Supported types are 'sql' or 'json'."
            logger.critical(message)
            raise RuntimeError(message)

        db_location = input_json.get('db_location', None)

        if db_location is None:
            if db_type == 'json':
                message = (f"No 'db_location' in {state_filename} - cannot create "
                           f"a new campaign database.")
                logger.critical(message)
                raise RuntimeError(message)
            else:
                message = (f"No 'db_location' in {state_filename} - will try"
                           f" default")
                logger.warning(message)

        self.db_type = db_type
        self.db_location = db_location

        if new_campaign:

            info = uq.data_structs.CampaignInfo(**input_json['campaign'],
                                                local=self.local)

            self.campaign_db = CampaignDB(location=db_location,
                                          new_campaign=True,
                                          name=name,
                                          local=self.local,
                                          info=info)

        else:

            self.campaign_db = CampaignDB(location=db_location, name=name,
                                          local=self.local)

        # TODO: Relocate input encoder validation
        # TODO: Decide whether to return to having self.encoder
        # TODO: Relocate output decoder validation
        # TODO: Decide whether to return to having self.decoder

    @staticmethod
    def _convert_old_state_file(input_state, default_prefix='EasyVVUQ_Campaign_'):
        """
        Old state files combined function as a database and workflow restart
        file. Here we refactor the information read from an old state file
        to conform to the organization we use now.

        Parameters
        ----------
        input_state

        Returns
        -------

        """

        try:

            converted = {}

            app_info = input_state['app']
            converted['campaign'] = {}

            for field in ['campaign_dir', 'campaign_dir_prefix', 'runs_dir']:
                if field in app_info:
                    converted['campaign'][field] = app_info.pop(field)

            converted['campaign']['easyvvuq_version'] = '0.0.1'

            converted['app'] = app_info

            converted['runs'] = input_state.get('runs', {})

            converted['sample'] = input_state.get('sample', {})

        except KeyError as err:
            message = f'Input state not valid: {err}'
            raise IOError(message)

        return converted

    def add_app(self, app_info):
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

        Returns
        -------

        """

        # TODO: Need to look at parameters

        # validate application input
        app = uq.data_structs.AppInfo(**app_info)

        self.campaign_db.add_app(app.to_dict())

    def _setup_campaign_dir(self):
        """
        Check if a 'campaign_dir' is found in `self.app_info`. If so use this
        as a top level directory for recording run and analysis information.
        If no directory provided or find it does not exist yet then create.

        Returns
        -------

        """

        campaign_info = self.campaign_db.campaign()

        # TODO: Decide if runs should be here
        sub_dirs = ['data', 'analysis', 'common']

        # Build a temp directory to store run files (unless it already exists)
        if 'campaign_dir' in campaign_info:

            campaign_dir = campaign_info['campaign_dir']
            if not os.path.exists(campaign_dir):
                print(f"Notice: Campaign directory not found "
                      f"- creating {campaign_dir}")
                try:
                    campaign_dir = str(campaign_dir)
                    os.makedirs(campaign_dir)
                except IOError:
                    raise IOError(f"Unable to create campaign directory: "
                                  f"{campaign_dir}")
        else:
            # Check if app_info already contains a prefix to use for the
            # campaign directory. If not, use the default one.
            if 'campaign_dir_prefix' not in self.campaign_info:
                self.campaign_info['campaign_dir_prefix'] = self.default_campaign_dir_prefix

            # Create temp dir for campaign
            campaign_dir = tempfile.mkdtemp(
                prefix=self.app_info['campaign_dir_prefix'], dir=self.workdir)

            print(f"Creating Campaign directory: {campaign_dir}")
            self.campaign_dir = campaign_dir

        campaign_dir = self.campaign_dir
        for sub_dir in sub_dirs:
            sub_path = os.path.join(campaign_dir, sub_dir)
            if not os.path.isdir(sub_path):
                if os.path.exists(sub_path):
                    raise RuntimeError(f"Unable to create sub path {sub_path},"
                                       f" invalid campaign directory.")
                os.makedirs(sub_path)

    @property
    def log(self):
        return self._log

    @property
    def campaign_dir(self):
        if 'campaign_dir' not in self.app_info:
            return None
        return self._app_info['campaign_dir']

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

    @campaign_dir.setter
    def campaign_dir(self, path, force=False):
        if self.campaign_dir and not force:

            message = (f'Cannot set a new runs directory because there is one '
                       f'already set ({self.app_info["campaign_dir"]})')
            raise RuntimeError(message)

        path = os.path.realpath(os.path.expanduser(path))

        self._app_info['campaign_dir'] = path

    @property
    def runs_dir(self):

        if 'runs_dir' not in self.app_info:
            return None

        return self._app_info['runs_dir']

    @runs_dir.setter
    def runs_dir(self, runs_dir):

        if self.runs_dir:

            message = (f'Cannot set a new runs directory because there is one '
                       f'already set ({self.app_info["runs_dir"]})')
            raise RuntimeError(message)

        self._app_info['runs_dir'] = runs_dir

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

        # TODO: Update to new approach

        reserved_keys = self._reserved_keys
        campaign_params = self.params_info.keys()

        # Validate:
        # Check if parameter names match those already known for this app
        for param in new_run.keys():
            if param not in campaign_params and param not in reserved_keys:

                reasoning = (
                    f"dict passed to add_run() contains extra parameter, "
                    f"{param}, which is not a known parameter name "
                    f"of this Campaign.")

                raise RuntimeError(reasoning)

        if 'fixtures' in new_run:
            run_fixtures = new_run['fixtures']
        else:
            run_fixtures = {}

        # If necessary parameter names are missing, fill them in from the
        # default values in params_info
        for param in self.params_info.keys():

            if param not in new_run.keys():

                default_val = self.params_info[param]["default"]
                new_run[param] = default_val

                if self.params_info[param]["type"] == "fixture":
                    run_fixtures[param] = self.fixtures[default_val]
                    new_run[param] = 'EASYVVUQ_FIXTURE'

            elif self.params_info[param]["type"] == "fixture":
                if new_run[param] != 'EASYVVUQ_FIXTURE':
                    run_fixtures[param] = self.fixtures[new_run[param]]
                    new_run[param] = 'EASYVVUQ_FIXTURE'

        # Add to run queue
        run_id = f"{prefix}{self.run_number}"
        self.runs[run_id] = new_run

        self.runs[run_id]['completed'] = False
        self.runs[run_id]['fixtures'] = run_fixtures
        self.run_number += 1

    def add_default_run(self):
        """
        Add a single new run to the queue, using only default values for
        all parameters.
        """

        new_run = {}
        self.add_run(new_run)

    def add_runs(self, sampling_element, max_num=0):

        # Make sure we have a sampling element
        if isinstance(sampling_element,
                      uq.elements.sampling.BaseSamplingElement) is False:
            raise RuntimeError(
                "add_runs() must be passed (an instance of) BaseSamplingElement")

        # Make sure num is not 0 for an infinite generator (this would add runs
        # forever...)
        if sampling_element.is_finite() is False and max_num <= 0:
            raise RuntimeError(
                "sampling_element '" +
                sampling_element.element_name() +
                "' is an infinite generator, therefore a max_num > 0 "
                "must be specified.'")

        num_added = 0
        for run in sampling_element.generate_runs():
            self.add_run(run)
            num_added += 1
            if num_added == max_num:
                break

        self.log_element_application(
            sampling_element, {
                "num_draws_requested": max_num, "num_draws_added": num_added})

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

    def populate_runs_dir(self):
        """Populate run directories as specified in the input Campaign object

        This calls the Campaigns encoder object to create input files for the
        specified application in each run directory, usually with varying input
        (scientific) parameters.

        Parameters
        ----------

        Returns
        -------

        """

        # TODO: Check this makes sense anymore

        # Get application info block and runs block
        runs = self.runs

        # Get application encoder to use
        encoder = self.encoder

        if self.encoder is None:
            raise RuntimeError('Cannot populate runs without valid '
                               'encoder in campaign')

        # Build a temp directory to store run files (unless it already exists)
        if not self.runs_dir:

            self.runs_dir = os.path.join(self.campaign_dir, 'runs')
            runs_dir = self.runs_dir
            if os.path.exists(runs_dir):
                raise RuntimeError(f"Cannot create a runs directory to "
                                   f"populate, as it already exists: "
                                   f"{runs_dir}")
            os.makedirs(runs_dir)
            print(f"Creating temp runs directory: {runs_dir}")

        for run_id, run_data in runs.items():
            # Make run directory
            target_dir = os.path.join(self.runs_dir, run_id)
            # TODO: Should we check if the run has been created?
            runs[run_id]['run_dir'] = target_dir
            os.makedirs(target_dir)

            encoder.encode(params=run_data, target_dir=target_dir)

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
