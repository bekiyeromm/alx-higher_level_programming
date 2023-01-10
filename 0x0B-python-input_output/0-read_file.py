#!/usr/bin/python3
""" a module that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """function that reads text from the file"""

    with open(filename, 'r', encoding="utf-8") as my:
        print(my.read(), end="")
