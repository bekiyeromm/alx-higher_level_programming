#!/usr/bin/python3
"""module Square

a class Square that defines a square by Private instance
attribute: size size must be an integer, otherwise
raise a TypeError exception with the message size must
be an integer
"""


class Square:
    """defines a Square"""

    def _init__(self, size=0):
        """instantition and set the class attribute

        Args:
            size (int): size of one side of a square

        Raises:
            TypeError: if size value is not int type
            ValueError: if size value is less than 0
        """

        if type(size) != int:
            raise TypeError("size must be an integer")

        if(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """calculate and return area of square"""
            return (self.__size) ** 2
