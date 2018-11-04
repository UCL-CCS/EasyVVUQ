import os
import sys
import json
import easyvvuq.utils.json as json_utils
import tempfile
from string import Template
from .base import BaseEncoder

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


def getCustomTemplate(template_txt, custom_delimiter='$'):
    class CustomTemplate(Template):
        delimiter = custom_delimiter
    return CustomTemplate(template_txt)


class GenericEncoder(BaseEncoder, encoder_name = "generic_template"):
    """GenericEncoder for substituting values into application template input.

    The `app_info` dictionary needs to contain either a `template` filename or
    `template_txt` string as the source of the application input template.
    Values from the `params` dict are then substituted in by the `encode` method.

    Parameters
    ----------
    app_info      : dict, dict or str or File
        Application information. Will try interpreting as a dict or JSON
        file/stream or filename.


    Attributes
    ----------
    app_info    : dict
        Contains application information.

    """

    def __init__(self, app_info, *args, **kwargs):

        # Handles creation of `self.app_info` attribute (dicts)
        super().__init__(app_info, *args, **kwargs)
        app_info = self.app_info
        print(app_info)

        # Check if an encoder delimiter is specified in the app_info. Else use $ by default.
        self.encoder_delimiter = '$'
        if 'encoder_delimiter' in app_info:
            self.encoder_delimiter = app_info['encoder_delimiter']

        # Look for the template text ( specified either in a file, or in app_info['template_txt'] )
        if 'template' in app_info:
            with open(app_info['template'], 'r') as template_file:
                template_txt = template_file.read()
            self.template = getCustomTemplate(template_txt, custom_delimiter=self.encoder_delimiter)
        elif 'template_txt' in app_info:
            self.template = getCustomTemplate(app_info['template_txt'], custom_delimiter=self.encoder_delimiter)
        else:
            raise RuntimeError('Template required in "app" specification input to GenericEncoder')

        # Check what name to give the output of this encoder
        if 'input_filename' in app_info:
            self.target_filename = app_info['input_filename']
        else:
            self.target_filename = 'app_input.txt'

        self.app_input_txt = None

    def encode(self, params={}, target_dir=''):
        """Substitutes `params` into a template application input, saves in target_dir

        Parameters
        ----------
        params        : dict, dict or str or File
            Parameter information. Will try interpreting as a dict or JSON
            file/stream or filename.
        target_dir    : str
            Path to directory where application input will be written.
        """

        if not target_dir:
            raise RuntimeError('No target directory specified to encoder')

        if not hasattr(params, 'items'):
            params = json_utils.process_json(params)

        params = self.parse_fixtures_params(params, target_dir)

        str_params = {}
        for key, value in params.items():
            str_params[key] = str(value)

        template = self.template
        target_filename = self.target_filename
        app_input_txt = self.app_input_txt

        try:
            app_input_txt = template.substitute(str_params)
        except KeyError as e:
            # TODO: Should we pass str_params here?
            self._log_substitution_failure(params, e)

        # Write target input file
        target_file_path = os.path.join(target_dir, target_filename)
        with open(target_file_path, 'w') as fp:
            fp.write(app_input_txt)

    def _log_substitution_failure(self, params, exception):
        app_info = self.app_info
        if 'template_txt' in app_info:
            fle, temp_filename = tempfile.mkstemp(text=True)

            with open(temp_filename, 'w') as temp_file:
                for line in app_info['template_txt']:
                    temp_file.write(line)
            reasoning = f"\nFailed substituting into template {temp_filename}.\n"
        else:
            reasoning = f"\nFailed substituting into template {app_info['template']}.\n"

        fle, temp_filename = tempfile.mkstemp(text=True)
        with open(temp_filename, 'w') as temp_params_file:
            json.dump(params, temp_params_file)

        reasoning += f"Parameters used in substitution written to {temp_filename}.\n"

        print(reasoning)
        raise KeyError(exception)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit("Usage: python3 generic_template.py INPUT_JSON_FILE OUTPUT_DIR")

    input_json_file = sys.argv[1]
    output_dir = sys.argv[2]

    encoder = GenericEncoder(params=input_json_file, target_dir=output_dir)
    encoder.encode()
