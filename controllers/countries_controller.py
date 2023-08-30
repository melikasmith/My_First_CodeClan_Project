from flask import Flask, render_template, request
from flask import Blueprint
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_cities_by_country(country)
    # print(country)
    # for city in cities:
    #     print(city)
    return render_template('countries/show.html', country = country, cities = cities)

@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def add_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template('countries/edit.html', country = country, all_cities = cities)