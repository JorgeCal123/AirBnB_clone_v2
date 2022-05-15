#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:

        name = ""
        @property
        def cities(self):
            list_c = []
            for c in models.storage.all('City').values():
                if(c.state_id == self.id):
                    list_c.append(c)
            return list_c
