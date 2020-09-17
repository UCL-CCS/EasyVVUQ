"""Classes implementing the sampling element for EasyVVUQ

Summary
-------
Samplers in the context of EasyVVUQ are classes that generate
sequences of parameter dictionaries. These dictionaries are then used
to create input files for the simulations.
"""

from .base import BaseSamplingElement, Vary
from .random import RandomSampler
from .stochastic_collocation import SCSampler
from .pce import PCESampler
from .qmc import QMCSampler
from .sweep import BasicSweep
from .sampler_of_samplers import MultiSampler
from .quasirandom import LHCSampler
from .empty import EmptySampler
from .replica_sampler import ReplicaSampler
from .mc_sampler import MCSampler

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
