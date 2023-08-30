# from db.run_sql import run_sql

# from models.user import User
# from models.destination import Destination
# import repositories.country_repository as country_repository

# def save(destination):
#     sql = "INSERT INTO destinations (country, user_id) VALUES (%s, %s) RETURNING *"
#     values = [destination.country, destination.country.id]
#     results = run_sql(sql, values)
#     #if len(results > 0):
#     id = results[0]['id']
#     destination.id = id
#     return destination
# #
# def select_all():
#     destinations = []

#     sql = "SELECT * FROM destinations"
#     results = run_sql(sql)

#     for row in results:
#         country = country_repository.select(row['country_id'])
#         destination = Destination(row['country'], row['id'])
#         destinations.append(destination)
#     return destinations

# def select(id):
#     destination = None
#     sql = "SELECT * FROM destinations WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         user = user_repository.select(result['user_id'])
#         destination = Destination(result['country'], result['id'])
#         return destination
    
# def delete_all():
#     sql = "DELETE  FROM destinations"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE  FROM destinations WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def update(destination):
#     sql = "UPDATE destinations SET (country, id) = (%s, %s) WHERE id = %s"
#     values = [destination.country, destination.id]
#     run_sql(sql, values)