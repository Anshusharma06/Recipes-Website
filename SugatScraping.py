
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from functools import reduce
from datetime import datetime
from urllib.error import HTTPError
from DataAcsess import extractIngredientTags, get_new_recipe_id,print_progress



max_pages = 30



def getSoupFromUrl(url):
    req = Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urlopen( req )
    html = con.read()
    return BeautifulSoup(html,features="lxml")

# recipes url
all_recipes_types_urls = ['https://www.sugat.com/recipes_cat/rice/','https://www.sugat.com/recipes_cat/meat/','https://www.sugat.com/recipes_cat/fish/','https://www.sugat.com/recipes_cat/side-dish/','https://www.sugat.com/recipes_cat/salad/','https://www.sugat.com/recipes_cat/stuffed/','https://www.sugat.com/recipes_cat/bread-and-pastry/','https://www.sugat.com/recipes_cat/soup/','https://www.sugat.com/recipes_cat/dessert/','https://www.sugat.com/recipes_cat/casserole/','https://www.sugat.com/recipes_cat/healthy/','https://www.sugat.com/recipes_cat/vegetarian/','https://www.sugat.com/recipes_cat/vegan/','https://www.sugat.com/recipes_cat/cakes-and-cookies/','https://www.sugat.com/recipes_cat/kids/','https://www.sugat.com/recipes_cat/pasta/','https://www.sugat.com/holidays']

def filterIngredientUnwantedWords(x):
    return x != '\n' and x !='קרא עוד' and x!='\xa0'

def getIngredientsFromHtmlSoup(so):
    div = so.find("div", class_ = "b-contain")
    all_li = div.find_all('li')
    Ingredients = list(map(lambda li : list(set(filter(filterIngredientUnwantedWords,li.find_all(text=True)))),all_li))
    return list(reduce(lambda lst1,lst2: lst1+ lst2,Ingredients))


def getRecipeFromHtmlSoup(so):
    ol =so.find("ol", class_ = "l-steps__ul")
    recipe = ol.find_all(text=True)
    return list(filter(filterIngredientUnwantedWords,recipe))

def getRecipeNameFromSoup(so):
    h1 =so.find("h1").find(text=True)
    return h1

def getRecipeData(recipe_url):
    try:
        so = getSoupFromUrl(recipe_url)
        ingredients = getIngredientsFromHtmlSoup(so)
        instructions = getRecipeFromHtmlSoup(so)
        name = getRecipeNameFromSoup(so)
        recipe_id = get_new_recipe_id()
        extractIngredientTags(ingredients,recipe_id)
        print_progress(recipe_id,'Sugat')
        return {'id': recipe_id, 'name': name, 'url': recipe_url,'instructions': instructions, 'ingredients' : ingredients }
    except:
       pass


def getAllUrlsFromFirstRecipePage(url,page_number=1):
    getPostfixByIndex = lambda i: 'page/'+str(i)+'/'
    if max_pages < page_number:
        return []
    try:
        so = getSoupFromUrl(url +getPostfixByIndex(page_number))
    except HTTPError as err:
        return []
    recipes_in_page = so.find_all("div", class_ = "s-recipe-category__col")
    if recipes_in_page is None:
        print(str(page_number)+ 'is not exist')
        return []
    page_links = list(map(lambda div: div.find(href=True).get('href') ,recipes_in_page ))
    return page_links + getAllUrlsFromFirstRecipePage(url,page_number+1)
        

def scrapRecipes():
    recipes=[]
    for recipe_type_url in all_recipes_types_urls:
        try:
            recipes_urls = getAllUrlsFromFirstRecipePage(recipe_type_url)
            print("gots urls")
            recipes = recipes +  list(map(getRecipeData,recipes_urls))
        except:
            pass
    print("done scrapping from sugat")
    return recipes



