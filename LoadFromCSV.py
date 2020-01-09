import csv
from DataAcsess import tags_to_recipes, all_recipes_data, initialTags,update_tags
from LoadToCSV import the_tags_url,the_ingredients_url, the_instructions_url, the_recipe_data_url


def get_recipes_general_data(url):
    all_recipes_general_data = {}
    try:
        with open(url, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                # the row is not empty
                if len(row) > 0:
                    recipe_id = int(row[0])
                    recipe_name = row[1]
                    recipe_url = row[2]
                    all_recipes_general_data[recipe_id] = {'name': recipe_name, 'url':recipe_url}
    except:
        print("Eror: url - " + url + " not found")

    return all_recipes_general_data


# return list of {'id': x, name:y}
def get_recipes_data(url):
    recipes_data = {}
    with open(url, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            # the row is not empty
            if len(row) > 0:
                recipe_id = int(row[0])
                content = row[1:]
                recipes_data[recipe_id] = content
    return recipes_data


# output item in list: {'id': x , 'ingredients': [], 'instr': []}
def upload_recipes_from_csv():
    initialTags()
    # the_tags_url,  the_recipe_data_url
    ingredients_list = get_recipes_data(the_ingredients_url)
    instructions_list = get_recipes_data(the_instructions_url)
    general_data_list = get_recipes_general_data(the_recipe_data_url)
    for id in ingredients_list:
        try:
            ingredients = ingredients_list[id]
            instructions = instructions_list[id]
            name = general_data_list[id]['name']
            url = general_data_list[id]['url']
            all_recipes_data[id] = {'name': name, 'url': url, 'ingredients': ingredients, 'instructions': instructions}
        except:
            pass

    tags_with_relevent_recipes = get_recipes_data(the_tags_url)
    for tag_id in tags_with_relevent_recipes:
        recipes_list = tags_with_relevent_recipes[tag_id]
        tags_to_recipes[tag_id] = set(recipes_list)
    update_tags()



