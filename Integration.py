
recipe_counter = 0
# id for all tags
ingrediens_tags_ids = {}
# list of relevent recipes for each tag
tags_to_recipes = {}
# ingrediant tags possible
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

# initial ingrediens_tags_ids
def setIngrediensTagsIds():
    tag_id = 0
    for tag in ingredients_set:
        ingrediens_tags_ids[tag] = tag_id
        tag_id = tag_id+1


setIngrediensTagsIds()

ids = []
for word in ingrediens_tags_ids:
    ids.append(ingrediens_tags_ids[word])

ids = list(set(ids))
for id in ids:
    tags_to_recipes[id] = set()


def extractIngredientTags(ingredients, recipe_id):
    tags = []
    for ingredient in ingredients:
        words = ingredient.split()
        for word in words:
            if word in ingredients_set:
                tag_id = ingrediens_tags_ids[word]
                tags_to_recipes[tag_id].add(recipe_id)
                tags.append(word)
    return tags


def get_new_recipe_id():
    global recipe_counter
    recipe_counter = recipe_counter + 1
    return recipe_counter


def cav_converted_tags_recipes():
    output_list = []
    for singl_tag in ingredients_set:
        tag_id = ingrediens_tags_ids[singl_tag]
        recipes_per_tsg = tags_to_recipes[tag_id]
        output_list.append({"id":tag_id, "recipe_list": recipes_per_tsg})
    return output_list




# def add_to_tags_list(tags, recipe_id):
#     for t in tags:
#         all_tags[t] = all_tags[t].append(recipe_id)

