#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        i = 0
        for j in element:
            print("{:d}{}".format(j, '' if i == (len(element) - 1) else ' ' ), end="")
            i += 1
        print()
