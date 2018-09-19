from .base import BaseDecoder

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


class GenericEncoder(BaseDecoder):

    def __init__(self, run_info, *args, **kwargs):

        # Handles creation of `self.app_info` attribute (dicts)
        super().__init__(run_info, *args, **kwargs)

    def sim_complete(self, run_info={}, *args, **kwargs):
        raise NotImplementedError

    def parse_sim_output(self, run_info={}, *args, **kwargs):
        raise NotImplementedError
