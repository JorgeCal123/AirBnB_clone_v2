#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import getenv

if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.file_storage import FileStorage
    print("entra y nose porque ")
    storage = DBStorage()
else:
    from models.engine.db_storage import DBStorage
    storage = FileStorage()
storage.reload()
