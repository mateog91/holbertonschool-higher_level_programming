#!/usr/bin/python3
"""find a peek
"""


def find_peak(list_of_integers):
    """finds a peak of list"""
    if not list_of_integers or len(list_of_integers) == 0:
        return None
    return max(list_of_integers)
