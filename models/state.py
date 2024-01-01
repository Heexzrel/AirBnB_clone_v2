#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from  models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column
from os import getenv
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") !='db':
        @property
        def cities(self):
            list_of_cities = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
