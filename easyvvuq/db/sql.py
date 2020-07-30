"""Provides class that allows access to an SQL format CampaignDB.
"""
import os
import json
import logging
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text
from .base import BaseCampaignDB
from easyvvuq import constants
from easyvvuq.sampling.base import BaseSamplingElement
from easyvvuq.encoders.base import BaseEncoder
from easyvvuq.decoders.base import BaseDecoder
from easyvvuq.collate.base import BaseCollationElement
from easyvvuq import ParamsSpecification
from easyvvuq.utils.helpers import multi_index_tuple_parser

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

logger = logging.getLogger(__name__)

Base = declarative_base()


class DBInfoTable(Base):
    """An SQLAlchemy schema for the database information table.
    """
    __tablename__ = 'db_info'
    id = Column(Integer, primary_key=True)
    next_run = Column(Integer)
    next_ensemble = Column(Integer)


class CampaignTable(Base):
    """An SQLAlchemy schema for the campaign information table.
    """
    __tablename__ = 'campaign_info'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    easyvvuq_version = Column(String)
    campaign_dir_prefix = Column(String)
    campaign_dir = Column(String)
    runs_dir = Column(String)
    sampler = Column(Integer, ForeignKey('sampler.id'))


class AppTable(Base):
    """An SQLAlchemy schema for the app table.
    """
    __tablename__ = 'app'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    input_encoder = Column(String)
    output_decoder = Column(String)
    collater = Column(String)
    params = Column(String)


class RunTable(Base):
    """An SQLAlchemy schema for the run table.
    """
    __tablename__ = 'run'
    id = Column(Integer, primary_key=True)
    run_name = Column(String)
    ensemble_name = Column(String)
    app = Column(Integer, ForeignKey('app.id'))
    params = Column(String)
    status = Column(Integer)
    run_dir = Column(String)
    campaign = Column(Integer, ForeignKey('campaign_info.id'))
    sampler = Column(Integer, ForeignKey('sampler.id'))


class SamplerTable(Base):
    """An SQLAlchemy schema for the run table.
    """
    __tablename__ = 'sampler'
    id = Column(Integer, primary_key=True)
    sampler = Column(String)


class CampaignDB(BaseCampaignDB):

    def __init__(self, location=None, new_campaign=False, name=None, info=None):

        if location is not None:
            self.engine = create_engine(location)
        else:
            self.engine = create_engine('sqlite://')

        session_maker = sessionmaker(bind=self.engine)

        self.session = session_maker()

        if new_campaign:
            if info is None:
                raise RuntimeError('No information provided to create'
                                   'database')
            if info.name != name:
                message = (f'Information for campaign {info.name} given '
                           f'for campaign database {name}')
                logging.critical(message)
                raise RuntimeError(message)

            Base.metadata.create_all(self.engine)

            is_db_empty = (self.session.query(CampaignTable).first() is None)

            version_check = self.session.query(
                CampaignTable).filter(CampaignTable.easyvvuq_version != info.easyvvuq_version).all()

            if (not is_db_empty) and (len(version_check) != 0):
                raise RuntimeError('Database contains campaign created with an incompatible' +
                                   ' version of EasyVVUQ!')

            self._next_run = 1
            self._next_ensemble = 1

            self.session.add(CampaignTable(**info.to_dict(flatten=True)))
            self.session.add(
                DBInfoTable(
                    next_run=self._next_run,
                    next_ensemble=self._next_ensemble))
            self.session.commit()
        else:
            info = self.session.query(
                CampaignTable).filter_by(name=name).first()
            if info is None:
                raise ValueError('Campaign with the given name not found.')

            db_info = self.session.query(DBInfoTable).first()
            self._next_run = db_info.next_run
            self._next_ensemble = db_info.next_ensemble

    def app(self, name=None):
        """
        Get app information. Specific applications selected by `name`,
        otherwise first entry in database 'app' selected.

        Parameters
        ----------
        name : str or None
            Name of selected app, if `None` given then first app will be
            selected.

        Returns
        -------
        dict:
            Application information.
        """

        if name is None:
            logging.warning('No app name provided so using first app '
                            'in database')
            selected = self.session.query(AppTable).all()
        else:
            selected = self.session.query(AppTable).filter_by(name=name).all()

        if len(selected) == 0:
            message = f'No entry for app: ({name}).'
            logger.critical(message)
            raise RuntimeError(message)
        if len(selected) > 1:
            message = f'Too many apps called: ({name}).'
            logger.critical(message)
            raise RuntimeError(message)

        selected_app = selected[0]

        app_dict = {
            'id': selected_app.id,
            'name': selected_app.name,
            'input_encoder': selected_app.input_encoder,
            'output_decoder': selected_app.output_decoder,
            'collater': selected_app.collater,
            'params': ParamsSpecification.deserialize(selected_app.params)
        }

        return app_dict

    def add_app(self, app_info):
        """
        Add application to the 'app' table.

        Parameters
        ----------
        app_info: AppInfo
            Application definition.

        Returns
        -------

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

    def add_sampler(self, sampler_element):
        """
        Add new Sampler to the 'sampler' table.

        Parameters
        ----------
        sampler_element: BaseSamplingElement

        Returns
        -------

        """
        db_entry = SamplerTable(sampler=sampler_element.serialize())

        self.session.add(db_entry)
        self.session.commit()

        return db_entry.id

    def update_sampler(self, sampler_id, sampler_element):
        """
        Update the state of the Sampler with id 'sampler_id' to
        that in the passed 'sampler_element'

        Parameters
        ----------
        sampler_id: int
            The id of the sampler in the db to update
        sampler_element: BaseSamplingElement
            The sampler whose state should be used as the new state

        Returns
        -------

        """

        selected = self.session.query(SamplerTable).get(sampler_id)
        selected.sampler = sampler_element.serialize()
        self.session.commit()

    def resurrect_sampler(self, sampler_id):
        """
        Return the sampler object corresponding to id sampler_id in the database.
        It is deserialized from the state stored in the database.

        Parameters
        ----------
        sampler_id: int
            The id of the sampler to resurrect

        Returns
        -------
        BaseSamplingElement
            The 'live' sampler object, deserialized from the state in the db

        """

        serialized_sampler = self.session.query(SamplerTable).get(sampler_id).sampler
        sampler = BaseSamplingElement.deserialize(serialized_sampler)
        return sampler

    def resurrect_app(self, app_name):
        """
        Return the 'live' encoder, decoder and collation objects corresponding to the app with
        name 'app_name' in the database. They are deserialized from the states previously
        stored in the database.

        Parameters
        ----------
        app_name: string
            Name of the app to resurrect

        Returns
        -------
        BaseEncoder, BaseDecoder, BaseCollationElement
            The 'live' encoder and decoder objects associated with this app

        """

        app_info = self.app(app_name)

        encoder = BaseEncoder.deserialize(app_info['input_encoder'])
        decoder = BaseDecoder.deserialize(app_info['output_decoder'])
        collater = BaseCollationElement.deserialize(app_info['collater'])
        return encoder, decoder, collater

    def add_runs(self, run_info_list=None, run_prefix='Run_', ensemble_prefix='Ensemble_'):
        """
        Add list of runs to the `runs` table in the database.

        Parameters
        ----------
        run_info_list: List of RunInfo objects
            Each RunInfo object contains relevant run fields: params, status (where in the
            EasyVVUQ workflow is this RunTable), campaign (id number), sample, app
        run_prefix: str
            Prefix for run id
        ensemble_prefix: str
            Prefix for ensemble id

        Returns
        -------

        """

        # Add all runs to RunTable
        runs_dir = self.runs_dir()
        for run_info in run_info_list:
            run_info.ensemble_name = f"{ensemble_prefix}{self._next_ensemble}"
            run_info.run_name = f"{run_prefix}{self._next_run}"
            run_info.run_dir = os.path.join(runs_dir, run_info.run_name)

            run = RunTable(**run_info.to_dict(flatten=True))
            self.session.add(run)
            self._next_run += 1
        self._next_ensemble += 1

        # Update run and ensemble counters in db
        db_info = self.session.query(DBInfoTable).first()
        db_info.next_run = self._next_run
        db_info.next_ensemble = self._next_ensemble

        self.session.commit()

    @staticmethod
    def _run_to_dict(run_row):
        """
        Convert the provided row from 'runs' table into a dictionary

        Parameters
        ----------
        run_row: RunTable
            Information on a particular run in the database.

        Returns
        -------
        dict:
            Contains run information (keys = run_name, params, status, sample,
            campaign and app)

        """

        run_info = {
            'run_name': run_row.run_name,
            'ensemble_name': run_row.ensemble_name,
            'params': json.loads(run_row.params),
            'status': constants.Status(run_row.status),
            'sampler': run_row.sampler,
            'campaign': run_row.campaign,
            'app': run_row.app,
            'run_dir': run_row.run_dir
        }

        return run_info

    def set_dir_for_run(self, run_name, run_dir, campaign=None, sampler=None):
        """
        Set the 'run_dir' path for the specified run in the database.

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

        Returns
        -------

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

    def get_run_status(self, run_name, campaign=None, sampler=None):
        """
        Return the status (enum) for the run with name 'run_name' (and, optionally,
        filtering for campaign and sampler by id)

        Parameters
        ----------
        run_name: str
            Name of the run
        campaign: int
            ID of the desired Campaign
        sampler: int
            ID of the desired Sampler

        Returns
        -------
        status: enum(Status)
            Status of the run.
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

        return constants.Status(selected.status)

    def set_run_statuses(self, run_name_list, status):
        """
        Set the specified 'status' (enum) for all runs in the list run_ID_list

        Parameters
        ----------
        run_name_list: list of str
            A list of run names run names (format is usually: prefix + int)
        status: enum(Status)
            The new status all listed runs should now have

        Returns
        -------

        """
        max_entries = 900

        for i in range(0, len(run_name_list), max_entries):
            selected = self.session.query(RunTable).filter(
                RunTable.run_name.in_(set(run_name_list[i:i + max_entries]))).all()

            for run in selected:
                run.status = status
            self.session.commit()

    def campaigns(self):
        """Get list of campaigns for which information is stored in the
        database.

        Returns
        -------
        list:
            Campaign names.
        """

        return [c.name for c in self.session.query(CampaignTable).all()]

    def _get_campaign_info(self, campaign_name=None):
        """
        Parameters
        ----------
        campaign_name: str
            Name of campaign to select

        Returns
        -------
            sqlalchemy query for campaign with this name

        """

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
        """
        Return the (database) id corresponding to the campaign with name 'name'.

        Parameters
        ----------
        name: str
            Name of the campaign.

        Returns
        -------
        int:
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
        """
        Return the (database) id corresponding to the sampler currently set
        for the campaign with id 'campaign_id'

        Parameters
        ----------
        campaign_id: int
            ID of the campaign.

        Returns
        -------
        int:
            The id of the sampler set for the specified campaign
        """

        sampler_id = self.session.query(CampaignTable).get(campaign_id).sampler
        return sampler_id

    def set_sampler(self, campaign_id, sampler_id):
        """
        Set specified campaign to be using specified sampler

        Parameters
        ----------
        campaign_id: int
            ID of the campaign.
        sampler_id: int
            ID of the sampler.

        Returns
        -------
        """

        self.session.query(CampaignTable).get(campaign_id).sampler = sampler_id
        self.session.commit()

    def campaign_dir(self, campaign_name=None):
        """Get campaign directory for `campaign_name`.

        Parameters
        ----------
        campaign_name: str
            Name of campaign to select

        Returns
        -------
        str:
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
        """
        Select all runs in the database which match the input criteria.

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
        """
        Get the information for a specified run.

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
        """
        A generator to return all run information for selected `campaign` and `sampler`.

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
        dict:
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
            yield r.run_name, self._run_to_dict(r)

    def run_ids(self, campaign=None, sampler=None, status=None, not_status=None, app_id=None):
        """
        A generator to return all run IDs for selected `campaign` and `sampler`.

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
        str:
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
        """
        Returns the number of runs matching the filtering criteria.

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
        int:
            The number of runs in the database matching the filtering criteria

        """

        selected = self._select_runs(
            campaign=campaign,
            sampler=sampler,
            status=status,
            not_status=not_status)

        return selected.count()

    def runs_dir(self, campaign_name=None):
        """
        Get the directory used to store run information for `campaign_name`.

        Parameters
        ----------
        campaign_name: str
            Name of the selected campaign.

        Returns
        -------
        str:
            Path containing run outputs.
        """

        return self._get_campaign_info(campaign_name=campaign_name).runs_dir

    def append_collation_dataframe(self, df, app_id):
        """
        Append the data in dataframe 'df' to that already collated in the database
        for the specified app.

        Parameters
        ----------
        df: pandas dataframe
            The dataframe whose contents need to be appended to the collation store
        app_id: int
            The id of the app in the sql database. Used to determine which collation
            table is appended to.

        Returns
        -------
        """

        if df.size == 0:
            logging.warning(
                f"Attempt to append empty dataframe to SQL collation table for app_id {app_id}.")
            return

        tablename = 'COLLATION_APP' + str(app_id)
        df.to_sql(tablename, self.engine, if_exists='append')

    def get_collation_dataframe(self, app_id):
        """
        Returns a dataframe containing the full collated results stored in this database
        for the specified app.
        i.e. the total of what was added with the append_collation_dataframe() method.

        Parameters
        ----------
        app_id: int
            The id of the app in the sql database. Used to determine which collation
            table is appended to.

        Returns
        -------
        df: pandas dataframe
            The dataframe with all contents that were appended to this database
        """

        tablename = 'COLLATION_APP' + str(app_id)
        if tablename in self.engine.table_names():
            query = "select * from " + tablename
            df = pd.read_sql_query(query, self.engine.execution_options(sqlite_raw_colnames=True))
            columns, multi = multi_index_tuple_parser(df.columns.values[1:])
            if multi:
                df = pd.DataFrame(df.values[:, 1:],
                                  columns=pd.MultiIndex.from_tuples(columns))
            return df
        else:
            return None

    def clear_collation(self, app_id):
        tablename = 'COLLATION_APP' + str(app_id)

        if tablename in self.engine.table_names():
            sqlcmd = text(f'DROP TABLE {tablename};')
            self.engine.execute(sqlcmd)
