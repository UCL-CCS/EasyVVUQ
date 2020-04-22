"""Validation by comparing Similarities between QoI distributions.
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


class Validate_Similarity(BaseComparisonElement):

    def __init__(self, metric="H"):
        """Compare Similarities between two QoI distributions.
        The comparison can use one of the following metrics:
            - Hellinger.
            - Jensen Shannon (symmetrized verion of Kullback-Leibler divergence),
            - Wasserstein 1 and Wasserstein 2 (called also Earth mover's).
        Lower distance means hight similarity.

        Parameters
        ----------
        metric : str, optional
           supported metrics:
           Hellinger (H), Jensen Shannon (JS), Wasserstein 1 (W1) and  Wasserstein 2 (W2).
           default: Hellinger (H).
        """

        if metric not in ["H", "JS", "W1", "W2"]:
            raise RuntimeError("Validate_Similarity: Unknown distance name.")

        self._metric = metric

    def element_name(self):
        return "validate_similarity"

    def element_version(self):
        return "0.1"

    def set_metric(self, metric):
        """
        Parameters
        ----------
        metric : str
            supported metrics:
                H  : Hellinger
                JS : Jensen Shannon
                W1 : Wasserstein 1
                W2 : Wasserstein 2
        """

        self._metric = metric

    def get_metric(self):
        return self._metric

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

        # Compute the distance
        def dist(p, q):
            if self._metric == "H":
                p /= p.sum()
                q /= q.sum()
                return np.sqrt(1. - np.sqrt(p * q).sum())

            if self._metric == "JS":
                p /= p.sum()
                q /= q.sum()
                m = 0.5 * (p + q)
                div = 0.5 * (st.entropy(p, m) + st.entropy(q, m))
                return np.sqrt(div / np.log(2))

            if self._metric == "W1":
                return st.wasserstein_distance(p, q)

            if self._metric == "W2":
                return st.energy_distance(p, q)

        # output
        shape = np.shape(dataframe1)
        if len(shape) == 2:
            results = []
            for i in range(len(dataframe1)):
                p1 = np.array(dataframe1[i])
                p2 = np.array(dataframe2[i])
                d = dist(p1, p2)
                results.append(d)
        else:
            p1 = np.array(dataframe1)
            p2 = np.array(dataframe2)
            results = dist(p1, p2)

        return results
