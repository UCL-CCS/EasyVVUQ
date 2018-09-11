import os, sys
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
        self.run_number = 0
        self.encoder = None

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

        if "params" not in input_json:
            raise RuntimeError("Input does not contain an 'params' block")

        self.params_info = input_json["params"]

        # `input_encoder` used to select encoder used to transfer other `app`
        # information and `params` into application specific input files.
        if "input_encoder" not in input_json["app"]:
            raise RuntimeError("State file 'app' block should contain "
                               "'app_name' to allow lookup of required encoder")
        else:

            input_encoder = input_json['app']['input_encoder']

            if input_encoder not in uq.app_encoders:
                raise RuntimeError(f'No encoder was found for '
                                   f'app_name {input_encoder}')

            module_location = uq.app_encoders[input_encoder]['module_location']
            encoder_name = uq.app_encoders[input_encoder]['encoder_name']

            module = importlib.import_module(module_location)
            encoder_class_ = getattr(module, encoder_name)
            self.encoder = encoder_class_(self.app_info)

    @property
    def run_dir(self):

        if 'runs_dir' not in self.app_info:
            return None

        return self._app_info['runs_dir']

    @run_dir.setter
    def run_dir(self, run_dir):

        if self.run_dir:

            message = (f'Cannot set a new runs directory because there is one '
                       f'already set ({self.app_info["runs_dir"]})')
            raise RuntimeError(message)

        self._app_info['runs_dir'] = run_dir

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
                       "runs": self.runs}

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
        self.run_number += 1

    def add_run_result(self, run_id, result):
        """Add result entry to existing run in `self.runs`

        Parameters
        ----------
        run_id  : str
            Identifier of run to be modified
        result
            Information on run output to be added to `self.runs`

        Returns
        -------

        """

        if run_id not in self.runs.keys():
            reasoning = (f"Attempt to add result for run {run_id} but there is"
                         f"no such run in this Campaign")
            raise RuntimeError(reasoning)

        self.runs[run_id]["result"] = result

    def __str__(self):
        """Returns formatted summary of the current Campaign state.
        Enables class to work with standard print() method"""

        return "\n".join(["Campaign info:", pprint.pformat(self.app_info, indent=4),
                          "Params info:",   pprint.pformat(self.params_info, indent=4),
                          "Runs:",          pprint.pformat(self.runs, indent=4)])

    def populate_runs_dir(self, prefix='Runs_EASYVVUQ_', default_dir='.'):
        """Populate run directories as specified in the input Campaign object

        This calls the Campaigns encoder object to create input files for the
        specified application in each run directory, usually with varying input
        (scientific) parameters.

        Parameters
        ----------
        prefix      : str
            Text that will appear at the start of each run directories name.
        default_dir : str
            Top level directory where all the run directories will be created.
        Returns
        -------

        """

        # Get application info block and runs block
        runs = self.runs

        # Get application encoder to use

        if self.encoder is None:
            raise RuntimeError('Cannot populate runs without valid '
                               'encoder in campaign')

        encoder = self.encoder

        # Build a temp directory to store run files (unless it already exists)
        if not self.run_dir:
            base_dir = tempfile.mkdtemp(prefix=prefix, dir=default_dir)
            print("Creating temp runs directory: " + base_dir)

            self.run_dir = base_dir

        else:
            base_dir = self.run_dir

        for run_id, run_data in runs.items():
            # Make run directory
            target_dir = os.path.join(base_dir, run_id)
            os.makedirs(target_dir)

            encoder.encode(params=run_data, target_dir=target_dir)

    def apply_for_each_run(self, func):
        """
        For each run in this Campaign's run list, apply the specified function
        

        Parameters
        ----------
        func : function
            The function to be applied to each run directory. func() will
            be called with the run directory path as its only argument.
        Returns
        -------

        """

        if "runs_dir" not in self.app_info.keys():
            raise RuntimeError("Missing 'runs_dir' key (Application info must "
                               "include runs directory path).")
        runs_dir = self.app_info["runs_dir"]

        # Loop through all runs in this campaign
        run_ids = self.runs.keys()
        for run_id in run_ids:
            dir_name = os.path.join(runs_dir, run_id)
            print("Applying " + func.__name__ + " to " + dir_name + "...")

            # Run user-specified function on this directory, and store result
            # back into the Campaign object (if there is a result returned)
            result = func(dir_name)
            if result is not None:
                self.add_run_result(run_id, result)


    def vary_param(self, param_name, dist=None):
        """
        Registers the named parameter as being variable (such as by any applied UQPs)
        """
        if param_name in self._vars.keys():
            print("Param '" + param_name + "' already in list of variables.")
        else:
            self._vars[param_name] = dist

    def get_vars(self):
        return self._vars
