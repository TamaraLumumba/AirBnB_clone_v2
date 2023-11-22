#!/usr/bin/python3
""" Classs City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
from sqlalchemy.orm import relationship
from os import environ

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    # state_id = ""
    # name = ""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id", ondelete='CASCADE'),
                      nullable=False)

    places = relationship("Place", backref="cities")

