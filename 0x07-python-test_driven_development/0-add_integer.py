#!/usr.bin/pytholn3
def add_integer(a, b=98):
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testmod()
