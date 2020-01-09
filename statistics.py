from LoadFromCSV import upload_recipes_from_csv
from DataAcsess import tags_to_recipes, ingredients_list, all_recipes_data, extractIngredientTags, getTagIdFromTagName, csv_converted_tags_recipes
from LoadToCSV import save_general_csv,the_tags_url

upload_recipes_from_csv()

tags_size = {k: len(v) for k, v in tags_to_recipes.items()}
sorted_tags_size_revers = {k: v for k, v in sorted(tags_size.items(), key=lambda item: item[1], reverse=True)}

for recip in all_recipes_data:
    extractIngredientTags(all_recipes_data[recip]['ingredients'], recip)

tags_list = csv_converted_tags_recipes()
print(tags_list)

save_general_csv(the_tags_url, tags_list, 'recipe_list', None)

tags_size = {k: len(v) for k, v in tags_to_recipes.items()}
sorted_tags_size_revers = {k: v for k, v in sorted(tags_size.items(), key=lambda item: item[1], reverse=True)}

print(sum(tags_size.values()))
max_ingredient_to_show = 10

counter = 1
print("top 10 ingredient")
for tag in sorted_tags_size_revers:
    print( sorted_tags_size_revers[tag], " - ", ingredients_list[tag], " .", counter)
    if max_ingredient_to_show == counter:
        break
    counter = counter + 1


sorted_tags_size = {k: v for k, v in sorted(tags_size.items(), key=lambda item: item[1])}

counter = 1
print("zero tags ingredient")
for tag in sorted_tags_size:
    if sorted_tags_size[tag] > 0:
        break
    print(sorted_tags_size[tag], " - ", ingredients_list[tag], " .", counter)
    counter = counter + 1
