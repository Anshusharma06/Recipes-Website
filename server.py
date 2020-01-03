
from flask import Flask,jsonify,request
#!/usr/bin/env python
# -*- coding: utf-8 -*-

app = Flask(__name__)


def getRecipes(ingredients):
    recipe = {}
    recipe['url'] = 'http://www.gogle.com/'
    recipe['ingredients'] = ingredients
    recipe['instructions'] = ['לוקחים את הבשר', 'מערבבים עם חציל ולתנור']
    return [recipe,recipe]


@app.route('/', methods=['GET', 'POST'])
def home():
    data_array = request.get_data().decode('UTF-8')
    recipes = getRecipes(data_array)
    response = jsonify(recipes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)








