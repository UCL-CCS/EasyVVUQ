import json
import types
from easyvvuq.constants import OutputType

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


def process_json(src):
    """Interpret JSON input (given as stream/file or filename), return dict

        Parameters
        ----------
        src
            Source stream/file or filename.

        Returns
        -------
        dict
            The result of interpreting input as JSON.

    """

    if hasattr(src, 'read'):

        json_stream = src

    else:

        try:
            json_stream = open(src, 'r')

        except Exception as e:

            reasoning = (
                f"\nInputs to Wrapper must be dict or valid JSON (stream "
                f"or read from filename) but received {type(src)} {src}"
            )

            raise Exception(str(e) + reasoning)

    return json.load(json_stream)


def jdefault(obj):
    """
    Create some default serializations for non-simple objects (to use in logging)

    Parameters
    ----------
    obj

    Returns
    -------

    """

    if isinstance(obj, set):
        return list(obj)

    if isinstance(obj, types.GeneratorType):
        return obj.__name__

    if callable(obj):
        return obj.__str__

    if isinstance(obj, OutputType):
        return obj.value

    return obj.__dict__
