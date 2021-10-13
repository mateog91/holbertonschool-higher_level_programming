#!/usr/bin/python3
"""Module for Task 11 Advanced"""


def add_attribute(object, key, value):
    """function that adds a new attribute to an object if it’s possible:

    Args:
        object ([class]): [Object in which attribute will be added]
        key ([string]): [Name of value to be added]
        value ([string]): [Value to be added for that key]
    """
    if "__dict__" in dir(object):
        object.key = value
    else:
        raise TypeError("can't add new attribute")


class MyClass():
    pass


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
