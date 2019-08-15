from .base import BaseSamplingElement

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

    def __init__(self, *samplers):
        """
            Expects one or more samplers
        """
        self.samplers = samplers

        # Multisampler is finite only if all samplers in it are finite
        self.is_finite = True
        for sampler in self.samplers:
            if sampler.is_finite() == False:
                self.is_finite = False
                break

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return self.is_finite

    def __next__(self):
        run_dict = {}
        for param_name, dist in self.vary.get_items():
            run_dict[param_name] = dist.sample(1)[0]
        return run_dict

    def is_restartable(self):
        return False

    def get_restart_dict(self):
        return None
