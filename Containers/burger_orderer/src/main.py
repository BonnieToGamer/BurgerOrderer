from flask import Flask, jsonify, request
import json
import pymongo
import os
import requests
from views import views


MONGODB_URL = os.getenv("MONGODB_URL")
KITCHEN_URL = os.getenv("KITCHEN_URL")

mongo_client = pymongo.MongoClient(MONGODB_URL)

burger_db = mongo_client["burger_db"]

burger_collection = burger_db["burgers"]

app = Flask(__name__)

def burger_exists(burger_name):
    """
    Gets the name of a burger and checks if it exists in the database.

    Parameters:
        burger_name: The name of a burger.

    Returns: A boolean that tells us whether or not the burger exists.
    """
    return burger_collection.count_documents({ 'name': burger_name }, limit = 1) != 0

with open("./hamburgers.json", encoding="utf-8") as json_file:
    parsed_json = json.load(json_file)

for burger_name, burger_details in parsed_json.items():
    burger = {
        "name": burger_name,
        "price": burger_details["Price"],
        "specials": burger_details["Specials"]
    }

    if not burger_exists(burger_name):
        burger_collection.insert_one(burger)

@app.route("/api/getBurgers")
def get_burgers():
    """
    Creates a list of all the available burgers and their corresponding prices. 

    Returns: The list of all the available burgers and their corresponding prices in json.
    """
    burgers = []
    for burger in burger_collection.find():
        burgers.append({"name": burger["name"], "price": burger["price"]})
    return jsonify(burgers)

@app.route("/api/getSpecials")
def get_specials():
    """
    Calls the burger_exists function to check if a specific burger exists.

    Returns: 
        If the burger exists: All the available specials for the burger
        If the burger doesn't exist: An error message saying the burger doesn't exist.
    """
    burger_name = request.args.get("burger", default = "", type = str)
    
    if burger_exists(burger_name):
        for burger in burger_collection.find({"name": burger_name}, limit = 1):
            return jsonify(burger["specials"])
    else:
        return jsonify({"error": "burger not found"}), 400

@app.route("/api/newOrder", methods=["POST"])
def new_order():
    """
    Sends a confirmed order to the kitchen. 
    
    Returns:
        If the order gets sent and received correctly: A text response in json and a status code.
        If the order doesn't get sent and received correctly: An error message saying what went wrong.
    """
    
    if request.is_json == False:
        return jsonify({'error': 'Failed to send request to kitchen', 'details': "No json data provided"}), 400
    
    order_data = request.get_json()

    target_url = KITCHEN_URL + 'newOrder'
    print(order_data)
    print(target_url)
    try:
        response = requests.post(target_url, json=order_data)
        return jsonify({"response": response.text}), response.status_code
    
    except requests.exceptions.RequestException as e:
        print("there was an error")
        return jsonify({'error': 'Failed to send request to kitchen', 'details': str(e)}), 500

if __name__ == "__main__":
    app.register_blueprint(views, url_prefix="/")
    app.run("0.0.0.0", port=8080)