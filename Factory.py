#Week 2 Assignment :

# An interface class Lead with an abstract method generate_lead().
# Two concrete classes WebsiteLead and AdvertisementLead implementing the Lead interface.
# A factory class LeadFactory with a static method create_lead() to create instances of
# different types of leads based on the input. In the client code, the user inputs the
# lead type (either 'website' or 'advertisement'), and the factory class creates and
# returns the corresponding lead object, which then generates the lead.

from abc import ABC, abstractmethod

# Interface class for Lead
class Lead(ABC):
    @abstractmethod
    def generate_lead(self):
        pass

# Concrete implementation of Lead
class WebsiteLead(Lead):
    def generate_lead(self):
        print("Website Lead generated")

class AdvertisementLead(Lead):
    def generate_lead(self):
        print("Advertisement Lead generated")

# Factory class for Lead generation
class LeadFactory:
    @staticmethod
    def create_lead(lead_type):
        if lead_type == 'website':
            return WebsiteLead()
        elif lead_type == 'advertisement':
            return AdvertisementLead()
        else:
            raise ValueError("Invalid lead type")

# Client code
if __name__ == "__main__":
    lead_type = input("Enter lead type (website/advertisement): ")
    lead = LeadFactory.create_lead(lead_type)
    lead.generate_lead()
