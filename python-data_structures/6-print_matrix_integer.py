#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        i = 0
        for j in element:
            is_last_element = i == (len(element) - 1)
            extra_text = '' if is_last_element else ' '
            print("{:d}{}".format(j, extra_text), end="")
            i += 1
        print()
