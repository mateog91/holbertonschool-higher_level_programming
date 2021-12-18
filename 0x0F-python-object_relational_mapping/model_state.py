#!/usr/bin/python3
"""contains the class definition of a State
    and an instance Base = declarative_base():
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String

    Base = declarative_base()

    class State(Base):
        """ Class for State inherited from Base
        """
        __tablename__ = 'states'

        id = Column(Integer, autoincrement=True,
                    nullable=False, primary_key=True)
        name = Column(String(128), nullable=False)
