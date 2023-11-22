#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Amenity(BaseModel, Base):
    """Amenity class that inherits from BaseModel and Base
    Attributes:
        name: an instance of the name to be created
    """
    __tablename__ = "amenities"
    place_amenities = relationship("Place", secondary=place_amenity)
    name = Column(String(128), nullable=False)
