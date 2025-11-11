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
        self.arr = arr

    def partition(self, arr, low, high):
        # pivot (Element to be placed at right position)
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
        if low < high:
            pi = self.partition(arr, low, high)
            self.QuickSort(arr, low, pi - 1)
            self.QuickSort(arr, pi + 1, high)

    def sort(self):
        low = 0
        high = len(self.arr) - 1
        self.QuickSort(self.arr, low, high)
        return self.arr

class InsertionSortStrategy(IStrategy):
    "A Concrete Strategy Subclass"
    def __init__(self, arr):
        self.arr = arr
# Insertion Sort
# Create the sorted output array the same length of unsorted input array, please each element of input array into theright
# index of output array with list.insert() and list.append() methods
# George Jen, Jen Tek LLC
    def InsertionSort(self, arr):
        output_list = []
        p = 0
        while p < len(arr):
            if p == 0:
                output_list.append(arr[0])
                p += 1
                continue
            if arr[p] < output_list[0]:
                output_list.insert(0, arr[p])
                p += 1
                continue
            else:
# find the right position to insert
                insert = False
        for i in range(1, len(output_list)):
            if arr[p] < output_list[i]:
                output_list.insert(i, arr[p])
                p += 1
                insert = True
                break
        if insert == False:
            output_list.append(arr[p])
            p += 1
            continue
     return output_list


def sort(self):
    self.arr = self.InsertionSort(self.arr)
    return self.arr

#Write a client code that check the size of a list, if the size of the list is <= 5, use
#InsertionSortStrategy; if the size of the list is > 4, useQuickSortStrategy
# The Client
import random

if __name__ == '__main__':
    CONTEXT = Context()
    listSize = int(input("Enter an integer: "))
    arr = [random.randint(1, listSize) for _ in range(0,
                                                      listSize)]
    if len(arr) > 5:
        print(f"Quick Sort Strategy to sort {arr}")
    # Write your code here
    else:
        print(f"Insertion Sort Strategy to sort {arr}")
