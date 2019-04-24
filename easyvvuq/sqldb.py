import os
import json
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import constants


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


class CampaignDB:

    def __init__(self, db_uri=None, new_campaign=False, name='default',
                 info={}):

        if db_uri is not None:
            self.engine = create_engine(db_uri)
        else:
            self.engine = create_engine('sqlite://')

        session_maker = sessionmaker(bind=self.engine)

        self.session = session_maker()

        if db_uri is not None and not new_campaign:

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

    def add_app(self, app_info):
        """
        Add passed application information to the `app` table in the database.

        Parameters
        ----------
        app_info :  dict
            

        Returns
        -------

        """

        app = App(**app_info)
        self.session.add(app)
        self.session.commit()
