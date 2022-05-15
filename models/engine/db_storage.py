#!/usr/bin/python3
"""New engine DBStorage"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv

class DBStorage:
    __engine = None
    __session = None
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
                }
    def __init__(self):
        """contructor of db"""
        self.__engine =create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        fclass = {}
        if cls is None:
            data = self.__session.query(User).all()
            data += self.__session.query(State).all()
            data += self.__session.query(City).all()
            data += self.__session.query(Amenity).all()
            data += self.__session.query(Place).all()
            data += self.__session.query(Review).all()
            for value in data:
                key = value.__name__ + '.' + value.id
                fclass[key] = value
            return fclass
        else:
            data = self.__session.query(cls).all()
            for clss in self.classes:
                if cls is None or cls is self.classes[clss] or cls is clss:
                    objs = self.__session.query(self.classes[clss]).all()
                    for obj in objs:
                        key = obj._class.name_ + '.' + obj.id
                        fclass[key] = obj
            return fclass
        

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload database"""
        Base.metadata.create_all(self.__engine)
        sess1 = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ScopSession = scoped_session(sess1)
        self.__session = ScopSession()
