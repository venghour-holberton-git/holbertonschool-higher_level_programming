#!/usr/bin/python3

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)