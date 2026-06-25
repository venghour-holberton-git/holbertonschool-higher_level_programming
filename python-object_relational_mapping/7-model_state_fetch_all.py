#!/usr/bin/python3
"""Module containing State class definition and Base instance"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import sys

Base = declarative_base()


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
with Session(engine) as session:
    class State(Base):
        """State class linked to states table"""

        __tablename__ = "states"

        id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
        name = Column(String(128), nullable=False)