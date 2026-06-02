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
                    temp_array.append(previous_row[element-1] + previous_row[element])
        triange_matrix.append(temp_array)
        # temp_array = []
    return triange_matrix

if __name__ == "__main__":
    def print_triangle(triangle):
        """Print the triangle"""
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    m_triangle = pascal_triangle(5)
    print_triangle(m_triangle)
