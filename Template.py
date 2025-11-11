# In this example, we define an interface class Listing with abstract methods
# representing the steps involved in listing a property. The list_property method
# serves as the template method, which orchestrates the sequence of steps
# required for listing a property.

# Concrete subclasses ResidentialListing and CommercialListing provide
# specific implementations for each step of the listing process.
# When the list_property method is called on an instance of these subclasses,
# it executes the steps in the defined sequence, ensuring consistency
# in the listing process while allowing flexibility in implementing specific
# behaviors for different types of properties.

from abc import ABC, abstractmethod

# Interface class for listing
class Listing(ABC):
    @abstractmethod
    def prepare_description(self):
        pass

    @abstractmethod
    def upload_photos(self):
        pass

    @abstractmethod
    def set_price(self):
        pass

    def list_property(self):
        self.prepare_description()
        self.upload_photos()
        self.set_price()
        print("Property listed successfully!")


# Concrete implementation for Residential Listing
class ResidentialListing(Listing):
    def prepare_description(self):
        print("Preparing residential property description...")

    def upload_photos(self):
        print("Uploading photos of residential property...")

    def set_price(self):
        print("Setting price for residential property...")


# Concrete implementation for Commercial Listing
class CommercialListing(Listing):
    def prepare_description(self):
        print("Preparing commercial property description...")

    def upload_photos(self):
        print("Uploading photos of commercial property...")

    def set_price(self):
        print("Setting price for commercial property...")


# Client code
if __name__ == "__main__":
    # Create a residential listing
    residential_listing = ResidentialListing()
    residential_listing.list_property()

    # Create a commercial listing
    commercial_listing = CommercialListing()
    commercial_listing.list_property()
