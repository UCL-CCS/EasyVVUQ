import logging
import chaospy as cp
from easyvvuq.distributions import Assymetric_Normal, Split_Normal

__license__ = "LGPL"

logger = logging.getLogger(__name__)


def QoiDist_from_samples(samples, lo=None, up=None):
    """
    Constructs distributions based on experimental QoI data.

    Estimates a distribution from the given samples by constructing a kernel
    density estimator (KDE).


    Attributes
    ----------
    samples : numpy.ndarray
        Name of the particular Validation Element.
    lo : float
        Location of lower threshold
    up : float
        Location of upper threshold
    """

    return cp.SampleDist(samples, lo, up)


# TODO define genic dist with chaospy structure
def QoiDist_from_moments(data, lo, up, dist=None):
    """
    Constructs distributions based on experimental QoI moments.

    Uses two-pieces normal distribution.

    Attributes
    ----------
    data : float
        The 1st moment (the mode or the mean)
    lo : float
        Location of lower threshold or the left-hand-side std
    up : float
        Location of upper threshold or the right-hand-side std
    """

    if dist=="assymetric_normal":
        return Assymetric_Normal(data, lo, up)

    if dist=="split_normal":
        return Split_Normal(data, lo, up)
