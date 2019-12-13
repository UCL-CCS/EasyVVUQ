"""Provides an element for aggregation of results from all complete runs.
"""

from .aggregate_samples import AggregateSamples
from easyvvuq import OutputType, constants
import pandas as pd

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


class AggregateByVariables(AggregateSamples, collater_name="aggregate_by_variables"):

    def collate(self, campaign, app_id):
        """
        Collected the decoded run results for all completed runs with ENCODED status

        Parameters
        ----------
        campaign : :obj:`easyvvuq.campaign.Campaign`
            EasyVVUQ coordination object from which to get information on runs
            to be collated.

        Returns
        -------
        `int`:
            The number of new data rows added during collation
        """

        decoder = campaign._active_app_decoder

        if decoder.output_type != OutputType.SAMPLE:
            raise RuntimeError('Can only aggregate sample type data')

        # Aggregate any uncollated runs into a dataframe (for appending to existing full df)
        new_data = pd.DataFrame()

        # Loop through all runs with status ENCODED (and therefore not yet COLLATED)
        processed_run_IDs = []
        for run_id, run_info in campaign.campaign_db.runs(
                status=constants.Status.ENCODED, app_id=app_id):

            # Use decoder to check if run has completed (in general application-specific)
            if decoder.sim_complete(run_info=run_info):
                sim_output = decoder.parse_sim_output(run_info=run_info)

                run_data = pd.DataFrame()

                params = run_info['params']

                # make a row for every sim_output value
                for i, output_val in enumerate(sim_output.columns.tolist()):
                    for param, value in params.items():
                        run_data.loc[i, param] = value
                    run_data.loc[i, 'Variable'] = output_val
                    run_data.loc[i, 'Value'] = sim_output.loc[0, output_val]
                    run_data.loc[i, 'run_id'] = run_id
                    run_data.loc[i, 'ensemble_id'] = run_info['ensemble_name']

                new_data = new_data.append(run_data, ignore_index=True)

                processed_run_IDs.append(run_id)

        self.append_data(campaign, new_data, app_id)
        campaign.campaign_db.set_run_statuses(processed_run_IDs, constants.Status.COLLATED)

        return len(processed_run_IDs)

    def element_version(self):
        return "0.1"

    def get_restart_dict(self):
        """Return dict required for restart from serlialized form.

        Returns
        -------
        dict:
            Only parameter needed for restart is the flag for averaging of
            collated data.
        """
        return {}
