import os
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


class DirectoryBuilder(BaseEncoder, encoder_name="directory_builder"):
    """DirectoryBuilder builds the specified directory structure for a Run.

    The dir structure is specified by the 'tree' parameter. This should be a dict of dicts,
    for example:

    tree = {'a' : {'b' : {'c' : None, 'd' : None}}, 'e' : {'f' : None}}


    Parameters
    ----------
        tree    : dict of dicts
            The desired directory structure
    Attributes
    ----------

    """

    def __init__(self, tree):
        self.tree = tree

    def encode(self, params={}, target_dir=''):
        """Builds the directory structure specified in self.tree into the `target_dir` directory

        Parameters
        ----------
        params        : dict
            Parameter information in dictionary.
        target_dir    : str
            Path to directory where application input will be written.
        """

        if not target_dir:
            raise RuntimeError('No target directory specified to encoder')

        self.create_dir_tree(self.tree, target_dir)

    def create_dir_tree(self, dirtree, root):
        # A beautiful Vytas creation
        if dirtree is not None:
            for directory in dirtree.keys():
                os.mkdir(os.path.join(root, directory))
                self.create_dir_tree(dirtree[directory], os.path.join(root, directory))

    def get_restart_dict(self):
        return {"tree": self.tree}

    def element_version(self):
        return "0.1"
