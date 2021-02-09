import pickle
from .base import BaseSamplingElement, Vary
import numpy as np

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
        self.max_num = max_num
        self.xi_d = []

    def element_version(self):
        return "0.1"

    def is_finite(self):
        if self.max_num > 0:
            return True
        return False

    def __next__(self):

        if self.is_finite():
            if self.count >= self.max_num:
                raise StopIteration

        run_dict = {}
        param = np.zeros(len(self.vary.get_keys()))
        idx = 0
        for param_name, dist in self.vary.get_items():
            sample = dist.sample(1)[0]
            param[idx] = sample
            idx += 1
            #convert integers to float, e.g 2 --> 2.0
            if type(sample) == np.dtype(int).type:
                sample = np.float(sample)
            run_dict[param_name] = sample

        self.xi_d.append(param)
        self.count += 1
        return run_dict

    def save_state(self, filename):
        print("Saving sampler state to %s" % filename)
        file = open(filename, 'wb')
        pickle.dump(self.__dict__, file)
        file.close()

    def load_state(self, filename):
        print("Loading sampler state from %s" % filename)
        file = open(filename, 'rb')
        self.__dict__ = pickle.load(file)
        file.close()

    def is_restartable(self):
        return True

    def get_restart_dict(self):
        return {"vary": self.vary.serialize(), "max_num": self.max_num, "count": self.count}
