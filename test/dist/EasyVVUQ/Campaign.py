import os, sys
import json
import numpy as np
import collections
from pprint import pprint

class Campaign:
    def __init__(self, state_fname=None):
        self.app_info = {}                    # Information needed to run application
        self.params_info = {}                 # Name and description of the model parameters
        self.runs = collections.OrderedDict() # List of runs that need to be performed by this app
        self.run_number = 0                   # Counter keeping track of what order runs were added

        if state_fname != None:
            self.load_state(state_fname)
            

    def load_state(self, state_fname):
        # Load info from input JSON file
        with open(state_fname, "r") as infile:
            input_json = json.load(infile)

        # Check that it contains an "app" and a "params" block
        if "app" not in input_json.keys():
            sys.exit("Input does not contain an 'app' block")
        if "params" not in input_json.keys():
            sys.exit("Input does not contain an 'params' block")

        # Make sure the app block contains a "wrapper" key
        if "wrapper" not in input_json["app"].keys():
            sys.exit("Input app block should contain a wrapper parameter, designating the wrapper(s) to be used for processing of the given application parameters")

        self.app_info = input_json["app"]
        self.params_info = input_json["params"]

    def save_state(self, state_fname):
        output_json = {"app": self.app_info, "params": self.params_info, "runs": self.runs}
        with open(state_fname, "w") as outfile:
            json.dump(output_json, outfile, indent=8)

    def has_run_dir(self):
        if 'runs_dir' not in self.app_info.keys():
            return False
        return True

    def set_run_dir(self, path):
        if self.has_run_dir() == True:
            sys.exit("Cannot set a new runs directory because there is one already set (" + self.app_info["run_dir"] + ")")
        self.app_info['runs_dir'] = path

    def get_run_dir(self):
        if self.has_run_dir() == False:
            sys.exit("Cannot get run directory path - none has been set for this application.")
        return self.app_info['runs_dir']
 
    def get_params_info(self):
        return self.params_info
    def get_application_info(self):
        return self.app_info
    def get_runs_info(self):
        return self.runs

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

    def print(self):
        print("Campaign info:")
        pprint(self.app_info)
        print("Params info:")
        pprint(self.params_info)
        print("Runs:")
        pprint(self.runs)
