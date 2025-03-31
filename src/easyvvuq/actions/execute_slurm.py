"""Provides a simple action element for interacting with a SLURM job. This lets you
execute your simulation on a SLURM cluster.
"""

import logging
import re
import subprocess
import time
import os
import random

__license__ = "LGPL"

logger = logging.getLogger(__name__)


class ExecuteSLURM():
    """An Action to launch and track the execution of a SLURM job.

    Parameters
    ----------
    template_script: str
        Filename of a file containing the script template.
    variable: str
        A string to be replaced with the directory in which the job is meant to be executed.
        This is to be used to make sure that the simulation can find the correct input files and knows
        where to put output files.
    """

    def __init__(self, template_script, variable):
        with open(template_script, 'r') as fd:
            self.template = fd.read()
        self.script_name = template_script
        self.variable = variable

    def start(self, previous=None):
        """Start the SLURM job.

        Parameters
        ----------
        previous: dict
            A dictionary containing information provided by previously executed actions.
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
            if self.job_id not in stdout:
                break
            time.sleep(random.randint(1, 600))
        return previous

    def finalise(self):
        """Performs clean-up if necessary. In this case it isn't. I think.
        """
        return None
