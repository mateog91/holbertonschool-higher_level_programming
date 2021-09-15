#!/usr/bin/python3
def uniq_add(my_list=[]):
    r = 0
    unique = []
    for e in my_list:
        if e not in unique:
            r += e
            unique.append(e)
    return r
