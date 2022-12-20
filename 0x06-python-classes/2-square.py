#!/usr/bin/python3
"""module Square,

checks weather the value of size is integer or not
"""


class Square:

    """defines a Square class"""

    def __init__(self, size=0):
        """instantation of private attribute of class

        Args:
            size: size
            """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
