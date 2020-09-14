from . import RandomSampler
from .base import Vary
import logging
import numpy as np
import chaospy as cp

__author__ = "Wouter Edeling"
"""
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


class MCSampler(RandomSampler, sampler_name='mc_sampler'):
    """
    This is a Monte Carlo sampler, used to compute the Sobol indices, mean
    and variance of the different QoIs.
    """

    def __init__(self, vary, n_mc_samples, **kwargs):
        """

        Parameters
        ----------
        + vary : a dictionary of chaospy input distributions
        + n_mc_samples : the number of MC samples. The total number of MC samples
          required to compute the Sobol indices using a Saltelli sampling plan
          will be n_mc_samples * (n_params + 1), where n_params is the number of
          uncertain parameters in vary.

        Returns
        -------
        None.

        """
        super().__init__(vary=vary, max_num=n_mc_samples, **kwargs)
        # the number of uncertain inputs
        self.n_params = len(vary)
        # the number of MC samples, for each of the n_params + 2 input matrices
        self.n_mc_samples = n_mc_samples
        self.vary = Vary(vary)
        self.count = 0
        # joint distribution
        self.joint = cp.J(*list(vary.values()))
        # create the Saltelli sampling plan
        self.saltelli(n_mc_samples)

    def __next__(self):

        if self.is_finite():
            if self.count >= self.max_num:
                raise StopIteration

        run_dict = {}
        for idx, param_name in enumerate(self.vary.get_keys()):
            run_dict[param_name] = self.xi_mc[self.count][idx]
        self.count += 1

        return run_dict

    def saltelli(self, n_mc):
        """
        Generates a Saltelli sampling plan of n_mc*(n_params + 2) input samples
        needed to compute the Sobol indices. Stored in xi_mc.

        Method: A. Saltelli, Making best use of model evaluations to compute
        sensitivity indices, Computer Physics Communications, 2002.

        Parameters
        ----------
        n_mc : the number of Monte Carlo samples per input matrix. The total
        number of samples is n_mc*(n_params + 2)

        Returns
        -------
        None.

        """
        logging.debug('Drawing input samples for Sobol index computation.')
        # the number of MC samples required to compute the Sobol indices
        self.max_num = n_mc * (self.n_params + 2)
        logging.debug('Generating {} input samples spread over {} sample matrices.'.format(
            self.max_num, self.n_params + 2))
        # Matrix M1, the sample matrix
        M_1 = self.joint.sample(n_mc).T
        # Matrix M2, the resample matrix (see reference above)
        M_2 = self.joint.sample(n_mc).T
        # array which contains all samples
        self.xi_mc = np.zeros([self.max_num, self.n_params])
        # The order in which the inputs samples must be stored is
        # [M2_1 N1_1, ..., Nd_1, M1_1, M2_2, N1_2, ...Nd_2, M1_2, M1_3 etc]
        # number of different sampling matrices
        step = self.n_params + 2
        # store M2 first, with entries separated by step places
        self.xi_mc[0:self.max_num:step] = M_2
        # store M1 entries last
        self.xi_mc[(step - 1):self.max_num:step] = M_1
        # store N_i entries between M2 and M1
        for i in range(self.n_params):
            N_i = np.array(M_2)
            # N_i = M2 with i-th colum from M1
            N_i[:, i] = M_1[:, i]
            self.xi_mc[(i + 1):self.max_num:step] = N_i
        logging.debug('Done.')

    def get_restart_dict(self):
        return {"vary": self.vary.serialize(), "n_mc_samples": self.n_mc_samples}
