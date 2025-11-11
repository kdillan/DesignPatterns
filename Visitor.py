#In this example:

#The Visitor interface defines the operations that can be performed on listings and customers.
#The ReportVisitor class implements these operations.
#The Element interface defines the accept method, which allows elements to accept visitors.
#The Listing and Customer classes are concrete elements that implement the accept method.
#The client code creates instances of listings and customers and then visits them using the ReportVisitor.
#This way, the Visitor pattern allows performing operations on listings or customers without modifying their underlying classes, enabling flexibility and separation of concerns.


from abc import ABC, abstractmethod


# Interface class for visitors
class Visitor(ABC):
    @abstractmethod
    def visit_listing(self, listing):
        pass

    @abstractmethod
    def visit_customer(self, customer):
        pass


# Concrete visitor implementing operations on listings and customers
class ReportVisitor(Visitor):
    def visit_listing(self, listing):
        print(f"Generating report for listing: {listing}")

    def visit_customer(self, customer):
        print(f"Generating report for customer: {customer}")


# Element interface class for accept method
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Concrete elements: Listing and Customer
class Listing(Element):
    def accept(self, visitor):
        visitor.visit_listing(self)


class Customer(Element):
    def accept(self, visitor):
        visitor.visit_customer(self)


# Client code
if __name__ == "__main__":
    # Creating elements
    listing1 = Listing()
    listing2 = Listing()
    customer1 = Customer()
    customer2 = Customer()

    # Creating visitor
    report_visitor = ReportVisitor()

    # Visiting elements
    listing1.accept(report_visitor)  # Output: Generating report for listing: <Listing object>
    customer1.accept(report_visitor)  # Output: Generating report for customer: <Customer object>
