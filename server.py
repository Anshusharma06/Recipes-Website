
from flask import Flask,jsonify,request
from service import getRecipes, getNumberOfRecipes,Init
import json
import webbrowser
from MainLoad import ScrapDataAndSaveToCsv
import sys
from LoadFromCSV import upload_recipes_from_csv
import os

debugMode= False
args = sys.argv
if len(args)>1 and args[1].lower()=='download':
    ScrapDataAndSaveToCsv()

app = Flask(__name__)

@app.route('/recipes', methods=['GET', 'POST'])
def home():
    request_json = request.get_data().decode('UTF-8')
    data = json.loads(request_json)
    recipes = getRecipes(data)
    response = jsonify(recipes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/resultsnumber', methods=['GET'])
def number():
    response = jsonify(getNumberOfRecipes())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

print("Initialize Data... please wait")
Init()
print("Done. enjoy")
webbrowser.open('file://' + os.getcwd()+'/index.html', new=2)

if __name__ == "__main__":
    app.run(debug=debugMode)










