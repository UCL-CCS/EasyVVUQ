import os
import tempfile
from easyvvuq import Campaign
from easyvvuq import OutputType
from .. import BaseElement

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


class BaseCollationElement(BaseElement):
    """Baseclass for all EasyVVUQ collation elements.

    Parameters
    ----------
    data_src    : dict or Campaign or stream
        Information on the infomration Application information.
        Will try interpreting as a dict or JSON file/stream or filename.


    Attributes
    ----------

    """

    def _collate(self):
        """
        Collates the campaign run output into a pandas dataframe.
        Must be implemented by all collation subclasses.
        """
        raise NotImplementedError

    def element_category(self):
        return "collation"

    def __init__(self, campaign):
        self.campaign = campaign

    def apply(self):
        """
        Run the collation, then log the details in the campaign (if it exists)
        """

        # Get dataframe (collation of results in the campaign object)
        df = self._collate()

        # Set up dirs and files to store collation results in
        data_dir = os.path.join(self.campaign.campaign_dir, 'data')
        out_dir = tempfile.mkdtemp(dir=data_dir)
        out_file = os.path.join(out_dir, 'aggregate_sample.tsv')

        # Convert dataframe to file
        df.to_csv(out_file, sep='\t', index=False)

        # Save campaign state
        state_file = os.path.join(out_dir, 'state_snapshot.json')
        self.campaign.save_state(state_file)

        # Log this collation with the campaign object
        data_info = {
            'files': [out_file],
            'type': OutputType('summary').value,
            'output_columns': self.campaign.decoder.output_columns,
            'state': state_file
        }
        self.campaign.log_element_application(self, data_info)

        # Point the campaign's 'data' var to this collated output
        self.campaign.data = data_info

        return df
