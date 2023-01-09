#!/usr/bin/python3
"""module BaseGeometrywith method area
that raise an Exception
"""


class BaseGeometry():
    """module BaseGeometry"""

    def area(self):
        """method area that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method which validates an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
