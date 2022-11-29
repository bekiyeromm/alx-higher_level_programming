#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    ss = ""
    for char in str:
        if i != n:
            ss += char
        i += 1
    return (ss)
