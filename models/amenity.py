#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """amenities class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
    place_amenities =  Table("place_amenity", Base.metadata,
            Column('place_id', String(60), ForeignKey('place.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))
