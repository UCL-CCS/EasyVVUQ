
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


def add_replicas(campaign, selection={}, replicates=2):

    # TODO: Could we do something neater with pandas here?

    runs = campaign.unique_runs()

    reps_made = False

    for run_info in runs:

        n_reps = len(run_info['run_ids'])

        if n_reps < replicates:

            if not selection:

                copy = True

            else:

                check_params = selection.keys()
                copy = all([run_info[param] == selection[param] for param in check_params])

            if copy:

                copy_info = {k: v for k, v in run_info.items() if k != 'run_ids'}

                new_reps = replicates - n_reps

                for rep_no in range(new_reps):
                    campaign.add_run(dict(copy_info))
                    reps_made = True

    if reps_made:
        # TODO: There must be a better way to record argument - using locals() maybe?
        campaign.record_sampling('add_replicas',
                                 {'selection': selection,
                                  'replicates': replicates},
                                 reps_made)
