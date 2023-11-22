#!/usr/bin/python3
""" State Module for HBNB project"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import shlex

Base = declarative_base()


class State(BaseModel, Base):
    """This class represents the State"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Retrieve a list of associated City instances"""
        values = models.storage.all()
        groups = []
        result = []
        try:
            for elements in values:
                city_info = elements.replace('.', ' ')
                city_info = shlex.split(city_info)
                if city_info[0] == 'City':
                    groups.append(values[elements])
            for values in groups:
                if values.state_id == self.id:
                    result.append(values)
        except Exception:
            pass
        return result
