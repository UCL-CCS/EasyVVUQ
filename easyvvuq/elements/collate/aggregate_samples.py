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


class AggregateSamples(BaseCollationElement):
    """
    Aggregate the results of all completed simulations described by the
    Campaign.

    Parameters
    ----------
    campaign:   `easyvvuq.Campaign`
        Campaign from which to get simulation output to aggregate.
    average:
        Should the values read in be averaged (mean).
    """

    def element_name(self):
        return "aggregate_samples"

    def element_version(self):
        return "0.1"

    # TODO: This is an ugly way to set the campaign object. Will need to refactor
    # this to do logging differently soon.
    def __init__(self, campaign, average=False, *args, **kwargs):
        super().__init__(campaign)
        self.average = average

        # TODO: This should be made actually transparent
        # It is unclear that these args are passed to the decoder
        # Is there a better way to do this?
        self.decoder_args = args
        self.decoder_kwargs = kwargs

    def _collate(self):
        """
        Returns
        -------
        `pd.DataFrame`:
            Aggregated data from all completed runs referenced in the input Campaign.
        """
        decoder = self.campaign.decoder

        if decoder.output_type != OutputType.SAMPLE:
            raise RuntimeError('Can only aggregate sample type data')

        runs = self.campaign.runs

        full_data = pd.DataFrame()

        for run_id, run_info in runs.items():
            if decoder.sim_complete(run_info=run_info, *self.decoder_args, **self.decoder_kwargs):
                runs[run_id]['completed'] = True
                run_data = decoder.parse_sim_output(run_info=run_info,
                                                    *self.decoder_args,
                                                    **self.decoder_kwargs)

                if self.average:
                    run_data = pd.DataFrame(run_data.mean()).transpose()

                column_list = list(run_info.keys()) + run_data.columns.tolist()

                for param, value in run_info.items():

                    # TODO: Improve this ugly hack
                    if param == 'fixtures':
                        run_data[param] = 'FIXTURE'
                    else:
                        run_data[param] = value

                # Reorder columns
                run_data = run_data[column_list]
                run_data['run_id'] = run_id
                full_data = full_data.append(run_data, ignore_index=True)

        return full_data

#        data_dir = os.path.join(campaign.campaign_dir, 'data')
#
#        out_dir = tempfile.mkdtemp(dir=data_dir)
#        out_file = os.path.join(out_dir, 'aggregate_sample.tsv')
#
#        full_data.to_csv(out_file, sep='\t', index=False)
#
#        state_file = os.path.join(out_dir, 'state_snapshot.json')
#        campaign.save_state(state_file)

#        campaign.data = {
#            'files': [out_file],
#            'type': OutputType('summary').value,
#            'output_columns': decoder.output_columns,
#            'state': state_file
#        }
