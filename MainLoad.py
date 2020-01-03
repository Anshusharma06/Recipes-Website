from ReadFromCSV import save_into_csv
from ExtractAllRecipes import main_page, foodie_url

# read from foodie
foodie_recipes = main_page(foodie_url)


# read sugat
sugat_recipes = {}

# {id: int, 'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
all_recipes = foodie_recipes
y = type(all_recipes)

save_into_csv(all_recipes, [])