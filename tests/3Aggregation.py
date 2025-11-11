'''In example 3:
The City class represents a city with attributes such as name and population.
The County class represents a county, which contains a list (cities) to hold instances of the City class.
The add_city() method allows adding cities to the county's list of cities.
There is an aggregation association relationship between the County class and the City class. The County class contains instances of the City class as part of its structure.
The __str__() method is overridden in both classes to provide a string representation for printing.
When I run this code, it creates a county object named "San Mateo County" and adds three cities to it. Finally, it prints information about the county and its cities.
'''
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def __str__(self):
        return f"{self.name} (Population: {self.population})"
class County:
    def __init__(self, name):
        self.name = name
        self.cities = []  # List to hold the cities in the county
    def add_city(self, city):
        self.cities.append(city)
    def __str__(self):
        city_names = ", ".join(city.name for city in self.cities)
        return f"County: {self.name}\nCities: {city_names}"

# Creating cities
city1 = City("Menlo Park", 8623000)
city2 = City("Redwood City", 399000)
city3 = City("Belmont", 271600)
city4 = City("San Carlos", 566000)
city5 = City("Foster City", 953000)
city6 = City("San Mateo", 5487000)
city7 = City("Millbrae", 8945600)

# Creating a county and adding cities to it
county = County("San Mateo County")
county.add_city(city1)
county.add_city(city2)
county.add_city(city3)
county.add_city(city4)
county.add_city(city5)
county.add_city(city6)
county.add_city(city7)
# Printing information about the county and its cities
print(county)
