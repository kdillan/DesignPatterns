#In this exercise, an interface class Observer defines the update method.
# Concrete observer classes Agent and Customer implement this interface and represent
# interested parties who will receive updates about listing changes. The Listing class
# acts as the subject and maintains a list of observers. It provides methods to add/remove
# observers and notify them of changes to availability or price. Finally, in the example usage,
# we create a listing, add observers, and update the availability and price,
# triggering notifications to all observers.

from abc import ABC, abstractmethod

# Interface class for Observer
class IObserver(ABC):
    @abstractmethod
    def update(self, listing):
        pass

# Concrete Observer classes representing interested parties
class Agent(IObserver):
    def __init__(self, name):
        self.name = name

    def update(self, listing):
        print(f"Agent {self.name}: Received update - {listing}")

class Customer(IObserver):
    def __init__(self, name):
        self.name = name

    def update(self, listing):
        print(f"Customer {self.name}: Received update - {listing}")

# Subject class representing the listing
class Listing:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def set_availability(self, availability):
        self.availability = availability
        self.notify_observers()

    def set_price(self, price):
        self.price = price
        self.notify_observers()

# Example usage
if __name__ == "__main__":
    # Creating listing
    listing = Listing()

    # Interested parties
    agent1 = Agent("Katie")
    agent2 = Agent("Michael")
    customer1 = Customer("George")
    customer2 = Customer("Patrick")

    # Adding observers
    listing.add_observer(agent1)
    listing.add_observer(agent2)
    listing.add_observer(customer1)
    listing.add_observer(customer2)

    # Updating availability
    listing.set_availability("Available")

    # Updating price
    listing.set_price("$30,000,000")
