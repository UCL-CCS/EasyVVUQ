import json
import logging
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from easyvvuq import constants
from .base import BaseCampaignDB


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


class AppTable(Base):
    """An SQLAlchemy schema for the app table.
    """
    __tablename__ = 'app'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    input_encoder = Column(String)
    encoder_options = Column(String)
    output_decoder = Column(String)
    decoder_options = Column(String)
    execution = Column(String)
    params = Column(String)
    fixtures = Column(String)
    collation = Column(String)


class RunTable(Base):
    """An SQLAlchemy schema for the run table.
    """
    __tablename__ = 'run'
    id = Column(Integer, primary_key=True)
    run_name = Column(String)
    app = Column(Integer, ForeignKey('app.id'))
    # Parameter values for this run
    params = Column(String)
    # TODO: Consider making status an ENUM to enforce relevant EasyVVUQ values
    status = Column(String)
    campaign = Column(Integer, ForeignKey('campaign_info.id'))
    sample = Column(Integer, ForeignKey('sample.id'))


class SampleTable(Base):
    """An SQLAlchemy schema for the run table.
    """
    __tablename__ = 'sample'
    id = Column(Integer, primary_key=True)
    sampler = Column(String)


class CampaignDB(BaseCampaignDB):

    def __init__(self, location=None, new_campaign=False, name=None,
                 info=None):

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

            self.session.add(CampaignTable(**info.dict_for_db()))
            self.session.commit()
            self._next_run = 1
        else:
            info = self.session.query(
                CampaignTable).filter_by(name=name).first()
            if info is None:
                raise ValueError('Campaign with the given name not found.')

            self._next_run = self.session.query(RunTable).count() + 1

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

        # TODO: Find efficient way for this
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
            'encoder_options': json.loads(selected_app.encoder_options),
            'output_decoder': selected_app.output_decoder,
            'decoder_options': json.loads(selected_app.decoder_options),
            'execution': json.loads(selected_app.execution),
            'params': json.loads(selected_app.params),
            'fixtures': json.loads(selected_app.fixtures),
            'collation': json.loads(selected_app.collation)
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

        # TODO: Check that no app with same name exists

        app_dict = app_info.dict_for_db()

        db_entry = AppTable(**app_dict)

        self.session.add(db_entry)
        self.session.commit()

    def add_sampler(self, sampler={}):
        """
        Add passed sampler information to the `sample` table in the database.

        Parameters
        ----------
        sampler  :  dict
            Information on the sampler that was used

        Returns
        -------

        """

        sampler = SampleTable(sampler=json.dumps(sampler))

        self.session.add(sampler)
        self.session.commit()

    def add_run(self, run_info=None, prefix='Run_'):
        """
        Add run to the `runs` table in the database.

        Parameters
        ----------
        run_info: RunInfo
            Contains relevant run fields: params, status (where in the
            EasyVVUQ workflow is this RunTable), campaign (id number),
            sample, app
        prefix: str
            Prefix for run id

        Returns
        -------

        """


        run_info.run_name = f"{prefix}{self._next_run}"

        run = RunTable(**run_info.dict_for_db())
        self.session.add(run)
        self.session.commit()
        self._next_run += 1

    @staticmethod
    def _run_to_dict(run_row):

        run_info = {
            'run_name': run_row.run_name,
            'params': json.loads(run_row.params),
            'status': run_row.status,
            'sample': run_row.sample,
            'campaign': run_row.campaign,
            'app': run_row.app,
        }

        return run_info

    def run(self, run_name, campaign=None, sampler=None):
        """
        Get the information for a specified run.

        Parameters
        ----------
        run_name: str
            Name of run to filter for.
        campaign:  int or None
            Campaign id to filter for.
        sampler: int or None
            Sample id to filter for.

        Returns
        -------
        dict
            Containing run information (run_name, params, status, sample,
            campaign, app)
        """

        if campaign is None and sampler is None:
            selected = self.session.query(RunTable).filter_by(run_name=run_name)
        elif campaign is not None and sampler is not None:
            selected = self.session.query(RunTable).filter_by(run_name=run_name,
                                                              campaign=campaign,
                                                              sample=sampler)
        elif campaign is not None:
            selected = self.session.query(RunTable).filter_by(run_name=run_name,
                                                              campaign=campaign)
        else:
            selected = self.session.query(RunTable).filter_by(run_name=run_name,
                                                              sample=sampler)

        if selected.count() != 1:
            logging.warning('Multiple runs selected - using the last')

        selected = selected.last()

        return self._run_to_dict(selected)

    def campaigns(self):

        return [c.name for c in self.session.query(CampaignTable).all()]

    def _get_campaign_info(self, campaign_name=None):

        query = self.session.query(CampaignTable)

        if campaign_name is None:
            campaign_info = query
        else:
            campaign_info = query.filter_by(name=campaign_name).all()

        if campaign_info.count() > 1:
            logger.warning('More than one campaign selected - using first one.')
        elif campaign_info.count() == 0:
            message = 'No campaign available.'
            logger.critical(message)
            raise RuntimeError(message)

        return campaign_info.first()

    def campaign_dir(self, campaign_name=None):

        self._get_campaign_info(campaign_name=campaign_name).campaign_dir

    def runs(self, campaign=None, sampler=None):

        # TODO: This is a bad idea - find a better generator solution

        if campaign is None and sampler is None:
            selected = self.session.query(RunTable).all()
        elif campaign is not None and sampler is not None:
            selected = self.session.query(RunTable).filter_by(campaign=campaign,
                                                              sample=sampler).all()
        elif campaign is not None:
            selected = self.session.query(RunTable)
            selected = selected.filter_by(campaign=campaign).all()
        else:
            selected = self.session.query(RunTable).filter_by(sample=sampler).all()

        return {r.run_name: self._run_to_dict(r) for r in selected}

    def runs_dir(self, campaign_name=None):
        return self._get_campaign_info(campaign_name=campaign_name).runs_dir
