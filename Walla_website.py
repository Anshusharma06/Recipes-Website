from urllib.request import urlopen
from bs4 import BeautifulSoup
from Integration import all_tags, get_new_recipe_id, ingredients_set


# FODIE WEBSITE
food_walla_url = 'https://food.walla.co.il/recipes'

web_bios = 'https://food.walla.co.il'


def find_main_page_categories_url(main_url):
    main_page = urlopen(main_url)
    soup = BeautifulSoup(main_page)
    category_table_url = soup.find_all('section', class_='css-18lisp8')

    # gose all over the categories
    categories_url = []
    for item in category_table_url:
            for c in item.find_all('li'):
                category_url = c.a['href']
                categories_url.append(category_url)
    return categories_url

def find_recipes_url_in_category_page(categories_url):
    single_recipe_url_list = []
    # run on each categorie and take the recipe url
    for category_url in categories_url:
        try:
            category_page = urlopen(category_url)
            category_soup = BeautifulSoup(category_page)
            recipees_table = category_soup.find_all('li', class_='single')

            for rec in recipees_table:
                for u in rec.find_all('a'):
                    single_recipe_url = u.get('href')
                    single_recipe_url = web_bios + single_recipe_url
                    # this is the website of the recipe
                    single_recipe_url_list.append(single_recipe_url)
        except:
            print(category_url)
    r_url = list(dict.fromkeys(single_recipe_url_list))
    return r_url


def extract_all_recipe_data(url):
    try:
        page = urlopen(url)
        soup = BeautifulSoup(page)

        ingredients = []
        tags = []
        instructions = []
        name = ''

        #name
        nams_section = soup.find('h2', class_="title recipe")
        name = nams_section.span.string

        ingredient_section = soup.find_all('ul', class_='box')
        # ingredient
        for t in ingredient_section:
            head = t.h2
            # insert section head if exist
            if head is not None:
                head = head.string
                ingredients.append(head)
            ingredient_lines = t.find_all('li', class_='ingredient-line')
            # insert all ingredients
            for line in ingredient_lines:
                ingredient_amount = line.find('span', class_='amount').string
                ingredient_name = line.find('span', class_='name').string
                full_ingredient = ingredient_amount + " " + ingredient_name
                ingredients.append(full_ingredient)
                # recipe ingrediant
        # recipe
        recipe_section = soup.find_all('div', class_='way-to-cook')
        for r in recipe_section:
            instructions_lines = r.find_all('div', class_='text')
            for line in instructions_lines:
                span = line.find_all('span')
                instruction = span[1].contents
                if len(instruction) > 1:
                    instruction = instruction[1]
                else:
                    instruction = instruction[0]
                instructions.append(instruction)
        return {"id": get_new_recipe_id(),"name": name, "url": url, "tags": tags, "ingredients": ingredients, "instructions": instructions}
    except():
        return -1


def main_page(url):
    all_recipes = []
    categories_url = find_main_page_categories_url(url)
    r_url = find_recipes_url_in_category_page(categories_url)

    for url in r_url:
            recipe = extract_all_recipe_data(url)
            if recipe != 1:
                all_recipes.append(recipe)

    return all_recipes

all_recipes = main_page(foodie_url)

