#!/usr/bin/python3
"""
This module has one function: ''matrix_dived'' divides all elements of a matrix.

Description:
- matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
- Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
- div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
- div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
- All elements of the matrix should be divided by div, rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """ Returns new matrix of all elements of a matrix by a constant

    Args:
        matrix (list): Matrix to be devided
        div (int or float): Divisor constant (cannot be 0)

    Returns:
        If success, Matrix with all elements of matrix diveded by div
    """
    if matrix == []:
        raise ValueError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check all rows are int or float
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # check through matrix
    row_length = len(matrix[0])
    for row in matrix:
        # check all rows are same length
        if row_length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            # check elements of row are int or float
            if type(element) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
                        integers/floats")
            # check elements is not too large
            if element + 1 == element:
                raise OverflowError("element is too large")

    return [[round(element / div, 2) for element in row] for row in matrix]
