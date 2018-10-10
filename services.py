from sqlalchemy import or_, func

from models import Recipe, Ingredient, RecipeIngredient

###### Service Layer ######
class RecipeSearchService():
  @staticmethod
  def search_for_recipe_with_ingredients(search_term, ingredient_ids=[]):
      """
        SELECT recipes.*, ingredients.*
        FROM recipes 
        JOIN recipes_ingredients 
          ON (recipes.id = recipes_ingredients.recipe_id)
        JOIN ingredients
          ON (ingredients.id = recipe_ingredients.ingredients_id)
        WHERE recipes.id IN (
          SELECT recipes_ingredients.recipe_id
          FROM recipes_ingredients
          JOIN ingredients 
            ON (ingredients.id = recipes_ingredients.ingredients_id)
          WHERE
            ingredients.name ILIKE '\%%{search_term}\%' OR 
            ingredients.id IN (%{ingredient_ids})
          GROUP BY recipes_ingredients.recipe_id
          HAVING COUNT(*) = %{search_query.old_ingredients.length + 1}
        );
      """
      return Recipe.query.\
        filter(Recipe.id.in_(
          Recipe.query.\
            with_entities(Recipe.id).\
            join(RecipeIngredient).\
            join(Ingredient).\
            filter(or_(
                Ingredient.name.ilike('%{}%'.format(search_term)),
                Ingredient.id.in_(ingredient_ids)
              )).\
            group_by(Recipe.id).\
            having(func.count(Ingredient.id) == len(ingredient_ids)
                + 1)))

