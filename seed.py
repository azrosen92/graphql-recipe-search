import random

from database.base import engine, db_session, Base
from models import Recipe, Ingredient

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    ingredients = [
        Ingredient(name=ing_name) 
        for ing_name 
        in [
            'chicken', 
            'beef', 
            'olive oil', 
            'salt', 
            'pepper', 
            'hot sauce', 
            'broccoli', 
            'green beans', 
            'spinach', 
            'carrots'
        ]]
    db_session.add_all(ingredients)
    db_session.commit()

    recipes = [
        Recipe(
            name=f'recipe {number}',
            ingredients=random.sample(ingredients, 4)
        ) for number in range(3)
    ]

    db_session.add_all(ingredients)
    db_session.commit()
