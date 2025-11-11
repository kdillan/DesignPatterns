# The CircuitBreaker class is introduced to implement the Circuit Breaker pattern for fault tolerance.
# The APIGateway class  uses the CircuitBreaker to execute calls to the microservices.
# Mock Listing and Customer services are implemented with random failures to simulate errors.
# The client code remains the same, but now the APIGateway handles failures gracefully using
# the Circuit Breaker pattern. If the failure rate exceeds the threshold, the circuit opens,
# preventing further calls until the timeout expires and the circuit resets.


import time
import random

# Circuit Breaker pattern implementation
class CircuitBreaker:
    def __init__(self, max_failures=3, reset_timeout=30):
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.circuit_open = False

    def execute(self, func):
        if self.circuit_open:
            if self._is_timeout_expired():
                self._reset_circuit()
            else:
                print("Circuit is open. Skipping execution.")
                return None

        try:
            result = func()
            self._handle_success()
            return result
        except Exception as e:
            self._handle_failure(e)
            return None

    def _handle_success(self):
        self.failure_count = 0
        self.last_failure_time = None

    def _handle_failure(self, error):
        self.failure_count += 1
        if self.failure_count >= self.max_failures:
            self.last_failure_time = time.time()
            self.circuit_open = True
            print(f"Circuit opened due to {self.max_failures} consecutive failures: {error}")

    def _is_timeout_expired(self):
        if self.last_failure_time is None:
            return True
        return time.time() - self.last_failure_time > self.reset_timeout

    def _reset_circuit(self):
        self.failure_count = 0
        self.last_failure_time = None
        self.circuit_open = False


# Updated API Gateway with Circuit Breaker
class APIGateway:
    def __init__(self, listing_service, customer_service):
        self.listing_service = listing_service
        self.customer_service = customer_service
        self.listing_circuit_breaker = CircuitBreaker()
        self.customer_circuit_breaker = CircuitBreaker()

    def create_listing(self, listing_info):
        return self.listing_circuit_breaker.execute(lambda: self.listing_service.create_listing(listing_info))

    def get_listing(self, listing_id):
        return self.listing_circuit_breaker.execute(lambda: self.listing_service.get_listing(listing_id))

    def create_customer(self, customer_info):
        return self.customer_circuit_breaker.execute(lambda: self.customer_service.create_customer(customer_info))

    def get_customer(self, customer_id):
        return self.customer_circuit_breaker.execute(lambda: self.customer_service.get_customer(customer_id))


# Mock Listing and Customer Service with random failures
class MockListingService:
    def create_listing(self, listing_info):
        if random.random() < 0.3:  # Simulate 30% failure rate
            raise Exception("Error creating listing")
        return "Listing created successfully"

    def get_listing(self, listing_id):
        if random.random() < 0.3:  # Simulate 30% failure rate
            raise Exception("Error fetching listing")
        return {"id": listing_id, "address": "4588 Rosemary St", "price": 2500000}


class MockCustomerService:
    def create_customer(self, customer_info):
        if random.random() < 0.3:  # Simulate 30% failure rate
            raise Exception("Error creating customer")
        return "Customer created successfully"

    def get_customer(self, customer_id):
        if random.random() < 0.3:  # Simulate 30% failure rate
            raise Exception("Error fetching customer")
        return {"id": customer_id, "name": "Michael", "email": "michael@abc.com"}


# Client code
if __name__ == "__main__":
    listing_service = MockListingService()
    customer_service = MockCustomerService()
    api_gateway = APIGateway(listing_service, customer_service)

    # Creating a listing through API gateway
    print(api_gateway.create_listing({"address": "456 El Camino Real", "price": 30000000}))

    # Fetching a listing through API gateway
    print(api_gateway.get_listing(1001))

    # Creating a customer through API gateway
    print(api_gateway.create_customer({"name": "Katie Dillan", "email": "Katie@abc.com"}))

    # Fetching a customer through API gateway
    print(api_gateway.get_customer(2001))
