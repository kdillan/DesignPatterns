#In this example, I defined three concrete states (Active, Pending, Sold)
# representing the different lifecycle stages of a listing. The Listing class
# acts as the context class that maintains the current state and facilitates
# state transitions. The transition_to_next_state() method transitions the
# listing to the next state in its lifecycle. Each state implements the
# ListingState interface, ensuring that they all provide the same interface
# for displaying the state and transitioning to the next state.



from abc import ABC, abstractmethod


# Interface class for listing state
class ListingState(ABC):
    @abstractmethod
    def display_state(self):
        pass

    @abstractmethod
    def transition_to_next_state(self):
        pass


# Concrete implementation of Active state
class ActiveState(ListingState):
    def display_state(self):
        return "Active"

    def transition_to_next_state(self):
        return PendingState()


# Concrete implementation of Pending state
class PendingState(ListingState):
    def display_state(self):
        return "Pending"

    def transition_to_next_state(self):
        return SoldState()


# Concrete implementation of Sold state
class SoldState(ListingState):
    def display_state(self):
        return "Sold"

    def transition_to_next_state(self):
        return None  # No transition from Sold state


# Context class representing the listing
class Listing:
    def __init__(self):
        self._state = ActiveState()  # Initial state

    def display_state(self):
        return self._state.display_state()

    def transition_to_next_state(self):
        next_state = self._state.transition_to_next_state()
        if next_state:
            self._state = next_state


# Example usage
if __name__ == "__main__":
    listing = Listing()

    # Initial state
    print("Initial state:", listing.display_state())  # Output: Initial state: Active

    # Transition to next state
    listing.transition_to_next_state()
    print("After transition:", listing.display_state())  # Output: After transition: Pending

    # Transition to next state
    listing.transition_to_next_state()
    print("After transition:", listing.display_state())  # Output: After transition: Sold

    # No further transition
    listing.transition_to_next_state()
    print("After transition:", listing.display_state())  # Output: After transition: Sold
