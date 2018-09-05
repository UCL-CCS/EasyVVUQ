import sys
import json
import importlib
import collections
from pprint import pprint
import easyvvuq as uq


class Campaign:

    def __init__(self, state_filename=None, *args, **kwargs):

        self._app_info = {}                     # Information needed to run application
        self._params_info = {}                  # Name and description of the model parameters
        self._runs = collections.OrderedDict()  # List of runs that need to be performed by this app
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

        # `input_encoder` used to select encoder used to transfer other `app`
        # information and `params` into application specific input files.
        if "input_encoder" not in input_json["app"]:
            raise RuntimeError("State file 'app' block should contain 'app_name' "
                               "to allow lookup of required encoder")
        else:

            input_encoder = input_json['app']['input_encoder']

            if input_encoder not in uq.app_encoders:
                raise RuntimeError(f'No encoder was found for app_name {input_encoder}')

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
            message = f'Cannot set a new runs directory because there is one already set ({self.app_info["runs_dir"]})'
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

    @app_info.setter
    def runs(self, runs):
        self._runs = runs

    def save_state(self, state_filename):

        output_json = {"app": self.app_info,
                       "params": self.params_info,
                       "runs": self.runs}

        with open(state_filename, "w") as outfile:
            json.dump(output_json, outfile, indent=4)

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

    def add_run_result(self, run_id, result):
        if run_id not in self.runs.keys():
            sys.exit("Attempt to add result for run '" + run_id + "' but there is no such run in this Campaign")
        self.runs[run_id]["result"] = result

    def print(self):
        print("Campaign info:")
        pprint(self.app_info)
        print("Params info:")
        pprint(self.params_info)
        print("Runs:")
        pprint(self.runs)
