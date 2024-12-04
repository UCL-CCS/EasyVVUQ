"""Implements ActionPool - a thin wrapper around the Python Executor interface
that is meant to simplify the execution of actions and retrieval of results.
This object is instantiated by the Campaign. The user would never instantiate it
manually. The user does interact with it to track the progress of execution.
"""
import concurrent
from concurrent.futures import ThreadPoolExecutor
from dask.distributed import Client
from tqdm import tqdm
import copy

from . import QCGPJPool

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
    """A class that handles the execution of Actions.

    Parameters
    ----------
    campaign: Campaign
        An instance of an EasyVVUQ campaign.
    actions: Actions
        An instance of `Actions` containing things to be done as part of the simulation.
    inits: iterable
        Initial inputs to be passed to each `Actions` representing a sample. Will usually contain
        dictionaries with the following information: {'run_id': ..., 'campaign_dir': ...,
        'run_info': ...}.
    sequential: bool
        Will run the actions sequentially.
    """

    def __init__(self, campaign, actions, inits, sequential=False):
        self.campaign = campaign
        self.actions = actions
        self.inits = inits
        self.sequential = sequential
        self.futures = []
        self.results = []
        self._collate_callback = lambda previous: previous

    def start(self, pool=None):
        """Start the actions.

        Parameters
        ----------
        pool: An Executor instance (e.g. ThreadPoolExecutor)

        Returns
        -------
        ActionPool
            Starts execution and returns a reference to itself for tracking progress
            and for collation.
        """
        if pool is None:
            pool = ThreadPoolExecutor()
        self.pool = pool
        for previous in self.inits:
            previous = copy.copy(previous)
            if self.sequential:
                result = self.actions.start(previous)
                self.results.append(result)
            else:
                future = self.pool.submit(self.actions.start, previous)
                self.futures.append(future)
        return self

    def progress(self):
        """Some basic stats about the action statuses status.

        Returns
        -------
        dict
            A dictionary with four keys - 'ready', 'active' and 'finished', 'failed'.
            Values under "ready" correspond to `Actions` waiting for execution, "active"
            corresponds to the number of currently running tasks.
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

    def add_collate_callback(self, fn):
        """Adds a callback to be called after collation is done.

        Parameters
        ----------
        fn - A callable that takes previous as it's only input.
        """
        self._collate_callback = fn

    def collate(self, progress_bar=False):
        """A command that will block until all Futures in the pool have finished.
        It will also store the results gather from `Actions` in the database.

        Parameters
        ----------
        progress_bar: bool
           Whether to show progress bar
        """
        if not progress_bar:
            def tqdm_(x, total=None): return x
        else:
            tqdm_ = tqdm
        if isinstance(self.pool, Client):
            self.results = self.pool.gather(self.futures)
        if self.sequential or isinstance(self.pool, Client):
            for result in tqdm_(self.results, total=len(self.results)):
                result = self._collate_callback(result)
                self.campaign.campaign_db.store_result(
                    result['run_id'], result, change_status=result['collated'])
        else:
            if isinstance(self.pool, QCGPJPool):
                as_completed_fn = self.pool.as_completed
                self.add_collate_callback(self.pool.convert_results)
            else:
                as_completed_fn = concurrent.futures.as_completed

            for future in tqdm_(as_completed_fn(self.futures), total=len(self.futures)):
                result = self._collate_callback(future.result())
                self.campaign.campaign_db.store_result(
                    result['run_id'], result, change_status=result['collated'])
        self.campaign.campaign_db.session.commit()
