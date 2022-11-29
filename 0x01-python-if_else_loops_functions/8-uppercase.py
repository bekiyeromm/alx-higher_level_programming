#!/usr/bin/python3
def uppercase(str):
    ss = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = ord(char) - 32
            ss = ss + chr(char)
        else:
            ss = ss + char
    print("{}".format(ss))
