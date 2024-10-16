from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("Ui-design.html")

@views.route("/order")
def order():
    return render_template("order.html")