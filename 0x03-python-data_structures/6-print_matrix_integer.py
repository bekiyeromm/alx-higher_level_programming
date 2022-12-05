#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if  matrix:
        for i in matrix:
            for j in i:
                if j == i[0]:
                    print(f"{j}", end=" ")
                else:
                    print(f"{j}", end=" ")
            print()

