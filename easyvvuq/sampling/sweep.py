from .base import BaseSamplingElement, Vary
import itertools

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

def wrap_dist(var_name, dist, max_num_draws):
    for i in range(max_num_draws):
        yield (var_name, dist.sample(1)[0])

class SweepSampler(BaseSamplingElement, sampler_name="sweep_sampler"):

    def __init__(self, vary=None):
        """
            Expects dict of var names, and their corresponding distributions
        """
        self.vary = Vary(vary)

        gens = []
        for var_name, dist in self.vary.get_items():
            gens.append(wrap_dist(var_name, dist, 3))

        # Combine all the iterables/generators into one
        self.sweep_iterator = itertools.product(*gens)

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def __next__(self):
        # Build runs
        for sweep_run in self.sweep_iterator:
            run_dict = {}
            for var_name, value in sweep_run:
                run_dict[var_name] = value
            return run_dict
        else:
            raise StopIteration

    def is_restartable(self):
        return False

    def get_restart_dict(self):
        return {"vary": self.vary.serialize()}
