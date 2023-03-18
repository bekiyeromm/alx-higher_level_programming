#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create connection to the database
    st = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database for state with matching state name
    states = session.query(State).filter_by(name=st).first()

    # Print results
    if not states:
        print("Not found")
    else:
        print(states.id)
