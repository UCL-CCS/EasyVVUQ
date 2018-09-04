import os
import json
import tempfile
from string import Template


class BaseEncoder(object):
    """Baseclass for all EasyVVUQ encoders.

    Skeleton encoder which establishes the format and provides the basis of our
    contract - take in ``app`` and ``params`` information, provide a ``encode``
    method to parse these and encode in application input files, and a
    ``write_application_files`` method to write those in a specified location.

    TODO: If we end up converting Attributed to Properties with ``@property``
    of Kristof style ``@advanced_property`` decorators then they should be
    documented in the property's getter method.

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

        run_info = {}

        if 'run_info' in kwargs:
            # Input run_info could be the dict containing `app` and `params`
            # or the same information encoded in JSON - accepted as either
            # a file/stream or filename

            run_info = kwargs['run_info']

            if not hasattr(run_info, 'items'):
                run_info = self._get_json_run_info(run_info)

        else:
            # Alternative to run_info is explicit app/params dict passing

            if 'app' in kwargs:
                run_info['app'] = kwargs['app']

            if 'params' in kwargs:
                run_info['params'] = kwargs['params']

        if 'app' in run_info:
            self.app = run_info['app']
        else:
            raise Exception('Input to Wrapper must contain "app"')

        if 'params' in run_info:
            self.params = run_info['params']
        else:
            raise Exception('Input to Wrapper must contain "params"')

        if 'target_dir' in kwargs:
            self.target_dir = kwargs['target_dir']
        else:
            self.target_dir = None

    @staticmethod
    def _get_json_run_info(src):
        """Interpret JSON input (given as stream/file or filename), return dict

            Parameters
            ----------
            src
                Source stream/file or filename.

            Returns
            -------
            dict
                The result of interpreting input as JSON.

        """

        if hasattr(src, 'read'):

            json_stream = src

        else:

            try:
                json_stream = open(src, 'r')

            except Exception as e:

                reasoning = (
                    f"\nInputs to Wrapper must be dict or valid JSON (stream "
                    f"or read from filename) but received {type(src)} {src}"
                )

                raise Exception(str(e) + reasoning)

        return json.load(json_stream)

    def encode(self):
        raise NotImplementedError

    def write_application_files(self):
        raise NotImplementedError


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
