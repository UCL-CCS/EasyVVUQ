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

    def dist(self, p, q):
        raise NotImplementedError

    def compare(self, dataframe1, dataframe2):
        """Perform comparison between two lists or arrays
        of discrete distributions.

        Parameters
        ----------
        dataframe1 : NumPy array or list
        dataframe2 : NumPy array or list

        Returns
        -------
        A list of distances between two lists of discrete distributions,
        dataframe1 and dataframe2.
        """

        if len(dataframe1) != len(dataframe2):
            raise RuntimeError("Input dataframe sizes are not equal")

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
        """ Compute Hellinger distance between two discrete probability
        distributions (PDF). The Hellinger distance metric gives an
        output in the range [0,1] with values closer to 0 meaning the
        PDFs are more similar.

        Parameters
        ----------
        p : NumPy array
        q : NumPy array

        Returns
        -------
        Hellinger distance between distributions p and q.
        https://en.wikipedia.org/wiki/Hellinger_distance
        """
        p /= p.sum()
        q /= q.sum()
        return np.sqrt(1. - np.sqrt(p * q).sum())


class ValidateSimilarityJensenShannon(ValidateSimilarity):
    def element_name(self):
        return "validate_similarity_jensen_shannon"

    def element_version(self):
        return "0.1"

    def dist(self, p, q):
        """ Compute Jensen-Shannon distance between two discrete
        probability distributions (PDF). It is based on Kullback–Leibler
        divergence and gives an output metric un the range [0,1] with
        values closer to 0 meaning the PDFs are more similar.

        Parameters
        ----------
        p : NumPy array
        q : NumPy array

        Returns
        -------
        Jensen-Shannon divergence between distributions p and q.
        https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence
        https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
        """
        p /= p.sum()
        q /= q.sum()
        m = 0.5 * (p + q)
        div = 0.5 * (st.entropy(p, m) + st.entropy(q, m))
        return np.sqrt(div / np.log(2))


class ValidateSimilarityWasserstein(ValidateSimilarity):
    def element_name(self):
        return "validate_similarity_wasserstein"

    def element_version(self):
        return "0.1"

    def dist(self, p, q):
        """ Compute Wasserstein distance between two discrete cumulative
        distributions (CDF). The Wasserstein distance has an
        unrestricted range with a lower limit of 0. A smaller distance
        indicates a stronger similarity between between CFDs.

        Parameters
        ----------
        p : NumPy array
        q : NumPy array

        Returns
        -------
        Wasserstein distance between distributions p and q.
        https://en.wikipedia.org/wiki/Wasserstein_metric
        """
        return st.wasserstein_distance(p, q)
