#!/usr/bin/python3
import operator
def add_tuple(tuple_a=(), tuple_b=()):
    temp = (0, 0)
    if len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    elif len(tuple_a) < 2:
        tuple_a = tuple_a + temp

    if len(tuple_b) > 2:
        tuple_a = tuple_b[:2]
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + temp
    element1 = tuple_a[0] + tuple_b[0]
    element2 = tuple_a[1] + tuple_b[1]
    sum_tuple = (element1, element2)
    return (sum_tuple)
