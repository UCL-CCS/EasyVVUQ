import time
from concurrent.futures import ThreadPoolExecutor

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

    def __init__(self, statuses, batch_size=8, poll_sleep_time=1):
        self.statuses = list(statuses)
        self.actions = []
        self.poll_sleep_time = poll_sleep_time
        self.pool = ThreadPoolExecutor(batch_size)

    def job_handler(self, status):
        """Will handle the execution of this action status.

        Parameters
        ----------
        status: ActionStatus
            ActionStatus of an action to be executed.
        """
        status.start()
        while not status.finished():
            time.sleep(self.poll_sleep_time)
        if status.succeeded():
            status.finalise()
            return True
        else:
            return False

    def start(self):
        """Start the actions.

        Returns
        -------
        A list of Python futures represending action execution.
        """
        self.actions = [self.pool.submit(self.job_handler, status) for status in self.statuses]
        return self.actions

    def progress(self):
        """Some basic stats about the action statuses status.

        Returns
        -------
        A dictionary with four keys - 'ready', 'active' and 'finished', 'failed'.
        """
        ready = 0
        running = 0
        done = 0
        failed = 0
        for action in self.actions:
            if action.running():
                running += 1
            elif action.done():
                if not action.result():
                    failed += 1
                else:
                    done += 1
            else:
                ready += 1
        return {'ready': ready, 'active': running, 'finished': done, 'failed': failed}
