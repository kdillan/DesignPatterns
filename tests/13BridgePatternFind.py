
from abc import ABCMeta, abstractmethod

class OSAbstract(metaclass=ABCMeta):
    "Abstract OS, could be windows or mac"
    @staticmethod
    @abstractmethod
    def uniformed_method(*args):
        "The method handle"

class MacOS(OSAbstract): #for MacOS
    "A Refined Abstraction"
    def __init__(self, implementer):
        self.implementer = implementer()

    def uniformed_method(self, *args):
        self.implementer.uniformed_method(*args)

class Windows(OSAbstract):  #windows
    "A Refined Abstraction"
    def __init__(self, implementer):
        self.implementer = implementer()

    def uniformed_method(self, *args):
        self.implementer.uniformed_method(*args)

class OSImplementorAbstract(metaclass=ABCMeta):
    "The Implementer Interface"
    @staticmethod
    @abstractmethod
    def uniformed_method(*args: tuple) -> None:
        "The method implementation"

class MacOSImplementor(OSImplementorAbstract):  #render the GUI objects on MacOS
    "A Concrete Implementer"
    @staticmethod
    def uniformed_method(*args: tuple) -> None:
        print("Now implement on Mac")
        print(args)

class WindowsImplementor(OSImplementorAbstract):  #render the GUI objects on windows
    "A Concrete Implementer"
    @staticmethod
    def uniformed_method(*args: tuple) -> None:
        print("Now implement on Windows")
        for arg in args:
            print(arg)

if __name__ == '__main__':
    # The Client
    windows = Windows(WindowsImplementor)
    windows.uniformed_method('a', 'b', 'c')
    macOS = MacOS(MacOSImplementor)
    macOS.uniformed_method('a', 'b', 'c')
