import logging
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


logger = logging.getLogger(__name__)


class Replicate(BaseSamplingElement):

    def __init__(self, campaign=None, sampler=None, run_name=None,
                 replicates=2):

        if replicates < 1:
            msg = (f"Number of replicates requested in 'replicate_samples' "
                   f"must be >= 1 (passed: {replicates}).")
            logging.error(msg)
            raise ValueError(msg)

        if campaign is None and sampler is None and run_name is None:
            logging.warning("Replicating all runs as no sampler, campaign or "
                            "run_name selected.")

        self.campaign = campaign
        self.sampler = sampler
        self.run_name = run_name
        self.replicates = replicates

    def element_category(self):
        return "sampling"

    def is_finite(self):
        return True

    def element_name(self):
        return "replicate_samples"

    def element_version(self):
        return "0.2"

    def generate_runs(self):



        # Get filtered list of unique runs
        # If no runs match then give error
        # Else loop through run specifications and replicates - yield new run

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

    def serialized_state(self):
        raise NotImplementedError

    def serialize(self):
        raise NotImplementedError
