import csv

all_recipes = {}
the_tags_url = 'tags.csv'
the_ingredients_url = 'ingredients.csv'
the_instructions_url = 'instructions.csv'
the_recipe_data_url = 'urls.csv'


# item in list: {id: int,'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
def save_general_csv(csv_url,list , tag, optional_tag):
    with open(csv_url, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in list:
            if optional_tag is None:
                writer.writerow([item[id]] + item[tag])
            else:
                writer.writerow([item[id]] + item[tag], item[optional_tag])


# item in list: {id: int,'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
def save_into_csv(recipes_list, tags_list):
    save_general_csv(the_instructions_url, recipes_list, 'instructions')
    save_general_csv(the_ingredients_url, recipes_list, 'ingredients')
    save_general_csv(the_tags_url, tags_list, 'recipe_list')
    # save_into_csv(the_recipe_data_url, recipes_list, 'name', 'url')


# return list of {'id': x, name:y}
def get_recipes_data(url, tag, recipes_list):
    recipes_data = []
    recipes_len = len(recipes_list)
    with open(url, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            # the row is not empty
            if len(row) > 0:
                recipe_id = row[0]
                if recipe_id in recipes_list:
                    recipes_len = recipes_len -1
                    content = row[1:]
                    recipes_data = recipes_data + [{'id': recipe_id, tag: content}]
            if recipes_len == 0:
                break
    return recipes_data


# output item in list: {'id': x , 'ingredients': [],'instr': []}
def read_recipes_csc(ingredients_url, instructions_url,general_data_url, recipes_list):
    ingredients_list = get_recipes_data(ingredients_url, 'ingredients', recipes_list)
    instructions_list = get_recipes_data(instructions_url, 'instructions', recipes_list)
    # general_data_list = get_recipes_data(general_data_url, ['url', 'name'], recipes_list)
    return_recipes = []
    for id in recipes_list:
        ingredients = filter(lambda recipe: recipe['id'] == id, ingredients_list).__next__()
        instructions = filter(lambda recipe: recipe['id'] == id, instructions_list).__next__()
        return_recipes = return_recipes + [{'id': id, 'ingredients': ingredients['ingredients'], 'instructions': instructions['instructions']}]
    return return_recipes


save_into_csv(the_instructions_url, the_ingredients_url, all_recipes)


print("********************************************************8")
print(all_recipes)
print("********************************************************8")
