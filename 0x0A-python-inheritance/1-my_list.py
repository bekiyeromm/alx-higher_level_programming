#!/usr/bin/python3
"""a module named MyList that inherited from module list
and prints alist in sorted (ascending sort)
"""


class MyList(list):
    """class Mylist inherited from class list
    with a method print_sorted that prints a list in sorted
    order"""

    def print_sorted(self):
        """prints a lists sorted in ascending order"""
        print(sorted(self))
