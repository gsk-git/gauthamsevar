from flask import Blueprint

views = Blueprint(__name__,"views")

@views.route("/")
def prof():
    return "This is client's page"