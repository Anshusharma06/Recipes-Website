from urllib.request import urlopen
from bs4 import BeautifulSoup
from Integration import all_tags, get_new_recipe_id

all_tags = {}
ingredients_set = {}
# FODIE WEBSITE

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


def find_main_page_categories_url(table_url):
    # gose all over the categories
    categories_url = []
    for item in table_url:

            for c in item.find_all('a'):
                y = c.get('href')
                if "foody.co.il/category" in y:
                    categories_url.append(y)
    print("end finding category url")
    print("**************************************************************")
    return categories_url


def find_recipes_url_in_categories(categories_url):
    r_url = []
    # run on each categorie and take the recipe url
    for category_url in categories_url:
        print("category: ", categories_url, "\n")
        # try:
        category_page = urlopen(category_url)
        category_soup = BeautifulSoup(category_page)
        recipees_table = category_soup.find_all('div', class_='container-fluid feed-container term-feed-container')

        for rec in recipees_table:
            for u in rec.find_all('a'):
                y = u.get('href')
                # this is the website of the recipe
                if "foody_recipe" in y:
                    r_url.append(y + "?page=2")
    r_url = list(dict.fromkeys(r_url))
    return r_url


def extract_recipe_ing(url):
    try:
        page = urlopen(url)
        soup = BeautifulSoup(page)
        table = soup.find_all('li', class_='ingredients')

        ing = []
        tags = []
        instr = []
        # ingredient
        for t in table:
            d = t.find('span', class_='amount')
            # recipe ingrediant
            singular = d.get('data-singular')
            amount = d.get('data-amount')
            unit = d.get('data-unit')
            if unit is None:
                unit = ""
            amount_unit = amount + " " + unit
            i = amount_unit + " " + singular
            ing.append(i)
            tags.append(singular)
        # recipe
        recipe = soup.find_all('div', class_='foody-content')
        for r in recipe:
            for line in r.find_all('li'):
                instr.append(line.string)
        return {"id": get_new_recipe_id(), "url": url, "tags": tags, "ingredients": ing, "instructions": instr}
    except():
        return -1


def main_page(url):
    all_recipes = []
    main_page = urlopen(url)
    soup = BeautifulSoup(main_page)
    category_table_url = soup.find_all('li', class_='menu-item')
    categories_url = find_main_page_categories_url(category_table_url)
    r_url = find_recipes_url_in_categories(categories_url)

    counter = 10
    for url in r_url:
        if counter == 0:
            recipe = extract_recipe_ing(url)
            if recipe != 1:
                counter = counter - 1
                all_recipes.append(recipe)

    return all_recipes

all_recipes = main_page('https://foody.co.il/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA/')


print(all_recipes)
