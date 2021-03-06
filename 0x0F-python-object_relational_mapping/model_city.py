#!/usr/bin/python3
"""contains the class definition of a City
    and an instance Base = declarative_base():
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
Base = declarative_base()


class City(Base):
    """ Class for City inherited from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
