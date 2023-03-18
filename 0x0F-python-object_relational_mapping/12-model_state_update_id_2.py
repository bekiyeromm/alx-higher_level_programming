#!/usr/bin/python3
"""script that changes the name of a State
object from the database hbtn_0e_6_usa"""


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

    # query and update the name of state with state id = 2
    states = session.query(State).filter(State.id == 2).first()
    if states:
        states.name = "New Mexico"
        session.commit()
