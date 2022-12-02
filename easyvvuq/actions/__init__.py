"""This module contains implementations of various Actions. Actions in
EasyVVUQ are responsible for anything that is related to the execution of
the simulation. That includes: actually executing the simulation, preparing
the input files, parsing the output files, creating directory structures
necessary to execute the simulation, cleaning up after, delegating work
to external execution back-ends such as Dask, etc.
"""

from .execute_local import ExecuteLocal, ExecutePython, CreateRunDirectory, Encode, Decode, local_execute
from .execute_local import CleanUp, Actions
from .execute_qcgpj import QCGPJPool, EasyVVUQBasicTemplate, EasyVVUQParallelTemplate
from .execute_kubernetes import ExecuteKubernetes
from .execute_slurm import ExecuteSLURM
from .action_statuses import ActionPool

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
