#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    c = False
    for keys in a_dictionary:
        if keys == key:
            c = True
    if c:
        del a_dictionary[key]
    return(a_dictionary)
