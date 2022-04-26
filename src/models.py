import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    password = Column(String(250)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, Foreign_key("character_id")
    character = relationship(character)
    planet_id = Column(Integer, Foreign_key("planet_id")
    planet = relationship(planet)
    vehicle_id = Column(Integer, Foreign_key("vehicle_id")
    vehicle = relationship(vehicle)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, Foreign_key("character_id")
    character = relationship(character)
    planet_id = Column(Integer, Foreign_key("planet_id")
    planet = relationship(planet)
    vehicle_id = Column(Integer, Foreign_key("vehicle_id")
    vehicle = relationship(vehicle)
    
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')