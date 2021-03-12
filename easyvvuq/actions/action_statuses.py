import time
import dill
from concurrent.futures import ThreadPoolExecutor, as_completed

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


class ActionPool:
    """A class that tracks statuses of a list of actions.

    Parameters
    ----------
    statuses: list of ActionStatus
        a list of action statuses to track
    poll_sleep_time: int
        a time to sleep for after iterating over all active statuses
        before starting again

    """

    def __init__(self, campaign, actions, max_workers=8):
        self.campaign = campaign
        self.actions = list(actions)
        self.max_workers = max_workers
        self.futures = []

    def start(self):
        """Start the actions.

        Returns
        -------
        A list of Python futures represending action execution.
        """
        self.pool = ThreadPoolExecutor(max_workers=self.max_workers)
        for action in self.actions:
            future = self.pool.submit(action.start)
            self.futures.append(future)
        return self

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
        for future in self.futures:
            if future.running():
                running += 1
            elif future.done():
                if not future.result():
                    failed += 1
                else:
                    done += 1
            else:
                ready += 1
        return {'ready': ready, 'active': running, 'finished': done, 'failed': failed}

    def collect(self):
        """A command that will block untill all futures in the pool have finished.
        """
        for future in as_completed(self.futures):
            action = future.result()
            action.finalise()
        self.campaign.campaign_db.session.commit()
