from flask import Flask, request
from typing import TypedDict
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)


class Order(TypedDict):
    burger: str
    specials: list[str]


def print_order(order: Order):
    """
    Recieves the order and prints it to the terminal.
    
    :param order: An instance of the Order class. It contains the details of the order, the burger type and any special requests

    The function prints the burger type and special requests in a user-friendly format.
    """
    
    print("New order::")
    print("-" * 30)
    print(f"{'Type of burger:':<20} {order['burger'].capitalize()}")
    print(f"{'Special requests:':<20} {', '.join(order['specials']).capitalize() if order['specials'] else 'Inga särskilda önskemål.'}")
    print("-" * 30 + "\n")

@app.route("/newOrder", methods=["POST"])
def handle_new_order():
    """
    Handles a new order request.
    
    :return: returns a response which indicates success or error.
    
    It takes the order data from the POST request and creates an instance of the Order class. 
    If any issues occur during processing of the data, it returns an error with the status code 400.
    If the order process was successful, it prints the order details with print_order(order) and returns a success message with status code 200.
    """
    try:
        order = request.get_json(force=True)["order"]
        order = Order(order)

    except:
        return "error", 400

    if  "burger" not in order or \
        "specials" not in order or \
        not isinstance(order["burger"], str) or \
        not isinstance(order["specials"], list) or \
        order["burger"] == "":
        return "error", 400

    for special in order["specials"]:
        if not isinstance(special, str):
            return "error", 400

    print_order(order)
    return "success", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
