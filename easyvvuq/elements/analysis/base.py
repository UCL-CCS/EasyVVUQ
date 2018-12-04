import os
import tempfile
import json
import easyvvuq.utils.json as json_utils
from pandas import DataFrame
from easyvvuq import Campaign
from easyvvuq import constants
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


class BaseAnalysisElement(BaseElement):
    """Baseclass for all EasyVVUQ analysis elements.

    Parameters
    ----------
    data_src    : dict or Campaign or stream
        Information on the infomration Application information.
        Will try interpreting as a dict or JSON file/stream or filename.


    Attributes
    ----------

    """

    def _apply_analysis(self):
        raise NotImplementedError

    def element_category(self):
        return "analysis"

    def __init__(self, data_src, output_dir=None, *args, **kwargs):

        self.campaign = None

        self.data_frame = None
        self.data = None

        self.output_dir = output_dir
        self.output_file = None
        self.output_type = None

        if isinstance(data_src, Campaign):
            self.campaign = data_src
            self.data_src = data_src.data
        
            if not self.output_dir:
                analysis_path = os.path.join(self.campaign.campaign_dir, 'analysis')
                self.output_dir = tempfile.mkdtemp(prefix=self.element_name() + '_',
                                                   dir=analysis_path)

        elif isinstance(data_src, dict):
            self.data_src = data_src
        elif isinstance(data_src, DataFrame):
            self.data_frame = data_src
        else:
            self.data_src = json_utils.process_json(data_src)

        if not self.output_dir:
            self.output_dir = tempfile.mkdtemp()


    def _log_analysis(self):
        output_dir = self.output_dir
        filename = f"{self.element_name()}.json"

        log_path = os.path.join(output_dir, filename)
        self_dict = {k: v for k, v in self.__dict__.items() if k not in ['data_frame', 'campaign']}

        with open(log_path, "w") as outfile:
            json.dump(self_dict, outfile, indent=4, default=json_utils.jdefault)

        if self.campaign is not None:
            state_file = os.path.join(output_dir, 'state_file.json')
            self.campaign.save_state(state_file)

        if isinstance(self.output_type, constants.OutputType):
            output_type_str = self.output_type.value

        log_info = {
                'output': self.output_file,
                'type': output_type_str,
                'logfile': log_path,
                'state': state_file,
                }

        self.campaign.log_element_application(self, log_info)


    def apply(self):
        # Run the element specific analysis, then log the application
        return_vals = self._apply_analysis()
        self._log_analysis()

        return return_vals
