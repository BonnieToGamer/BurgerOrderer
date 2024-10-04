from flask import Flask, jsonify, request

import json

app = Flask(__name__)

with open("./hamburgers.json", encoding="utf-8") as json_file:
    parsed_json = json.load(json_file)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def test():
    return "world"

@app.route("/api/getBurgers")
def get_burgers():
    burgers = []
    for burger in parsed_json.keys():
        burgers.append(burger)
    return jsonify(burgers)

@app.route("/api/getSpecials")
def get_specials():
    burger_name = request.args.get("burger", default = "", type = str)

    print(burger_name)

    if burger_name in parsed_json:
        return jsonify(parsed_json[burger_name])
    else:
        return jsonify({"error": "burger not found"})

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)