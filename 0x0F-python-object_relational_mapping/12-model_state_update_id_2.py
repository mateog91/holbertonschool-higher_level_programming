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

    state_to_change = session.query(State).filter_by(id=2).first()
    state_to_change.name = "New Mexico"
    print(state_to_change.name)

    session.commit()
    session.close()
