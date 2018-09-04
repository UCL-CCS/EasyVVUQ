import os
import sys
import json
import easyvvuq.utils.json as json_utils
import tempfile
from string import Template
from .base import BaseEncoder


class GenericEncoder(BaseEncoder):
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

        if 'template' in app_info:

            with open(app_info['template'], 'r') as template_file:
                template_txt = template_file.read()

            self.template = Template(template_txt)

        elif 'template_txt' in app_info:

            self.template = Template(app_info['template_txt'])

        else:

            raise RuntimeError('Template required in "app" specification input to GenericEncoder')

        if 'input_filename' in app_info:
            self.target_filename = app_info['input_filename']
        else:
            self.target_filename = 'app_input.txt'

        if 'run_cmd' in app_info:
            self.local_run_cmd = app_info['run_cmd']
        else:
            self.local_run_cmd = None

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

        str_params = {}

        for key, value in params.items():

            str_params[key] = str(value)

        template = self.template
        target_filename = self.target_filename
        app_input_txt = self.app_input_txt
        local_run_cmd = self.local_run_cmd

        try:

            app_input_txt = template.substitute(str_params)

        except Exception as e:

            # TODO: Should we pass str_params here?
            self._log_substitution_failure(e, params)

        # Write target input file
        target_file_path = os.path.join(target_dir, target_filename)
        with open(target_file_path, 'w') as fp:
            fp.write(app_input_txt)

        # Write execution file
        run_cmd_file_path = os.path.join(target_dir, 'run_cmd.sh')
        with open(run_cmd_file_path, 'w') as fp:
            fp.write(local_run_cmd)

    def _log_substitution_failure(self, exception, params):

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

        reasoning += f"Parameters used in substitution written to {temp_params_file}.\n"

        raise Exception(str(exception) + reasoning)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit("Usage: python3 generic.py INPUT_JSON_FILE OUTPUT_DIR")

    input_json_file = sys.argv[1]
    output_dir = sys.argv[2]

    encoder = GenericEncoder(params=input_json_file, target_dir=output_dir)
    encoder.encode()
