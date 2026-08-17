#!/usr/bin/python3
"""Add Louisiana as a State object to a MySQL database."""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    session = Session(engine)

    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print(state.id)

    session.close()
