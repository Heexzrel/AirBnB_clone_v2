#!/usr/bin/python3
""" Instantiating a storage object
if env var.(HBNB_TYPE_STORAGE) is db imports DBStorage class,
Otherwise imports FileStorage
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
