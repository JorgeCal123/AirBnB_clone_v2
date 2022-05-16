#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv
=======
from os import getenv
from sqlalchemy.orm import relationship
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String
>>>>>>> fe6769e13aaaf258bd774e513cac1c177028df05

class Amenity(BaseModel, Base):

<<<<<<< HEAD
class Amenity(BaseModel, Base):
    """ class Amenity"""
    __tablename__ = 'amenities'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary='place_amenity')

    else:
        name = ""
=======
    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
    
>>>>>>> fe6769e13aaaf258bd774e513cac1c177028df05
