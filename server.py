
from flask import Flask,jsonify,request
from service import getRecipes
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    request_json = request.get_data().decode('UTF-8')
    data = json.loads(request_json)
    recipes = getRecipes(data)
    response = jsonify(recipes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)








