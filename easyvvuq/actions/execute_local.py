"""Provides element to execute a shell command in a given directory.
"""

import os
from pathlib import Path
import shutil
import sys
import logging
import subprocess
from . import BaseAction
import concurrent
import dill

__license__ = "LGPL"

class CreateRunDirectory():
    def __init__(self, root):
        self.root = root

    def start(self, previous=None):
        run_id = previous['run_id']
        level1_a, level1_b = int(run_id / 100 ** 4) * 100 ** 4, int(run_id / 100 ** 4 + 1) * 100 ** 4
        level2_a, level2_b = int(run_id / 100 ** 3) * 100 ** 3, int(run_id / 100 ** 3 + 1) * 100 ** 3
        level3_a, level3_b = int(run_id / 100 ** 2) * 100 ** 2, int(run_id / 100 ** 2 + 1) * 100 ** 2
        level4_a, level4_b = int(run_id / 100 ** 1) * 100 ** 1, int(run_id / 100 ** 1 + 1) * 100 ** 1
        level1_dir = "runs_{}-{}/".format(level1_a, level1_b)
        level2_dir = "runs_{}-{}/".format(level2_a, level2_b)
        level3_dir = "runs_{}-{}/".format(level3_a, level3_b)
        level4_dir = "runs_{}-{}/".format(level4_a, level4_b)
        path = os.path.join(self.root, level1_dir, level2_dir, level3_dir, level4_dir)
        Path(path).mkdir(parents=True, exist_ok=True)
        previous = dict(previous)
        previous['rundir'] = path
        self.previous = previous
        return self

    def finished(self):
        return True

    def finalise(self):
        pass

    def succeeded(self):
        return True

class Encode():
    def __init__(self, encoder):
        self.encoder = encoder

    def start(self, previous=None):        
        self.encoder.encode(previous['run_info'], params=previous['run_info']['params'],
                            target_dir=previous['rundir'])
        self.previous = dict(previous)
        return self

    def finished(self):
        return True

    def finalise(self):
        pass

    def succeeeded(self):
        return True

class Decode():
    def __init__(self, decoder):
        self.decoder = decoder

    def start(self, previous=None):
        run_info = dict(previous['run_info'])
        run_info['run_dir'] = previous['rundir']
        result = self.decoder.parse_sim_output(run_info)
        previous = dict(previous)
        previous['result'] = result
        self.previous = previous
        return self

    def finished(self):
        return True

    def finalise(self):
        self.previous['campaign'].campaign_db.store_result(self.previous['run_id'], self.previous['result'])

    def succeeded(self):
        return True

class CleanUp():
    def __init__(self):
        pass

    def start(self, previous=None):
        if not ('rundir' in previous.keys()):
            raise RuntimeError('must be used with actions that create a directory structure')
        shutil.rmtree(previous['rundir'])
        self.previous = dict(previous)
        return self
                
    def finished(self):
        return True

    def finalise(self):
        pass

    def succeeded(self):
        return True

class ExecutePython():
    def __init__(self, function):
        self.function = function
        self.params = None
        self.result = None

    def start(self, previous=None):
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
    def __init__(self, full_cmd):
        self.full_cmd = full_cmd.split()
        self.popen_object = None
        self.ret = None
        self._started = False

    def start(self, previous=None):
        target_dir = previous['rundir']
        self.ret = subprocess.run(self.full_cmd, cwd=target_dir)
        self.previous = dict(previous)
        return self

    def finished(self):
        return True

    def finalise(self):
        """Performs clean-up if necessary. In this case it isn't. I think.
        """
        pass

    def succeeded(self):
        """Will return True if the process finished successfully.
        It judges based on the return code and will return False
        if that code is not zero.
        """
        if self.ret != 0:
            return False
        else:
            return True

class Actions():
    def __init__(self, *args):
        self.actions = list(args)

    def start(self, previous=None):
        for action in self.actions:
            previous = action.start(previous).previous
        self.previous = dict(previous)
        return self

    def finished(self):
        return all([action.finished() in self.actions])

    def finalise(self):
        for action in self.actions:
            action.finalise()

    def succeeded(self):
        return all([action.succeeded() in self.actions])
