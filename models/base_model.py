#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class"""
        if kwargs:
            try:
                for key, val in kwargs.items():
                    if key in ("created_at", "updated_at"):
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    if key != "__class__":
                        setattr(self, key, val)

                if "id" not in kwargs:
                    self.id = str(uuid.uuid4())
                if "created_at" not in kwargs:
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                    self.updated_at = datetime.now()

            except Exception:
                pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """Return a string representation"""
        return self.__str__()

    def save(self):
        """Updates the public instance attribute updated_at to current"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates dictionary of the class and returns"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the object"""
        models.storage.delete(self)
