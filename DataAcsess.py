
recipe_counter = 0
# recipes data
# {"id": int, "name": str, "url": str, "tags": list, "ingredients": list<str>, "instructions": list<str>}
all_recipes_data = {}
# id for all tags
# [tag]=id
tag_name_to_id = {}
# list of relevant recipes for each tag
# [id] = relevant recipes list (=[1,2,3])
tags_to_recipes = {}
# ingrediant tags possible
ingredients_set = {'אבוקדו', 'אבטיח', 'אגוזי לוז', 'אגוזים', 'אוכמניות', 'אוראו', 'אורז'
       , 'אטריות', 'אטריות אורז', 'ארטישוק', 'בזיליקום', 'בננה', 'בצל', 'בצל ירוק'
       , 'בצק סוכר', 'בצק עלים', 'בצק פריך', 'בצקניות', 'ברוקולי', 'בשר', "ג'לי"
       , 'גבינה', 'גבינה בולגרית', 'גבינה טבעונית', 'גבינה צהובה', 'גבינת שמנת', 'גזר'
       , 'גרנולה', 'דבש', 'דגים', 'דובדבנים', 'דלורית', 'דלעת', 'דלעת ערמונים'
       , 'דפי אורז', 'וופל', 'וניל', 'זיתים', 'חומוס', 'חלב מרוכז', 'חלב סויה'
       , 'חלבה', 'חמוציות', 'חסה', 'חציל', 'טונה', 'טופו', 'טורטיה', 'טורטליני'
       , 'טחינה', 'טפיוקה', 'טריאקי', 'יוגורט', 'יין לבן', 'ירקות', 'כרוב', 'כרובית'
       , 'כרישה', 'לוטוס', 'לימון', 'מוצרלה', 'מייפל', 'מיץ תפוזים', 'מלון', 'מנגו'
       , 'מנגולד', 'מסקרפונה', 'מצה', 'מרנג', 'מרציפן', 'מרשמלו', 'משמש', 'נוגט'
       , 'נודלס', 'נוטלה', 'ניוקי', 'סויה', 'סוכר חום', 'סילאן', 'סלמון', 'סלק'
       , 'עגבניות', 'עדשים', 'עוף', 'עלי לזניה', 'ענבים', 'ערמונים', 'עשבי תיבול'
       , 'פודינג', 'פטרוזיליה', 'פטריות', 'פטריות מיובשות', 'פיטאיה', 'פירורי לחם'
       , 'פירות', 'פירות יער', 'פיתה', 'פלפלים', 'פסטה', 'פסטו', 'פסיפלורה', 'פפריקה'
       , 'פקאנים', 'פרג', 'פרגית', 'פרמזן', 'פתי בר', 'פתיתים', 'צימוקים', 'צנוברים', 'קדאיף'
       , 'קוואקר', 'קולורבי', 'קוסקוס', 'קוקוס', 'קטשופ', 'קינמון', 'קישואים', 'קישוט עוגות'
       , 'קמח חומוס', 'קמח ללא גלוטן', 'קמח מלא', 'קמח מצה', 'קפה', 'קצפת', 'קקאו'
       , 'קרם פטיסייר', 'קרמל', 'קרקרים', 'קשיו', 'רביולי', 'רוטב עגבניות', 'ריבה'
       , 'ריבת חלב', 'ריקוטה', 'רסק עגבניות', 'שום', 'שומשום', 'שוקולד'
       , 'שוקולד לבן', "שוקולד צ'יפס", 'שמיר', 'שמנת לבישול', 'שמנת מתוקה'
       , 'שמרים', 'שעועית ירוקה', 'שקדים', 'תותים', 'תירס', 'תמרים'
       , 'תפוזים', 'תפוזים סינים', 'תפוחי אדמה', 'תפוחי עץ', 'תרד'}

ingredients_variants_set ={}
ingredients_variants_set['עגבניה'] = 'עגבניות'
ingredients_variants_set['אוכמניה'] = 'אוכמניות'
ingredients_variants_set['אגוז'] = 'אגוזים'
ingredients_variants_set['אבטיחים'] = 'אבטיח'
ingredients_variants_set['אבוקדואים'] = 'אבוקדו'
ingredients_variants_set['בצלים'] = 'בצל'
ingredients_variants_set['בננות'] = 'בננה'
ingredients_variants_set['בשרים'] = 'בשר'
ingredients_variants_set['ברוקולים'] = 'ברוקולי'
ingredients_variants_set['גזרים'] = 'גזר'
ingredients_variants_set['גבינות'] = 'גבינה'
ingredients_variants_set['דובדבן'] = 'דובדבנים'
ingredients_variants_set['דג'] = 'דגים'
ingredients_variants_set['וופלות'] = 'וופל'
ingredients_variants_set['חצילים'] = 'חציל'
ingredients_variants_set['חסות'] = 'חסה'
ingredients_variants_set['כרובים'] = 'כרוב'
ingredients_variants_set['ירק'] = 'ירקות'
ingredients_variants_set['יוגורטים'] = 'יוגורט'
ingredients_variants_set['מנגוים'] = 'מנגו'
ingredients_variants_set['מלונים'] = 'מלון'
ingredients_variants_set['לימונים'] = 'לימון'
ingredients_variants_set['כרישות'] = 'כרישה'
ingredients_variants_set['משמשים'] = 'משמש'
ingredients_variants_set['מרציפנים'] = 'מרציפן'
ingredients_variants_set['מצות'] = 'מצה'
ingredients_variants_set['עופות'] = 'עוף'
ingredients_variants_set['פטריה'] = 'פטריות'
ingredients_variants_set['פסטות'] = 'פסטה'
ingredients_variants_set['פלפל'] = 'פלפלים'
ingredients_variants_set['פיתות'] = 'פיתה'
ingredients_variants_set['פרי'] = 'פירות'
ingredients_variants_set['פרגיות'] = 'פרגית'
ingredients_variants_set['קישוא'] = 'קישואים'
ingredients_variants_set['ריבות'] = 'ריבה'
ingredients_variants_set['קרקר'] = 'קרקרים'
ingredients_variants_set['שוקולדים'] = 'שוקולד'
ingredients_variants_set['תמר'] = 'תמרים'
ingredients_variants_set['תות'] = 'תותים'
ingredients_variants_set['תפוז'] = 'תפוזים'



ingredients_list = ['אבוקדו', 'אבטיח', 'אגוזי לוז', 'אגוזים', 'אוכמניות', 'אוראו', 'אורז'
       , 'אטריות', 'אטריות אורז', 'ארטישוק', 'בזיליקום', 'בננה', 'בצל', 'בצל ירוק'
       , 'בצק סוכר', 'בצק עלים', 'בצק פריך', 'בצקניות', 'ברוקולי', 'בשר', "ג'לי"
       , 'גבינה', 'גבינה בולגרית', 'גבינה טבעונית', 'גבינה צהובה', 'גבינת שמנת', 'גזר'
       , 'גרנולה', 'דבש', 'דגים', 'דובדבנים', 'דלורית', 'דלעת', 'דלעת ערמונים'
       , 'דפי אורז', 'וופל', 'וניל', 'זיתים', 'חומוס', 'חלב מרוכז', 'חלב סויה'
       , 'חלבה', 'חמוציות', 'חסה', 'חציל', 'טונה', 'טופו', 'טורטיה', 'טורטליני'
       , 'טחינה', 'טפיוקה', 'טריאקי', 'יוגורט', 'יין לבן', 'ירקות', 'כרוב', 'כרובית'
       , 'כרישה', 'לוטוס', 'לימון', 'מוצרלה', 'מייפל', 'מיץ תפוזים', 'מלון', 'מנגו'
       , 'מנגולד', 'מסקרפונה', 'מצה', 'מרנג', 'מרציפן', 'מרשמלו', 'משמש', 'נוגט'
       , 'נודלס', 'נוטלה', 'ניוקי', 'סויה', 'סוכר חום', 'סילאן', 'סלמון', 'סלק'
       , 'עגבניות', 'עדשים', 'עוף', 'עלי לזניה', 'ענבים', 'ערמונים', 'עשבי תיבול'
       , 'פודינג', 'פטרוזיליה', 'פטריות', 'פטריות מיובשות', 'פיטאיה', 'פירורי לחם'
       , 'פירות', 'פירות יער', 'פיתה', 'פלפלים', 'פסטה', 'פסטו', 'פסיפלורה', 'פפריקה'
       , 'פקאנים', 'פרג', 'פרגית', 'פרמזן', 'פתי בר', 'פתיתים', 'צימוקים', 'צנוברים', 'קדאיף'
       , 'קוואקר', 'קולורבי', 'קוסקוס', 'קוקוס', 'קטשופ', 'קינמון', 'קישואים', 'קישוט עוגות'
       , 'קמח חומוס', 'קמח ללא גלוטן', 'קמח מלא', 'קמח מצה', 'קפה', 'קצפת', 'קקאו'
       , 'קרם פטיסייר', 'קרמל', 'קרקרים', 'קשיו', 'רביולי', 'רוטב עגבניות', 'ריבה'
       , 'ריבת חלב', 'ריקוטה', 'רסק עגבניות', 'שום', 'שומשום', 'שוקולד'
       , 'שוקולד לבן', "שוקולד צ'יפס", 'שמיר', 'שמנת לבישול', 'שמנת מתוקה'
       , 'שמרים', 'שעועית ירוקה', 'שקדים', 'תותים', 'תירס', 'תמרים'
       , 'תפוזים', 'תפוזים סינים', 'תפוחי אדמה', 'תפוחי עץ', 'תרד']

# initial ingrediens_tags_ids
def setIngrediensTagsIds():
    tag_id = 0
    for tag in ingredients_list:
        tag_name_to_id[tag] = tag_id
        tag_id = tag_id+1

def initialTags():
    setIngrediensTagsIds()
    ids = []
    for word in tag_name_to_id:
        ids.append(tag_name_to_id[word])

    ids = list(set(ids))
    for id in ids:
        tags_to_recipes[id] = set()





def extractIngredientTags(ingredients, recipe_id):
    for ingredient in ingredients:
        words = ingredient.split()
        for word in words:
            if word in ingredients_set or word in ingredients_variants_set:
                tag_id = getTagIdFromTagName(word)
                tags_to_recipes[tag_id].add(recipe_id)

def getTagIdFromTagName(name):
    return tag_name_to_id[ingredients_variants_set[name]] if name in ingredients_variants_set else tag_name_to_id[name]


def get_new_recipe_id():
    global recipe_counter
    recipe_counter = recipe_counter + 1
    return recipe_counter


def csv_converted_tags_recipes():
    output_list = []
    for singl_tag in ingredients_list:
        tag_id = getTagIdFromTagName(singl_tag)
        recipes_per_tsg = list(tags_to_recipes[tag_id])
        output_list.append({"id":tag_id, "recipe_list": recipes_per_tsg})
    return output_list


def print_progress(id,site_name):
    if id%20==0:
        print(str(id)+ " recipes have scrapped - " + site_name)
