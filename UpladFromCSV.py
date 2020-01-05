import csv
from DataAcsess import tags_to_recipes, all_recipes_data
from LoadToCSV import the_tags_url,the_ingredients_url, the_instructions_url, the_recipe_data_url


def get_recipes_general_data(url):
    all_recipes_general_data = []
    with open(url, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            # the row is not empty
            if len(row) > 0:
                recipe_id = row[0]
                recipe_name = row[1]
                recipe_url = row[2]
                all_recipes_general_data = all_recipes_general_data + [{'id': recipe_id, 'name': recipe_name, 'url':recipe_url}]
    return all_recipes_general_data


# return list of {'id': x, name:y}
def get_recipes_data(url, tag):
    recipes_data = []
    with open(url, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            # the row is not empty
            if len(row) > 0:
                recipe_id = row[0]
                content = row[1:]
                recipes_data = recipes_data + [{'id': recipe_id, tag: content}]
    return recipes_data


# output item in list: {'id': x , 'ingredients': [], 'instr': []}
def upload_recipes_from_csc():
    # the_tags_url,  the_recipe_data_url
    ingredients_list = get_recipes_data(the_ingredients_url, 'ingredients')
    instructions_list = get_recipes_data(the_instructions_url, 'instructions')
    general_data_list = get_recipes_general_data(the_recipe_data_url)
    for recipe_line in ingredients_list:
        id = recipe_line['id']
        ingredients = filter(lambda recipe: recipe['id'] == id, ingredients_list).__next__()
        instructions = filter(lambda recipe: recipe['id'] == id, instructions_list).__next__()
        general_data = filter(lambda recipe: recipe['id'] == id, general_data_list).__next__()
        all_recipes_data.append({'id': id, 'name': general_data['name'], 'url': general_data['url'],
                                 'ingredients': ingredients['ingredients'], 'instructions': instructions['instructions']})



    tags_with_relevent_recipes = get_recipes_data(the_instructions_url, 'recipe_list')
