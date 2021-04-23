"""Provides a simple action element for interacting with a SLURM job. This lets you
execute your simulation on a SLURM cluster.
"""

import logging
import re
import subprocess
from . import BaseAction
import time
import os
import random

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


class ExecuteSLURM():
    """An ActionStatus to track the execution of a SLURM job.

    Parameters
    ----------
    script: str
        The body of the script. Will be written to a file
        relative to target_dir named script_name.
    script_name: str
        Name of the script file. This will be written to.
        So beware of overwriting issues.
    target_dir: str
        Name of the execution directory for this job.
    """

    def __init__(self, template_script, variable):
        with open(template_script, 'r') as fd:
            self.template = fd.read()
        self.script_name = template_script
        self.variable = variable

    def start(self, previous=None):
        """Start the SLURM job.
        """
        target_dir = previous['rundir']
        script_name = os.path.join(target_dir, os.path.basename(self.script_name))
        script, = self.template.replace(self.variable, target_dir),
        with open(script_name, 'w') as fd:
            fd.write(script)
        result = subprocess.run(
            ['sbatch', script_name],
            cwd=target_dir, check=True, capture_output=True)
        stdout = result.stdout.decode('utf-8')
        self.job_id = re.findall(r'\d+', stdout)[0]
        while True:
            result = subprocess.run(
                ['squeue', '-j', self.job_id],
                cwd=target_dir, check=True, capture_output=True)
            stdout = result.stdout.decode('utf-8')
            if not self.job_id in stdout:
                break
            time.sleep(random.randint(1, 600))
        return previous

    def finalise(self):
        """Performs clean-up if necessary. In this case it isn't. I think.
        """
        return None
