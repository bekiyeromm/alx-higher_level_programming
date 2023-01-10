#!/usr/bin/python3
"""a module that writes a string to a text file"""


def write_file(filename="", text=""):
    """a method to write in to a file and it returns
    the number of characters written"""

    with open(filename, "w", encoding="utf-8") as my:
        return (my.write(text))
