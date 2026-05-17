#!/usr/bin/python3
"""module for matrix division"""


def matrix_divided(matrix, div):
    """divide matrix by div"""
    new_matrix = []
    row_length = len(matrix[0])
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for arr in matrix:
        if len(arr) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        chunk = []
        for ele in arr:
            if type(ele) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            chunk.append(round((ele / div), 2))
        new_matrix.append(chunk)
    return new_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 'a'],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
