from Loaders.LoadToCSV import save_into_csv
from Scraping.GoodiesWebsite import goodie_main_page
from Scraping.Walla_website import walla_main_page
from Data.DataAcsess import csv_converted_tags_recipes,initialTags
from Scraping.SugatScraping import scrapRecipes
import time
# read from foodie
#

def scrapFromWebsites():
    print("start scrapping")
    start = time.localtime()
    print("start at: " + str(start))
    sugat_recipes = scrapRecipes()
    walla_recipes = walla_main_page()
    foodie_recipes = goodie_main_page()
    # {id: int, 'url': '', 'tags': [], 'ingredients': [],'instructions': [],name: ''}
    all_recipes =  sugat_recipes + walla_recipes + foodie_recipes

    print("done scraping")
    now = time.localtime()
    try:
        print("time : " + str(now - start))
    except:
        pass
    return all_recipes

def saveSataToCsv(all_recipes):
    tags = csv_converted_tags_recipes()
    save_into_csv(all_recipes, tags)


def ScrapDataAndSaveToCsv():
    initialTags()
    all_recipes = scrapFromWebsites()
    saveSataToCsv(all_recipes)

ScrapDataAndSaveToCsv()