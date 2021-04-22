from concurrent.futures import ThreadPoolExecutor, as_completed
from dask.distributed import Client
from tqdm import tqdm
import copy

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
    """A class that handles the execution of actions.

    Parameters
    ----------
    campaign: Campaign
        An instance of an EasyVVUQ campaign.
    actions: Actions
        An instance of Actions containing things to be done as part of the simulation.
    inits: iterable
        Initial inputs to be passed to each Actions representing a sample. Will usually contain
        dictionaries with the following information: {'run_id': ..., 'campaign_dir': ..., 'run_info': ...}.
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

    def start(self, pool=None):
        """Start the actions.

        Parameters
        ----------
        pool: An Executor instance (e.g. ThreadPoolExecutor)

        Returns
        -------
        ActionPool
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

    def collate(self, progress_bar=False):
        """A command that will block untill al futures in the pool have finished.
        It will also store the results in the database.

        Parameters
        ----------
        progress_bar: bool
           Whether to show progress bar
        """
        if not progress_bar:
            tqdm_ = lambda x, total=None: x
        else:
            tqdm_ = tqdm
        if isinstance(self.pool, Client):
            self.results = self.pool.gather(self.futures)
        if self.sequential or isinstance(self.pool, Client):
            for result in tqdm_(self.results, total=len(self.results)):
                self.campaign.campaign_db.store_result(result['run_id'], result)
        else:
            for future in tqdm_(as_completed(self.futures), total=len(self.futures)):
                result = future.result()
                self.campaign.campaign_db.store_result(result['run_id'], result)
        self.campaign.campaign_db.session.commit()
