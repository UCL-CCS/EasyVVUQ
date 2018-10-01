import os
import tempfile
import json
import importlib
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

    The `app_info` dictionary needs to contain either a `template` filename or
    `template_txt` string as the source of the application input template.
    Values from the `params` dict are then substituted in by the `encode` method.

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
        with an encoder class from `uq.app_encoders` and inizialized
        dynamically.

    """

    def __init__(self, state_filename=None, *args, **kwargs):

        # Information needed to run application
        self._app_info = {}
        # Name and description of the model parameters
        self._params_info = {}
        # Which parameters can be varied, and what prior distributions they have
        self._vars = {}
        # List of runs that need to be performed by this app
        self._runs = collections.OrderedDict()

        self._data = {}

        self._sample_uqps = []
        self._analysis_uqps = []

        self.run_number = 0
        self.encoder = None
        self.decoder = None

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

        if "params" not in input_json:
            raise RuntimeError("Input does not contain an 'params' block")

        self.params_info = input_json["params"]

        # `input_encoder` used to select encoder used to transfer other `app`
        # information and `params` into application specific input files.
        if "input_encoder" not in input_json["app"]:
            raise RuntimeError("State file 'app' block should contain "
                               "'input_encoder' to allow lookup of required encoder")
        else:

            input_encoder = input_json['app']['input_encoder']

            if input_encoder not in uq.app_encoders:
                raise RuntimeError(f"No encoder found. Looking for "
                                   f"'input_encoder': {input_encoder}")

            module_location = uq.app_encoders[input_encoder]['module_location']
            encoder_name = uq.app_encoders[input_encoder]['encoder_name']

            module = importlib.import_module(module_location)
            encoder_class_ = getattr(module, encoder_name)
            self.encoder = encoder_class_(self.app_info)

        # `output_decoder` used to select decoder used to read simulation output
        if "output_decoder" not in input_json["app"]:
            raise RuntimeError("State file 'app' block should contain "
                               "'output_decoder' to allow lookup of required encoder")
        else:

            output_decoder = input_json['app']['output_decoder']

            if output_decoder not in uq.app_decoders:
                raise RuntimeError(f'No output decoder was found with the name '
                                   f'{output_decoder}')

            module_location = uq.app_decoders[output_decoder]['module_location']
            decoder_name = uq.app_decoders[output_decoder]['decoder_name']

            module = importlib.import_module(module_location)
            decoder_class_ = getattr(module, decoder_name)
            self.decoder = decoder_class_(self.app_info)

    def _setup_campaign_dir(self):

        app_info = self.app_info

        # TODO: Decide if runs should be here
        sub_dirs = ['data', 'analysis']

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

            campaign_dir = tempfile.mkdtemp(prefix='EasyVVUQ_Campaign',
                                            dir='.')
            print(f"Creating Campaign directory: {self.campaign_dir}")
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
    def data(self):

        return self._data

    @data.setter
    def data(self, new_data):

        self._data = new_data

    @property
    def campaign_dir(self):

        if 'campaign_dir' not in self.app_info:
            return None

        return self._app_info['campaign_dir']

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
                       "runs": self.runs,
                       "data": self.data}

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

        # Validate:
        # Check if parameter names match those already known for this app
        for param in new_run.keys():
            if param not in self.params_info.keys():

                reasoning = (f"dict passed to add_run() contains extra {param} "
                             f"parameter which is not a known parameter name "
                             f"of this Campaign.")

                raise RuntimeError(reasoning)

        # If necessary parameter names are missing, fill them in from the default values in params_info
        for param in self.params_info.keys():
            if param not in new_run.keys():
                new_run[param] = self.params_info[param]["default"]

        # Add to run queue
        run_id = f"{prefix}{self.run_number}"
        self.runs[run_id] = new_run
        self.runs[run_id]['completed'] = False
        self.run_number += 1

    def scan_completed(self):
        """
        Check each run in `self.runs` to see if output has been generated by a completed simulation.

        Returns
        -------

        """

        decoder = self.decoder
        runs = self.runs

        for run_id in runs.keys():

            if decoder.sim_complete(run_info=runs[run_id]):
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
                          "Runs:",          pprint.pformat(self.runs, indent=4)])

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
        runs_dir = self.runs_dir

        # Get application encoder to use
        encoder = self.encoder

        if self.encoder is None:
            raise RuntimeError('Cannot populate runs without valid '
                               'encoder in campaign')

        # Build a temp directory to store run files (unless it already exists)
        if not runs_dir:

            runs_dir = os.path.join(self.campaign_dir, 'runs')
            if os.path.exists(runs_dir):
                raise RuntimeError(f"Cannot create a runs directory to populate, as it already exists: {runs_dir}")
            os.makedirs(runs_dir)
            print(f"Creating temp runs directory: {runs_dir}")

        for run_id, run_data in runs.items():
            # Make run directory
            target_dir = os.path.join(runs_dir, run_id)
            # TODO: Should we check if the run has been created?
            runs[run_id]['run_dir'] = 'target_dir'
            os.makedirs(target_dir)

            encoder.encode(params=run_data, target_dir=target_dir)

    def record_sampling(self, primitive_name, primitive_args, success):
        """

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

