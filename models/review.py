#!/usr/bin/python3
"""Module that creates the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Float, Column, ForeignKey, Integer, String


class Review(BaseModel, Base):
    """Review class that inherits from BaseModel
    Attributes:
        user_id: an instance of the user id
        text: an object that reviews description of other instances
        place_id: an instance of the place id
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
