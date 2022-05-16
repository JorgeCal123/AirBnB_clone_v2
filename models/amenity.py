#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String

class Amenity(BaseModel, Base):

    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
    
