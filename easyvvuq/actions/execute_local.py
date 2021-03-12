"""Provides element to execute a shell command in a given directory.
"""

import os
import sys
import logging
import subprocess
from . import BaseAction
import concurrent
import dill

__license__ = "LGPL"


class ExecutePython():
    def __init__(self, function):
        self.function = function
        self.params = None
        self.result = None

    def start(self):
        self.result = self.function(self.params)
        return self

    def finished(self):
        if self.result is None:
            return False
        else:
            return True

    def finalise(self):
        self.campaign.campaign_db.store_result(self.run_id, self.result)

    def succeeded(self):
        if not self.finished():
            raise RuntimeError('action did not finish yet')
        else:
            return True


class ExecuteLocal():
    def __init__(self, full_cmd, target_dir):
        self.full_cmd = full_cmd
        self.target_dir = target_dir
        self.popen_object = None
        self.ret = None
        self._started = False

    def start(self):
        self.popen_object = subprocess.Popen(self.full_cmd, cwd=self.target_dir)
        self._started = True

    def started(self):
        return self._started

    def finished(self):
        """Returns true if action is finished. In this case if calling poll on
        the popen object returns a non-None value.
        """
        if self.popen_object is None:
            return False
        ret = self.popen_object.poll()
        if ret is not None:
            self.ret = ret
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


class ExecuteLocal():
    """An improvement over ExecuteLocal that uses Popen and provides the non-blocking
    execution that allows you to track progress. In line with other Action classes in EasyVVUQ.
    """

    def act_on_dir(self, target_dir):
        """
        Executes `self.run_cmd` in the shell in `target_dir`.

        target_dir : str
            Directory in which to execute command.

        """

        if self.interpreter is None:
            full_cmd = self.run_cmd.split()
        else:
            full_cmd = [self.interpreter] + self.run_cmd.split()
        return ActionStatusLocalV2(full_cmd, target_dir)
