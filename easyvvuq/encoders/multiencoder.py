import logging

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

logger = logging.getLogger(__name__)


class MultiEncoder:

    def __init__(self, *encoders):
        """
            Expects one or more encoders
        """
        self.encoders = encoders

    def encode(self, params={}, target_dir=''):
        """
            Applies all encoders in the list of encoders.
        """
        for encoder in self.encoders:
            encoder.encode(params=params, target_dir=target_dir)

    def is_restartable(self):
        return True
