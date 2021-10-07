#!/bin/python3
"""
This module has only one function: add_integer which adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a (int): The first integer. Must be entered at least one valid value
        b (int): The second integr. No value can be entered and default value of
        98 will be assigned.

    Returns:
        Integer: Returns the integer sum of the two integers.
        If not an integer the code will fail.
        At least one value must be entered.
        If is a float it will be casted into integer. 
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if (a + 1 == a):
        raise OverflowError("a is too large")
    if (b + 1 == b):
        raise OverflowError("b is too large")

    a, b = int(a), int(b)
    return a + b
