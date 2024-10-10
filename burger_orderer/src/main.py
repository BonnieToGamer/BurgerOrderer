from flask import Flask, jsonify, request
import json
import pymongo
import os

MONGODB_URL = os.getenv("MONGODB_URL")
mongo_client = pymongo.MongoClient(MONGODB_URL)

burger_db = mongo_client["burger_db"]

burger_collection = burger_db["burgers"]

app = Flask(__name__)

def burger_exists(burger_name):
    return burger_collection.count_documents({ 'name': burger_name }, limit = 1) != 0

with open("./hamburgers.json", encoding="utf-8") as json_file:
    parsed_json = json.load(json_file)

for burger_name, burger_details in parsed_json.items():
    burger = {
        "name": burger_name,
        "specials": burger_details["Specials"]
    }

    if not burger_exists(burger_name):
        burger_collection.insert_one(burger)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def test():
    return "world"

@app.route("/api/getBurgers")
def get_burgers():
    burgers = []
    for burger in burger_collection.find():
        burgers.append(burger["name"])
    return jsonify(burgers)

@app.route("/api/getSpecials")
def get_specials():
    burger_name = request.args.get("burger", default = "", type = str)
    
    if burger_exists(burger_name):
        for burger in burger_collection.find({"name": burger_name}, limit = 1):
            return jsonify(burger["specials"])
    else:
        return jsonify({"error": "burger not found"})

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)