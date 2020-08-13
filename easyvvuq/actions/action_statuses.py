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

    Parameters
    ----------
    statuses: list of ActionStatus
        a list of action statuses to track
    poll_sleep_time: int
        a time to sleep for after iterating over all active statuses
        before starting again

    """

    def __init__(self, statuses, batch_size, poll_sleep_time=1):
        self.ready = list(statuses)
        self.active = []
        self.finished = []
        self.failed = []
        self.batch_size = batch_size
        self.poll_sleep_time = poll_sleep_time
        self._stats = {
            'ready': len(self.ready),
            'active': 0,
            'finished': 0,
            'failed': 0
        }
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
            ready_ = []
            for status in self.ready:
                if len(self.active) < self.batch_size:
                    status.start()
                    self.active.append(status)
                    self._stats['active'] += 1
                    self._stats['ready'] -= 1
                else:
                    ready_.append(status)
            self.ready = ready_
            active_ = []
            for status in self.active:
                if status.finished():
                    self._stats['active'] -= 1
                    if status.succeeded():
                        self._stats['finished'] += 1
                        status.finalise()
                        self.finished.append(status)
                    else:
                        self._stats['failed'] += 1
                        self.failed.append(status)
                else:
                    active_.append(status)
            self.active = active_
            if (not active_) and (not ready_):
                break
            else:
                time.sleep(self.poll_sleep_time)

    def progress(self):
        """Return the number of active, finished and failed jobs.
        """
        return self._stats
