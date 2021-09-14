#!/usr/bin/python3
def check_tuple(a):
    l = len(a)
    if l < 2:
        if l < 1:
            a = (0, 0)
        else:
            a = (a[0], 0)
    return a


def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None

    a = check_tuple(tuple_a)
    b = check_tuple(tuple_b)

    return (a[0] + b[0], a[1] + b[1])
