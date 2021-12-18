#!/usr/bin/python3
"""lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""
from sys import argv


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    louisiana_state = State(name='Louisiana')
    session.add(louisiana_state)
    session.commit()
    print(louisiana_state.id)
    session.close()
