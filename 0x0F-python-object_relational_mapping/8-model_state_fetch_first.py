#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa
"""
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

    instance = session.query(State.id, State.name).order_by(State.id).first()
    if instance:
        print(f"{instance[0]}: {instance[1]}")
    else:
        print("Nothing")
    session.commit()
    session.close()
