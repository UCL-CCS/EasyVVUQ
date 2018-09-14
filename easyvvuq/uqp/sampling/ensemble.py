
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


def make_ensemble(campaign, selection={}, replicates=1):

    runs = campaign.runs

    check_params = selection.keys()

    for run_id, run_info in runs.items():

        if not selection:
            copy = True
        else:

            # TODO: Could we do something neater with pandas here?
            # TODO: Check if already have enough replicates?
            copy = all(run_info[param] == selection[param] for param in check_params)

        if copy:
            for rep_no in range(replicates):
                campaign.add_run(run_info)









