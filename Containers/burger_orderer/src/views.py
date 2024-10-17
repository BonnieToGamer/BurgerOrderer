from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    """
    Gets the name of the home template, which is then used to render the homepage.
    
    Returns: The name of the home template
    """
    return render_template("Ui-design.html")

@views.route("/order")
def order():
    """
    Gets the name of the order template, which is then used to render the order page.

    Returns: the name of the order template
    """
    return render_template("order.html")