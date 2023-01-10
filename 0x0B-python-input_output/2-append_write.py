#!/usr/bin/python3
"""module to append a file"""


def append_write(filename="", text=""):
    """a method that append a string at the end of text file"""

    with open(filename, "a", encoding="utf-8") as my:
        return (my.write(text))
