# This code demonstrates the use of the Worker Pool pattern, MapReduce pattern,
# Read-Write Lock pattern, Reactor pattern, and Resource Pool pattern in a
# real estate sales management software context. Each pattern is used to handle
# specific aspects of the software, such as updating listings, processing data,
# managing database access, handling events, and managing resources efficiently.

import threading
import concurrent.futures
import time
import random


# Interface for worker objects
class WorkerInterface:
    def execute_task(self, task):
        pass


# Concrete worker implementing WorkerInterface
class ListingUpdater(WorkerInterface):
    def execute_task(self, task):
        print(f"Updating listing: {task}")
        # Simulate updating listing in database
        time.sleep(random.randint(1, 3))
        print(f"Listing {task} updated successfully")


# Worker pool pattern
class WorkerPool:
    def __init__(self, num_workers):
        self.pool = []
        for _ in range(num_workers):
            self.pool.append(ListingUpdater())

    def execute_task(self, task):
        worker = self.get_available_worker()
        if worker:
            worker.execute_task(task)
        else:
            print("All workers busy, task queued.")

    def get_available_worker(self):
        for worker in self.pool:
            if not isinstance(worker, threading.Thread) or not worker.is_alive():
                return worker
        return None


# MapReduce pattern
def map_reduce(data):
    # Map phase: Split data and assign to workers
    chunks = split_data(data)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(update_listing, chunks)

    # Reduce phase: Combine results
    return combine_results(results)


def split_data(data):
    # Simulate splitting data into chunks
    return [data[i:i + 3] for i in range(0, len(data), 3)]


def update_listing(listings):
    # Simulate updating listings
    time.sleep(random.randint(1, 3))
    return [f"Listing {listing} updated successfully" for listing in listings]


def combine_results(results):
    # Simulate combining results
    return sum(results, [])


# Read-Write Lock pattern
class Database:
    def __init__(self):
        self.data = []
        self.lock = threading.RLock()

    def read_data(self):
        with self.lock:
            return self.data

    def write_data(self, new_data):
        with self.lock:
            self.data = new_data


# Reactor pattern
class EventHandler:
    def handle_event(self, event):
        print(f"Event handled: {event}")


# Resource Pool pattern
class ResourcePool:
    def __init__(self, num_resources):
        self.pool = [EventHandler() for _ in range(num_resources)]

    def get_resource(self):
        return self.pool.pop()


# Client code
if __name__ == "__main__":
    # Worker pool pattern
    worker_pool = WorkerPool(num_workers=3)
    worker_pool.execute_task("listing1")
    worker_pool.execute_task("listing2")
    worker_pool.execute_task("listing3")

    # MapReduce pattern
    data = ["listing1", "listing2", "listing3", "listing4", "listing5", "listing6"]
    result = map_reduce(data)
    print(f"MapReduce result: {result}")

    # Read-Write Lock pattern
    db = Database()
    db.write_data(data)
    print(f"Database data: {db.read_data()}")

    # Reactor pattern
    event_handler = ResourcePool(num_resources=2).get_resource()
    event_handler.handle_event("New listing added")

    # Resource Pool pattern
    resource = ResourcePool(num_resources=2).get_resource()
    resource.handle_event("New customer inquiry")
