from urllib.request import urlopen
from bs4 import BeautifulSoup
from DataAcsess import extractIngredientTags, get_new_recipe_id, print_progress


# FODIE WEBSITE
food_walla_url = 'https://food.walla.co.il/recipes'

web_bios = 'https://food.walla.co.il'

recipes_limit = 10

def getSoupFromUrl(url):
    # req = Request(url, headers={'User-Agent' : "Magic Browser"})
    # con = urlopen( req )
    # html = con.read()
    html = urlopen(url)
    return BeautifulSoup(html,features="lxml")


def find_main_page_categories_url(main_url):
    try:
        soup = getSoupFromUrl(main_url)
        category_table_url = soup.find_all('section', class_='css-18lisp8')
        # gose all over the categories
        categories_url = []
        for item in category_table_url:
            for c in item.find_all('li'):
                category_url = c.a['href']
                categories_url.append(category_url)
        print("Walla First part :Done successfully")
        return categories_url
    except:
        print("Walla First part :Fail")
    return categories_url

def find_recipes_url_in_category_page(categories_url):
    single_recipe_url_list = []
    # run on each categorie and take the recipe url
    for category_url in categories_url:
        try:
            category_soup = getSoupFromUrl(category_url)
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
    print("Walla Second part :Done successfully")
    return r_url


def get_name(soup_for_name):
    nams_section = soup_for_name.find('h2', class_="title recipe")
    if nams_section is not None:
        name_output = nams_section.span.string
    return name_output


def get_ingredient(soup_for_ingredient):
    ingredients_output = []
    ingredient_section = soup_for_ingredient.find_all('ul', class_='box')
    # ingredient
    for t in ingredient_section:
        head = t.h2
        # insert section head if exist
        if head is not None:
            head = head.string
            ingredients_output.append(head)
        ingredient_lines = t.find_all('li', class_='ingredient-line')
        # insert all ingredients
        for line in ingredient_lines:
            ingredient_amount = line.find('span', class_='amount').string
            ingredient_name = line.find('span', class_='name').string
            full_ingredient = ingredient_amount + " " + ingredient_name
            ingredients_output.append(full_ingredient)
            # recipe ingrediant
    return ingredients_output


def get_recipe(soup_for_recipe):
    instructions_output = []
    recipe_section = soup_for_recipe.find_all('div', class_='way-to-cook')
    for r in recipe_section:
        instructions_lines = r.find_all('div', class_='text')
        for line in instructions_lines:
            span = line.find_all('span')
            instruction = span[1].contents
            if len(instruction) > 1:
                instruction = instruction[1]
            else:
                instruction = instruction[0]
                instructions_output.append(instruction)
    return instructions_output


def extract_all_recipe_data(url):
    soup = getSoupFromUrl(url)
    name = get_name(soup)
    ingredients = get_ingredient(soup)
    instructions = get_recipe(soup)
    recipe_walla_id = get_new_recipe_id()
    extractIngredientTags(ingredients, recipe_walla_id)
    print_progress(recipe_walla_id,'Walla')
    return {"id": recipe_walla_id, "name": name, "url": url, "ingredients": ingredients, "instructions": instructions}


def walla_main_page():
    all_recipes = []
    categories_url = find_main_page_categories_url(food_walla_url)
    r_url = find_recipes_url_in_category_page(categories_url)

    for url in r_url:
        try:
            recipe = extract_all_recipe_data(url)
            all_recipes.append(recipe)
        except:
            pass
    print("\nWalla :Done")
    return all_recipes

