#!/usr/bin/python3
import operator
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = ()
    temp = (0, 0)
    tp1 = tuple_a + temp
    tp2 = tuple_b + temp
    sum_tuple = tp1[0] + tp2[0], tp1[1] + tp2[1]
    return (sum_tuple)
