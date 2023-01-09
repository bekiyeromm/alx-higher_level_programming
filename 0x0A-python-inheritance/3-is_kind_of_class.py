#!/usr/bin/python3
"""module with the method is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """method is_kind_of_class which checks if the object
    is an instance of a class that inherited from, the
    specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
