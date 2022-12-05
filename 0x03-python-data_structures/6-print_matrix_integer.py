#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if  matrix:
        for i in matrix:
            for j in i:
                if j != i[- 1]:
                    sep = " "
                else:
                    sep = ""
                print("{:d}".format(j), end=sep)
            print()

