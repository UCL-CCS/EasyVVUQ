from .base import BaseCollationElement
from easyvvuq import OutputType
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
    Campaign.

    Parameters
    ----------
    average:
        Should the values read in be averaged (mean).
    """

    def element_version(self):
        return "0.1"

    def __init__(self, average=False):
        self.average = average

    def collate(self, campaign):
        """
        Returns
        -------
        `pd.DataFrame`:
            Aggregated data from all completed runs referenced in the input Campaign.
        """
        decoder = campaign._active_app_decoder

        if decoder.output_type != OutputType.SAMPLE:
            raise RuntimeError('Can only aggregate sample type data')

        full_data = pd.DataFrame()

        # TODO: Find nicer way than forcing collate to access deep internal
        # vars of campaign object like this
        runs = campaign.campaign_db.runs()

        for run_id, run_info in runs.items():
            if decoder.sim_complete(run_info=run_info):

                campaign.campaign_db.set_run_status(run_id, "completed")

                run_data = decoder.parse_sim_output(run_info=run_info)

                if self.average:
                    run_data = pd.DataFrame(run_data.mean()).transpose()

                params = run_info['params']

                column_list = list(params.keys()) + run_data.columns.tolist()

                for param, value in params.items():
                    run_data[param] = value

                # Reorder columns
                run_data = run_data[column_list]
                run_data['run_id'] = run_id
                full_data = full_data.append(run_data, ignore_index=True)

        return full_data

    def get_restart_dict(self):
        return {"average": self.average}
