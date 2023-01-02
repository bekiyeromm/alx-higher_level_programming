#!/usr/bin/python3
def matrix_divided(matrix, div):
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(message)
    if not isinstance(matrix, list):
        raise TypeError(message)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(message)
        for item in lists:
            if not isinstance(item, (float, int)):
                raise TypeError(message)
    for lists in matrix:
         if len(lists) == 0:
             raise TypeError(message)
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return([[round(j / div, 2) for j in i] for i in matrix])
