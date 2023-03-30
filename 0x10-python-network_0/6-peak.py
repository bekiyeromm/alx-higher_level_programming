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
    if not len(list_of_integers):
        return None
    else:
        return max(list_of_integers)
