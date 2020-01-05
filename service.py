from DataAcsess import initialTags, tag_name_to_id , tags_to_recipes, all_recipes_data
from UpladFromCSV import upload_recipes_from_csv

import functools

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def convertIngredientsNamesToIds(ingrediens):
    return list(map(lambda ingredient: tag_name_to_id[ingredient] ,ingrediens))

def get_compatible_recipes_ids(ingredients_ids):
    tags_recipes_ids = list(map(lambda id: list(tags_to_recipes[id]),ingredients_ids))
    return list(functools.reduce(lambda tag_recipes_ids1,tag_recipes_ids2: intersection(tag_recipes_ids1,tag_recipes_ids2), tags_recipes_ids))

def convertStringToIntegers(strings):
    return list(map(lambda str: int(str),strings))

def get_recipes_from_ids(ids):
    ids = convertStringToIntegers(ids)
    return list(map(lambda id: all_recipes_data[id],ids))

def getRecipes(ingredients):
    initialTags()
    upload_recipes_from_csv()
    ingredients_ids = convertIngredientsNamesToIds(ingredients)
    compatible_recipes_ids = get_compatible_recipes_ids(ingredients_ids)
    recipes = get_recipes_from_ids(compatible_recipes_ids)
    return recipes

