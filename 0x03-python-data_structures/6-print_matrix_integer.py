#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if  matrix:
        for i in matrix:
            for j in i:
                print(f"{j}", end=" ")
            print()

