# Exercise Week 8: Complex property management subsystems

# PropertyDatabase and EmailService represent complex subsystems for managing
# properties and sending emails, respectively.  PropertyManagementFacade provides
# a simplified interface for interacting with these subsystems. The client interacts
# only with the PropertyManagementFacade class, which internally delegates the tasks
# to the appropriate subsystems. The facade pattern hides the complexities of the
# subsystems from the client, providing a simpler and more unified interface for
# property management operations.

class PropertyDatabase:
    def __init__(self):
        self.properties = []

    def add_property(self, property_details):
        self.properties.append(property_details)

class EmailService:
    def send_email(self, recipient, message):
        print(f"Email sent to {recipient}: {message}")

# Facade

class PropertyManagementFacade:
    def __init__(self):
        self.property_db = PropertyDatabase()
        self.email_service = EmailService()

    def list_properties(self):
        return self.property_db.properties

    def add_property(self, property_details):
        self.property_db.add_property(property_details)
        self.email_service.send_email("admin@designpattern.edu", "New property added")

# Client code

if __name__ == "__main__":
    facade = PropertyManagementFacade()

    # Adding a property
    facade.add_property("123 Main St, City, State")

    # Listing properties
    properties = facade.list_properties()
    print("Properties:")
    for prop in properties:
        print(prop)
