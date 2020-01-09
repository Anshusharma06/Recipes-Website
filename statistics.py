from LoadFromCSV import upload_recipes_from_csv,the_tags_url
from DataAcsess import tags_to_recipes, ingredients_list, getTagIdFromTagName,update_tags, csv_converted_tags_recipes, all_recipes_data
from LoadToCSV import save_general_csv
import csv

upload_recipes_from_csv()


tags_size = {k: len(v) for k, v in tags_to_recipes.items()}
sorted_tags_size_revers = {k: v for k, v in sorted(tags_size.items(), key=lambda item: item[1], reverse=True)}

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


# recepies with avocado
id = getTagIdFromTagName('אבוקדו')
print("avocado been tag to :", sorted_tags_size[id], 'number of recipes')



# this make a csv file that contain how much recipes each tags has
# with open('statistics.csv', 'w') as csvfile:
#     fieldnames = ['ingredient', 'amount']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for ing in sorted_tags_size_revers:
#         writer.writerow({'ingredient': ingredients_list[ing], 'amount': sorted_tags_size_revers[ing]})


