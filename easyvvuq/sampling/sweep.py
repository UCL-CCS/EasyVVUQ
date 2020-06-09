from .base import BaseSamplingElement
import itertools
import logging
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


def wrap_iterable(var_name, iterable):
    for val in iterable:
        yield (var_name, val)


class BasicSweep(BaseSamplingElement, sampler_name="basic_sweep"):

    def __init__(self, sweep=None, count=0):
        """
            Expects dict of var names, and their corresponding lists of values to cycle through
        """
        self.sweep = sweep

        gens = []
        for var_name, iterable in self.sweep.items():
            gens.append(wrap_iterable(var_name, iterable))

        # Combine all the iterables/generators into one
        self.sweep_iterator = itertools.product(*gens)

        self.count = 0
        for i in range(count):
            try:
                self.__next__()
            except StopIteration:
                logger.warning("BasicSweep constructed, but has no samples left to draw.")

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def n_samples(self):
        """Returns the number of samples in this sampler.

        Returns
        -------
        a product of the lengths of lists passed to BasicSweep
        """
        return functools.reduce(
            lambda x, y: x * y, [len(lst) for lst in [self.sweep[key] for key in self.sweep]], 1)

    def __next__(self):
        # Will raise StopIteration when there are none left
        sweep_run = self.sweep_iterator.__next__()

        run_dict = {}
        for var_name, value in sweep_run:
            run_dict[var_name] = value

        self.count += 1
        return run_dict

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {"sweep": self.sweep, "count": self.count}
