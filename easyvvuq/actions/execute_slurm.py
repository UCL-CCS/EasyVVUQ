"""Provides element to execute a shell command in a given directory.
"""

import os
import sys
import logging
import subprocess
from . import BaseAction

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

class ActionStatusSLURM():
    def __init__(self, script, script_name, target_dir):
        self.script = script
        self.script_name = script_name
        self.target_dir = target_dir
        self._started = False

    def start(self):
        result = subprocess.run(['sbatch', self.script_name], cwd=self.target_dir, check=True)
        stdout = result.stdout.decode('utf-8')
        self.job_id = re.findall(r'\d+', stdout)[0]
        self._started = True

    def started(self):
        return self._started

    def finished(self):
        """Returns true if action is finished. In this case if calling poll on
        the popen object returns a non-None value.
        """
        if not self.started():
            return False
        result = subprocess.run(['squeue', '-j', self.job_id], cwd=self.target_dir, check=True)
        stdout = result.stdout.decode('utf-8')
        if len(re.findall(r'\d+', stdout)) > 0:
            return True
        else:
            return False

    def finalise(self):
        """Performs clean-up if necessary. In this case it isn't. I think.
        """
        return None

    def succeeded(self):
        """Will return True if the process finished successfully.
        It judges based on the return code and will return False
        if that code is not zero.
        """
        if not self.started():
            return False
        if self.ret != 0:
            return False
        else:
            return True


class ExecuteSLURM(ExecuteLocal):
    """An improvement over ExecuteLocal that uses Popen and provides the non-blocking
    execution that allows you to track progress. In line with other Action classes in EasyVVUQ.

    Parameters
    ----------
    template_script: str
       filename for the template slurm script

    variable: str
       a string in the template script that will be replaced with the target_dir
    """

    def __init__(self, template_script, variable):
        with open(template_script, 'r') as fd:
            self.template = fd.read()
        self.script_name = template_script
        self.variable = variable

    def act_on_dir(self, target_dir):
        """
        Executes `self.run_cmd` in the shell in `target_dir`.

        target_dir : str
            Directory in which to execute command.

        """
        return ActionStatusSLURM(self.template.replace(self.variable, target_dir), target_dir)
