#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for i in matrix:
        for j in i:
            print(f"{j}", end=" ")
        print()

