"""Provides an element for aggregation of results from all complete runs.
"""

from .base import BaseCollationElement
from easyvvuq import OutputType, constants
from easyvvuq.utils.helpers import multi_index_tuple_parser
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


class AggregateSamples(BaseCollationElement, collater_name="aggregate_samples"):
    """
    Aggregate the results of all completed simulations described by the
    Campaign. Will simply concatenate all simulation data into one big
    DataFrame.

    Parameters
    ----------
    average : bool
    Should the values read in be averaged (mean).
    """

    def __init__(self, average=False):
        self.average = average

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

                run_data = decoder.parse_sim_output(run_info=run_info)

                if self.average:
                    run_data = pd.DataFrame(run_data.mean()).transpose()

                mult = isinstance(run_data.columns, pd.MultiIndex)

                params = run_info['params']
                for param, value in params.items():
                    if isinstance(value, list):
                        # need to have multi-index dataframe
                        if not mult:
                            col, mult = multi_index_tuple_parser(run_data.columns.values)
                            col = [(c, '') for c in col]
                            run_data.columns = pd.MultiIndex.from_tuples(col)
                        # add list values using columns tuple
                        for i in range(len(value)):
                            run_data[(param, i)] = value[i]
                    else:
                        run_data[param] = value
                column_list = run_data.columns.tolist()

                # we need to convert columns to tuples to account for multi-indexing
                # should not influence non-multi-index frames, I hope. hacky?
                # TODO from Jalal: I think we don't need it, must be handled in the decoder
                if any([isinstance(x, tuple) for x in column_list]):
                    column_list_ = []
                    for column in column_list:
                        if not isinstance(column, tuple):
                            column_list_.append((column, ''))
                        else:
                            column_list_.append(column)
                    column_list = column_list_

                # Reorder columns
                run_data = run_data[column_list]
                run_data['run_id'] = run_id
                run_data['ensemble_id'] = run_info['ensemble_name']
                new_data = new_data.append(run_data, ignore_index=True)
                processed_run_IDs.append(run_id)

        self.append_data(campaign, new_data, app_id)
        campaign.campaign_db.set_run_statuses(processed_run_IDs, constants.Status.COLLATED)

        return len(processed_run_IDs)

    def append_data(self, campaign, new_data, app_id):
        campaign.campaign_db.append_collation_dataframe(new_data, app_id)

    def get_collated_dataframe(self, campaign, app_id):
        return campaign.campaign_db.get_collation_dataframe(app_id)

    def element_version(self):
        return "0.1"

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        """Return dict required for restart from serlialized form.

        Returns
        -------
        dict:
            Only parameter needed for restart is the flag for averaging of
            collated data.
        """
        return {"average": self.average}
