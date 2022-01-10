#!/usr/bin/python3
"""find a peek
"""


def peak(lst):
    """finds a peak of list"""
    if not lst or len(lst) == 0:
        return None
    return max(lst)
