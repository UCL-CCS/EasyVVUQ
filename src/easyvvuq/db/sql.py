"""Provides class that allows access to an SQL Database that serves as the back-end to EasyVVUQ.


"""
import os
import json
import logging
import pandas as pd
import numpy as np
from sqlalchemy.sql import case
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import MetaData
from sqlalchemy import text
from sqlalchemy.engine import Engine
from sqlalchemy import event
from .base import BaseCampaignDB
from easyvvuq import constants
from easyvvuq import ParamsSpecification
from easyvvuq.utils.helpers import easyvvuq_serialize, easyvvuq_deserialize


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

COMMIT_RATE = 50000

logger = logging.getLogger(__name__)

Base = declarative_base()


class DBInfoTable(Base):
    """An SQLAlchemy schema for the database information table.
    """
    __tablename__ = 'db_info'
    id = Column(Integer, primary_key=True)
    next_run = Column(Integer)


class CampaignTable(Base):
    """An SQLAlchemy schema for the campaign information table.
    """
    __tablename__ = 'campaign_info'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    easyvvuq_version = Column(String)
    campaign_dir_prefix = Column(String)
    campaign_dir = Column(String)
    runs_dir = Column(String)
    sampler = Column(Integer, ForeignKey('sampler.id'))
    active_app = Column(Integer, ForeignKey('app.id'))


class AppTable(Base):
    """An SQLAlchemy schema for the app table.
    """
    __tablename__ = 'app'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    params = Column(String)
    actions = Column(String)


class RunTable(Base):
    """An SQLAlchemy schema for the run table.
    """
    __tablename__ = 'run'
    id = Column(Integer, primary_key=True)
    run_name = Column(String, index=True)
    app = Column(Integer, ForeignKey('app.id'))
    params = Column(String)
    status = Column(Integer)
    run_dir = Column(String)
    result = Column(String, default="{}")
    execution_info = Column(String, default="{}")
    campaign = Column(Integer, ForeignKey('campaign_info.id'))
    sampler = Column(Integer, ForeignKey('sampler.id'))
    iteration = Column(Integer, default=0)


class SamplerTable(Base):
    """An SQLAlchemy schema for the run table.
    """
    __tablename__ = 'sampler'
    id = Column(Integer, primary_key=True)
    sampler = Column(String)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA synchronous = OFF")
    cursor.execute("PRAGMA journal_mode = OFF")
    cursor.close()


class CampaignDB(BaseCampaignDB):
    """An interface between the campaign database and the campaign.

    Parameters
    ----------
    location: str
       database URI as needed by SQLAlchemy
    """

    def __init__(self, location=None):
        if location is not None:
            self.engine = create_engine(location)
        else:
            self.engine = create_engine('sqlite://')
        self.commit_counter = 0
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()
        Base.metadata.create_all(self.engine, checkfirst=True)

    def resume_campaign(self, name):
        """Resumes campaign.

        Parameters
        ----------
        name: str
           Name of the Campaign to resume. Must already exist in the database.
        """
        info = self.session.query(
            CampaignTable).filter_by(name=name).first()
        if info is None:
            raise ValueError('Campaign with the given name not found.')
        db_info = self.session.query(DBInfoTable).first()
        self._next_run = db_info.next_run

    def create_campaign(self, info):
        """Creates a new campaign in the database.

        Parameters
        ----------
        info: CampaignInfo
            This `easyvvuq.data_structs.CampaignInfo` will contain information
            needed to construct the Campaign table.
        """
        is_db_empty = (self.session.query(CampaignTable).first() is None)
        version_check = self.session.query(
            CampaignTable).filter(CampaignTable.easyvvuq_version != info.easyvvuq_version).all()
        if (not is_db_empty) and (len(version_check) != 0):
            raise RuntimeError('Database contains campaign created with an incompatible' +
                               ' version of EasyVVUQ!')
        self._next_run = 1
        self.session.add(CampaignTable(**info.to_dict(flatten=True)))
        self.session.add(DBInfoTable(next_run=self._next_run))
        self.session.commit()

    def get_active_app(self):
        """Returns active app table.

        Returns
        -------
        AppTable
        """
        return self.session.query(AppTable, CampaignTable).filter(
            AppTable.id == CampaignTable.active_app).first()

    def campaign_exists(self, name):
        """Check if campaign specified by that name already exists.

        Parameters
        ----------
        name: str

        Returns
        -------
        bool
          True if such a campaign already exists, False otherwise
        """
        result = self.session.query(CampaignTable).filter(
            CampaignTable.name == name).all()
        return len(result) > 0

    def app(self, name=None):
        """Get app information. Specific applications selected by `name`,
        otherwise first entry in database 'app' selected.

        Parameters
        ----------
        name : str or None
            Name of selected app, if `None` given then first app will be
            selected.

        Returns
        -------
        dict
            Information about the application.
        """

        if name is None:
            selected = self.session.query(AppTable).all()
        else:
            selected = self.session.query(AppTable).filter_by(name=name).all()

        if len(selected) == 0:
            message = f'No entry for app: ({name}).'
            logger.critical(message)
            raise RuntimeError(message)

        selected_app = selected[0]

        app_dict = {
            'id': selected_app.id,
            'name': selected_app.name,
            'params': ParamsSpecification.deserialize(selected_app.params),
            'actions': selected_app.actions,
        }

        return app_dict

    def set_active_app(self, name):
        """Set an app specified by name as active.

        Parameters
        ----------
        name: str
           name of the app to set as active
        """
        selected = self.session.query(AppTable).filter_by(name=name).all()
        if len(selected) == 0:
            raise RuntimeError('no such app - {}'.format(name))
        assert (not (len(selected) > 1))
        app = selected[0]
        self.session.query(CampaignTable).update({'active_app': app.id})
        self.session.commit()

    def add_app(self, app_info):
        """Add application to the 'app' table.

        Parameters
        ----------
        app_info: AppInfo
            Application definition.
        """

        # Check that no app with same name exists
        name = app_info.name
        selected = self.session.query(AppTable).filter_by(name=name).all()
        if len(selected) > 0:
            message = (
                f'There is already an app in this database with name {name}'
                f'(found {len(selected)}).'
            )
            logger.critical(message)
            raise RuntimeError(message)

        app_dict = app_info.to_dict(flatten=True)

        db_entry = AppTable(**app_dict)
        self.session.add(db_entry)
        self.session.commit()

    def replace_actions(self, app_name, actions):
        """Replace actions for an app with a given name.

        Parameters
        ----------
        app_name: str
            Name of the app.
        actions: Actions
            `Actions` instance, will replace the current `Actions` of an app.
        """
        self.session.query(AppTable).filter_by(name=app_name).update(
            {'actions': easyvvuq_serialize(actions)})
        self.session.commit()

    def add_sampler(self, sampler_element):
        """Add new Sampler to the 'sampler' table.

        Parameters
        ----------
        sampler_element: Sampler
            An EasyVVUQ sampler.

        Returns
        -------
        int
            The sampler `id` in the database.
        """
        db_entry = SamplerTable(sampler=easyvvuq_serialize(sampler_element))

        self.session.add(db_entry)
        self.session.commit()

        return db_entry.id

    def update_sampler(self, sampler_id, sampler_element):
        """Update the state of the Sampler with id 'sampler_id' to
        that in the passed 'sampler_element'

        Parameters
        ----------
        sampler_id: int
            The id of the sampler in the db to update
        sampler_element: Sampler
            The sampler that should be used as the new state
        """

        selected = self.session.get(SamplerTable,sampler_id)
        selected.sampler = easyvvuq_serialize(sampler_element)
        self.session.commit()

    def resurrect_sampler(self, sampler_id):
        """Return the sampler object corresponding to id sampler_id in the database.
        It is deserialized from the state stored in the database.

        Parameters
        ----------
        sampler_id: int
            The id of the sampler to resurrect

        Returns
        -------
        Sampler
            The 'live' sampler object, deserialized from the state in the db
        """
        try:
            serialized_sampler = self.session.get(SamplerTable,sampler_id).sampler 
            sampler = easyvvuq_deserialize(serialized_sampler.encode('utf-8'))
        except AttributeError:
            sampler = None
        return sampler

    def resurrect_app(self, app_name):
        """Return the 'live' encoder, decoder and collation objects corresponding to the app with
        name 'app_name' in the database. They are deserialized from the states previously
        stored in the database.

        Parameters
        ----------
        app_name: string
            Name of the app to resurrect

        Returns
        -------
        Actions
            The 'live' `Actions` object associated with this app. Used to execute the simulation
            associated with the app as well as do any pre- and post-processing.
        """
        app_info = self.app(app_name)
        actions = easyvvuq_deserialize(app_info['actions'])
        return actions

    def add_runs(self, run_info_list=None, run_prefix='run_', iteration=0):
        """Add list of runs to the `runs` table in the database.

        Parameters
        ----------
        run_info_list: List of RunInfo objects
            Each RunInfo object contains relevant run fields: params, status (where in the
            EasyVVUQ workflow is this RunTable), campaign (id number), sample, app
        run_prefix: str
            Prefix for run name
        iteration: int
            Iteration number used by iterative workflows. For example, MCMC. Can be left
            as default zero in other cases.
        """
        # Add all runs to RunTable
        commit_counter = 0
        for run_info in run_info_list:
            run_info.run_name = f"{run_prefix}{self._next_run}"
            run_info.iteration = iteration
            run = RunTable(**run_info.to_dict(flatten=True))
            self.session.add(run)
            self._next_run += 1
            commit_counter += 1
            if commit_counter % COMMIT_RATE == 0:
                self.session.commit()
        # Update run and ensemble counters in db
        db_info = self.session.query(DBInfoTable).first()
        db_info.next_run = self._next_run
        self.session.commit()

    @staticmethod
    def _run_to_dict(run_row):
        """Convert the provided row from 'runs' table into a dictionary

        Parameters
        ----------
        run_row: RunTable
            Information on a particular run in the database.

        Returns
        -------
        dict
            Contains run information (keys = run_name, params, status, sample,
            campaign and app)
        """

        run_info = {
            'run_name': run_row.run_name,
            'params': json.loads(run_row.params),
            'status': constants.Status(run_row.status),
            'sampler': run_row.sampler,
            'campaign': run_row.campaign,
            'app': run_row.app,
            'result': run_row.result,
            'run_dir': run_row.run_dir
        }

        return run_info

    def set_dir_for_run(self, run_name, run_dir, campaign=None, sampler=None):
        """Set the 'run_dir' path for the specified run in the database.

        Parameters
        ----------
        run_name: str
            Name of run to filter for.
        run_dir: str
            Directory path associated to set for this run.
        campaign:  int or None
            Campaign id to filter for.
        sampler: int or None
            Sample id to filter for.
        """
        filter_options = {'run_name': run_name}
        if campaign:
            filter_options['campaign'] = campaign
        if sampler:
            filter_options['sampler'] = sampler
        selected = self.session.query(RunTable).filter_by(**filter_options)
        if selected.count() != 1:
            logging.critical('Multiple runs selected - using the first')
        selected = selected.first()
        selected.run_dir = run_dir
        self.session.commit()

    def get_run_status(self, run_id, campaign=None, sampler=None):
        """Return the status (enum) for the run with name 'run_name' (and, optionally,
        filtering for campaign and sampler by id)

        Parameters
        ----------
        run_id: int
            id of the run
        campaign: int
            ID of the desired Campaign
        sampler: int
            ID of the desired Sampler

        Returns
        -------
        enum(Status)
            Status of the run.
        """
        filter_options = {'id': run_id}
        if campaign:
            filter_options['campaign'] = campaign
        if sampler:
            filter_options['sampler'] = sampler
        selected = self.session.query(RunTable).filter_by(**filter_options)
        if selected.count() != 1:
            logging.critical('Multiple runs selected - using the first')
        selected = selected.first()
        return constants.Status(selected.status)

    def set_run_statuses(self, run_id_list, status):
        """Set the specified 'status' (enum) for all runs in the list run_id_list

        Parameters
        ----------
        run_id_list: list of int
            a list of run ids
        status: enum(Status)
            The new status all listed runs should now have
        """
        self.session.query(RunTable).filter(
            RunTable.id.in_(run_id_list)).update(
                {RunTable.status: status}, synchronize_session='fetch')
        self.session.commit()

    def campaigns(self):
        """Get list of campaigns for which information is stored in the
        database.

        Returns
        -------
        list
            Campaign names.
        """

        return [c.name for c in self.session.query(CampaignTable).all()]

    def _get_campaign_info(self, campaign_name=None):
        """Retrieves Campaign info based on name.

        Parameters
        ----------
        campaign_name: str
            Name of campaign to select.

        Returns
        -------
            SQLAlchemy query for campaign with this name.
        """
        assert (isinstance(campaign_name, str) or campaign_name is None)
        query = self.session.query(CampaignTable)
        if campaign_name is None:
            campaign_info = query
        else:
            campaign_info = query.filter_by(name=campaign_name).all()
        if campaign_name is not None:
            if len(campaign_info) > 1:
                logger.warning(
                    'More than one campaign selected - using first one.')
            elif len(campaign_info) == 0:
                message = 'No campaign available.'
                logger.critical(message)
                raise RuntimeError(message)
            return campaign_info[0]
        return campaign_info.first()

    def get_campaign_id(self, name):
        """Return the (database) id corresponding to the campaign with name 'name'.

        Parameters
        ----------
        name: str
            Name of the campaign.

        Returns
        -------
        int
            The id of the campaign with the specified name
        """

        selected = self.session.query(
            CampaignTable.name.label(name),
            CampaignTable.id).filter(CampaignTable.name == name).all()
        if len(selected) == 0:
            msg = f"No campaign with name {name} found in campaign database"
            logger.error(msg)
            raise RuntimeError(msg)
        if len(selected) > 1:
            msg = (
                f"More than one campaign with name {name} found in"
                f"campaign database. Database state is compromised."
            )
            logger.error(msg)
            raise RuntimeError(msg)
        # Return the database ID for the specified campaign
        return selected[0][1]

    def get_sampler_id(self, campaign_id):
        """Return the (database) id corresponding to the sampler currently set
        for the campaign with id 'campaign_id'

        Parameters
        ----------
        campaign_id: int
            ID of the campaign.

        Returns
        -------
        int
            The id of the sampler set for the specified campaign
        """
        sampler_id = self.session.get(CampaignTable,campaign_id).sampler
        return sampler_id

    def set_sampler(self, campaign_id, sampler_id):
        """Set specified campaign to be using specified sampler

        Parameters
        ----------
        campaign_id: int
            ID of the campaign.
        sampler_id: int
            ID of the sampler.
        """
        self.session.get(CampaignTable,campaign_id).sampler = sampler_id
        self.session.commit()

    def campaign_dir(self, campaign_name=None):
        """Get campaign directory for `campaign_name`.

        Parameters
        ----------
        campaign_name: str
            Name of campaign to select

        Returns
        -------
        str
            Path to campaign directory.
        """
        return self._get_campaign_info(campaign_name=campaign_name).campaign_dir

    def _select_runs(
            self,
            name=None,
            campaign=None,
            sampler=None,
            status=None,
            not_status=None,
            app_id=None):
        """Select all runs in the database which match the input criteria.

        Parameters
        ----------
        name: str
            Name of run to filter for.
        campaign:  int or None
            Campaign id to filter for.
        sampler: int or None
            Sampler id to filter for.
        status: enum(Status) or None
            Status string to filter for.
        not_status: enum(Status) or None
            Exclude runs with this status string
        app_id: int or None
            App id to filter for.

        Returns
        -------
        sqlalchemy.orm.query.Query
            Selected runs from the database run table.
        """
        filter_options = {}
        if name:
            filter_options['run_name'] = name
        if campaign:
            filter_options['campaign'] = campaign
        if sampler:
            filter_options['sampler'] = sampler
        if status:
            filter_options['status'] = status
        if app_id:
            filter_options['app'] = app_id

        # Note that for some databases this can be sped up with a yield_per(), but not all
        selected = self.session.query(RunTable).filter_by(
            **filter_options).filter(RunTable.status != not_status)

        return selected

    def run(self, name, campaign=None, sampler=None, status=None, not_status=None, app_id=None):
        """Get the information for a specified run.

        Parameters
        ----------
        name: str
            Name of run to filter for.
        campaign:  int or None
            Campaign id to filter for.
        sampler: int or None
            Sampler id to filter for.
        status: enum(Status) or None
            Status string to filter for.
        not_status: enum(Status) or None
            Exclude runs with this status string
        app_id: int or None
            App id to filter for.

        Returns
        -------
        dict
            Containing run information (run_name, params, status, sample,
            campaign, app)
        """
        selected = self._select_runs(
            name=name,
            campaign=campaign,
            sampler=sampler,
            status=status,
            not_status=not_status,
            app_id=app_id)
        if selected.count() != 1:
            logging.warning('Multiple runs selected - using the first')
        selected = selected.first()
        return self._run_to_dict(selected)

    def runs(self, campaign=None, sampler=None, status=None, not_status=None, app_id=None):
        """A generator to return all run information for selected `campaign` and `sampler`.

        Parameters
        ----------
        campaign: int or None
            Campaign id to filter for.
        sampler: int or None
            Sampler id to filter for.
        status: enum(Status) or None
            Status string to filter for.
        not_status: enum(Status) or None
            Exclude runs with this status string
        app_id: int or None
            App id to filter for.

        Yields
        ------
        dict
            Information on each selected run (key = run_name, value = dict of
            run information fields.), one at a time.
        """
        selected = self._select_runs(
            campaign=campaign,
            sampler=sampler,
            status=status,
            not_status=not_status,
            app_id=app_id)
        for r in selected:
            yield r.id, self._run_to_dict(r)

    def run_ids(self, campaign=None, sampler=None, status=None, not_status=None, app_id=None):
        """A generator to return all run IDs for selected `campaign` and `sampler`.

        Parameters
        ----------
        campaign: int or None
            Campaign id to filter for.
        sampler: int or None
            Sampler id to filter for.
        status: enum(Status) or None
            Status string to filter for.
        not_status: enum(Status) or None
            Exclude runs with this status string
        app_id: int or None
            App id to filter for.

        Yields
        ------
        str
            run ID for each selected run, one at a time.
        """
        selected = self._select_runs(
            campaign=campaign,
            sampler=sampler,
            status=status,
            not_status=not_status,
            app_id=app_id)
        for r in selected:
            yield r.run_name

    def get_num_runs(self, campaign=None, sampler=None, status=None, not_status=None):
        """Returns the number of runs matching the filtering criteria.

        Parameters
        ----------
        campaign: int or None
            Campaign id to filter for.
        sampler: int or None
            Sampler id to filter for.
        status: enum(Status) or None
            Status string to filter for.
        not_status: enum(Status) or None
            Exclude runs with this status string

        Returns
        -------
        int
            The number of runs in the database matching the filtering criteria

        """
        selected = self._select_runs(
            campaign=campaign,
            sampler=sampler,
            status=status,
            not_status=not_status)
        return selected.count()

    def runs_dir(self, campaign_name=None):
        """Get the directory used to store run information for `campaign_name`.

        Parameters
        ----------
        campaign_name: str
            Name of the selected campaign.

        Returns
        -------
        str
            Path containing run outputs.
        """
        return self._get_campaign_info(campaign_name=campaign_name).runs_dir

    def store_result(self, run_id, result, change_status=True):
        """Stores results of a simulation inside the RunTable given a run id.

        Parameters
        ----------
        run_id: int
            The id of a run to store the results in. This will be the run with which these
            results are associated with. Namely the run that has the inputs used to generate
            these results.
        result: dict
            Results in dictionary form. This is the same format as used by the `Decoder`.
        change_status: bool
            If set to False will not update the runs' status to COLLATED. This is sometimes
            useful in scenarios where you want several apps to work on the same runs.
        """
        self.commit_counter += 1

        def convert_nonserializable(obj):
            if isinstance(obj, np.int64):
                return int(obj)
            raise TypeError('Unknown type:', type(obj))
        result_ = result['result']
        result.pop('result')
        result.pop('run_info')
        if change_status:
            self.session.query(RunTable).\
                filter(RunTable.id == run_id).\
                update({'result': json.dumps(result_, default=convert_nonserializable),
                        'status': constants.Status.COLLATED,
                        'run_dir': result['rundir']})
        else:
            self.session.query(RunTable).\
                filter(RunTable.id == run_id).\
                update({'result': json.dumps(result_, default=convert_nonserializable),
                        'run_dir': result['rundir']})
        if self.commit_counter % COMMIT_RATE == 0:
            self.session.commit()

    def store_results(self, app_name, results):
        """Stores the results from a given run in the database.

        Parameters
        ----------
        run_name: str
            name of the run
        results: dict
            dictionary with the results (from the decoder)
        """
        try:
            app_id = self.session.query(AppTable).filter(AppTable.name == app_name).all()[0].id
        except IndexError:
            raise RuntimeError("app with the name {} not found".format(app_name))
        commit_counter = 0
        for run_id, result in results:
            try:
                self.session.query(RunTable).\
                    filter(RunTable.id == run_id, RunTable.app == app_id).\
                    update({'result': json.dumps(result), 'status': constants.Status.COLLATED})
                commit_counter += 1
                if commit_counter % COMMIT_RATE == 0:
                    self.session.commit()
            except IndexError:
                raise RuntimeError("no runs with name {} found".format(run_id))
        self.session.commit()

    def get_results(self, app_name, sampler_id, status=constants.Status.COLLATED, iteration=-1):
        """Returns the results as a pandas DataFrame.

        Parameters
        ----------
        app_name: str
            Name of the app to return data for.
        sampler_id: int
            ID of the sampler.
        status: STATUS
            Run status to filter for.
        iteration: int
            If a positive integer will return the results for a given iteration only.

        Returns
        -------
        DataFrame
            Will construct a `DataFrame` from the decoder output dictionaries.
        """
        try:
            app_id = self.session.query(AppTable).filter(AppTable.name == app_name).all()[0].id
        except IndexError:
            raise RuntimeError("app with the name {} not found".format(app_name))
        pd_result = {}
        query = self.session.query(RunTable).\
            filter(RunTable.app == app_id).\
            filter(RunTable.sampler == sampler_id).\
            filter(RunTable.status == status)
        # if only a specific iteration is requested filter it out
        if iteration >= 0:
            query = query.filter(RunTable.iteration == iteration)
        for row in query:
            params = {'run_id': row.id}
            params['iteration'] = row.iteration
            params = {**params, **json.loads(row.params)}
            result = json.loads(row.result)
            pd_dict = {**params, **result}
            for key in pd_dict.keys():
                if not isinstance(pd_dict[key], list):
                    try:
                        pd_result[(key, 0)].append(pd_dict[key])
                    except KeyError:
                        pd_result[(key, 0)] = [pd_dict[key]]
                else:
                    for i, elt in enumerate(pd_dict[key]):
                        try:
                            pd_result[(key, i)].append(pd_dict[key][i])
                        except KeyError:
                            pd_result[(key, i)] = [pd_dict[key][i]]
        try:
            return pd.DataFrame(pd_result)
        except ValueError:
            raise RuntimeError(
                'the results received from the database seem to be malformed - commonly because a vector quantity of interest changes dimensionality')

    def relocate(self, new_path, campaign_name):
        """Update all runs in the db with the new campaign path.

        Parameters
        ----------
        new_path: str
            new runs directory
        campaign_name: str
            name of the campaign
        """
        campaign_id = self.get_campaign_id(campaign_name)
        campaign_info = self.session.query(CampaignTable).\
            filter(CampaignTable.id == campaign_id).first()
        path, runs_dir = os.path.split(campaign_info.runs_dir)
        self.session.query(CampaignTable).\
            filter(CampaignTable.id == campaign_id).\
            update({'campaign_dir': str(new_path),
                    'runs_dir': str(os.path.join(new_path, runs_dir))})
        self.session.commit()

    def dump(self):
        """Dump the database as JSON for debugging purposes.

        Returns
        -------
        dict
            A database dump in JSON format.
        """
        meta = MetaData()
        meta.reflect(bind=self.engine)
        result = {}

        # Create a connection from the engine
        with self.engine.connect() as connection:
            for table in meta.sorted_tables:
                try:
                    query_result = connection.execute(table.select()).fetchall()
                    result[table.name] = [dict(row) for row in query_result]
                except Exception as e:
                    result[table.name] = str(e)

        return json.dumps(result)
    
