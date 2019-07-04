"""Data structures to ensure consistency during serialization for databases.

"""
import logging
import cerberus
import json

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

class ParamsSpecification:

    def __init__(self, params, appname=None):

        if not isinstance(params, dict):
            msg = "params must be of type 'dict'"
            logger.error(msg)
            raise Exception(msg)

        if not params:
            msg = ("params must not be empty. At least one parameter "
                   "should be specified.")
            logger.error(msg)
            raise Exception(msg)

        # Check each param has a dict as a value, and that dict has a "default" defined
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

        self.params_dict = params
        self.appname = appname

        # Create a validator for the schema defined by params_dict
        self.cerberus_validator = cerberus.Validator(self.params_dict)

    def process_run(self, new_run, verify=True):

        # If necessary parameter names are missing, fill them in from the
        # default values in params_info
        for param in self.params_dict.keys():
            if param not in new_run.keys():
                default_val = self.params_dict[param]["default"]
                new_run[param] = default_val

        if verify:
            # Check if parameter names match those already known for this app
#            for param in new_run.keys():
#                if param not in self.params_dict.keys():
#                    allowed_params_str = ','.join(list(self.params_dict.keys()))
#                    reasoning = (
#                        f"Run dict contains extra parameter, "
#                        f"{param}, which is not a known parameter name "
#                        f"of app {self.appname}.\n"
#                        f"The allowed param names for this app appear to be:\n"
#                        f"{allowed_params_str}")
#                    logger.error(reasoning)
#                    raise RuntimeError(reasoning)

            if not self.cerberus_validator.validate(new_run):
                errors = self.cerberus_validator.errors
                msg = (
                    f"Error during verification of params in added run:\n"
                    f"{new_run}\n"
                    f"Error was:\n"
                    f"{errors}")
                logger.error(msg)
                raise RuntimeError(msg)

        return new_run

    def serialize(self):
        return json.dumps(self.params_dict)

    @staticmethod
    def deserialize(serialized_params):
        return ParamsSpecification(json.loads(serialized_params))
