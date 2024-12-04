import os
from string import Template
import logging

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


def get_custom_template(template_txt, custom_delimiter='$'):
    class CustomTemplate(Template):
        delimiter = custom_delimiter
    return CustomTemplate(template_txt)


class GenericEncoder:
    """GenericEncoder for substituting values into application template input.

    Parameters
    ----------

    Attributes
    ----------

    """

    def __init__(self, template_fname, delimiter='$', target_filename="app_input.txt"):
        self.delimiter = delimiter
        self.target_filename = target_filename
        self.template_fname = template_fname

    def encode(self, params={}, target_dir=''):
        """Substitutes `params` into a template application input, saves in
        `target_dir`

        Parameters
        ----------
        params        : dict
            Parameter information in dictionary.
        target_dir    : str
            Path to directory where application input will be written.
        """

        try:
            with open(self.template_fname, 'r') as template_file:
                template_txt = template_file.read()
                self.template = Template(template_txt)
        except FileNotFoundError:
            raise RuntimeError(
                "the template file specified ({}) does not exist".format(self.template_fname))

        if not target_dir:
            raise RuntimeError('No target directory specified to encoder')

        str_params = {}
        for key, value in params.items():
            str_params[key] = str(value)

        try:
            app_input_txt = self.template.substitute(str_params)
        except KeyError as e:
            self._log_substitution_failure(e)

        # Write target input file
        target_file_path = os.path.join(target_dir, self.target_filename)
        with open(target_file_path, 'w') as fp:
            fp.write(app_input_txt)

    def _log_substitution_failure(self, exception):
        reasoning = (f"\nFailed substituting into template "
                     f"{self.template_fname}.\n"
                     f"KeyError: {str(exception)}.\n")
        logging.error(reasoning)

        raise KeyError(reasoning)
