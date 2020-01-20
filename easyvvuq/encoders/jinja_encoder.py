import os
#from string import Template
from jinja2 import Template
from .base import BaseEncoder
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


class JinjaEncoder(BaseEncoder, encoder_name="jinja_template"):
    """JinjaEncoder for substituting values into application template input.
    Uses the jinja2 template system, which supports more complex expressions than
    the GenericEncoder.
    See https://jinja.palletsprojects.com/en/2.10.x/templates/ for template syntax.

    Parameters
    ----------

    Attributes
    ----------

    """

    def __init__(self, template_fname=None,
                 target_filename="app_input.txt"):

        self.target_filename = target_filename
        self.template_fname = template_fname

        self.fixture_support = True

        # Check that user has specified the file to use as template
        if template_fname is None:
            msg = ("JinjaEncoder must be given 'template_fname' - the "
                   "location of a file containing the template text.")
            logging.error(msg)
            raise RuntimeError(msg)

        with open(template_fname, 'r') as template_file:
            template_txt = template_file.read()
            self.template = Template(template_txt)

    def encode(self, params={}, target_dir='', fixtures=None):
        """Substitutes `params` into a template application input, saves in
        `target_dir`

        Parameters
        ----------
        params        : dict
            Parameter information in dictionary.
        target_dir    : str
            Path to directory where application input will be written.
        fixtures      : dict
            Information of files/assets for fixture type parameters.
        """

        if fixtures is not None:
            local_params = self.substitute_fixtures_params(params, fixtures,
                                                           target_dir)
        else:
            local_params = params

        if not target_dir:
            raise RuntimeError('No target directory specified to encoder')

        try:
            app_input_txt = self.template.render(local_params)
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

    def get_restart_dict(self):
        return {"target_filename": self.target_filename,
                "template_fname": self.template_fname}

    def element_version(self):
        return "0.1"
