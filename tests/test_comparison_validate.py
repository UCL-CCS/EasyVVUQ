import numpy as np
import chaospy as cp
import easyvvuq as uq
import pytest


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


def test_validate_similarity():
    pass


def test_validate_similarity_hellinger():
    validator = uq.comparison.validate.ValidateSimilarityHellinger()
    assert(validator.element_name() == 'validate_similarity_hellinger')
    assert(validator.element_version() == '0.1')
    d1 = cp.Exponential(1)
    d2 = cp.Exponential(2)
    xmin = min(d1.lower[0], d2.lower[0])
    xmax = max(d1.upper[0], d2.upper[0])
    x = np.linspace(xmin, xmax, 100)
    p1 = d1.pdf(x)
    p2 = d2.pdf(x)
    distance = validator.compare(p1, p2)
    err = abs(distance - np.sqrt(1 - 2 * np.sqrt(2) / 3))
    assert err < 1.e-2


def test_validate_similarity_jensen_shannon():
    validator = uq.comparison.validate.ValidateSimilarityJensenShannon()
    assert(validator.element_name() == 'validate_similarity_jensen_shannon')
    assert(validator.element_version() == '0.1')
    d1 = cp.Normal(0, 1)
    d2 = cp.Normal(1, 2)
    xmin = min(d1.lower[0], d2.lower[0])
    xmax = max(d1.upper[0], d2.upper[0])
    x = np.linspace(xmin, xmax, 100)
    p1 = d1.pdf(x)
    p2 = d2.pdf(x)
    distance = validator.compare(p1, p2)
    assert distance >= 0.0 and distance <= 1.0


def test_validate_similarity_wasserstein():
    validator = uq.comparison.validate.ValidateSimilarityWasserstein()
    assert(validator.element_name() == 'validate_similarity_wasserstein')
    assert(validator.element_version() == '0.1')
    d1 = cp.Normal(0, 1)
    d2 = cp.Normal(1, 2)
    xmin = min(d1.lower[0], d2.lower[0])
    xmax = max(d1.upper[0], d2.upper[0])
    x = np.linspace(xmin, xmax, 100)
    p1 = (xmax - xmin) * d1.cdf(x)
    p2 = (xmax - xmin) * d2.cdf(x)
    distance = validator.compare(p1, p2)
    assert distance >= 0.0
