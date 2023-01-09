#!/usr/bin/python3
"""module with funaction named lookup which returns list
of availlable object methods and attribute
s"""


def lookup(obj):
    """returns the list of available attributes and
    methods of an object"""
    return (list(dir(obj)))
