# This exercise includes all four pillars of object-oriented programming:

# Inheritance: Both the House and Apartment classes inherit from the IProperty interface class.
# They inherit attributes and methods from the base class (IProperty) and can also define their
# own unique attributes and methods.

# Encapsulation: Encapsulation is achieved by bundling the data (attributes) and methods that
# operate on the data within each class. For example, the location, price, and num_bedrooms
# (or num_rooms) are encapsulated within their respective classes (IProperty, House, Apartment).

# Polymorphism: Polymorphism is demonstrated by the display_property_info() function,
# which accepts any object of type Property (either House or Apartment) and calls its
# display_info() method. The method behaves differently depending on the actual type of object
# passed to it, allowing for different implementations of display_info() to be executed.

# Abstraction: Abstraction is achieved by defining a base class IProperty with a generic
# display_info() method. This method serves as an abstraction that hides the implementation
# details of displaying property information. Subclasses (House, Apartment) provide their own
# concrete implementations of the method, fulfilling the abstraction provided by the base class.

class IProperty:
    def __init__(self, location, price):
        self.location = location
        self.price = price

    def display_info(self):
        print(f"Location: {self.location}, Price: ${self.price}")


class House(IProperty):
    def __init__(self, location, price, num_bedrooms):
        super().__init__(location, price)
        self.num_bedrooms = num_bedrooms

    def display_info(self):
        print(f"Type: House, Location: {self.location}, Price: ${self.price}, Bedrooms: {self.num_bedrooms}")


class Apartment(IProperty):
    def __init__(self, location, price, num_rooms):
        super().__init__(location, price)
        self.num_rooms = num_rooms

    def display_info(self):
        print(f"Type: Apartment, Location: {self.location}, Price: ${self.price}, Rooms: {self.num_rooms}")


# Polymorphic function
def display_property_info(property):
    property.display_info()


# Usage
property1 = House("Downtown", 250000, 3)
property2 = Apartment("Suburb", 150000, 2)

display_property_info(property1)  # Output: Type: House, Location: Downtown, Price: $250000, Bedrooms: 3
display_property_info(property2)  # Output: Type: Apartment, Location: Suburb, Price: $150000, Rooms: 2
