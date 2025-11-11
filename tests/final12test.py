from abc import ABCMeta, abstractmethod

class Context():
  #  "This is the object whose behavior will change"
    @staticmethod
    def request(strategy):
        """The request is handled by the class passed in"""
        return strategy
class IStrategy(metaclass=ABCMeta):
    "A strategy abstract interface"
    @staticmethod
    @abstractmethod
    def __init__(self, arr):
        ""

    def sort():
        "Implement sort"


class QuickSortStrategy(IStrategy):
    "A Concrete Strategy Subclass"

    # Quick Sort Implementation, in place sort
    # George Jen, Jen Tek LLC
    def __init__(self, arr):
        print(f"In Init QuickSort")
        self.arr = arr

    def partition(self, arr, low, high):
        # pivot (Element to be placed at right position)
        print(f"In QuickSort Partition")
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
        # If current element is smaller than the pivot
            if arr[j] < pivot:
                i += 1;  # increment index of smaller element
            # swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def QuickSort(self, arr, low, high):
        print(f"In QuickSort()")

    def sort(self):
        print(f"In QuickSort Sort()")
        low = 0
        high = len(self.arr) - 1
        self.QuickSort(self.arr, low, high)
        return self.arr

class InsertionSortStrategy(IStrategy):
    "A Concrete Strategy Subclass"
    def __init__(self, arr):
        self.arr = arr
        print(f"In Init InsertionSort")
# Insertion Sort
# Create the sorted output array the same length of unsorted input array, please each element of input array into theright
# index of output array with list.insert() and list.append() methods
# George Jen, Jen Tek LLC
    def InsertionSort(self, arr):
        print(f"In InsertionSort() ")

    def sort(self):
        print(f"In InsertionSort Sort() ")
        self.arr = self.InsertionSort(self.arr)
        return self.arr

#Write a client code that check the size of a list, if the size of the list is <= 5, use
#InsertionSortStrategy; if the size of the list is > 4, useQuickSortStrategy
# The Client
import random

if __name__ == '__main__':
    CONTEXT = Context()
    listSize = int(input("Enter an integer: "))
    arr = [random.randint(1, listSize)
    for _ in range(0,listSize)]
    if len(arr) > 5:
            print(CONTEXT.request(QuickSortStrategy))
    #  codefix here
    else:
            print(CONTEXT.request(InsertionSortStrategy))

    print(f"Quick Sort Strategy to sort {arr}")
    print(f"Insertion Sort Strategy to sort {arr}")


#  Quick output:
#  Enter an integer: 50
# <class '__main__.QuickSortStrategy'>
# Quick Sort Strategy to sort [17, 20, 47, 50, 31, 8, 30, 25, 24, 9, 46, 18, 15, 18, 11, 14, 5, 27, 6, 2, 18, 7, 17, 42, 40, 5, 22, 50, 40, 19, 36, 16, 45, 9, 37, 13, 49, 10, 42, 2, 20, 21, 48, 27, 9, 42, 9, 15, 16, 40]
# Insertion Sort Strategy to sort [17, 20, 47, 50, 31, 8, 30, 25, 24, 9, 46, 18, 15, 18, 11, 14, 5, 27, 6, 2, 18, 7, 17, 42, 40, 5, 22, 50, 40, 19, 36, 16, 45, 9, 37, 13, 49, 10, 42, 2, 20, 21, 48, 27, 9, 42, 9, 15, 16, 40]

