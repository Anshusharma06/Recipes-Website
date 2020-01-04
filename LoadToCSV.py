import csv

the_tags_url = 'tags.csv'
the_ingredients_url = 'ingredients.csv'
the_instructions_url = 'instructions.csv'
the_recipe_data_url = 'data.csv'


# item in list: {id: int,'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
def save_general_csv(csv_url, current_list, tag, optional_tag):
    with open(csv_url, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in current_list:
            if optional_tag is None:
                writer.writerow([item["id"]] + item[tag])
            else:
                writer.writerow([item["id"]] + item[tag], item[optional_tag])


# item in list: {id: int,'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
def save_into_csv(recipes_list, tags_list):
    save_general_csv(the_instructions_url, recipes_list, 'instructions', None)
    save_general_csv(the_ingredients_url, recipes_list, 'ingredients', None)
    save_general_csv(the_tags_url, tags_list, 'recipe_list', None)
    save_into_csv(the_recipe_data_url, recipes_list, 'name', 'url')


