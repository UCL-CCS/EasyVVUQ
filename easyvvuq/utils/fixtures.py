import os
import shutil

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


class Fixture(object):

    def __init__(self, path, is_dir=False, common=False, exists_local=True,
                 target="", campaign_dir='.', group=''):
        """

        Parameters
        ----------
        path
            Path to file or directory
        common
            Will fixture be common to multiple runs
        exists_local
            Does the file exist on the local machine (i.e. can it be copied to
            a common or run directory by EasyVVUQ)
        target
            Target file name or path. Path should be relative to a run directory
            except for when `common` is set.
        """

        self.exists_local = exists_local

        if exists_local:

            abs_path = os.path.realpath(os.path.expanduser(path))

            if not os.path.exists(abs_path):
                raise IOError(f"Unable to find local fixture: {path}")

            self.src_path = abs_path

        else:

            self.src_path = path

        self.target = target
        self.common = common
        self._common_copied = False
        self.is_dir = is_dir
        self.campaign_dir = campaign_dir
        self.group = group

    def copy_to_target(self):

        target_path = self.target_path

        if self.common and self._common_copied:
            return

        if self.is_dir:
            shutil.copytree(self.src_path, target_path)
        else:
            shutil.copy2(self.src_path, target_path)

        if self.common:
            self._common_copied = True

    def target_path(self, run_id=None):

        if not self.exists_local:
            return self.src_path

        target_path = self.campaign_dir

        if self.common:
            target_path = os.path.join(target_path, 'common')

            if self.group:
                target_path = os.path.join(target_path, 'group')

        else:

            if run_id is None:
                raise RuntimeError(f"A run_id is needed to create target path "
                                   f"for the fixture {self.path}")

            target_path = os.path.join(target_path, run_id)

        target_path = os.path.join(target_path, self.target)

        return target_path



