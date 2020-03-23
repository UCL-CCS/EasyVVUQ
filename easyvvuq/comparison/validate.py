import numpy as np
from scipy.stats import entropy, wasserstein_distance
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
__license__ = "LGPL"


class Validate_Similarity(BaseComparisonElement):

    def __init__(self, metric="jensen_shannon"):
        """Compare Similarities between two QoI distributions.

        Parameters
        ----------
        metric : str, optional
            supported metrics: jensen_shannon, hellinger, wasserstein.
            default: jensen_shannon, based on Kullback-Leibler divergence.
        """

        if metric not in ["jensen_shannon", "hellinger", "wasserstein"]:
            raise RuntimeError("Validate_Similarity: Unknown distance name.")

        self._metric = metric

    def element_name(self):
        return "validate_similarity"

    def element_version(self):
        return "0.1"

    def set_metric(self, metric):
        self._metric = metric

    def compare(self, dataframe1, dataframe2):
        """Perform comparaison between dataframe1 and dataframe2,
        two lists of discrete probability distributions.

        ASSUMPTION: each list can contain a set of numpy.array or lists
        of (floats, intgers), results from the probability density function.
        """

        if len(dataframe1) != len(dataframe2):
            raise RuntimeError("Input dataframe sizes are not equal")

        # Compute probability distance
        def dist(p, q):
            if self._metric == "jensen_shannon":
                return np.sqrt(0.5 * (entropy(p, 0.5 * (p + q)) +
                                      entropy(q, 0.5 * (p + q))))

            if self._metric == "hellinger":
                return np.sqrt(0.5 * ((np.sqrt(p) - np.sqrt(q))**2).sum())

            if self._metric == "wasserstein":
                return wasserstein_distance(p, q)

        #
        results = []
        for i in range(len(dataframe1)):
            p1 = np.array(dataframe1[i])
            p2 = np.array(dataframe2[i])
            d = dist(p1, p2)
            results.append(d)

        return results
