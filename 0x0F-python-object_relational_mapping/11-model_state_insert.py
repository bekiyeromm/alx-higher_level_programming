#!/usr/bin/python3
"""that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
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

    states = State(name='Louisiana')
    session.add(states)
    session.commit()

    # Print results
    print(states.id)
