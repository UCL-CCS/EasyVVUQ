__copyright__ = """

    Copyright 2020 Vytautas Jancauskas

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


class ActionStatuses:
    """A class that tracks statuses of a list of actions.
    """
    def __init__(self):
        self.active = []
        self.finished = []
        self.failed = []

    def add(self, action_status):
        """Add a new action status to the list.

        Parameters
        ----------
        action_status : ActionStatus
            an object representing an actions status
        """
        self.active.append(action_status)

    def poll(self):
        """Iterate over active actions, finalize finished ones,
        sort finished actions into finished and failed. An action
        is considered finished if it has finished executed and reports
        success. It is considered failed if it has reported failure and
        is considered active (running) otherwise.
        """
        active_ = []
        for status in self.active:
            if status.finished():
                if status.succeeded():
                    status.finalise()
                    self.finished.append(status)
                else:
                    self.failed.append(status)
            else:
                active_.append(status)
        self.active = active_

    def stats(self):
        """Return the number of active, finished and failed jobs.
        """
        return {'active': len(self.active),
                'finished': len(self.finished),
                'failed': len(self.failed)}
