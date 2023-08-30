# from models.user import User
# from models.destination import Destination
from models.country import Country
from models.city import City

# import repositories.user_repository as user_repository
# import repositories.destination_repository as destination_repository
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

# user_1 = User("Melika")
# user_repository.save(user_1)
# user_2 = User("Alfie")
# user_repository.save(user_2)

#user_repository.select_all()

#  make counties and cities

# destination_1 = Destination("Turkey", 1)
# destination_repository.save(destination_1)
# destination_2 = Destination("England", 2)
# destination_repository.save(destination_2)
city_repository.delete_all()
country_repository.delete_all()



country_1 = Country("Turkey")
country_repository.save(country_1)
country_2 = Country("England")
country_repository.save(country_2)
country_3 = Country("Japan")
country_repository.save(country_3)
country_4 = Country("France")
country_repository.save(country_4)

city_1 = City("Istanbul", False, country_1)
city_repository.save(city_1)
city_2 = City("Izmir", False, country_1)
city_repository.save(city_2)
city_3 = City("Ankara", False, country_1)
city_repository.save(city_3)
city_4 = City("Konya", False, country_1)
city_repository.save(city_4)
city_5 = City("London", False, country_2)
city_repository.save(city_5)
city_6 = City("Manchester", False, country_2)
city_repository.save(city_6)
city_7 = City("Birmingham", False, country_2)
city_repository.save(city_7)
city_8 = City("Newcastle", False, country_2)
city_repository.save(city_8)
city_9 = City("Tokyo", False, country_3)
city_repository.save(city_9)
city_10 = City("Osaka", False, country_3)
city_repository.save(city_10)
city_11 = City("Kyoto", False, country_3)
city_repository.save(city_11)
city_12 = City("Hiroshima", False, country_3)
city_repository.save(city_12)
city_13 = City("Paris", False, country_4)
city_repository.save(city_13)
city_14 = City("Marseille", False, country_4)
city_repository.save(city_14)
city_15 = City("Nice", False, country_4)
city_repository.save(city_15)
city_16 = City("Lyon", False, country_4)
city_repository.save(city_16)
