import os
import json
from easyvvuq.encoders import BaseEncoder

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


class GaussEncoder(BaseEncoder, encoder_name="gauss"):

    def __init__(self, target_filename="gauss_input.json"):
        self.target_filename = target_filename

    def encode(self, params={}, target_dir=''):

        out_file = params['out_file']
        num_steps = params['num_steps']
        mu = params['mu']
        sigma = params['sigma']

        output_str = (f'{{"outfile": "{out_file}", "num_steps": "{num_steps}",'
                      f' "mu": "{mu}", "sigma": "{sigma}"}}\n')

        target_file_path = os.path.join(target_dir, self.target_filename)
        with open(target_file_path, "w") as outfile:
            outfile.write(output_str)

    def get_restart_dict(self):
        return {"target_filename": self.target_filename}

    def element_version(self):
        return "0.1"
