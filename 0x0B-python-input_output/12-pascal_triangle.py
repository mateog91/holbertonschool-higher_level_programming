#!/usr/bin/python3

""" Module of the pascal triangle """


def pascal_triangle(i):
    """ generates the pascal triangle"""
    if i <= 0:
        return []

    matrix = [[1]]
    while len(matrix) < i:

        last_row = matrix[-1]  # last row inserted
        actual_row = [1]  # [1] in left
        [actual_row.append(last_row[i] + last_row[i + 1])
         for i in range(len(last_row) - 1)]
        actual_row.append(1)  # [1] in right

        matrix.append(actual_row)
    return matrix
