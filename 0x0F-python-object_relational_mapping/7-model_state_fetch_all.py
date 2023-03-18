#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and sort by id
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print('{}: {}'.format(state.id, state.name))
