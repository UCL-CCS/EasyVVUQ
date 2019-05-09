from .base import BaseSamplingElement

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


class Replicate(BaseSamplingElement):

    def __init__(self, campaign, selection={}, replicates=2):
        self.campaign = campaign
        self.selection = selection
        self.replicates = replicates

    def element_name(self):
        return "replicate"

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def generate_runs(self):
        runs = self.campaign.unique_runs()
        reps_made = False
        for run_info in runs:

            n_reps = len(run_info['run_ids'])
            if n_reps < self.replicates:
                if not self.selection:
                    copy = True
                else:
                    check_params = self.selection.keys()
                    copy = all([run_info[param] == self.selection[param]
                                for param in check_params])

                if copy:
                    copy_info = {k: v for k, v in run_info.items()
                                 if k != 'run_ids'}
                    new_reps = self.replicates - n_reps
                    for rep_no in range(new_reps):
                        yield dict(copy_info)
