from DataAcsess import tags_to_recipes, all_recipes_data
from LoadToCSV import save_into_csv
from LoadFromCSV import upload_recipes_from_csv

recipe_id = [0,1,2]
names = ['hadas', 'atiya', 'hello']
url =['aaa', 'bbbb', 'ccc']
tags = ['A', 'B', 'C', 'D']
ingredients = [['A', 'G', 'B'], ['A', 'B', 'C', 'R'], ['B', 'C', 'Q']]
instructions = [['aaa','aaa'],['bbbb','bbbb'],['cccc','cccc']]
data =[]

A = {"id":1, "recipe_list":[1,2]}
B = {"id":2, "recipe_list":[1,2,3]}
C = {"id":3, "recipe_list":[2,3]}
tags_to_recipes = [A, B, C]

for id in recipe_id:
    data.append({"id": id, "name": names[id], "url": url[id], "tags": tags[id],"ingredients": ingredients[id], "instructions": instructions[id]})

save_into_csv(data, tags_to_recipes)


upload_recipes_from_csv()

print(tags_to_recipes)
print('=' * 80)
print(all_recipes_data)

