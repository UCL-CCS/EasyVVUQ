"""An encoder meant to simply copy a file to the input directory unchanged.
It is meant to be used in combination with MultiBuilder encoder and possibly
the DirectoryBuilder. It duplicates some functionality of the ApplyFixtures
encoder but can be useful for very simple cases.

Examples
--------
>>> multiencoder = uq.encoders.MultiEncoder(
      DirectoryBuilder(tree={"parent" : {"child1" : None, "child2" : None}}),
      CopyEncoder('/home/user/input1.conf', 'parent/child1/input1.conf')
      CopyEncoder('/home/user/input2.conf', 'parent/child1/input2.conf')
      CopyEncoder('/home/user/input3.conf', 'parent/child2/input3.conf')
      GenericEncoder(delimiter='$', template_fname='/home/user/template.in',
                     target_filename='parent/input.int'))
"""

import os
import shutil
from .base import BaseEncoder


class CopyEncoder(BaseEncoder, encoder_name="copy_encoder"):
    """An Encoder to copy an input file to a simulation.

    Parameters
    ----------
    source_filename : str
      a full path to some file that a simulation needs

    target_filename : str
      a target filename inside the simulation directory
    """

    def __init__(self, source_filename, target_filename):
        self.source_filename = source_filename
        self.target_filename = target_filename
        if not os.path.isfile(self.source_filename):
            raise RuntimeError("Specified source file does not exist:", source_filename)

    def encode(self, params={}, target_dir=''):
        """Copy a file to target_dir.

        Parameters
        ----------
        params : dict
           keep empty, has no effect

        target_dir : str
           target directory, full path
        """
        if not os.path.isdir(target_dir):
            raise RuntimeError("Specified target directory does not exist:", target_dir)
        shutil.copyfile(self.source_filename, os.path.join(target_dir, self.target_filename))

    def get_restart_dict(self):
        return {"source_filename": self.source_filename,
                "target_filename": self.target_filename}

    def element_version(self):
        return "0.1"
