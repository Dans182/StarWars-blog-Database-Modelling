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

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250))

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)    
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    Favorite = relationship(Favorite)

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    Favorite = relationship(Favorite)
    
class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    capacity = Column(Integer, nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    Favorite = relationship(Favorite)

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')