#!/usr/bin/python3
"""a module that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using binary search algorithm.

    Args:
    - list_of_integers: a list of unsorted integers

    Returns:
    - A peak element in the list.
    """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid+1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
