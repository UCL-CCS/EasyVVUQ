import os
import logging
import pandas as pd
from easyvvuq.decoders import BaseDecoder
from easyvvuq import OutputType

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


logger = logging.Logger(__name__)


class GaussDecoder(BaseDecoder, decoder_name="gauss"):

    def __init__(self, target_filename=None):

        if target_filename is None:
            msg = (
                f"target_filename must be set for SimpleCSV. This should be"
                f"the name of the output file this decoder acts on."
            )
            logging.error(msg)
            raise Exception(msg)

        self.output_type = OutputType('sample')
        self.target_filename = target_filename

    @staticmethod
    def _get_output_path(run_info=None, outfile=None):

        run_path = run_info['run_dir']

        if not os.path.isdir(run_path):
            raise RuntimeError(f"Run directory does not exist: {run_path}")

        return os.path.join(run_path, outfile)

    def sim_complete(self, run_info=None):

        out_path = self._get_output_path(run_info, self.target_filename)

        if not os.path.isfile(out_path):
            return False
        else:
            return True

    def parse_sim_output(self, run_info={}):

        out_path = self._get_output_path(run_info, self.target_filename)

        data = pd.read_csv(out_path, header=0, index_col=False)

        return data

    def get_restart_dict(self):
        return {"target_filename": self.target_filename}

    def element_version(self):
        return "0.1"
