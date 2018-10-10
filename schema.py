from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import ObjectType, List, relay, String, Field, Schema, Int

from services import RecipeSearchService
from models import Recipe as RecipeModel, Ingredient as IngredientModel

###### GQL Schemas ######
class Recipe(SQLAlchemyObjectType):
  class Meta:
    model = RecipeModel
    only_fields = ("id", "name", "url", "ingredients")


class Ingredient(SQLAlchemyObjectType):
  class Meta:
    model = IngredientModel
    only_fields = ("id", "name")

  amount = String()

  def resolve_amount(self, info):
    return '1 cup'
    
   
class RecipeSearchResult(ObjectType):
  results = List(Recipe)


class Query(ObjectType):
  node = relay.Node.Field()
  recipe_search_results = Field(
      RecipeSearchResult, 
      search_term=String(),
      ingredients=List(Int))

  def resolve_recipe_search_results(self, info, search_term, ingredients=[]):
    results = RecipeSearchService.search_for_recipe_with_ingredients(search_term,
        ingredients)

    return RecipeSearchResult(results=results)


schema = Schema(query=Query)
