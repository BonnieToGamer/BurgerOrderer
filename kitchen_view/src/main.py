from flask import Flask, request
from typing import TypedDict
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

# why is this just not in the language?
class Order(TypedDict):
    burger: str
    specials: list [str]


def print_order(order: Order):
    print("Ny beställning:")
    print("-" * 30)
    print(f"{'Typ av Burger:':<20} {order['burger'].capitalize()}")
    print(f"{'Särskilda önskemål:':<20} {', '.join(order['specials']).capitalize() if order['specials'] else 'Inga särskilda önskemål.'}")
    print("-" * 30 + "\n")

@app.route("/newOrder", methods=["POST"])
def handle_new_order():
    try:
        order = request.get_json(force=True)["order"]
        order = Order(order)
    except:
        return "error", 400

    print_order(order)
    return "success", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
