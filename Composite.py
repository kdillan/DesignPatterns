# In this code, the Composite pattern represents hierarchical structures of properties
# for commercial buildings. I have created two types of components: Unit and Property.
# Unit represents individual units within a property, while Property represents
# the main property itself, which can contain multiple units or sub-properties.
# The Property class acts as both a leaf and a composite component, allowing it
# to contain other properties or units. Finally, the client code demonstrates
# how to create a complex hierarchical structure of properties, including hotels,
# medical offices, apartments, and shopping malls, each containing multiple units.

from abc import ABC, abstractmethod

# Component Interface
class IPropertyComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf Component
class Unit(IPropertyComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Unit: {self.name}")

# Composite Component
class Property(IPropertyComponent):
    def __init__(self, name):
        self.name = name
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)

    def remove_unit(self, unit):
        self.units.remove(unit)

    def display(self):
        print(f"Property: {self.name}")
        for unit in self.units:
            unit.display()

# Client Code
if __name__ == "__main__":
    # Create units
    unit1 = Unit("Unit 1")
    unit2 = Unit("Unit 2")
    unit3 = Unit("Unit 3")

    # Create properties
    hotel = Property("Hotel")
    medical_office = Property("Medical Office")
    apartment = Property("Apartment")
    shopping_mall = Property("Shopping Mall")

    # Add units to properties
    hotel.add_unit(unit1)
    medical_office.add_unit(unit2)
    apartment.add_unit(unit3)

    # Add properties to shopping mall
    shopping_mall.add_unit(hotel)
    shopping_mall.add_unit(medical_office)
    shopping_mall.add_unit(apartment)

    # Display structure
    shopping_mall.display()
