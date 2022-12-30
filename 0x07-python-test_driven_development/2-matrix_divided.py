#!/usr/bin/python3
"""module matrix_dividde

divides two matrix element
"""


def matrix_divided(matrix, div):
    """
    divides matrix element 
    
    Args:
        matrix (list): matrix element to be divided
        div (int, float) divider
    """
    return([[round(j / div, 2) for j in i] for i in matrix])
