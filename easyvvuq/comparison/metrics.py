import logging
import numpy as np
import scipy as sp

__license__ = "LGPL"

logger = logging.getLogger(__name__)


def wasserstein(dist1, dist2):
    """
    Compute Wasserstein distance between two distributions
    (or samples from these distributions)
    """

    # TODO test if args are dist
    return sp.stats.wasserstein_distance(dist1, dist2)


def hellinger(dist1, dist2):
    """
    Calculate Hellinger distance between two distributions.

    Return value in range [0, 1], where 0 is min distance: max similarity,
    and 1 is max distance: min similarity.
    """

    # TODO test if args are dist
    return np.sqrt(0.5 * ((np.sqrt(dist1) - np.sqrt(dist2))**2).sum())


def kullback_leibler(dist1, dist2):
    """
    Calculate Kullback-Leibler distance between two distributions.

    Return value in range [0, +inf), where values closer to 0 mean less
    distance: higher similarity.
    """

    # TODO test if args are dist and convert samples to dense
    return sp.stats.entropy(dist1, dist2)
