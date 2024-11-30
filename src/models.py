import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    image_src = Column(String(500), nullable=False)
    likes = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    favorites = relationship('Favorites', back_populates='character')

class Planet(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    image_src = Column(String(500), nullable=False)
    likes = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    favorites = relationship('Favorites', back_populates='planet')

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    character = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    user = relationship('User', back_populates='favorites')

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False)
    password = Column(String(500), nullable=False)
    favorites = relationship('Favorites', back_populates='user')

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
