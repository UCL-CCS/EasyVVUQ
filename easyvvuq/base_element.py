import json

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


class BaseElement(object):
    """Baseclass for all EasyVVUQ elements.

    Attributes
    ----------

    """

    def element_name(self):
        raise NotImplementedError

    def element_version(self):
        raise NotImplementedError

    def element_category(self):
        raise NotImplementedError

    def is_restartable(self):
        return False

    def get_restart_dict(self):
        return None

    def serialize(self):
        return json.dumps({
            "element_name": self.element_name(),
            "element_version": self.element_version(),
            "element_category": self.element_category(),
            "restartable": self.is_restartable(),
            "state": self.get_restart_dict()
        })
