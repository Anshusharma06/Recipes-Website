
all_tags = {}
recipe_counter = 0
ingredients_set = {'בשר', 'בצל', 'שום', 'ביצה', 'ביצים', 'עגבניה'}


def get_new_recipe_id():
    global recipe_counter
    recipe_counter = recipe_counter + 1
    return recipe_counter

def add_to_tags_list(tags, recipe_id):
    for t in tags:
        all_tags[t] = all_tags[t].append(recipe_id)


def extractIngredientTags(ingredients):
    tags = []
    for ingredient in ingredients:
        words = ingredient.split()
        for word in words:
            if word in ingredients_set:
                tags.append(word)
    return tags

