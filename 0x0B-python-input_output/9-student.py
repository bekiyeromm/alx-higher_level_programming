#!/usr/bin/python3
"""a module named student class that defines that defines a student by
Public instance attributes"""


class Student:
    """a class we shall json"""

    def __init__(self, first_name, last_name, age):
        """init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get dict"""

        return self.__dict__.copy()
