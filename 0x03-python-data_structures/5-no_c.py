#!/usr/bin/python3
def no_c(my_string):
    str1 = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            str1 = str1 + i
    return str1
