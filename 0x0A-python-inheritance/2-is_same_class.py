#!/usr/bin/python3
"""a method with name is_ame_class, which returns
true if the object is exactly an instance of the specified class
otherwise false
"""


def is_same_class(obj, a_class):
    """checks weather obje and a_class having
    the same class or not"""
    if type(obj) == a_class:
        return True
    else:
        return False
