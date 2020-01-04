from urllib.request import urlopen
from bs4 import BeautifulSoup
from Integration import all_tags, get_new_recipe_id, ingredients_set


# FODIE WEBSITE
foodie_url = "https://foody.co.il/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA/"




def find_main_page_categories_url(table_url):
    # gose all over the categories
    categories_url = []
    for item in table_url:
            for c in item.find_all('a'):
                y = c.get('href')
                if "foody.co.il/category" in y:
                    categories_url.append(y)
    return categories_url


def find_recipes_url_in_categories(categories_url):
    r_url = []
    # run on each categorie and take the recipe url
    for category_url in categories_url:
        print("category: ", category_url, "\n")
        # try:
        category_page = urlopen(category_url)
        category_soup = BeautifulSoup(category_page)
        recipees_table = category_soup.find_all('div', class_='container-fluid feed-container term-feed-container')

        for rec in recipees_table:
            for u in rec.find_all('a'):
                y = u.get('href')
                # this is the website of the recipe
                if "foody_recipe" in y:
                    r_url.append(y)
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
                instructions_line = line.string
                if not instructions_line is None:
                    instr.append(line.string)
        return {"id": get_new_recipe_id(), "url": url, "tags": tags, "ingredients": ing, "instructions": instr}
    except():
        return -1


def goodie_main_page(url):
    all_recipes = []
    main_page = urlopen(url)
    soup = BeautifulSoup(main_page)
    category_table_url = soup.find_all('li', class_='menu-item')
    categories_url = find_main_page_categories_url(category_table_url)
    r_url = find_recipes_url_in_categories(categories_url)

    for url in r_url:
            recipe = extract_recipe_ing(url)
            if recipe != 1:
                all_recipes.append(recipe)

    return all_recipes

# all_recipes = main_page('https://foody.co.il/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA/')

