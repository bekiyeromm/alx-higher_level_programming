#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""module rectangle"""


class Rectangle(BaseGeometry):
    """class Rectangle, inherited from class
    BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        """__str__ method for return the next string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
