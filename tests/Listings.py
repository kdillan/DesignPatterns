
from abc import ABC, abstractmethod


# Creational Patterns

# Factory Method Pattern
class ListingFactory(ABC):
    @abstractmethod
    def create_listing(self):
        pass

class ResidentialListingFactory(ListingFactory):
    def create_listing(self):
        return ResidentialListing()

class CommercialListingFactory(ListingFactory):
    def create_listing(self):
        return CommercialListing()

class Listing(ABC):
    @abstractmethod
    def display(self):
        pass

class ResidentialListing(Listing):
    def display(self):
        print("Residential Listing")

class CommercialListing(Listing):
    def display(self):
        print("Commercial Listing")


# Singleton Pattern
class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance


# Builder Pattern
class ListingBuilder(ABC):
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

class ConcreteListingBuilder(ListingBuilder):
    def __init__(self):
        self._listing = None

    def set_address(self, address):
        self._listing.address = address
        return self

    def set_price(self, price):
        self._listing.price = price
        return self

    def set_square_footage(self, square_footage):
        self._listing.square_footage = square_footage
        return self

    def build(self):
        return self._listing


# Structural Patterns

# Adapter Pattern
class ExternalAPIAdapter:
    def fetch_data(self):
        return {"address": "123 Main St", "price": 100000}

class Adapter:
    def __init__(self, external_api):
        self._external_api = external_api

    def get_listing_data(self):
        data = self._external_api.fetch_data()
        return {"address": data["address"], "price": data["price"]}

# Bridge Pattern
class ListingView:
    def __init__(self, listing):
        self._listing = listing

    def show(self):
        print(self._listing.display())

class ListingType:
    @abstractmethod
    def display(self):
        pass

class ResidentialListingType(ListingType):
    def display(self):
        return "Residential Listing"

class CommercialListingType(ListingType):
    def display(self):
        return "Commercial Listing"


# Behavioral Patterns

# Observer Pattern
class ListingObserver:
    def update(self, listing):
        print(f"Listing updated: {listing}")


class Listing:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)


# Concurrency Patterns

# Lock Pattern
from threading import Lock

class DatabaseLock:
    _lock = Lock()

    @staticmethod
    def acquire():
        DatabaseLock._lock.acquire()

    @staticmethod
    def release():
        DatabaseLock._lock.release()


# Architectural Patterns

# Model-View-Controller (MVC)
class Model:
    def __init__(self):
        self._data = []

    def add_data(self, data):
        self._data.append(data)

    def get_data(self):
        return self._data

class View:
    def show_data(self, data):
        for item in data:
            print(item)

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def add_data(self, data):
        self._model.add_data(data)

    def show_data(self):
        data = self._model.get_data()
        self._view.show_data(data)


# Example usage
if __name__ == "__main__":
    # Factory Method Pattern
    residential_factory = ResidentialListingFactory()
    residential_listing = residential_factory.create_listing()
    residential_listing.display()  # Output: Residential Listing

    # Singleton Pattern
    db_manager1 = DatabaseManager()
    db_manager2 = DatabaseManager()
    print(db_manager1 == db_manager2)  # Output: True

    # Builder Pattern
    listing_builder = ConcreteListingBuilder()
    listing = listing_builder.set_address("123 Main St").set_price(100000).set_square_footage(2000).build()

    # Adapter Pattern
    external_api = ExternalAPIAdapter()
    adapter = Adapter(external_api)
    listing_data = adapter.get_listing_data()

    # Bridge Pattern
    residential_listing_type = ResidentialListingType()
    listing_view = ListingView(residential_listing_type)
    listing_view.show()  # Output: Residential Listing

    # Observer Pattern
    listing = Listing()
    observer = ListingObserver()
    listing.add_observer(observer)
    listing.notify_observers()

    # Lock Pattern
    lock = DatabaseLock()
    lock.acquire()
    # Critical section
    lock.release()

    # MVC Pattern
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.add_data("Data 1")
    controller.add_data("Data 2")
    controller.show_data()  # Output: Data 1\nData 2
