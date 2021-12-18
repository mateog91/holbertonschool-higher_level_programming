#!/usr/bin/python3
"""contains the class definition of a State
    and an instance Base = declarative_base():
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String
    from sqlalchemy import ForeignKey

    Base = declarative_base()

    class City(Base):
        __tablename__ = 'cities'

        id = Column(Integer, autoincrement=True,
                    nullable=False, primary_key=True)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('states.id'))
