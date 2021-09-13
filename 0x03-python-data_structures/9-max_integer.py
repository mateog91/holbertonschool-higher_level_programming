#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or my_list == []:
        return None
    if len(my_list) == 1:
        return my_list[0]

    biggest = my_list[0]
    for element in my_list:
        biggest = bigger(biggest, element)
    return biggest


def bigger(a, b):
    if a > b:
        return a
    else:
        return b
