# In this example, the ListingManager acts as the invoker, and commands
# such as AddListingCommand and UpdateListingCommand encapsulate actions
# to add and update property listings, respectively. This pattern allows
# for decoupling of the client code from the actual actions performed on
# the listings, providing flexibility and extensibility in managing
# property listings within the real estate management system.

from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Concrete Command: Add Listing
class AddListingCommand(Command):
    def __init__(self, listing):
        self._listing = listing

    def execute(self):
        # Logic to add a new listing
        print(f"Added new listing: {self._listing}")

    def undo(self):
        # Logic to undo adding a listing
        print(f"Undo adding listing: {self._listing}")

# Concrete Command: Update Listing
class UpdateListingCommand(Command):
    def __init__(self, listing_id, updated_listing):
        self._listing_id = listing_id
        self._updated_listing = updated_listing

    def execute(self):
        # Logic to update a listing
        print(f"Updated listing {self._listing_id}: {self._updated_listing}")

    def undo(self):
        # Logic to undo updating a listing
        print(f"Undo updating listing {self._listing_id}: {self._updated_listing}")

# Invoker
class ListingManager:
    def __init__(self):
        self._history = []

    def execute_command(self, command):
        command.execute()
        self._history.append(command)

    def undo_last_command(self):
        if self._history:
            last_command = self._history.pop()
            last_command.undo()
        else:
            print("No commands to undo")

# Client
if __name__ == "__main__":
    manager = ListingManager()

    # Add a new listing
    add_command = AddListingCommand("New apartment for sale")
    manager.execute_command(add_command)

    # Update an existing listing
    update_command = UpdateListingCommand(123, "Updated price for condo")
    manager.execute_command(update_command)

    # Undo last command
    manager.undo_last_command()
