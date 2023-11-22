#!/usr/bin/python3
"""Module that defines the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """User class that inherits from BaseModel, Base
    Attributes:
        password: instance of the password
        last_name: instance of last name
        first_name: instance of the first name
        email: instance of the email address
    """
    __tablename__ = "users"
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    """places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")"""
