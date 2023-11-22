#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:

    """"
    Args:
        __engine (sqlalchemy.engine): working engine
        __session (sqlalchemy.session): current session
        """
    __engine = None
    __session = None

    def __init__(self):
        """creates an engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
        format(getenv("HBNB_MYSQL_USER"),
               getenv("HBNB_MYSQL_PWD"),
               getenv("HBNB_MYSQL_HOST"),
               getenv("HBNB_MYSQL_DB")),
               pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self,   cls=None):
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Review))
            objs.extend(self.__session.query(User))
        else:
            if isinstance(cls, str):
                cls = eval(cls)
                objs = self.__session.query(cls)
                myob = {"{}.{}".format(type(o).__name__,
                                       o.id): o for o in objs}
                return myobj

    def new(self, obj):
        """adds obj to current session"""
        self.__session.add(obj)

    def save(self):
        """adds changes to current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes objs from db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in db and creates current session"""
        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scope_session(my_session)
        self.__session = Session()

    def close(self):
        """closes all session"""
        self.__session.close()
