from flask import Flask, render_template, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities/<id>")
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)

@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities/<id>')

@cities_blueprint.route("/cities/<id>/visited")
def visited_city(id):
    city = city_repository.select(id)
    city.visited = True
    city_repository.update(city)
    return redirect('/cities/'+ id)

@cities_blueprint.route("/cities/<id>/want_to_visit")
def want_to_visit_city(id):
    city = city_repository.select(id)
    city.want_to_visit = True
    city_repository.update(city)
    return redirect('/cities/'+ id)