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


def test_validate_similarity_shannon_jensen():
    validator = uq.comparison.validate.ValidateSimilarityShannonJensen()
    assert(validator.element_name() == 'validate_similarity_shannon_jensen')
    assert(validator.element_version() == '0.1')


def test_validate_similarity_wasserstein1():
    validator = uq.comparison.validate.ValidateSimilarityWasserstein1()
    assert(validator.element_name() == 'validate_similarity_wasserstein1')
    assert(validator.element_version() == '0.1')


def test_validate_similarity_wasserstein2():
    validator = uq.comparison.validate.ValidateSimilarityWasserstein2()
    assert(validator.element_name() == 'validate_similarity_wasserstein2')
    assert(validator.element_version() == '0.1')


def test_validate_compatibility():
    validator = uq.comparison.validate.ValidateCompatibility()
    validator.weight_factor = 0.2
    with pytest.raises(RuntimeError):
        validator.weight_factor = 1.5
    assert(validator.weight_factor == 0.2)
