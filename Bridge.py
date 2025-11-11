from abc import ABC, abstractmethod

#  This is an exercise for Bridge Design Pattern in Python
#  The MLSDataBridge class is a concrete implementation of the IBridge interface.
#  It encapsulates an instance of the IMLSDataAdapter class and provides a method fetch_and_convert()
#  to fetch data from the external MLS API and convert it using the adapter.

class IExternalMLSAPI(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

# External MLS API implementation
class ExternalMLSAPIImpl(IExternalMLSAPI):
    def fetch_data(self):
        # Simulating fetching data from external MLS API
        return {"address": "4880 El Camino St", "price": 100000000}

# Adapter interface
class IMLSDataAdapter(ABC):
    @abstractmethod
    def convert_data(self):
        pass

# Adapter implementation
class MLSDataAPIAdapter(IMLSDataAdapter):
    def __init__(self, external_mls_api):
        self.external_mls_api = external_mls_api

    def convert_data(self):
        data = self.external_mls_api.fetch_data()
        return {"Address": data["address"], "Price": data["price"]}

# Bridge interface
class IBridge(ABC):
    @abstractmethod
    def fetch_and_convert(self):
        pass

# Bridge implementation
class MLSDataBridge(IBridge):
    def __init__(self, adapter):
        self.adapter = adapter

    def fetch_and_convert(self):
        return self.adapter.convert_data()

# Client code
if __name__ == "__main__":
    external_mls_api = ExternalMLSAPIImpl()
    adapter = MLSDataAPIAdapter(external_mls_api)
    bridge = MLSDataBridge(adapter)
    converted_data = bridge.fetch_and_convert()
    print("Converted MLS Data:", converted_data)
