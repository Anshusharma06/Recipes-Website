#!/usr/bin/env python
# coding: utf-8

# In[12]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from functools import reduce
from datetime import datetime
from urllib.error import HTTPError


max_pages = 1
ingredients_set = {' אבוקדו', ' אבטיח', 'אגוזי לוז', 'אגוזים', ' אוכמניות', ' אוראו', 'אורז'
       , ' אטריות', ' אטריות אורז', 'ארטישוק', ' בזיליקום', ' בננה', ' בצל', ' בצל ירוק'
       , ' בצק סוכר', ' בצק עלים', ' בצק פריך', ' בצקניות', ' ברוקולי', 'בשר', " ג'לי"
       , 'גבינה', ' גבינה בולגרית', ' גבינה טבעונית', ' גבינה צהובה', ' גבינת שמנת', ' גזר'
       , ' גרנולה', ' דבש', ' דגים', ' דובדבנים', ' דלורית', ' דלעת', ' דלעת ערמונים'
       , ' דפי אורז', ' וופל', ' וניל', ' זיתים', ' חומוס', ' חלב מרוכז', ' חלב סויה'
       , 'חלבה', ' חמוציות', ' חסה', ' חציל', ' טונה', ' טופו', ' טורטיה', ' טורטליני'
       , 'טחינה', ' טפיוקה', ' טריאקי', ' יוגורט', ' יין לבן', ' ירקות', ' כרוב', ' כרובית'
       , ' כרישה', ' לוטוס', ' לימון', ' מוצרלה', 'מייפל', ' מיץ תפוזים', ' מלון', ' מנגו'
       , ' מנגולד', ' מסקרפונה', ' מצה', ' מרנג', ' מרציפן', ' מרשמלו', ' משמש', ' נוגט'
       , ' נודלס', ' נוטלה', ' ניוקי', ' סויה', ' סוכר חום', 'סילאן', ' סלמון', ' סלק'
       , ' עגבניות', ' עדשים', ' עוף', ' עלי לזניה', ' ענבים', ' ערמונים', ' עשבי תיבול'
       , ' פודינג', ' פטרוזיליה', ' פטריות', ' פטריות מיובשות', ' פיטאיה', ' פירורי לחם'
       , ' פירות', ' פירות יער', ' פיתה', ' פלפלים', ' פסטה', ' פסטו', ' פסיפלורה', ' פפריקה'
       , ' פקאנים', ' פרג', ' פרגית', ' פרמזן', ' פתי בר', ' פתיתים', ' צימוקים', ' צנוברים', ' קדאיף'
       , ' קוואקר', ' קולורבי', ' קוסקוס', ' קוקוס', ' קטשופ', ' קינמון', ' קישואים', ' קישוט עוגות'
       , ' קמח חומוס', ' קמח ללא גלוטן', ' קמח מלא', ' קמח מצה', ' קפה', ' קצפת', ' קקאו'
       , ' קרם פטיסייר', ' קרמל', ' קרקרים', ' קשיו', ' רביולי', ' רוטב עגבניות', ' ריבה'
       , ' ריבת חלב', ' ריקוטה', ' רסק עגבניות', ' שום', ' שומשום', ' שוקולד'
       , ' שוקולד לבן', " שוקולד צ'יפס", ' שמיר', ' שמנת לבישול', ' שמנת מתוקה'
       , ' שמרים', ' שעועית ירוקה', ' שקדים', ' תותים', ' תירס', ' תמרים'
       , ' תפוזים', ' תפוזים סינים', ' תפוחי אדמה', ' תפוחי עץ', ' תרד'}


def setIngrediensTagsIds():
    tag_id=0
    ingrediens_tags_ids = {}
    for tag in ingredients_set:
        ingrediens_tags_ids[tag] = tag_id
        tag_id= tag_id+1
    return ingrediens_tags_ids


ingrediens_tags_ids = setIngrediensTagsIds()
tags_to_recipes={}
ids=[]
for word in ingrediens_tags_ids:
    ids.append(ingrediens_tags_ids[word])

ids = list(set(ids))
for id in ids:
    tags_to_recipes[id] = set()

def extractIngredientTags(ingredients,recipe_id):
    for ingredient in ingredients:
        words = ingredient.split()
        for word in words:
            if word in ingredients_set:
                tag_id = ingrediens_tags_ids[word]
                tags_to_recipes[tag_id].add(recipe_id)

def getSoupFromUrl(url):
    req = Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urlopen( req )
    html = con.read()
    return BeautifulSoup(html,features="lxml")

# recipes url
all_recipes_types_urls = ['https://www.sugat.com/recipes_cat/rice/']



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

recipe_id = 0

def getRecipeData(recipe_url):
    so = getSoupFromUrl(recipe_url)
    ingredients = getIngredientsFromHtmlSoup(so)
    recipe = getRecipeFromHtmlSoup(so)
    ingredientTags = extractIngredientTags(ingredients,recipe_id)
    return (ingredients,recipe)
    
    


def getAllUrlsFromFirstRecipePage(url,page_number=1):
    getPostfixByIndex = lambda i: 'page/'+str(i)+'/'
    if max_pages < page_number:
        return []
    try:
        so = getSoupFromUrl(url +getPostfixByIndex(page_number))
        print(page_number)
    except HTTPError as err:
        print(err)
        return []
    recipes_in_page = so.find_all("div", class_ = "s-recipe-category__col")
    if recipes_in_page is None:
        print(str(page_number)+ 'is not exist')
        return []
    page_links = list(map(lambda div: div.find(href=True).get('href') ,recipes_in_page ))
    return page_links + getAllUrlsFromFirstRecipePage(url,page_number+1)
        
        
for recipe_type_url in all_recipes_types_urls:
    recipe_id = recipe_id +1
    recipes_urls = getAllUrlsFromFirstRecipePage(recipe_type_url)
    recipe_and_ingrediant = list(map(getRecipeData,recipes_urls))
    for x in recipe_and_ingrediant:
        print(x)
        print('\n')





