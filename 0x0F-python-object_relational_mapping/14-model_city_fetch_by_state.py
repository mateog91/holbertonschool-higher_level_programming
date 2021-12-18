#!/usr/bin/python3
"""lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s, c in session.query(State, City).\
            filter(State.id == City.state_id).\
            order_by(City.id).\
            all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))

    session.close()
