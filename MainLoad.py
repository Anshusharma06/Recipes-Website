from LoadToCSV import save_into_csv
from GoodiesWebsite import goodie_main_page, foodie_url
from Walla_website import walla_main_page, food_walla_url
from DataAcsess import csv_converted_tags_recipes,initialTags
from SugatScraping import scrapRecipes

# read from foodie
# foodie_recipes = goodie_main_page(foodie_url)

def scrapFromWebsites():
    print("start scrapping")
    sugat_recipes = scrapRecipes()
    # walla_recipes = walla_main_page(food_walla_url)
    # {id: int, 'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
    all_recipes = sugat_recipes
    print("done scraping")
    return all_recipes

def saveSataToCsv(all_recipes):
    tags = csv_converted_tags_recipes()
    save_into_csv(all_recipes, tags)


def ScrapDataAndSaveToCsv():
    initialTags()
    all_recipes = scrapFromWebsites()
    saveSataToCsv(all_recipes)


ScrapDataAndSaveToCsv()