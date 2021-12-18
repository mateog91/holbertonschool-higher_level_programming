#!/usr/bin/python3
"""contains the class definition of a City
    and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from relationship_state import Base


class City(Base):
    """ Class for City inherited from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
