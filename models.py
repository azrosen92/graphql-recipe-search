from sqlalchemy import *
from sqlalchemy.orm import backref, relationship

from database.base import Base


class Recipe(Base):
  __tablename__ = 'recipe'

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  url = Column(String(255))

  ingredients = relationship('Ingredient', secondary='recipe_ingredient', backref=backref('recipes', lazy='joined'))

class Ingredient(Base):
  __tablename__ = 'ingredient'

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  amount = Column(String(255))

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredient'

    recipe_id = Column(Integer, ForeignKey('recipe.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    ingredient = relationship(Ingredient, backref='recipe_ingredients')
    amount = Column(String)

