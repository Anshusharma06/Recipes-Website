from ReadFromCSV import save_into_csv

all_tags = {}
recipe_counter = 0
ingredients_set = {'בשר', 'בצל', 'שום', 'ביצה', 'ביצים', 'עגבניה'}


def get_new_recipe_id():
    global recipe_counter
    recipe_counter = recipe_counter + 1
    return recipe_counter

# read from foodie
foodie_recipes = {}

# read sugat
sugat_recipes = {}

# {id: int, 'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
all_recipes = {}

save_into_csv(all_recipes, all_tags)
