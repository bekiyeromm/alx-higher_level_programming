#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for keys, values in a_dictionary.items():
        new_dictionary[keys] = values * 2
    return(new_dictionary)
