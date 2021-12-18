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

    state_search = argv[4]

    flag = False
    for instance in session.query(State).order_by(State.id):
        if state_search == instance.name:
            print(f"{instance.id}")
            flag = True
            break
    if not flag:
        print("Not found")

    session.commit()
    session.close()
