import time
import threading

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

    def __init__(self, statuses, poll_sleep_time=10):
        self.active = list(statuses)
        self.finished = []
        self.failed = []
        self.poll_sleep_time = poll_sleep_time
        polling_thread = threading.Thread(target=self.poll)
        polling_thread.start()

    def poll(self):
        """Iterate over active actions, finalize finished ones,
        sort finished actions into finished and failed. An action
        is considered finished if it has finished executed and reports
        success. It is considered failed if it has reported failure and
        is considered active (running) otherwise.
        """
        while True:
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
            if not active_:
                break
            else:
                time.sleep(self.poll_sleep_time)
        self.active = active_

    def stats(self):
        """Return the number of active, finished and failed jobs.
        """
        return {'active': len(self.active),
                'finished': len(self.finished),
                'failed': len(self.failed)}
