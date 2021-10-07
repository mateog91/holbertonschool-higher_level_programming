#!/bin/python3
""" Module has only one function ''print_square''
Description:
- size is the size length of the square
- size must be an integer, otherwise raise a TypeError exception with the
  message size must be an integer
- if size is less than 0, raise a ValueError exception with the message
  size must be >= 0
- if size is a float and is less than 0, raise a TypeError exception with
  the message size must be an integer
"""


def print_square(size):
    """ returns nothing, prints a square with #

    Args:
        size (int): is the size of the square

    Description:
        Prints a square of size
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for rows in range(0, size):
        print("#" * size)
