from ReadFromCSV import save_into_csv
from GoodiesWebsite import goodie_main_page, foodie_url
from Walla_website import walla_main_page, food_walla_url
from Integration import cav_converted_tags_recipes

# read from foodie
foodie_recipes = goodie_main_page(foodie_url)


# read sugat
sugat_recipes = {}


# read walla
walla_recipes = walla_main_page(food_walla_url)

# {id: int, 'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
all_recipes = foodie_recipes + walla_recipes
y = type(all_recipes)

tags = cav_converted_tags_recipes()

save_into_csv(all_recipes, tags)
