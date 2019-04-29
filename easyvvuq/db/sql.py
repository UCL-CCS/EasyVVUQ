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


class CampaignInfo(Base):
    """An SQLAlchemy schema for the campaign information table.
    """
    __tablename__ = 'campaign_info'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    easyvvuq_version = Column(String)
    campaign_dir_prefix = Column(String)
    campaign_dir = Column(String)
    runs_dir = Column(String)


class App(Base):
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
    variable = Column(String)


class Run(Base):
    """An SQLAlchemy schema for the run table.
    """
    __tablename__ = 'run'
    id = Column(Integer, primary_key=True)
    run_name = Column(String)
    app = Column(Integer, ForeignKey('app.id'))
    # Parameter values for this run
    config = Column(String)
    # TODO: Consider making status an ENUM to enforce relevant EasyVVUQ values
    status = Column(String)
    campaign = Column(Integer, ForeignKey('campaign_info.id'))
    sample = Column(Integer, ForeignKey('sample.id'))


class Sample(Base):
    """An SQLAlchemy schema for the run table.
    """
    __tablename__ = 'sample'
    id = Column(Integer, primary_key=True)
    sampler = Column(String)


class CampaignDB(BaseCampaignDB):

    def __init__(self, src=None, new_campaign=False, name='default',
                 info={}):

        if src is not None:
            self.engine = create_engine(src)
        else:
            self.engine = create_engine('sqlite://')

        session_maker = sessionmaker(bind=self.engine)

        self.session = session_maker()

        if src is not None and not new_campaign:

            self.info = self.session.query(CampaignInfo).filter_by(name=name).first()
            if self.info is None:
                raise ValueError('Campaign with the given name not found.')

        else:
            Base.metadata.create_all(self.engine)

            self.info = CampaignInfo(
                name=name,
                easyvvuq_version=constants.version,
                campaign_dir_prefix=info['campaign_dir_prefix'],
                campaign_dir=info['campaign_dir'],
                runs_dir=info['runs_dir'],
            )

            self.session.add(self.info)
            self.session.commit()

    def app(self, name=None):
        """
        Get app information. Specific applications selected by `name`, otherwise
        first entry in database 'app' selected.

        Parameters
        ----------
        name : str or None
            Name of selected app, if `None` given then first app will be selected.

        Returns
        -------
        dict:
            Application information.
        """

        if name:
            selected = self.session.query(App).filter_by(name=name).first()
        else:
            selected = self.session.query(App).first()

        if not selected:
            message = f'No entry for app: ({name}).'
            logger.critical(message)
            raise RuntimeError(message)

        app_dict = {
                    'name': selected.name,
                    'input_encoder': selected.input_encoder,
                    'encoder_options': json.loads(selected.encoder_options),
                    'output_decoder': selected.output_decoder,
                    'decoder_options': json.loads(selected.decoder_options),
                    'execution': json.loads(selected.execution),
                    'params': json.loads(selected.params),
                    'fixtures': json.loads(selected.fixtures),
                    'collation': json.loads(selected.collation),
                    'variable': json.loads(selected.variable),
        }

        return app_dict

    def add_app(self, app):
        """
        Add passed `app`lication information to the 'app' table in the database.

        Parameters
        ----------
        app : `easyvvuq.data_structs.AppInfo`
            Validated app information.

        Returns
        -------

        """

        # TODO: Check that no app with same name exists

        db_entry = App(
                  name=app.name,
                  input_encoder=app.input_encoder,
                  encoder_options=json.dumps(app.encoder_options),
                  output_decoder=app.output_decoder,
                  decoder_options=json.dumps(app.decoder_options),
                  execution=json.dumps(app.execution),
                  params=json.dumps(app.params),
                  fixtures=json.dumps(app.fixtures),
                  collation=json.dumps(app.collation),
                  variable=json.dumps(app.variable),
                 )

        self.session.add(db_entry)
        self.session.commit()

    def add_sampler(self, sampler={}):
        """
        Add passed application information to the `app` table in the database.

        Parameters
        ----------
        sampler  :  dict
            Information on the sampler that was used

        Returns
        -------

        """

        sampler = Sample(sampler=json.dumps(sampler))

        self.session.add(sampler)
        self.session.commit()

    def add_run(self, run_info={}):
        """
        Add run to the `runs` table in the database.

        Parameters
        ----------
        run_info  :  dict
            Information on the run to be added

        Returns
        -------

        """

        pass
