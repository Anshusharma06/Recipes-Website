from urllib.request import urlopen
from bs4 import BeautifulSoup
from DataAcsess import extractIngredientTags, get_new_recipe_id, print_progress



# FODIE WEBSITE
foodie_url = "https://foody.co.il/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA/"

Max_page = '2'

def getSoupFromUrl(url):
    # req = Request(url, headers={'User-Agent' : "Magic Browser"})
    # con = urlopen( req )
    # html = con.read()
    html = urlopen(url)
    return BeautifulSoup(html,features="lxml")

def find_main_page_categories_url(url):
    try:
        soup = getSoupFromUrl(url)
        category_table_url = soup.find_all('li', class_='menu-item')
        # gose all over the categories
        categories_url = []
        for item in category_table_url:
                for c in item.find_all('a'):
                    y = c.get('href')
                    if "foody.co.il/category" in y:
                        categories_url.append(y + "?page=" + Max_page)
        print("Goodie First part :Done successfully")
        return categories_url
    except:
        print("Goodie First part :Fail")


def find_recipes_url_in_categories(categories_url):
    r_url = []
    # run on each categorie and take the recipe url
    for category_url in categories_url:
        try:
            category_soup = getSoupFromUrl(category_url)
            grid_items = category_soup.find_all('h2', class_='grid-item-title')
            for rec in grid_items:
                single_url = rec.find('a').get('href')
                r_url.append(single_url)
        except:
            pass
    r_url = list(dict.fromkeys(r_url))
    print("Goodie Second part :Done successfully")
    return r_url


def get_name(soup_for_name):
    name_section = soup_for_name.find('h1', class_='col p-0')
    name = name_section.string
    return name


def get_ingredient(soup_for_ingredient):
    tags = []
    ingredients_output = []
    table = soup_for_ingredient.find_all('li', class_='ingredients')
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
        ingredients_output.append(i)
        tags.append(singular)
    return ingredients_output ,tags


def get_recipe(soup_for_recipe):
    instructions_output = []
    recipe = soup_for_recipe.find_all('div', class_='foody-content')
    for r in recipe:
        for line in r.find_all('li'):
            instructions_line = line.string
            if not instructions_line is None:
                instructions_output.append(line.string)
    return instructions_output


def extract_recipe_ing(url):
        soup = getSoupFromUrl(url)
        ingredient, tags = get_ingredient(soup)
        name = get_name(soup)
        instructions = get_recipe(soup)
        recipe_goodie_id = get_new_recipe_id()
        extractIngredientTags(tags, recipe_goodie_id)
        print_progress(recipe_goodie_id)
        return {"id": recipe_goodie_id, "name": name, "url": url, "ingredients": ingredient, "instructions": instructions}



def goodie_main_page():
    all_recipes = []
    categories_url = find_main_page_categories_url(foodie_url)
    r_url = find_recipes_url_in_categories(categories_url)

    for url in r_url:
        try:
            recipe = extract_recipe_ing(url)
            all_recipes.append(recipe)
        except:
            print('bad url:' + url)
    print("Goodie :Done")
    return all_recipes

# all = goodie_main_page('https://foody.co.il/%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA/')


# n ='\n\t\tהעיקר זה הרומנטיקה – סופלה שוקולד וקרמל של קרין גורן    '
# print(re.sub('\W+\s','', n))