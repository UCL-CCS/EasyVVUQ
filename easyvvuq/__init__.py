import json
from .campaign import Campaign
from .execute import execute_local
from . import uqp
from . import reader
import pkg_resources

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


DEFAULT_ENCODERS = pkg_resources.resource_filename(__name__, 'default_app_encoders.json')

with open(DEFAULT_ENCODERS) as fin:
    app_encoders = json.load(fin)

# TODO: Search for user specified encoders list
user_encoders = ''

if user_encoders:
    with open(user_encoders) as fin:
        app_encoders.update(json.load(fin))
