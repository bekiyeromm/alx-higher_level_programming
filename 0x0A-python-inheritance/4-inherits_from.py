#!/usr/bin/python3
"""module with a method name inherits_from, which checks
object is an instance of a class that inherited
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """method inherits_from:"""
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
