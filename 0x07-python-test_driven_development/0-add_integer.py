#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """func add_integer: -adds two int
    Args:
        a (int): integer a
        b (int): integer b
    Return: the sum of a and b
    """

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
