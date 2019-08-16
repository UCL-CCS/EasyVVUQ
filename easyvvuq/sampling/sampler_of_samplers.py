from .base import BaseSamplingElement
import itertools
import sys

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


class MultiSampler(BaseSamplingElement, sampler_name="multisampler"):

    def __init__(self, *samplers, count=0):
        """
            Expects one or more samplers
        """
        self.samplers = samplers

        # Multisampler is finite only if all samplers in it are finite
        self._is_finite_bool = True
        for sampler in self.samplers:
            if sampler.is_finite() == False:
                self._is_finite_bool = False
                break

        if self._is_finite_bool == False:
            sys.exit("Multisampler must be composed of finite samplers")

        # Combine all the iterables/generators into one
        self.multi_iterator = itertools.product(*self.samplers)

        self.count = 0
        for i in range(count):
            try:
                self.__next__()
            except StopIteration:
                logger.warning("Multisampler constructed, but has no samples left to draw.")

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return self._is_finite_bool

    def __next__(self):
        # Will raise StopIteration when there are none left
        multisampler_run = self.multi_iterator.__next__()

        run_dict = {}
        for contribution in multisampler_run:
            run_dict = {**run_dict, **contribution}

        self.count += 1
        return run_dict

    def is_restartable(self):
        return False

    def get_restart_dict(self):
        return None
