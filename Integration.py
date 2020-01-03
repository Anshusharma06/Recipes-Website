
all_tags = {}
recipe_counter = 0
ingredients_set = {'בשר', 'בצל', 'שום', 'ביצה', 'ביצים', 'עגבניה'}


def get_new_recipe_id():
    global recipe_counter
    recipe_counter = recipe_counter + 1
    return recipe_counter


