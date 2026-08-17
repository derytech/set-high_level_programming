#!/usr/bin/python3
"""Delete State objects whose names contain the letter a."""

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

    session.query(State).filter(State.name.contains("a")).delete(
        synchronize_session=False
    )
    session.commit()

    session.close()
