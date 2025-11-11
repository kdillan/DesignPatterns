from abc import ABCMeta, abstractmethod
CONTEXT = 0

class Context():
 def __init__(self, handle=None):
  self.handle = handle

 def request(self):
  return self.handle()


class IState(metaclass=ABCMeta):

 @staticmethod
 @abstractmethod
 def ProcessExpense():
  #"Set the default method"
  print("ProcessExpense not  Implemented in the Interface here")

class FileExpense(IState):

 def ProcessExpense(self):
  print("Expense Filed")
  CONTEXT.handle = ReviewExpense()


class ReviewExpense(IState):
 def ProcessExpense(self):
  print("Expense Processed")
  CONTEXT.handle = ApproveExpense()

class ApproveExpense(IState):
 def ProcessExpense(self):
  print("Expense Approved")
  CONTEXT.handle = None

 #Client
# The Client
 if __name__ == '__main__':
   print(f"1: ")
   CONTEXT = Context(FileExpense)
   print(f"2:")

   CONTEXT.request().ProcessExpense()
   print(f"3:")

   CONTEXT.request().ProcessExpense()
   print(f"4:")

   CONTEXT.request().ProcessExpense()
   print(f"5:")

