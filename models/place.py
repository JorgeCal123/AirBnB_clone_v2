#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    
    """place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True)"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", backref="places",
                              cascade="all, delete, delete-orphan")
        """amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)"""

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def cities(self):
            """return list of cities relation with this state"""
            list_c = []
            for c in models.storage.all(models.review).values():
                if(c.place_id == self.id):
                    list_c.append(c)
            return list_c

        @property
        def amenities(self):
            my_atr_amenity = []
            for a in amenity_ids:
                if self.id == a.id:
                    my_atr_amenity.append(a)
            return my_atr_amenity

        @amenities.setter
        def amenities(self, amenity):
            if type(amenity).__name__ == 'Amenity':
                self.amenity_ids.append(amenity)
