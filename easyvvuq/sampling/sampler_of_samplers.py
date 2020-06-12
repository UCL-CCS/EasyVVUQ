from .base import BaseSamplingElement
import logging
import itertools
import functools

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


class MultiSampler(BaseSamplingElement, sampler_name="multisampler"):

    def __init__(self, *samplers, count=0, serialized_list_of_samplers=None):
        """
            Expects one or more samplers
        """

        # If no serialized samplers list passed, generate one. Else deserialize the passed samplers.
        if len(samplers) < 1 and serialized_list_of_samplers is None:
            raise RuntimeError("You need to supply at least one sampler to the MultiSampler")
        if serialized_list_of_samplers is None:
            self.samplers = samplers
            self.serialized_list_of_samplers = [sampler.serialize() for sampler in self.samplers]
        else:
            self.serialized_list_of_samplers = serialized_list_of_samplers
            self.samplers = []
            for serialized_sampler in self.serialized_list_of_samplers:
                self.samplers.append(BaseSamplingElement.deserialize(serialized_sampler))

        # Multisampler is finite only if all samplers in it are finite
        for sampler in self.samplers:
            if sampler.is_finite() is False:
                msg = "Multisampler must be composed of finite samplers"
                logger.critical(msg)
                raise RuntimeError(msg)

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
        return True

    def n_samples(self):
        """Returns the number of samples in this sampler.

        Returns
        -------
        a product of the sizes of samplers passed to MultiSampler
        """
        return functools.reduce(
            lambda x, y: x * y, [sampler.n_samples() for sampler in self.samplers], 1)

    def __next__(self):
        # Will raise StopIteration when there are none left
        multisampler_run = self.multi_iterator.__next__()

        run_dict = {}
        for contribution in multisampler_run:
            run_dict = {**run_dict, **contribution}

        self.count += 1
        return run_dict

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {'serialized_list_of_samplers': self.serialized_list_of_samplers}
