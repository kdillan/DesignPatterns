from abc import ABCMeta, abstractmethod

class Context():
    "This is the object whose behavior will change"
    def __init__(self, handle=None):
        self.handle = handle

    def request(self):
        """A method of the state that dynamically changes which class
        it uses depending on the value of self.handle"""
        return self.handle()

class IState(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def ProcessExpense():
        "Set the default method"

class FileExpense(IState):
    "A ConcreteState Subclass"

    def ProcessExpense(self):
        print("Expense Filed")
        CONTEXT.handle = ReviewExpense

#        return ReviewExpense()  # Set the state for next request

class ReviewExpense(IState):
    "A ConcreteState Subclass"
    def ProcessExpense(self):
        print("Expense Processed")
        CONTEXT.handle = ApproveExpense

     #   return ApproveExpense()  # Set the state for next request

class ApproveExpense(IState):
    def ProcessExpense(self):
        print("Expense Approved")
        CONTEXT.handle = None
        # return None

# Client
if __name__ == '__main__':
    CONTEXT = Context(FileExpense)
    CONTEXT.request().ProcessExpense()
    CONTEXT.request().ProcessExpense()
    CONTEXT.request().ProcessExpense()

# Sample Output:
# Expense Filed
# Expense Processed
# Expense Approved