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
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="states",
                              cascade="all, delete, delete-orphan")
    else:

        name = ""
        @property
        def cities(self):
            """return list of cities relation with this state"""
            list_c = []
            for c in models.storage.all(models.City).values():
                if(c.state_id == self.id):
                    list_c.append(c)
            return list_c
