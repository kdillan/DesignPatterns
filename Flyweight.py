# In this example, PropertyFlyweight represents the shared data (location and amenities)
# for property listings. The PropertyListing class represents individual property listings
# that reference the shared flyweight object. The PropertyManager class manages the creation
# and retrieval of flyweight objects. This ensures that similar property listings share
# the same flyweight object, reducing memory usage and improving performance.

from abc import ABC, abstractmethod
from typing import Dict

class Property(ABC):
    @abstractmethod
    def display(self):
        pass

class PropertyFlyweight(Property):
    def __init__(self, location: str, amenities: Dict[str, bool]):
        self._location = location
        self._amenities = amenities

    def display(self):
        return f"Location: {self._location}, Amenities: {self._amenities}"

class PropertyListing(Property):
    def __init__(self, property_flyweight: PropertyFlyweight, price: int):
        self._property_flyweight = property_flyweight
        self._price = price

    def display(self):
        return f"{self._property_flyweight.display()}, Price: {self._price}"

class PropertyManager:
    _flyweights = {}

    @staticmethod
    def get_property_flyweight(location: str, amenities: Dict[str, bool]) -> PropertyFlyweight:
        key = (location, tuple(amenities.items()))
        if key not in PropertyManager._flyweights:
            PropertyManager._flyweights[key] = PropertyFlyweight(location, amenities)
        return PropertyManager._flyweights[key]


# Usage example
if __name__ == "__main__":
    # Shared property data (flyweight)
    shared_data = PropertyManager.get_property_flyweight("City Center", {"Swimming Pool": True, "Gym": True})

    # Property listings using shared data
    property1 = PropertyListing(shared_data, 100000)
    property2 = PropertyListing(shared_data, 120000)

    print(property1.display())  # Output: Location: City Center, Amenities: {'Swimming Pool': True, 'Gym': True}, Price: 100000
    print(property2.display())  # Output: Location: City Center, Amenities: {'Swimming Pool': True, 'Gym': True}, Price: 120000
