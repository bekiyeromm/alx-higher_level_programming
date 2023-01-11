#!/usr/bin/python3
"""a module named append_after"""


def append_after(filename="", search_string="", new_string=""):
    """insert text after string search_string."""

    lines = []
    with open(filename, "r", encoding="utf-8") as my:
        getline = my.readlines()
        i = 0
        while i < len(getline):
            if search_string in getline[i]:
                getline[i:i + 1] = [getline[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as my:
        my.writelines(getline)
