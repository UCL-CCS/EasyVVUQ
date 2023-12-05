"""This module provides an assortment of actions generally concerned with executing
simulations locally. Some Actions will also be useful when using Dask.
"""

import os
from pathlib import Path
import shutil
import subprocess
import dill
import copy
import logging

__license__ = "LGPL"


def local_execute(encoder, command, decoder, root='/tmp'):
    """A helper function for a simple local execution.
    It will create a directory under your specified root folder, encode the sampler output, execute a command
    and decode the results of the simulation.

    Parameters
    ----------
    encoder: Encoder
      an encoder to use
    command: list of str
      a command to run your simulation (same as argument to popen, e.g. ['ls', '-al'])
    decoder: Decoder
      a decoder to use
    root: str
      root folder, for example '/tmp' or if you want to use ram based filesystem it could be '/dev/shm'

    Returns
    -------
    Actions
    """
    return Actions(
        CreateRunDirectory(root),
        Encode(encoder),
        ExecuteLocal(command),
        Decode(decoder))


class CreateRunDirectory():
    """Creates a directory structure for storing simulation input and output files.

    Parameters
    ----------
    root: str
        Root directory to create a directory structure in.
    flatten: bool
        If set to True will result in a flat directory structure (each run gets a directory
        under root). If left as False will create a hierarchical structure. This is useful
        so as not to overload the filesystem.
    """

    def __init__(self, root, flatten=False):
        self.root = root
        self.flatten = flatten

    def start(self, previous=None):
        """Starts the action.

        Will read a `run_id` from a dictionary supplied by the previous `Action`.
        Will then create a directory structure based on the numerical value of the `run_id`.

        Returns
        -------
        dict
            A dictionary to be passed to the following `Action`.
        """
        run_id = previous['run_id']
        level1_a, level1_b = (int(run_id / 100 ** 4) * 100 ** 4,
                              int(run_id / 100 ** 4 + 1) * 100 ** 4)
        level2_a, level2_b = (int(run_id / 100 ** 3) * 100 ** 3,
                              int(run_id / 100 ** 3 + 1) * 100 ** 3)
        level3_a, level3_b = (int(run_id / 100 ** 2) * 100 ** 2,
                              int(run_id / 100 ** 2 + 1) * 100 ** 2)
        level4_a, level4_b = (int(run_id / 100 ** 1) * 100 ** 1,
                              int(run_id / 100 ** 1 + 1) * 100 ** 1)
        level1_dir = "runs_{}-{}/".format(level1_a, level1_b)
        level2_dir = "runs_{}-{}/".format(level2_a, level2_b)
        level3_dir = "runs_{}-{}/".format(level3_a, level3_b)
        level4_dir = "runs_{}-{}/".format(level4_a, level4_b)
        level5_dir = "run_{}".format(int(run_id))

        if self.flatten:
            path = os.path.join(self.root, previous['campaign_dir'], 'runs', level5_dir)
        else:
            path = os.path.join(self.root, previous['campaign_dir'], 'runs',
                                level1_dir, level2_dir, level3_dir, level4_dir, level5_dir)

        Path(path).mkdir(parents=True, exist_ok=True)
        previous['rundir'] = path
        self.result = previous
        return self.result

    def succeeded(self):
        """Has the `Action` finished successfully.

        Returns
        -------
        bool
            True if `Action` completed successfully. False otherwise.
        """
        return True


class Encode():
    def __init__(self, encoder):
        self.encoder = encoder

    def start(self, previous=None):
        self.encoder.encode(
            params=previous['run_info']['params'],
            target_dir=previous['rundir'])
        try:
            previous['encoder_filename'] = self.encoder.target_filename
        except AttributeError:
            if os.getenv("EasyVVUQ_Debug"): print('AttributeError raised and ignored')
        return previous

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
        run_info = copy.copy(previous['run_info'])
        run_info['run_dir'] = previous['rundir']
        result = self.decoder.parse_sim_output(run_info)
        previous['result'] = result
        previous['decoder_filename'] = self.decoder.target_filename
        previous['collated'] = True
        return previous

    def finished(self):
        return True

    def finalise(self):
        pass

    def succeeded(self):
        return True


class CleanUp():
    def __init__(self):
        pass

    def start(self, previous=None):
        if not ('rundir' in previous.keys()):
            raise RuntimeError('must be used with actions that create a directory structure')
        shutil.rmtree(previous['rundir'])
        return previous

    def finished(self):
        return True

    def finalise(self):
        pass

    def succeeded(self):
        return True


class ExecutePython():
    def __init__(self, function):
        self.function = dill.dumps(function)
        self.params = None
        self.eval_result = None

    def start(self, previous=None):
        function = dill.loads(self.function)
        self.eval_result = function(previous['run_info']['params'])
        previous['result'] = self.eval_result
        previous['collated'] = True
        return previous

    def finished(self):
        if self.eval_result is None:
            return False
        else:
            return True

    def finalise(self):
        pass

    def succeeded(self):
        if not self.finished():
            raise RuntimeError('action did not finish yet')
        else:
            return True


class ExecuteLocal():
    def __init__(self, full_cmd, stdout=None, stderr=None):
        self.full_cmd = full_cmd.split()
        self.popen_object = None
        self.ret = None
        self._started = False
        self.stdout = stdout
        self.stderr = stderr

        # Fix for the Matlab command, do not split: -r 'test(); quit'
        # matlab -nodesktop  -nojvm -r 'test(); quit'"
        if "-r" in self.full_cmd:
            start = full_cmd.find("-r ")
            cmd = full_cmd[:start].split()
            cmd.append(full_cmd[start:])
            self.full_cmd = cmd
            logging.info(f"Updating the split of the command for the Matlab's -r argument.")
            logging.info(f"Full command reads: {cmd}")

    def start(self, previous=None):
        target_dir = previous['rundir']
        if isinstance(self.stdout, str):
            stdout = open(os.path.join(target_dir, self.stdout), 'w')
        else:
            stdout = self.stdout
        if isinstance(self.stderr, str):
            stderr = open(os.path.join(target_dir, self.stderr), 'w')
        else:
            stderr = self.stderr
        self.ret = subprocess.run(
            self.full_cmd, cwd=target_dir,
            stdout=stdout, stderr=stderr)
        if isinstance(self.stdout, str): close(stdout)
        if isinstance(self.stderr, str): close(stderr)
        return previous

    def finished(self):
        return True

    def finalise(self):
        """Performs clean-up if necessary. In this case it isn't. I think.
        """
        stdout.close()
        stderr.close()
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
        self.wrapper = lambda action, previous: action.start(previous)

    def set_wrapper(self, wrapper):
        """Adds a wrapper to be called on each Action.

        Parameters
        ----------
        wrapper: callable
            A function to call on each Action. Should pass through the return of the
            start method.
        """
        self.wrapper = wrapper

    def start(self, previous=None):
        for action in self.actions:
            if not hasattr(action, 'start'):
                raise RuntimeError('action in the actions list does not provide a start method')
        previous = copy.copy(previous)
        run_id = previous['run_id']
        for action in self.actions:
            previous = self.wrapper(action, previous)
        self.result = previous
        assert (self.result['run_id'] == run_id)
        return previous

    def finished(self):
        return all([action.finished() for action in self.actions])

    def finalise(self):
        for action in self.actions:
            action.finalise()

    def succeeded(self):
        return all([action.succeeded() for action in self.actions])
