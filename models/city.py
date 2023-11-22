#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class City(BaseModel, Base):
    """Class for City that inherits from BaseModel and Base
    Attributes:
        state_id: The state id
        name: instance for name input
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="delete",
                          backref="cities")
