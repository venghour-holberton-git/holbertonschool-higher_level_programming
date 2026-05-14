#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print("{:d} ".format(j), end="")
        print()

print_matrix_integer([[3, 1], [2, 6], [4, 2]])
