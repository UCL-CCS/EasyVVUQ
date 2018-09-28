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


def aggregate_samples(campaign, average=False):
    """
    Aggregate the results of all completed simulations described by the
    Campaign.

    Parameters
    ----------
    campaign:   `easyvvuq.Campaign`
        Campaign from which to get simulation output to aggregate.
    average:
        Should the values read in be averaged (mean).

    Returns
    -------
    `pd.DataFrame`:
        Aggregated data from all completed runs referenced in the input Campaign.

    """

    decoder = campaign.decoder

    if decoder.sample_type != OutputType.SAMPLE:
        raise RuntimeError('Can only aggregate sample type data')

    runs = campaign.runs

    full_data = pd.DataFrame()

    for run_id, run_info in runs.items():

        if decoder.sim_complete(run_info=run_info):

            run_data = decoder.parse_sim_output(run_info=run_info)

            if average:

                run_data = pd.DataFrame(run_data.mean()).transpose()

            for param, value in run_info.items():

                run_data[param] = value

            run_data['run_id'] = run_id

            full_data.append(run_data, ignore_index=True)

    return full_data








