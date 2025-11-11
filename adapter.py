
# ExternalMLSAPI defines the interface for fetching MLS data from external APIs.
# ExternalMLSAPIImpl implements the interface for fetching MLS data from an external API.
# MLSDataAdapter defines the interface for converting MLS data into a compatible format.
# MLSDataAPIAdapter adapts the external MLS API to the format required by the real estate
# database software.The client code demonstrates fetching data from the external MLS API,
# adapting it using the adapter, and printing the converted data.

from abc import ABC, abstractmethod

# External MLS API interface
class ExternalMLSAPI(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

# External MLS API implementation
class ExternalMLSAPIImpl(ExternalMLSAPI):
    def fetch_data(self):
        # Simulating fetching data from external MLS API
        return {"address": "4880 El Camino St", "price": 100000000}

# Adapter interface
class MLSDataAdapter(ABC):
    @abstractmethod
    def convert_data(self):
        pass

# Adapter implementation
class MLSDataAPIAdapter(MLSDataAdapter):
    def __init__(self, external_mls_api):
        self.external_mls_api = external_mls_api

    def convert_data(self):
        data = self.external_mls_api.fetch_data()
        return {"Address": data["address"], "Price": data["price"]}

# Client code
if __name__ == "__main__":
    external_mls_api = ExternalMLSAPIImpl()
    adapter = MLSDataAPIAdapter(external_mls_api)
    converted_data = adapter.convert_data()
    print("Converted MLS Data:", converted_data)
