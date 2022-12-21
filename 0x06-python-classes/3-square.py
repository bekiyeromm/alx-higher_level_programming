#!/usr/bin/python3
"""module Square.

defines a Square class.
"""


class Square:

    """ class Square.
    intializes a square attribut
    """

    def __init__(self, size=0):
        """intialize attributes
        Args:
            size (int): size of a square
        Returns: none
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2
