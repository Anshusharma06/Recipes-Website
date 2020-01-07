from LoadToCSV import save_into_csv
from GoodiesWebsite import goodie_main_page
from Walla_website import walla_main_page
from DataAcsess import csv_converted_tags_recipes,initialTags
from SugatScraping import scrapRecipes

# read from foodie
#

def scrapFromWebsites():
    print("start scrapping")
    walla_recipes = walla_main_page()
    foodie_recipes = goodie_main_page()
    print("\nfoodies num of recipes" + str(len(foodie_recipes)))
    sugat_recipes = scrapRecipes()
    # {id: int, 'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
    all_recipes =  foodie_recipes + walla_recipes + foodie_recipes
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