#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Amenity(BaseModel, Base):
    """
    Class Amenity
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
