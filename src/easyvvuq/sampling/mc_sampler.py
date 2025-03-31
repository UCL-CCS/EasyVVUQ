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


class MCSampler(RandomSampler, sampler_name='MC_sampler'):
    """
    This is a Monte Carlo sampler, used to compute the Sobol indices, mean
    and variance of the different QoIs.
    """

    def __init__(self, vary, n_mc_samples, rule='latin_hypercube', **kwargs):
        """

        Parameters
        ----------
        vary : dict
            A dictionary of chaospy input distributions

        n_mc_samples : int
            The number of MC samples. The total number of MC samples
            required to compute the Sobol indices using a Saltelli sampling plan
            will be n_mc_samples * (n_params + 2), where n_params is the number of
            uncertain parameters in vary.

        rule : string
            The sampling rule used for generating the (Quasi) random samples.
            The default value is 'latin_hypercube', for a space-filling plan.           
            Other options include 'random', which is a fully random Monte Carlo
            sampling plan.

        Returns
        -------
        None.

        """
        super().__init__(vary=vary, count=0, max_num=n_mc_samples, **kwargs)
        # the number of uncertain inputs
        self.n_params = len(vary)
        # List of the probability distributions of uncertain parameters
        self.params_distribution = list(vary.values())
        # the number of MC samples, for each of the n_params + 2 input matrices
        self.n_mc_samples = n_mc_samples
        # sampling rule
        self.rule = rule
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
            current_param = self.xi_mc[self.count][idx]
            if isinstance(self.params_distribution[idx], cp.DiscreteUniform):
                current_param = int(current_param)
            run_dict[param_name] = current_param


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
        input_samples = self.joint.sample(2 * n_mc, rule=self.rule).T
        # Matrix M1, the sample matrix
        # M_1 = self.joint.sample(n_mc, rule=self.rule).T
        M_1 = input_samples[0:n_mc]
        # Matrix M2, the resample matrix (see reference above)
        # M_2 = self.joint.sample(n_mc, rule=self.rule).T
        M_2 = input_samples[n_mc:]
        # array which contains all samples
        self.xi_mc = np.zeros([self.max_num, self.n_params])
        # The order in which the inputs samples must be stored is
        # [M2_1 N1_1, ..., Nd_1, M1_1, M2_2, N1_2, ...Nd_2, M1_2, M1_3 etc]
        # number of different sampling matrices
        step = self.n_params + 2
        # store M2 first, with entries separated by step places
        if M_2.ndim == 1:
            M_2 = M_2.reshape([-1, 1])
        self.xi_mc[0:self.max_num:step] = M_2
        # store M1 entries last
        if M_1.ndim == 1:
            M_1 = M_1.reshape([-1, 1])
        self.xi_mc[(step - 1):self.max_num:step] = M_1
        # store N_i entries between M2 and M1
        for i in range(self.n_params):
            N_i = np.copy(M_2)
            # N_i = M2 with i-th colum from M1
            N_i[:, i] = M_1[:, i]
            self.xi_mc[(i + 1):self.max_num:step] = N_i
        logging.debug('Done.')

    @property
    def analysis_class(self):
        """Return a corresponding analysis class.
        """
        from easyvvuq.analysis import QMCAnalysis
        return QMCAnalysis
