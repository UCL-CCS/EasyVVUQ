import logging
import chaospy as cp
from .base import BaseSamplingElement, Vary

__author__ = "Jalal Lakhlili"
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


class QMCSampler(BaseSamplingElement, sampler_name="QMC_sampler"):
    def __init__(self,
                 vary=None,
                 count=0,
                 number_of_samples=1000,
                 sampling_rule="L"):
        """
        Create the sampler using Quasi-Monte Carlo Method

        Parameters
        ----------
        vary: dict or None
            keys = parameters to be sampled, values = distributions.

        count : int, optional
            Specified counter for Fast forward, default is 0.

        number_of_samples : int
            The number of samples requierd to get a given acccuray,
            default is 1000.

        sampling_rule : char, optional
            The sampling method, default is Latin Hypercube "L".

        """

        if vary is None:
            msg = ("'vary' cannot be None. RandomSampler must be passed a "
                   "dict of the names of the parameters you want to vary, "
                   "and their corresponding distributions.")
            logging.error(msg)
            raise Exception(msg)
        if not isinstance(vary, dict):
            msg = ("'vary' must be a dictionary of the names of the "
                   "parameters you want to vary, and their corresponding "
                   "distributions.")
            logging.error(msg)
            raise Exception(msg)
        if len(vary) == 0:
            msg = "'vary' cannot be empty."
            logging.error(msg)
            raise Exception(msg)

        self.vary = Vary(vary)
        self.sampling_rule = sampling_rule
        self.number_of_samples = number_of_samples

        # List of the probability distributions of uncertain parameters
        params_distribution = list(vary.values())

        # Multivariate distribution
        self.distribution = cp.J(*params_distribution)

        # Generate samples
        self._samples = self.distribution.sample(size=number_of_samples, rule=sampling_rule)

        # Fast forward to specified count, if possible
        self.count = 0
        if self.count >= self.number_of_samples:
            msg = (f"Attempt to start sampler fastforwarded to count {self.count}, "
                   f"but sampler only has {self._number_of_samples} samples, therefore"
                   f"this sampler will not provide any more samples.")
            logging.warning(msg)
        else:
            for i in range(count):
                self.__next__()

    def element_version(self):
        return "0.1"

    def is_finite(self):
        return True

    def is_restartable(self):
        return True

    def __next__(self):
        if self.count < self.number_of_samples:
            run_dict = {}
            i_par = 0
            for param_name in self.vary.get_keys():
                run_dict[param_name] = self._samples.T[self.count][i_par]
                i_par += 1
            self.count += 1
            return run_dict
        else:
            raise StopIteration

    def get_restart_dict(self):
        return {"vary": self.vary.serialize(),
                "count": self.count,
                "number_of_samples": self.number_of_samples,
                "sampling_rule": self.sampling_rule}
