import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key = True)
    image_src = Column(String(500), nullable = False)
    likes = Column(Integer, nullable = False) 
    name = Column(String(100), nullable = False)
    description = Column(String(500), nullable = False)
    category = relationship("category")
    favorites = relationship("favorites")

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key = True)
    image_src = Column(String(500), nullable = False)
    likes = Column(Integer, nullable = False)
    name = Column(String(100), nullable = False)
    description = Column(String(500), nullable = False)
    category = relationship("category")
    favorites = relationship("favorites")

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key = True)
    description = Column(String(100), nullable = True)
    characters_id = Column(Integer, ForeignKey("characters.id"), nullable = False)
    planets_id = Column(Integer, ForeignKey("planets.id"), nullable = False)

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    favorite_posts = relationship("user")
    characters_id = Column(Integer, ForeignKey("characters.id"), nullable = False)
    planets_id = Column(Integer, ForeignKey("planets.id"), nullable = False)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    email = Column(String(30), nullable = False)
    password = Column(String(500), nullable = False)
    favorites_id = Column(Integer, ForeignKey("favorites.id"), nullable = False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')