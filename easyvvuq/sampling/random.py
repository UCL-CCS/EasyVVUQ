from .base import BaseSamplingElement, Vary
from copy import deepcopy
import numpy as np
import chaospy as cp

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


class RandomSampler(BaseSamplingElement, sampler_name="random_sampler"):

    def __init__(self, vary=None, count=0, max_num=0):
        """
            Expects dict of var names, and their corresponding distributions
        """
        self.vary = Vary(vary)
        self.count = count
        #the number of MC samples
        self.max_num = max_num
        #the number of uncertain inputs
        self.n_params = len(vary)
        #compute the Sobol indices
        self.compute_sobol = False
        #joint distribution
        self.joint = cp.J(*list(vary.values()))

    def element_version(self):
        return "0.2"

    def is_finite(self):
        if self.max_num > 0:
            return True
        return False

    def n_samples(self):
        """
        Returns the number of samples in this sampler.

        Returns
        -------
        if the user specifies maximum number of samples than return that, otherwise - error
        """
        if self.is_finite():
            return self.max_num
        else:
            raise RuntimeError("You can't get the number of samples in an infinite sampler")

    def __next__(self):

        if self.is_finite():
            if self.count >= self.max_num:
                raise StopIteration

        run_dict = {}
        if not self.compute_sobol:
            for param_name, dist in self.vary.get_items():
                run_dict[param_name] = dist.sample(1)[0]
        else:
            idx = 0
            for param_name in self.vary.get_keys():
                run_dict[param_name] = self.xi_mc[self.sobol_count][idx]
                idx += 1
            self.sobol_count += 1

        self.count += 1
        return run_dict

    def generate_sobol_samples(self, n_mc):
        """
        Generates the n_mc*(n_params + 2) input samples needed to compute the
        Sobol indices. Stored in MCAnalysis.xi_mc.

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
        print('Drawing input samples for Sobol index computation.')
        #set the flag to True
        self.compute_sobol = True
        #the index in the dataframe of the first sobol sample
        self.sobol_start = self.count
        #a counter for the sobol samples. Used in __next__
        self.sobol_count = 0
        #the number of MC samples required to compute the Sobol indices
        self.max_num = n_mc*(self.n_params + 2)
        print('Generating %d input samples spread over %d sample matrices.' % 
              (self.max_num, self.n_params + 2))
        #Matrix M1, the sample matrix
        M_1 = self.joint.sample(n_mc).T
        #<atrix M2, the resample matrix (see reference above)
        M_2 = self.joint.sample(n_mc).T
        #xi_mc will stores all input samples
        self.xi_mc = []
        self.xi_mc.append(M_1)
        self.xi_mc.append(M_2)
        #Compute the N_i matrices (see again reference above)
        for i in range(self.n_params):
            N_i = deepcopy(M_2)
            #N_i = M2 with i-th colum from M1
            N_i[:, i] = M_1[:, i]
            self.xi_mc.append(N_i)
        #turn into array of size n_mc*(n_params + 2) x n_params
        self.xi_mc = np.array(self.xi_mc).reshape([self.max_num, self.n_params])
        print('Done.')

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {"vary": self.vary.serialize(), 
                "max_num": self.max_num, "count": self.count}
