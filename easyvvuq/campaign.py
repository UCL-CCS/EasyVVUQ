import os, sys
import json
import importlib
import numpy as np
import collections
from pprint import pprint
import easyvvuq as uq


class Campaign:

    def __init__(self, state_filename=None, *args, **kwargs):

        self.app_info = {}                     # Information needed to run application
        self.params_info = {}                  # Name and description of the model parameters
        self.runs = collections.OrderedDict()  # List of runs that need to be performed by this app
        self.run_number = 0                    # Counter keeping track of what order runs were added
        self.encoder = None

        if state_filename is not None:
            self.load_state(state_filename)

    def load_state(self, state_filename):

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

        # `app_name` used to select encoder used to transfer other `app`
        # information and `params` into application specific input files.
        if "app_name" not in input_json["app"]:
            raise RuntimeError("State file 'app' block should contain 'app_name' "
                               "to allow lookup of required encoder")
        else:

            app_name = input_json['app']['app_name']

            if app_name not in uq.app_encoders:
                raise RuntimeError(f'No encoder was found for app_name {app_name}')

            module_location = uq.app_encoders[app_name]['module_location']
            encoder_name = uq.app_encoders[app_name]['encoder_name']

            module = importlib.import_module(module_location)
            encoder_class_ = getattr(module, encoder_name)
            self.encoder = encoder_class_(self.app_info)

    def save_state(self, state_filename):

        output_json = {"app": self.app_info,
                       "params": self.params_info,
                       "runs": self.runs}

        with open(state_filename, "w") as outfile:
            json.dump(output_json, outfile, indent=4)

    @property
    def run_dir(self):

        if 'runs_dir' not in self.app_info:
            return None

        return self.app_info['runs_dir']

    @run_dir.setter
    def run_dir(self, run_dir):

        if self.run_dir:
            message = f'Cannot set a new runs directory because there is one already set ({self.app_info["runs_dir"]})'
            raise RuntimeError(message)

        self.app_info['runs_dir'] = run_dir
 
    def get_params_info(self):
        return self.params_info

    def get_application_info(self):
        return self.app_info

    def get_runs_info(self):
        return self.runs
    
    def get_run_IDs(self):
        return self.runs.keys()
 
    # Expects a dict defining the value of each model parameter listed in self.params_info
    def add_run(self, new_run_dict):
        # Validate (check if parameter names match those already known for this app)
        for param in self.params_info.keys():
            if param not in new_run_dict.keys():
                sys.exit("dict passed to add_run() is missing the " + param + " parameter.")
        for param in new_run_dict.keys():
            if param not in self.params_info.keys():
                sys.exit("dict passed to add_run() contains extra " + param + " parameter which is not a known parameter name of this Campaign.")

        # Add to run queue
        run_id = "Run_" + str(self.run_number)
        self.runs[run_id] = new_run_dict
        self.run_number += 1

    def add_run_result(self, run_ID, result):
        if run_ID not in self.runs.keys():
            sys.exit("Attempt to add result for run '" + run_ID + "' but there is no such run in this Campaign")
        self.runs[run_ID]["result"] = result

    def print(self):
        print("Campaign info:")
        pprint(self.app_info)
        print("Params info:")
        pprint(self.params_info)
        print("Runs:")
        pprint(self.runs)
