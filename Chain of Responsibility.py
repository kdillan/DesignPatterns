
# InquiryHandler is the interface class defining the method handle_inquiry() to handle property inquiries.
# ListingInquiryHandler and ViewingRequestHandler are concrete handlers for handling listing inquiries
# and viewing requests, respectively.
# InquiryHandlerProxy acts as a proxy to control access to the real handler (ViewingRequestHandler).
# It performs access control before delegating the inquiry to the real handler.
# Inquiry represents a property inquiry, containing information such as the type of inquiry, property ID,
# and client ID.
# Client code demonstrates how inquiries are processed using the proxy, and access control is enforced based on the client's role.

from abc import ABC, abstractmethod

# Interface class for handling property inquiries
class IInquiryHandler(ABC):
    @abstractmethod
    def handle_inquiry(self, inquiry):
        pass

# Concrete implementation of InquiryHandler for handling listing inquiries
class ListingInquiryHandler(IInquiryHandler):
    def handle_inquiry(self, inquiry):
        if inquiry.type == 'listing':
            return f"Listing inquiry processed for property ID {inquiry.property_id}"
        else:
            return "Listing inquiry handler cannot handle this type of inquiry."

# Concrete implementation of InquiryHandler for handling viewing requests
class ViewingRequestHandler(IInquiryHandler):
    def __init__(self):
        self._next_handler = None

    def set_next_handler(self, next_handler):
        self._next_handler = next_handler

    def handle_inquiry(self, inquiry):
        if inquiry.type == 'viewing':
            return f"Viewing request processed for property ID {inquiry.property_id}"
        elif self._next_handler:
            return self._next_handler.handle_inquiry(inquiry)
        else:
            return "No handler available to process this type of inquiry."

# Proxy class for managing property inquiries
class InquiryHandlerProxy(IInquiryHandler):
    def __init__(self, real_handler):
        self._real_handler = real_handler

    def handle_inquiry(self, inquiry):
        # Perform access control or additional processing before delegating to the real handler
        if inquiry.client_id == 'admin':
            return self._real_handler.handle_inquiry(inquiry)
        else:
            return "Access denied. Only administrators can access this feature."

# Inquiry object representing a property inquiry
class Inquiry:
    def __init__(self, type, property_id, client_id):
        self.type = type
        self.property_id = property_id
        self.client_id = client_id

# Client code
if __name__ == "__main__":
    # Create concrete handlers
    listing_handler = ListingInquiryHandler()
    viewing_handler = ViewingRequestHandler()

    # Configure chain of responsibility
    viewing_handler.set_next_handler(listing_handler)

    # Create proxy for managing inquiries
    proxy = InquiryHandlerProxy(viewing_handler)

    # Simulate property inquiries
    admin_inquiry = Inquiry(type='listing', property_id=123, client_id='admin')
    client_inquiry = Inquiry(type='listing', property_id=456, client_id='user')

    # Process inquiries using the proxy
    print(proxy.handle_inquiry(admin_inquiry))   # Output: Listing inquiry processed for property ID 123
    print(proxy.handle_inquiry(client_inquiry))  # Output: Access denied. Only administrators can access this feature.
