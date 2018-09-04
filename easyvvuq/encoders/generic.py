import os
import sys
import json
import tempfile
from string import Template
from .base import BaseEncoder


class GenericEncoder(BaseEncoder):
    """GenericEncoder for substituting values into application template input.

    The `app` dictionary needs to contain either a `template` filename or
    `template_txt` string as the source of the application input template.
    Values from the `params` dict are then substituted in by the `encode` method.

    Parameters
    ----------
    run_info : dict or str or File, optional
        If specifies is used as the source for `app` and `params` dicts. Will
        try interpreting as a dict or JSON file/stream or filename. If not
        specified must have `app` and `params` supplied.
    app      : dict, optional
        Application information, used if no `run_info` provided.
    params   : dict, optional
        Parameters for particular execution of the application, used if no
        `run_info` provided.

    Attributes
    ----------
    app    : dict
        Contains application information.
    params : dict
        Contains parameters for run which need encoding.

    """

    def __init__(self, *args, **kwargs):

        # Handles creation of `self.app` and `self.params` attributes (dicts)
        super().__init__(self, *args, **kwargs)

        app = self.app

        if 'template' in app:

            with open(app['template'], 'r') as template_file:
                template_txt = template_file.read()

            self.template = Template(template_txt)

        elif 'template_txt' in app:

            self.template = Template(app['template_txt'])

        else:

            raise RuntimeError('Template required in "app" specification input to GenericEncoder')

        if 'input_filename' in app:
            self.target_filename = app['input_filename']
        else:
            self.target_filename = 'app_input.txt'

        if 'run_cmd' in self.app:
            self.local_run_cmd = app['run_cmd']
        else:
            self.local_run_cmd = None

        self.app_input_txt = None

    def encode(self):
        """Substitutes `params` into a template application input"""

        template = self.template
        params = self.params
        app = self.app

        str_params = {}

        for key, value in params.items():

            str_params[key] = str(value)

        try:

            self.app_input_txt = template.substitute(str_params)

        except Exception as e:

            if 'template_txt' in app:

                fle, temp_filename = tempfile.mkstemp(text=True)

                with open(temp_filename, 'w') as temp_file:

                    for line in app['template_txt']:
                        temp_file.write(line)

                reasoning = f"\nFailed substituting into template {temp_filename}.\n"

            else:

                reasoning = f"\nFailed substituting into template {app['template']}.\n"

            fle, temp_filename = tempfile.mkstemp(text=True)
            with open(temp_filename, 'w') as temp_params_file:
                json.dump(params, temp_params_file)

            reasoning += f"Parameters written to {temp_params_file}.\n"

            raise Exception(str(e) + reasoning)

    def write_application_files(self):
        """Writes application input created by `encoder` into `target_dir`"""

        target_dir = self.target_dir
        target_filename = self.target_filename
        app_input_txt = self.app_input_txt
        local_run_cmd = self.local_run_cmd

        if not target_dir:
            raise RuntimeError('No target directory specified to encoder')

        if app_input_txt:

            # Write target input file
            target_file_path = os.path.join(target_dir, target_filename)
            with open(target_file_path, 'w') as fp:
                fp.write(app_input_txt)

            # Write execution file
            run_cmd_file_path = os.path.join(target_dir, 'run_cmd.sh')
            with open(run_cmd_file_path, 'w') as fp:
                fp.write(local_run_cmd)

        else:
            raise RuntimeError('No application input created (try encode method)')


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit("Usage: python3 generic_wrapper.py INPUT_JSON_FILE OUTPUT_DIR")

    input_json_file = sys.argv[1]
    output_dir = sys.argv[2]

    encoder = GenericEncoder(run_info=input_json_file, target_dir=output_dir)
    encoder.encode()
    encoder.write_application_files()