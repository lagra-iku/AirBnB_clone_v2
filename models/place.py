#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City
from models.user import User


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Class representing a place.
    Attributes:
        city_id: City ID
        user_id: User ID
        name: Name input
        description: Description string
        number_rooms: Number of rooms (int)
        number_bathrooms: Number of bathrooms (int)
        max_guest: Maximum guest count (int)
        price_by_night: Price for a stay (int)
        latitude: Latitude (float)
        longitude: Longitude (float)
        amenity_ids: List of Amenity IDs
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Returns a list of review IDs."""
            my_variable = models.storage.all()
            my_elements = []
            my_total = []
            for value in my_variable:
                review = value.replace('.', ' ')
                review = shlex.split(review)
                if review[0] == 'Review':
                    my_elements.append(my_variable[value])
            for elem in my_elements:
                if elem.place_id == self.id:
                    my_total.append(elem)
            return my_total

        @property
        def amenities(self):
            """Returns a list of amenity IDs."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Appends amenity IDs to the attribute."""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
