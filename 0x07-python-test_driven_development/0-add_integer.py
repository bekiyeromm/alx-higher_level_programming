#!/usr.bin/pytholn3
"""function add_integer.

adds two integer value.
"""


def add_integer(a, b=98):
    """adds integer a and integer b.
    Args:
        a (int): first integer.
        b (int): second integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
