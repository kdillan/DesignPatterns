# In this assignment, I have an interface class IPropertyBuilder that defines
# the methods for setting property attributes (address, price, square_footage)
# and building the property object. Then, I have a concrete implementation
# ConcretePropertyBuilder of the builder interface that implements these methods.
# Finally, I have a Property class which represents the product being built.
# The client code demonstrates how to use the builder to create property objects
# with different attributes.c


from abc import ABC, abstractmethod


# Interface class for Property Builder
class IPropertyBuilder(ABC):
    @abstractmethod
    def set_address(self, address):
        pass

    @abstractmethod
    def set_price(self, price):
        pass

    @abstractmethod
    def set_square_footage(self, square_footage):
        pass

    @abstractmethod
    def build(self):
        pass


# Concrete implementation of Property Builder
class ConcretePropertyBuilder(IPropertyBuilder):
    def __init__(self):
        self._address = None
        self._price = None
        self._square_footage = None

    def set_address(self, address):
        self._address = address
        return self

    def set_price(self, price):
        self._price = price
        return self

    def set_square_footage(self, square_footage):
        self._square_footage = square_footage
        return self

    def build(self):
        return Property(self._address, self._price, self._square_footage)


# Product class
class Property:
    def __init__(self, address, price, square_footage):
        self.address = address
        self.price = price
        self.square_footage = square_footage

    def display(self):
        print(f"Address: {self.address}, Price: ${self.price}, Square Footage: {self.square_footage}")


# Client code
if __name__ == "__main__":
    # Creating a property using the builder
    property_builder = ConcretePropertyBuilder()
    property1 = property_builder.set_address("123 Main St").set_price(20000000).set_square_footage(1500).build()
    property1.display()  # Output: Address: 123 Main St, Price: $200000, Square Footage: 1500

    # Creating another property using the builder
    property2 = property_builder.set_address("456 El Camino Real St").set_price(30000000).set_square_footage(2000).build()
    property2.display()  # Output: Address: 456 Elm St, Price: $300000, Square Footage: 2000


