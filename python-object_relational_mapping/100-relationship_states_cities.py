#!/usr/bin/python3
"""Create a California state and its San Francisco city."""

from relationship_state import Base, State
from relationship_city import City
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

    Base.metadata.create_all(engine)

    session = Session(engine)

    state = State(name="California")
    city = City(name="San Francisco")

    state.cities.append(city)

    session.add(state)
    session.commit()

    session.close()
