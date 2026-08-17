#!/usr/bin/python3
"""Define the City class and its database mapping."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Represent a city stored in the cities database table."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State")
