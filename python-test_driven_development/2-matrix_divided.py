#!/usr/bin/python3
"""module for matrix division"""


def matrix_divided(matrix, div):
    """divide matrix by div"""
    new_matrix = []
    row_length = len(matrix[0])
    for arr in matrix:
        if len(arr) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        chunk = []
        for ele in arr:
            if isinstance(ele, int):
                chunk.append(round((ele / div), 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append(chunk)
    return new_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 'a'],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
