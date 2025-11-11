#In this example, the Prototype interface defines the clone() method, which allows objects to be cloned.
# The Customer class is a concrete implementation of the prototype, representing a customer with a name and email.
# The CRMSystem class manages the prototypes and allows sending marketing campaigns to customers by cloning the prototypes.

from abc import ABC, abstractmethod
import copy

# Interface class for the prototype
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete prototype class
class Customer(Prototype):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def clone(self):
        return copy.deepcopy(self)

# Client class to manage prototypes and send marketing campaigns
class CRMSystem:
    def __init__(self):
        self._prototype = {}

    def register_prototype(self, key, prototype):
        self._prototype[key] = prototype

    def unregister_prototype(self, key):
        del self._prototype[key]

    def send_campaign(self, key):
        if key in self._prototype:
            customer = self._prototype[key].clone()
            print(f"Sending marketing campaign to {customer.name} at {customer.email}")
        else:
            print(f"No customer found with key {key}")

# Usage
if __name__ == "__main__":
    # Create prototype customers
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    # Register prototypes in CRM system
    crm_system = CRMSystem()
    crm_system.register_prototype("alice_key", customer1)
    crm_system.register_prototype("bob_key", customer2)

    # Send marketing campaigns using prototypes
    crm_system.send_campaign("alice_key")  # Output: Sending marketing campaign to Alice at alice@example.com
    crm_system.send_campaign("bob_key")    # Output: Sending marketing campaign to Bob at bob@example.com
    crm_system.send_campaign("charlie_key")  # Output: No customer found with key charlie_key
