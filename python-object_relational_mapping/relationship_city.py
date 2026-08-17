#!/usr/bin/python3
"""Define the City class for the SQLAlchemy relationship."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """Represent a city stored in the cities table."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id", ondelete="CASCADE"),
        nullable=False
    )

    state = relationship("State", back_populates="cities")
