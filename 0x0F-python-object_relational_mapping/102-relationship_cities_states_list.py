#!/usr/bin/python3
"""lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from relationship_city import City
    from relationship_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # cities as an attribute of state object
    query = session.query(State).join(City).order_by(
        State.id, City.id).filter(State.id == City.state_id).all()
    for s in query:
        # print(f"{s.id}: {s.name}")
        for each_c in s.cities:
            print(f"{each_c.id}: {each_c.name} -> {s.name}")

    session.close()
