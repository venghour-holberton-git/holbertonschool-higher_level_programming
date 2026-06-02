#!/usr/bin/python3
"""pascal triangle module"""


def pascal_triangle(n):
    """get pascal triangle"""

    triange_matrix = []
    for row in range(n):
        temp_array = []
        for element in range(row + 1):
            if row < 2:
                temp_array.append(1)
            else:
                if element == 0 or element == row:
                    temp_array.append(1)
                else:
                    previous_row = triange_matrix[row - 1]
                    i_value = previous_row[element-1] + previous_row[element]
                    temp_array.append(i_value)
        triange_matrix.append(temp_array)
        # temp_array = []
    return triange_matrix
