"""Validation by comparing QoI distributions.
"""
import numpy as np
import scipy.stats as st
from . import BaseComparisonElement


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
__author__ = 'Jalal Lakhlili'
__license__ = "LGPL"


class ValidateSimilarity(BaseComparisonElement):

    def __init__(self):
        pass

    def dist(p, q):
        raise NotImplemented

    def compare(self, dataframe1, dataframe2):
        """Perform comparaison between dataframe1 and dataframe2, two lists of:
            - discrete probability densities if the metric is Hellinger or Shannon-Jenson,
            - discrete cumulative distributions if the metric is Wasserstein 1 or 2.

        ASSUMPTION: each list can contain a set of scalar (floats, intgers), numpy.array
        or lists of (floats, intgers), results from the probability density or cumulative
        distribution functions.
        """

        if len(dataframe1) != len(dataframe2):
            raise RuntimeError("Input dataframe sizes are not equal")

        # output
        shape = np.shape(dataframe1)
        if len(shape) == 2:
            results = []
            for i in range(len(dataframe1)):
                p1 = np.array(dataframe1[i])
                p2 = np.array(dataframe2[i])
                d = self.dist(p1, p2)
                results.append(d)
        else:
            p1 = np.array(dataframe1)
            p2 = np.array(dataframe2)
            results = self.dist(p1, p2)

        return results


class ValidateSimilarityHellinger(ValidateSimilarity):
    def element_name(self):
        return "validate_similarity_hellinger"

    def element_version(self):
        return "0.1"

    def dist(self, p, q):
        p /= p.sum()
        q /= q.sum()
        return np.sqrt(1. - np.sqrt(p * q).sum())


class ValidateSimilarityShannonJenson(ValidateSimilarity):
    def element_name(self):
        return "validate_similarity_shannon_jenson"

    def element_version(self):
        return "0.1"

    def dist(self, p, q):
        p /= p.sum()
        q /= q.sum()
        m = 0.5 * (p + q)
        div = 0.5 * (st.entropy(p, m) + st.entropy(q, m))
        return np.sqrt(div / np.log(2))


class ValidateSimilarityWasserstein1(ValidateSimilarity):
    def element_name(self):
        return "validate_similarity_wasserstein1"

    def element_version(self):
        return "0.1"

    def dist(self, p, q):
        return st.wasserstein_distance(p, q)


class ValidateSimilarityWasserstein2(ValidateSimilarity):
    def element_name(self):
        return "validate_similarity_wassertstein1"

    def element_version(self):
        return "0.1"

    def dist(self, p, q):
        return st.energy_distance(p, q)


class ValidateCompatability(ValidateSimilarity):
    def __init__(self, weight_factor=0.5):
        """Measure compatability between two QoI distributions.
        Each distribution is characterized by three moments:
        Mean, variance and skewness.
        Lower metric means hight compatability.

        Parameters
        ----------
        weight_factor : float, optional
           parameter in [0, 1]
           default: 0.5
        """

        if weight_factor < 0. or weight_factor > 1.:
            raise RuntimeError("Validate_Compatability: Wrong parameter value.")

        self._weight_factor = weight_factor

    def element_name(self):
        return "Validate_Compatability"

    def element_version(self):
        return "0.1"

    def set_weight_factor(self, weight_factor):
        """
        Parameters
        ----------
        weight_factor : float
        """

        if weight_factor < 0. or weight_factor > 1.:
            raise RuntimeError("set_weight_factor: wrong parameter value.")
        self._weight_factor = weight_factor

    def get_weight_factor(self):
        return self._weight_factor

    def dist(self, mom1, mom2):
        m1 = mom1[0]
        v1 = mom1[1]
        s1 = mom1[2]
        m2 = mom2[0]
        v2 = mom2[1]
        s2 = mom2[2]
        term1 = (m2 - m1)**2 / (2 * (v1 + v2) + (m2 - m1)**2)
        term2 = (s2 - s1)**2 / (2 * (v1 + v2) + (m2 - m1)**2 + (abs(s1) + abs(s2))**2)
        return (1 - self._weight_factor) * term1 + self._weight_factor * term2
