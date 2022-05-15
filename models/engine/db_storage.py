#!/usr/bin/python3
"""New engine DBStorage"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    configdb = {
        "HBNB_MYSQL_USER" : "",
        "HBNB_MYSQL_PWD": "",
        "HBNB_MYSQL_HOST": "",
        "HBNB_MYSQL_DB": "",
        "HBNB_TYPE_STORAGE": "",
        "HBNB_ENV": ""
    }
    def __init__(self):
        """contructor of db"""
        self.__engine =create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(self.configdb["HBNB_MYSQL_USER"], self.configdb["HBNB_MYSQL_PWD"],
                                      self.configdb["HBNB_MYSQL_HOST"], self.configdb["HBNB_MYSQL_DB"]), pool_pre_ping=True)
        if self.configdb["HBNB_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        fclass = {}
        if cls is None:
            data = self.__session.query(User, State, City, Amenity, Place, Review).all()
        else:
            data = self.__session.query(cls).all()
        for value in data:
            key = value.__name__ + '.' + value.id
            fclass[key] = value
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
