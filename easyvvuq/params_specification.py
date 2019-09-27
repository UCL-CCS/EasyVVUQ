"""Data structures to ensure consistency during serialization for databases.

"""
import logging
import cerberus
import json
import numpy

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


class EasyVVUQValidator(cerberus.Validator):
    def __init__(self, *args, **kwargs):
        super(EasyVVUQValidator, self).__init__(*args, **kwargs)

        # Add numpy.int64 as an acceptable 'integer' type
        integer_type = cerberus.TypeDefinition('integer', (int, numpy.int64), ())
        cerberus.Validator.types_mapping['integer'] = integer_type

        # Add 'fixture' type (for now, it's expected just to be a string)
        fixture_type = cerberus.TypeDefinition('fixture', (str), ())
        cerberus.Validator.types_mapping['fixture'] = fixture_type


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
        self.cerberus_validator = EasyVVUQValidator(self.params_dict)

    def process_run(self, new_run, verify=True):

        # If necessary parameter names are missing, fill them in from the
        # default values in params_info
        for param in self.params_dict.keys():
            if param not in new_run.keys():
                default_val = self.params_dict[param]["default"]
                new_run[param] = default_val

        # Optionally verify that all params are known for this app, that the types are
        # correct, params are within specified ranges etc. Uses cerberus for this.
        if verify:
            if not self.cerberus_validator.validate(new_run):
                errors = self.cerberus_validator.errors
                msg = (
                    f"Error when verifying the following new run:\n"
                    f"{new_run}\n"
                    f"Identified errors were:\n"
                    f"{errors}\n")

                errors_list = [error[0] for error in self.cerberus_validator.errors.values()]
                if 'unknown field' in errors_list:
                    msg += (
                        f"The allowed parameter names for this app are:\n"
                        f"{list(self.params_dict.keys())}")

                logger.error(msg)
                raise RuntimeError(msg)

        return new_run

    def serialize(self):
        return json.dumps(self.params_dict)

    @staticmethod
    def deserialize(serialized_params):
        return ParamsSpecification(json.loads(serialized_params))
