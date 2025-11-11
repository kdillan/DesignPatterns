#This code demonstrates a simple real estate management system. It includes abstract class Property with concrete subclasses ResidentialProperty and CommercialProperty. It also includes an interface class PropertyManager with a concrete implementation RealEstateAgent. This example showcases the use of abstract classes and an interface class in Python.

from abc import ABC, abstractmethod

# Abstract class for Property
class Property(ABC):
    def __init__(self, address, price):
        self.address = address
        self.price = price

    @abstractmethod
    def display_details(self):
        pass

# Concrete class for Residential Property
class ResidentialProperty(Property):
    def __init__(self, address, price, num_bedrooms):
        super().__init__(address, price)
        self.num_bedrooms = num_bedrooms

    def display_details(self):
        print(f"Residential Property Details:\nAddress: {self.address}\nPrice: ${self.price}\nBedrooms: {self.num_bedrooms}")

# Concrete class for Commercial Property
class CommercialProperty(Property):
    def __init__(self, address, price, sqft):
        super().__init__(address, price)
        self.sqft = sqft

    def display_details(self):
        print(f"Commercial Property Details:\nAddress: {self.address}\nPrice: ${self.price}\nSquare Footage: {self.sqft} sqft")

# Interface class for Property Manager
class PropertyManager(ABC):
    @abstractmethod
    def add_property(self, property):
        pass

    @abstractmethod
    def display_properties(self):
        pass

# Concrete class implementing Property Manager interface
class RealEstateAgent(PropertyManager):
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def display_properties(self):
        print("List of Properties:")
        for prop in self.properties:
            prop.display_details()


# Demo
if __name__ == "__main__":
    agent = RealEstateAgent()

    # Add residential property
    residential_prop = ResidentialProperty("123 Main St", 250000, 3)
    agent.add_property(residential_prop)

    # Add commercial property
    commercial_prop = CommercialProperty("456 Broadway", 500000, 2000)
    agent.add_property(commercial_prop)

    # Display all properties
    agent.display_properties()
