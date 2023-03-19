#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':

    # Create SQLAlchemy engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities and states from the database
    cities = session.query(City, State).filter(City.state_id == State.id)\
                    .order_by(City.id).all()

    # Print results grouped by state
    for city, state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')
