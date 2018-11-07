import os
import tempfile
import json
import collections
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


class Campaign:
    """Campaign coordinates information for a series of related runs

    Campaign stores information about the practical elements of creating
    simulation runs the `app_info` dictionary and information defining the
    potential values for parameters and settings in `params_info`. The
    information from both is combined to form inputs to simulation codes via
    an `encoder`.

    Sampling Primitives need to be applied to the object to specify the runs to
    be included in the simulation 'campaign'. Information on each run is stored
    in the `runs` dictionary.

    Parameters
    ----------
    state_filename  : str
        Path to file containing serialized state of a Campaign in JSON format

    Attributes
    ----------
    run_number    : int
        Counter keeping track of what order runs were added
    encoder
        Encoder for the application input files. Initialized to None and
        with an encoder class from `uq.app_encoders` and initialized
        dynamically.

    """

    def __init__(self, state_filename=None, workdir='./', default_campaign_dir_prefix='EasyVVUQ_Campaign_', *args, **kwargs):

        # Information needed to run application
        self._app_info = {}
        # Name and description of the model parameters
        self._params_info = {}
        # Files and directories that are required by runs
        self._fixtures = {}
        # Which parameters can be varied, and what prior distributions they have
        self._vars = {}
        # Categorical variables
        self._categoricals = {}

        # List of runs that need to be performed by this app
        self._runs = collections.OrderedDict()

        self._data = {}

        self._sample_uqps = []
        self._analysis_uqps = []

        self.run_number = 0
        self.encoder = None
        self.decoder = None

        self._reserved_keys = ['completed', 'fixtures']

        self.workdir = workdir
        self.default_campaign_dir_prefix = default_campaign_dir_prefix

        if state_filename is not None:
            self.load_state(state_filename)

    def load_state(self, state_filename):
        """Load Campaign state from file (JSON format)

        Parameters
        ----------
        state_filename  : str
            JSON file from which to load the Campaign state

        Returns
        -------

        """

        # Load info from input JSON file
        with open(state_filename, "r") as infile:
            input_json = json.load(infile)

        # Check that it contains an "app" and a "params" block
        if "app" not in input_json:
            raise RuntimeError("Input does not contain an 'app' block")

        self.app_info = input_json["app"]

        # Check for campaign directory - if doesn't exist create one
        self._setup_campaign_dir()

        if "sample_uqps" in input_json:
            self._sample_uqps = input_json["sample_uqps"]

        if "analysis_uqps" in input_json:
            self._sample_uqps = input_json["analysis_uqps"]

        if "params" not in input_json:
            raise RuntimeError("Input does not contain an 'params' block")

        self.params_info = input_json["params"]

        if "fixtures" in input_json:
            self._fixtures = input_json["fixtures"]

        # `input_encoder` used to select encoder used to transfer other `app`
        # information and `params` into application specific input files.
        if "input_encoder" not in input_json["app"]:
            raise RuntimeError("State file 'app' block should contain "
                               "'input_encoder' to allow lookup of required encoder")
        else:
            input_encoder = input_json['app']['input_encoder']
            available_encoders = uq.encoders.base.available_encoders
            if input_encoder not in available_encoders:
                raise RuntimeError(f"No encoder found. Looking for "
                                   f"'input_encoder': {input_encoder}\n"
                                   f"Available encoders are:\n"
                                   f"{available_encoders}")

            encoder_class = available_encoders[input_encoder]
            self.encoder = encoder_class(self.app_info)

        # `output_decoder` used to select decoder used to read simulation output
        if "output_decoder" not in input_json["app"]:
            raise RuntimeError("State file 'app' block should contain "
                               "'output_decoder' to allow lookup of required decoder")
        else:

            output_decoder = input_json['app']['output_decoder']
            available_decoders = uq.decoders.base.available_decoders

            if output_decoder not in available_decoders:
                raise RuntimeError(f'No output decoder was found with the name '
                                   f'{output_decoder}\n'
                                   f"Available decoders are:\n"
                                   f"{available_decoders}")

            decoder_class = available_decoders[output_decoder]
            self.decoder = decoder_class(self.app_info)

    def _setup_campaign_dir(self):
        """
        Check if a 'campaign_dir' is found in `self.app_info`. If so use this as
        top level directory for recording run and analysis information. If no
        directory provided or find it does not exist yet then create.

        Returns
        -------

        """

        app_info = self.app_info

        # TODO: Decide if runs should be here
        sub_dirs = ['data', 'analysis', 'common']

        # Build a temp directory to store run files (unless it already exists)
        if 'campaign_dir' in app_info:

            campaign_dir = app_info['campaign_dir']
            if not os.path.exists(campaign_dir):
                print(f"Notice: Campaign directory not found - creating {campaign_dir}")
                try:
                    campaign_dir = str(campaign_dir)
                    os.makedirs(campaign_dir)
                except IOError:
                    raise IOError(f"Unable to create campaign directory: {campaign_dir}")
        else:
            # Check if app_info already contains a prefix to use for the campaign directory. If not, use the default one.
            if 'campaign_dir_prefix' not in self.app_info:
                self.app_info['campaign_dir_prefix'] = self.default_campaign_dir_prefix
            
            # Create temp dir for campaign
            campaign_dir = tempfile.mkdtemp(prefix=self.app_info['campaign_dir_prefix'],
                                            dir=self.workdir)

            print(f"Creating Campaign directory: {campaign_dir}")
            self.campaign_dir = campaign_dir

        campaign_dir = self.campaign_dir
        for sub_dir in sub_dirs:
            sub_path = os.path.join(campaign_dir, sub_dir)
            if not os.path.isdir(sub_path):
                if os.path.exists(sub_path):
                    raise RuntimeError(f"Unable to create sub path {sub_path}, "
                                       f"invalid campaign directory.")
                os.makedirs(sub_path)

    @property
    def sample_uqps(self):
        return tuple(self._sample_uqps)

    @property
    def analysis_uqps(self):
        return tuple(self._analysis_uqps)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def fixtures(self):
        return self._fixtures

    @property
    def campaign_dir(self):
        if 'campaign_dir' not in self.app_info:
            return None
        return self._app_info['campaign_dir']

    def campaign_ID(self, without_prefix=False):

        # The "ID" of the campaign is just the name of the campaign directory (without the trailing slash)
        campaign_ID = os.path.basename(os.path.normpath(self.app_info['campaign_dir']))

        if without_prefix == False:
            return campaign_ID
        else:
            # Ignore the prefix at the start of the string.
            prefix = self.app_info['campaign_dir_prefix']
            if campaign_ID.startswith(prefix):
                return campaign_ID[len(prefix):]
            else:
                print(f"Warning: campaign_ID() called with option without_prefix set, but prefix {prefix} was not found at the start of campaign_ID {campaign_ID}.")
                return campaign_ID

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

    @property
    def params_info(self):
        return self._params_info

    @params_info.setter
    def params_info(self, info):

        reserved_keys = self._reserved_keys

        disallowed_keys = set(reserved_keys).intersection(info.keys())
        if disallowed_keys:
            raise RuntimeError(f'The keys {reserved_keys} are not allowed in the '
                               f'params dictionary , we found: {disallowed_keys}')

        self._params_info = info

    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, info):
        self._app_info = info

    @property
    def runs(self):
        return self._runs

    @runs.setter
    def runs(self, runs):
        self._runs = runs

    @property
    def vars(self):
        return self._vars

    @vars.setter
    def vars(self, variables):
        self._vars = variables

    def save_state(self, state_filename):
        """Save the current Campaign state to file in JSON format

        Parameters
        ----------
        state_filename  :   str
            Name of file in which to save the state

        Returns
        -------

        """

        output_json = {"app": self.app_info,
                       "params": self.params_info,
                       "fixtures": self.fixtures,
                       "runs": self.runs,
                       "sample_uqps": self._sample_uqps,
                       "analysis_uqps": self._analysis_uqps,
                       "data": self.data,
                       }

        with open(state_filename, "w") as outfile:
            json.dump(output_json, outfile, indent=4)

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

        reserved_keys = self._reserved_keys
        campaign_params = self.params_info.keys()

        # Validate:
        # Check if parameter names match those already known for this app
        for param in new_run.keys():
            if param not in campaign_params and param not in reserved_keys:

                reasoning = (f"dict passed to add_run() contains extra parameter, "
                             f"{param}, which is not a known parameter name "
                             f"of this Campaign.")

                raise RuntimeError(reasoning)

        if 'fixtures' in new_run:
            run_fixtures = new_run['fixtures']
        else:
            run_fixtures = {}

        # If necessary parameter names are missing, fill them in from the default values in params_info
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

    def add_default_run(self, prefix='Run_'):
        """Add a single new run to the queue, using only default values for all parameters

        Parameters
        ----------
        prefix      : str
            Prepended to the key used to identify the run in `self.runs`

        Returns
        -------

        """

        new_run = {}
        self.add_run(new_run)


    def scan_completed(self, *args, **kwargs):
        """
        Check each run in `self.runs` to see if output has been generated by a completed simulation.

        Returns
        -------

        """

        decoder = self.decoder
        runs = self.runs

        for run_id in runs.keys():

            if decoder.sim_complete(run_info=runs[run_id], *args, **kwargs):
                runs[run_id]['completed'] = True

    def all_complete(self):
        """
        Check if all runs have reported having output generated by a completed simulation.

        Returns
        -------

        """

        completed = [run_info['completed'] for run_id, run_info in self.runs.items()]

        return all(completed)

    def __str__(self):
        """Returns formatted summary of the current Campaign state.
        Enables class to work with standard print() method"""

        return "\n".join(["Campaign info:", pprint.pformat(self.app_info, indent=4),
                          "Params info:",   pprint.pformat(self.params_info, indent=4),
                          "Runs:",          pprint.pformat(self.runs, indent=4),
                          "Data:", pprint.pformat(self.data, indent=4)])

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
                raise RuntimeError(f"Cannot create a runs directory to populate, as it already exists: {runs_dir}")
            os.makedirs(runs_dir)
            print(f"Creating temp runs directory: {runs_dir}")

        for run_id, run_data in runs.items():
            # Make run directory
            target_dir = os.path.join(self.runs_dir, run_id)
            # TODO: Should we check if the run has been created?
            runs[run_id]['run_dir'] = target_dir
            os.makedirs(target_dir)

            encoder.encode(params=run_data, target_dir=target_dir)

    def record_sampling(self, primitive_name, primitive_args, success):
        """
        Add information about sampling primitives applied to this Campaign to
        `self._sample_uqps`.

        Parameters
        ----------
        primitive_name:     str
            Name of the primitive applied.
        primitive_args:     dictionary
            Arguments passed to the primitive.
        success:            bool
            Did the primitive run successfully.

        Returns
        -------

        """

        # TODO: Need some checks + potentially warnings here
        self._sample_uqps.append((primitive_name, primitive_args, success))

    def vary_param(self, param_name, dist=None):
        """
        Registers the named parameter as being variable (such as by any applied UQPs)
        """
        if param_name in self._vars.keys():
            print("Param '" + param_name + "' already in list of variables.")
        else:
            self._vars[param_name] = dist

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

        info = {
                'primitive': primitive,
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
        For each run in this Campaign's run list, apply the specified action (an object of type Action)

        Parameters
        ----------
        object : the action to be applied to each run directory
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
