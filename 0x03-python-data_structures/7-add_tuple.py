#!/usr/bin/python3
import operator
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = ()
    temp = (0, 0)
    if(len(tuple_a) < 2):
        tuple_a = tuple_a + temp
    elif (len(tuple_a) > 2):
        tuple_a = tuple_a[:2] + temp
    if(len(tuple_b) < 2):
        tuple_b = tuple_b + temp
    elif (len(tuple_b) > 2):
        tuple_b = tuple_b[:2] + temp
    sum_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_a[1]
    return (sum_tuple)
