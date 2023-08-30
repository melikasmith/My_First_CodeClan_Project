from db.run_sql import run_sql


from models.country import Country
from models.city import City
# import repositories.destination_repository as destination_repository

def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    #if len(results > 0):
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        # destiantion = destination_repository.select(row['user_id'])
        country = Country(row['name'], row['id'])
        countries.append(country)
    return countries



def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        # destination = destination_repository.select(result['destination_id'])
        country = Country(result['name'], result['id'])
        return country
    
def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name) = (%s) WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)