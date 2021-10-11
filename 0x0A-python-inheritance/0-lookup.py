#!/usr/bin/python3
"""Write a function that returns the list of available attributes
    and methods of an object:"""


def lookup(obj):
    """ returns  list of available attributes and methods of an object:
    Args:
        obj: Input object
     """
    return dir(obj)
