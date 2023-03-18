#!/usr/bin/python3
"""python file that contains the class definition of a State and
an instance Base = declarative_base():"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


class State(Base):
    """defines state class that inherited from Base, and properties of
    state class"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
