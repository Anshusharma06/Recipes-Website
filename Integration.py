from ReadFromCSV.py import save_into_csv

all_tags = {}
recipe_counter = 0
ingredients_set = {'בשר', 'בצל', 'שום', 'ביצה', 'ביצים', 'עגבניה'}


def get_new_recipe_id():
    global recipe_counter
    recipe_counter = recipe_counter + 1
    return recipe_counter


def fill_all_tags():
    for ingredient in ingredients_set:
        all_tags[ingredient] = []


fill_all_tags()

# read from foodie
foodie_recipes = {}

# read sugat
sugat_recipes = {}

# {id: int, 'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
all_recipes = {}

save_into_csv(the_instructions_url, the_ingredients_url, all_recipes)