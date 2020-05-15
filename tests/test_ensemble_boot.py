from easyvvuq.analysis.ensemble_boot import confidence_interval, bootstrap
from easyvvuq.analysis.ensemble_boot import ensemble_bootstrap, EnsembleBoot
import os
import numpy as np
import pandas as pd
import pytest


def test_confidence_interval():
    dist = np.array([])
    with pytest.raises(ValueError):
        stat, low, high = confidence_interval(dist, 0.0, 0.05)
    dist = np.array([0.0])
    stat, low, high = confidence_interval(dist, 0.0, 0.05)
    assert(stat == low == high == 0.0)
