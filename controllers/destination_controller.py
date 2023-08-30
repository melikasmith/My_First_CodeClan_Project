
from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from models.destination import Destination
# import repositories.destination_repository as destination_repository
# import repositories.user_repository as user_repository

# destinations_blueprint = Blueprint("destinations", __name__)

# @destinations_blueprint.route("/index.html")
# def log_in():
#     # country = request.form['country']
#     # city = request.form['city']
#     # visited = request.form['visited']
#     # user_id = request.form['user_id']
#     # user = user_repository.select(user_id)
#     # destination = Destination(country, city, visited, user_id)
#     # destination_repository.save(destination)
#     return render_template("/index.html")

# @destinations_blueprint.route("/")
# def home_page():
#     return "hello"

# @destinations_blueprint.route("/index", methods=['GET'])
# def log_in():
#     users = user_repository.select_all()
#     return render_template("index.html", all_users = users)

# @destinations_blueprint.route("/destinations")
# def destinations():
#     destinations = destination_repository.select_all()
#     return render_template("destinations/destinations.html", all_destinations = destinations)

# @destinations_blueprint.route("/destinations")
# def destinations():
#     destinations = destination_repository.select_all()
#     return render_template("destinations/index.html", all_destinations = destinations)