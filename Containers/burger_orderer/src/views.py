<<<<<<< Updated upstream:Containers/burger_orderer/src/views.py
from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("Ui-design.html")

@views.route("/order")
def order():
=======
from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    """
    A function that returns the name of the home template, which is then used to render the homepage.
    """
    return render_template("Ui-design.html")

@views.route("/order")
def order():
    """
    A function that returns the name of the order template, which is then used to render the order page.
    """
>>>>>>> Stashed changes:burger_orderer/src/views.py
    return render_template("order.html")