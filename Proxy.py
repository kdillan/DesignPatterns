#In this example, ContactInfo is the interface class defining the method get_contact_info().
# I have a concrete implementation of this interface in the RealContactInfo class, which
# represents the actual access to the sensitive resource (customer contact information).
# The ContactInfoProxy class acts as a proxy to control access to the real contact information
# based on the user's access level. Depending on the access level provided during proxy instantiation,
# it either allows access to the real contact information or denies access.

from abc import ABC, abstractmethod

# Interface class
class ContactInfo(ABC):
    @abstractmethod
    def get_contact_info(self):
        pass

# Concrete implementation of the interface
class RealContactInfo(ContactInfo):
    def __init__(self, customer_id):
        self._customer_id = customer_id

    def get_contact_info(self):
        # Simulating fetching contact info from database
        return f"Contact info for customer ID {self._customer_id}: Phone: 123-456-7890, Email: customer@example.com"

# Proxy class
class ContactInfoProxy(ContactInfo):
    def __init__(self, customer_id, access_level):
        self._customer_id = customer_id
        self._real_contact_info = RealContactInfo(customer_id)
        self._access_level = access_level

    def get_contact_info(self):
        if self._access_level == 'admin':
            return self._real_contact_info.get_contact_info()
        else:
            return "Access denied. You do not have permission to view customer contact information."

# Client code
if __name__ == "__main__":
    # Create a proxy instance with admin access
    admin_proxy = ContactInfoProxy(customer_id=123, access_level='admin')
    print(admin_proxy.get_contact_info())  # Output: Contact info for customer ID 123: Phone: 123-456-7890, Email: customer@example.com

    # Create a proxy instance with restricted access
    restricted_proxy = ContactInfoProxy(customer_id=456, access_level='restricted')
    print(restricted_proxy.get_contact_info())  # Output: Access denied. You do not have permission to view customer contact information.
