#!/usr/bin/python3
"""Define the State class for the SQLAlchemy relationship."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class State(Base):
    """Represent a state stored in the states table."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )
