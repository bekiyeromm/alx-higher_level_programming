#!/usr/bin/python3
"""moduledefine rectange wz aea and width."""


class Rectangle():
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """intialization.
        Args:
            width (int): width of rect
            height (int): height of rect
        """
        self.width = width
        self.height = height
        @property
        def width(self):
            """set/get private instance attribute width"""
            return self.__width
        @width.setter
        def width(self, value):
            """setting the value of private attribute width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        @property
        def height(self):
            """set/get value of height"""
            return self.__height
        @height.setter
        def height(self, value):
            """seting a private value for height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
