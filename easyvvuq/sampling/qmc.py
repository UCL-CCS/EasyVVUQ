"""This sampler is meant to be used with the QMC Analysis module.
"""

import logging
import numpy as np
import chaospy as cp
from SALib.sample import saltelli
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
    def __init__(self, vary, n_mc_samples, count=0):
        """Create a Quasi Monte Carlo sampler.

        Parameters 
        ---------- 

        vary: dict
            Expects a dictionary where the keys are variable names
            (inputs for your simulation that you want to vary during
            sampling) and values are ChaosPy distributions you want to
            sample from.
        n_mc_samples : int
            An estimate for how many samples the monte carlo run will need.
        count : int
            This is used to resume sampling. It will skip the first
            count samples if this parameter is not zero.
        """
        if not isinstance(vary, dict):
            msg = ("'vary' must be a dictionary of the names of the "
                   "parameters you want to vary, and their corresponding "
                   "distributions.")
            raise RuntimeError(msg)
        if len(vary) == 0:
            msg = "'vary' cannot be empty."
            raise RuntimeError(msg)

        self.vary = Vary(vary)
        self.n_mc_samples = n_mc_samples

        # List of the probability distributions of uncertain parameters
        params_distribution = list(vary.values())

        # Multivariate distribution
        self.distribution = cp.J(*params_distribution)

        # Generate samples
        self.n_params = len(vary)
        n_sobol_samples = int(np.round(n_mc_samples / 2.))

        dist_U = []
        for i in range(self.n_params):
            dist_U.append(cp.Uniform())
        dist_U = cp.J(*dist_U)

        problem = {
            "num_vars": self.n_params,
            "names": list(vary.keys()),
            "bounds": [[0, 1]] * self.n_params
        }

        nodes = saltelli.sample(problem, n_sobol_samples, calc_second_order=False)
        
        self._samples = self.distribution.inv(dist_U.fwd(nodes.transpose()))

        self._n_samples = n_sobol_samples * (self.n_params + 2)

        # Fast forward to specified count, if possible
        self.count = 0
        if self.count >= self._n_samples:
            msg = (f"Attempt to start sampler fastforwarded to count {self.count}, "
                   f"but sampler only has {self._n_samples} samples, therefore"
                   f"this sampler will not provide any more samples.")
            logging.warning(msg)
        else:
            for i in range(count):
                self.__next__()

    def element_version(self):
        """Version number for the sampler."""
        return "0.2"

    def is_finite(self):
        """Can this sampler produce only a finite number of samples."""
        return True

    @property
    def n_samples(self):
        """
        Number of samples (Ns) of QMC method.
        To be able to compute the Sobol indices, using Saltelli's
        sampling scheme: NS = (d + 2)*N/2.
        Where: d is the number of uncertain parameters and N is the
        number of samples for MC method, by default N = 10**4.
        """
        return self._n_samples

    def is_restartable(self):
        """Can this sampler be resumed.
        """
        return True

    def __next__(self):
        if self.count < self.n_samples:
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
        """This information 
        return {
            "vary": self.vary.serialize(),
            "count": self.count,
            "n_mc_samples": self.n_mc_samples
        }
